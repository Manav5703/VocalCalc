/**
 * VocalCalc - Speech Module
 * Handles speech recognition and synthesis
 */

class Speech {
    constructor() {
        // Initialize speech recognition
        this.initSpeechRecognition();
        
        // State
        this.isListening = false;
        
        // Elements
        this.micButton = document.getElementById('mic-btn');
        this.voiceVisualization = document.getElementById('voice-visualization');
        
        // Set up event listeners
        this.setupEventListeners();
    }
    
    /**
     * Initialize speech recognition
     */
    initSpeechRecognition() {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        
        if (!SpeechRecognition) {
            ui.showToast('Speech recognition is not supported in your browser. Please try Chrome or Edge.', 'error');
            return false;
        }
        
        this.recognition = new SpeechRecognition();
        this.recognition.continuous = false;
        this.recognition.interimResults = false;
        
        // Set language from settings
        this.recognition.lang = appSettings.getSetting('language');
        
        // Set up event handlers
        this.recognition.onstart = this.handleRecognitionStart.bind(this);
        this.recognition.onresult = this.handleRecognitionResult.bind(this);
        this.recognition.onerror = this.handleRecognitionError.bind(this);
        this.recognition.onend = this.handleRecognitionEnd.bind(this);
        
        return true;
    }
    
    /**
     * Set up event listeners
     */
    setupEventListeners() {
        // Microphone button
        this.micButton.addEventListener('click', () => {
            this.toggleListening();
        });
    }
    
    /**
     * Toggle listening state
     */
    toggleListening() {
        if (this.isListening) {
            this.stopListening();
        } else {
            this.startListening();
        }
    }
    
    /**
     * Start listening for voice commands
     */
    startListening() {
        if (!this.recognition) {
            if (!this.initSpeechRecognition()) {
                return;
            }
        }
        
        try {
            // Update language from settings
            this.recognition.lang = appSettings.getSetting('language');
            
            // Start recognition
            this.recognition.start();
        } catch (error) {
            console.error('Speech recognition error:', error);
            ui.showToast('Error starting speech recognition. Please try again.', 'error');
        }
    }
    
    /**
     * Stop listening for voice commands
     */
    stopListening() {
        if (this.recognition && this.isListening) {
            try {
                this.recognition.stop();
            } catch (error) {
                console.error('Error stopping speech recognition:', error);
            }
        }
        
        this.isListening = false;
        this.micButton.classList.remove('listening');
        this.voiceVisualization.classList.remove('active');
    }
    
    /**
     * Handle recognition start event
     */
    handleRecognitionStart() {
        this.isListening = true;
        this.micButton.classList.add('listening');
        this.voiceVisualization.classList.add('active');
        ui.updateCommandDisplay('Listening...');
    }
    
    /**
     * Handle recognition result event
     * @param {SpeechRecognitionEvent} event - The recognition event
     */
    handleRecognitionResult(event) {
        if (event.results.length > 0) {
            const result = event.results[0][0];
            const command = result.transcript;
            const confidence = result.confidence;
            
            console.log(`Speech recognized: "${command}" (confidence: ${confidence.toFixed(2)})`);
            
            // Check confidence threshold
            const threshold = appSettings.getSetting('confidenceThreshold');
            if (confidence >= threshold) {
                ui.updateCommandDisplay(`You said: ${command}`);
                
                // Process the command
                if (typeof calculator !== 'undefined') {
                    calculator.processCommand(command);
                }
            } else {
                ui.updateCommandDisplay(`Low confidence (${(confidence * 100).toFixed(0)}%). Please try again.`);
                ui.showToast(`Low confidence in speech recognition. Please speak more clearly.`, 'warning');
            }
        } else {
            ui.updateCommandDisplay('No speech detected. Please try again.');
        }
    }
    
    /**
     * Handle recognition error event
     * @param {SpeechRecognitionErrorEvent} event - The error event
     */
    handleRecognitionError(event) {
        console.error('Speech recognition error:', event.error);
        
        let errorMessage = 'Error with speech recognition';
        
        // Provide more user-friendly error messages
        switch(event.error) {
            case 'no-speech':
                errorMessage = 'No speech was detected. Please try again.';
                break;
            case 'aborted':
                errorMessage = 'Speech recognition was aborted.';
                break;
            case 'audio-capture':
                errorMessage = 'No microphone was found or microphone is disabled.';
                break;
            case 'network':
                errorMessage = 'Network error occurred. Please check your connection.';
                break;
            case 'not-allowed':
            case 'service-not-allowed':
                errorMessage = 'Microphone access was not allowed. Please enable microphone access.';
                break;
            default:
                errorMessage = `Error: ${event.error}`;
        }
        
        ui.updateCommandDisplay(errorMessage);
        ui.showToast(errorMessage, 'error');
        
        this.stopListening();
    }
    
    /**
     * Handle recognition end event
     */
    handleRecognitionEnd() {
        this.stopListening();
    }
    
    /**
     * Speak text using speech synthesis
     * @param {string} text - The text to speak
     */
    speak(text) {
        if ('speechSynthesis' in window) {
            try {
                // Cancel any ongoing speech
                window.speechSynthesis.cancel();
                
                const utterance = new SpeechSynthesisUtterance();
                
                // Set text
                utterance.text = text;
                
                // Set speech parameters from settings
                utterance.rate = appSettings.getSetting('speechRate');
                utterance.pitch = appSettings.getSetting('speechPitch');
                utterance.volume = appSettings.getSetting('speechVolume');
                utterance.lang = appSettings.getSetting('language');
                
                // Add event handlers for debugging
                utterance.onstart = () => console.log('Speech started');
                utterance.onend = () => console.log('Speech ended');
                utterance.onerror = (e) => console.error('Speech error:', e);
                
                // Speak
                window.speechSynthesis.speak(utterance);
            } catch (error) {
                console.error('Text-to-speech error:', error);
                ui.showToast('Error with text-to-speech. Please try again.', 'error');
            }
        } else {
            console.warn('Text-to-speech not supported in this browser');
        }
    }
}

// Create global speech instance
const speech = new Speech();
