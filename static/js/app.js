/**
 * VocalCalc - Main Application
 * Initializes and coordinates all modules
 */

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
    console.log('VocalCalc initialized');

    // Check for browser compatibility
    checkBrowserCompatibility();

    // Check server connectivity
    checkServerConnectivity();

    // Initialize modules
    // Note: These are already initialized in their respective files
    // - appSettings (settings.js)
    // - ui (ui.js)
    // - speech (speech.js)
    // - calculator (calculator.js)

    // Set up additional event listeners
    setupGlobalEventListeners();
});

/**
 * Check browser compatibility for required features
 */
function checkBrowserCompatibility() {
    // Check for Speech Recognition
    const hasSpeechRecognition = 'SpeechRecognition' in window || 'webkitSpeechRecognition' in window;

    // Check for Speech Synthesis
    const hasSpeechSynthesis = 'speechSynthesis' in window;

    // Check for Fetch API
    const hasFetch = 'fetch' in window;

    // Check for localStorage
    const hasLocalStorage = (() => {
        try {
            localStorage.setItem('test', 'test');
            localStorage.removeItem('test');
            return true;
        } catch (e) {
            return false;
        }
    })();

    // Log compatibility status
    console.log('Browser compatibility check:');
    console.log('- Speech Recognition:', hasSpeechRecognition ? 'Supported' : 'Not supported');
    console.log('- Speech Synthesis:', hasSpeechSynthesis ? 'Supported' : 'Not supported');
    console.log('- Fetch API:', hasFetch ? 'Supported' : 'Not supported');
    console.log('- localStorage:', hasLocalStorage ? 'Supported' : 'Not supported');

    // Show warning if any required feature is missing
    if (!hasSpeechRecognition || !hasSpeechSynthesis || !hasFetch || !hasLocalStorage) {
        const missingFeatures = [];

        if (!hasSpeechRecognition) missingFeatures.push('Speech Recognition');
        if (!hasSpeechSynthesis) missingFeatures.push('Speech Synthesis');
        if (!hasFetch) missingFeatures.push('Fetch API');
        if (!hasLocalStorage) missingFeatures.push('Local Storage');

        const warningMessage = `Your browser doesn't support: ${missingFeatures.join(', ')}. Some features may not work correctly.`;
        ui.showToast(warningMessage, 'warning');

        // Show help modal with browser compatibility info
        setTimeout(() => {
            ui.openModal(document.getElementById('help-modal'));
        }, 1000);
    }
}

/**
 * Set up global event listeners
 */
function setupGlobalEventListeners() {
    // Handle visibility change (tab switching)
    document.addEventListener('visibilitychange', () => {
        if (document.visibilityState === 'hidden') {
            // Stop listening when tab is not visible
            if (speech.isListening) {
                speech.stopListening();
            }
        }
    });

    // Handle online/offline status
    window.addEventListener('online', () => {
        ui.showToast('You are back online', 'success');
    });

    window.addEventListener('offline', () => {
        ui.showToast('You are offline. Voice recognition may not work.', 'warning');

        // Stop listening if offline
        if (speech.isListening) {
            speech.stopListening();
        }
    });

    // Handle beforeunload event to save data
    window.addEventListener('beforeunload', () => {
        // Save any unsaved data
        ui.saveHistory();
        appSettings.saveSettings();
    });
}

/**
 * Check server connectivity
 */
async function checkServerConnectivity() {
    try {
        // Try to connect to the health check endpoint
        const response = await fetch(window.location.origin + '/api/health', {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
            },
            // Set a timeout to avoid waiting too long
            signal: AbortSignal.timeout(5000) // 5 second timeout
        });

        if (response.ok) {
            const data = await response.json();
            console.log('Server health check:', data);
            ui.showToast('Connected to server successfully', 'success');
        } else {
            throw new Error(`Server responded with status: ${response.status}`);
        }
    } catch (error) {
        console.error('Server connectivity check failed:', error);

        // Show a more user-friendly error message
        let errorMessage = 'Could not connect to the server. Voice commands may not work.';

        if (error.name === 'AbortError') {
            errorMessage = 'Server connection timed out. Please check if the server is running.';
        } else if (error.name === 'TypeError') {
            errorMessage = 'Network error. Please check if the server is running on port 5000.';
        }

        ui.showToast(errorMessage, 'error');

        // Show a helpful message in the result display
        ui.updateResultDisplay('Server connection error. Please start the Flask server.');
    }
}
