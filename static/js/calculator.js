/**
 * VocalCalc - Calculator Module
 * Handles calculation logic and API communication
 */

class Calculator {
    constructor() {
        // API endpoint - use absolute URL to avoid path issues
        this.apiUrl = window.location.origin + '/api/calculate';
    }

    /**
     * Process a voice command
     * @param {string} command - The voice command to process
     */
    async processCommand(command) {
        try {
            // Show loading state
            ui.showLoading();

            // Log the command being processed
            console.log('Processing command:', command);
            console.log('API URL:', this.apiUrl);

            // Create request payload
            const payload = { command };
            console.log('Request payload:', payload);

            // Send command to API with timeout
            const controller = new AbortController();
            const timeoutId = setTimeout(() => {
                console.log('Request timeout triggered');
                controller.abort();
            }, 10000); // 10 second timeout

            try {
                console.log('Sending fetch request to:', this.apiUrl);
                const response = await fetch(this.apiUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json'
                    },
                    body: JSON.stringify(payload),
                    signal: controller.signal,
                    // Add cache control to prevent caching issues
                    cache: 'no-cache'
                });

                clearTimeout(timeoutId); // Clear the timeout if the request completes
                console.log('Received response:', response);
                console.log('Response status:', response.status);
                console.log('Response headers:', [...response.headers.entries()]);

                // Check for HTTP errors
                if (!response.ok) {
                    throw new Error(`Server responded with status: ${response.status}`);
                }

                // Parse response
                const data = await response.json();
                console.log('Response data:', data);

                // Check for API errors
                if (data.error) {
                    ui.showError(data.error);
                    speech.speak(data.error);
                    return;
                }

                // Format and display result
                this.displayResult(data);
            } catch (fetchError) {
                console.error('Fetch error details:', fetchError);

                // Handle fetch-specific errors
                if (fetchError.name === 'AbortError') {
                    throw new Error('Request timed out. The server took too long to respond.');
                } else {
                    throw fetchError; // Re-throw for the outer catch block
                }
            }
        } catch (error) {
            console.error('Error processing command:', error);
            let errorMessage;

            // Provide more user-friendly error messages
            if (error.message.includes('Failed to fetch') || error.name === 'TypeError') {
                errorMessage = 'Network error. Please check if the server is running.';
                // Try to ping the server to check connectivity
                this.checkServerConnectivity();
            } else {
                errorMessage = error.message || 'Error processing your request. Please try again.';
            }

            ui.showError(`Error: ${errorMessage}`);
            speech.speak(`Error: ${errorMessage}`);
        }
    }

    /**
     * Display calculation result
     * @param {Object} data - The calculation result data
     */
    displayResult(data) {
        const { result, history_entry } = data;

        // Format result for display
        let displayResult;
        if (typeof result === 'string') {
            // Error message or text result
            displayResult = result;
        } else if (Number.isInteger(result)) {
            // Integer result
            displayResult = result;
        } else {
            // Float result - format to 2 decimal places if needed
            displayResult = Math.abs(result) < 0.01 ? result.toExponential(2) : result.toFixed(2);
        }

        // Update UI
        ui.updateResultDisplay(displayResult);
        ui.showSuccess();

        // Add to history if there's a valid history entry
        if (history_entry) {
            ui.addToHistory(history_entry);
        }

        // Speak result
        this.speakResult(result);
    }

    /**
     * Check server connectivity
     */
    async checkServerConnectivity() {
        try {
            console.log('Checking server connectivity...');
            // Try to connect to the health check endpoint
            const response = await fetch(window.location.origin + '/api/health', {
                method: 'GET',
                headers: {
                    'Accept': 'application/json',
                },
                // Set a timeout to avoid waiting too long
                signal: AbortSignal.timeout(3000) // 3 second timeout
            });

            if (response.ok) {
                const data = await response.json();
                console.log('Server health check:', data);
                ui.showToast('Server is running', 'success');
                return true;
            } else {
                throw new Error(`Server responded with status: ${response.status}`);
            }
        } catch (error) {
            console.error('Server connectivity check failed:', error);
            ui.showToast('Server connection failed. Please check if the server is running.', 'error');
            return false;
        }
    }

    /**
     * Speak the calculation result
     * @param {string|number} result - The result to speak
     */
    speakResult(result) {
        // Format text for speech
        let speechText;

        if (typeof result === 'string' && result.startsWith('Error')) {
            // Error message
            speechText = result;
        } else if (typeof result === 'number') {
            // Number result
            if (Number.isInteger(result)) {
                speechText = `The result is ${result}`;
            } else {
                // Format decimal numbers for speech
                const formattedResult = Math.abs(result) < 0.01 ?
                    result.toExponential(2) :
                    result.toFixed(2).replace(/\.?0+$/, ''); // Remove trailing zeros

                speechText = `The result is ${formattedResult}`;
            }
        } else {
            // Other result
            speechText = `The result is ${result}`;
        }

        // Speak the result
        speech.speak(speechText);
    }
}

// Create global calculator instance
const calculator = new Calculator();
