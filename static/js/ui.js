/**
 * VocalCalc - UI Module
 * Handles UI interactions and animations
 */

class UI {
    constructor() {
        // Initialize UI elements
        this.initElements();

        // Set up event listeners
        this.setupEventListeners();

        // Initialize tabs
        this.initTabs();
    }

    /**
     * Initialize UI elements
     */
    initElements() {
        // Tabs
        this.tabButtons = document.querySelectorAll('.tab-button');
        this.tabPanes = document.querySelectorAll('.tab-pane');

        // Modals
        this.settingsModal = document.getElementById('settings-modal');
        this.helpModal = document.getElementById('help-modal');
        this.closeModalButtons = document.querySelectorAll('.close-modal');

        // Buttons
        this.themeToggle = document.getElementById('theme-toggle');
        this.settingsBtn = document.getElementById('settings-btn');
        this.helpBtn = document.getElementById('help-btn');
        this.clearHistoryBtn = document.getElementById('clear-history');

        // Display elements
        this.commandDisplay = document.getElementById('command-display');
        this.resultDisplay = document.getElementById('result-display');
        this.historyList = document.getElementById('history-list');

        // Example commands
        this.exampleCommands = document.querySelectorAll('.example-commands li');
    }

    /**
     * Set up event listeners
     */
    setupEventListeners() {
        // Tab buttons
        this.tabButtons.forEach(button => {
            button.addEventListener('click', () => {
                this.switchTab(button.dataset.tab);
            });
        });

        // Theme toggle
        this.themeToggle.addEventListener('click', () => {
            this.toggleTheme();
        });

        // Settings button
        this.settingsBtn.addEventListener('click', () => {
            this.openModal(this.settingsModal);
        });

        // Help button
        this.helpBtn.addEventListener('click', () => {
            this.openModal(this.helpModal);
        });

        // Close modal buttons
        this.closeModalButtons.forEach(button => {
            button.addEventListener('click', () => {
                this.closeAllModals();
            });
        });

        // Clear history button
        this.clearHistoryBtn.addEventListener('click', () => {
            this.clearHistory();
        });

        // Example commands
        this.exampleCommands.forEach(command => {
            command.addEventListener('click', () => {
                const commandText = command.textContent.replace(/["]/g, '');
                this.simulateCommand(commandText);
            });
        });

        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {
            // 'M' key for microphone
            if (e.key === 'm' && !e.ctrlKey && !e.altKey && !e.metaKey) {
                const micBtn = document.getElementById('mic-btn');
                if (micBtn) {
                    micBtn.click();
                }
            }

            // 'T' key for theme toggle
            if (e.key === 't' && !e.ctrlKey && !e.altKey && !e.metaKey) {
                this.toggleTheme();
            }

            // 'H' key for history
            if (e.key === 'h' && !e.ctrlKey && !e.altKey && !e.metaKey) {
                this.switchTab('history');
            }

            // 'Escape' key to close modals
            if (e.key === 'Escape') {
                this.closeAllModals();
            }
        });

        // Click outside modal to close
        window.addEventListener('click', (e) => {
            if (e.target === this.settingsModal || e.target === this.helpModal) {
                this.closeAllModals();
            }
        });
    }

    /**
     * Initialize tabs
     */
    initTabs() {
        // Set the first tab as active by default
        this.switchTab('standard');
    }

    /**
     * Switch to a specific tab
     * @param {string} tabId - The ID of the tab to switch to
     */
    switchTab(tabId) {
        // Update tab buttons
        this.tabButtons.forEach(button => {
            if (button.dataset.tab === tabId) {
                button.classList.add('active');
            } else {
                button.classList.remove('active');
            }
        });

        // Update tab panes
        this.tabPanes.forEach(pane => {
            if (pane.id === `${tabId}-tab`) {
                pane.classList.add('active');
            } else {
                pane.classList.remove('active');
            }
        });
    }

    /**
     * Toggle between light and dark theme
     */
    toggleTheme() {
        const currentTheme = appSettings.getSetting('theme');
        let newTheme;

        if (currentTheme === 'auto') {
            // If auto, switch to explicit light/dark based on current state
            newTheme = document.body.classList.contains('dark-theme') ? 'light' : 'dark';
        } else {
            // Toggle between light and dark
            newTheme = currentTheme === 'light' ? 'dark' : 'light';
        }

        // Update settings
        appSettings.settings.theme = newTheme;
        appSettings.themeSelect.value = newTheme;
        appSettings.applyTheme();
        appSettings.saveSettings();
    }

    /**
     * Open a modal
     * @param {HTMLElement} modal - The modal to open
     */
    openModal(modal) {
        // Close any open modals first
        this.closeAllModals();

        // Open the specified modal
        modal.classList.add('active');
    }

    /**
     * Close all modals
     */
    closeAllModals() {
        this.settingsModal.classList.remove('active');
        this.helpModal.classList.remove('active');
    }

    /**
     * Update the command display
     * @param {string} command - The command to display
     */
    updateCommandDisplay(command) {
        this.commandDisplay.textContent = command;
    }

    /**
     * Update the result display
     * @param {string|number} result - The result to display
     */
    updateResultDisplay(result) {
        this.resultDisplay.textContent = result;

        // Adjust font size based on length
        if (result.toString().length > 15) {
            this.resultDisplay.style.fontSize = 'var(--font-size-lg)';
        } else if (result.toString().length > 10) {
            this.resultDisplay.style.fontSize = 'var(--font-size-xl)';
        } else {
            this.resultDisplay.style.fontSize = 'var(--font-size-xxl)';
        }
    }

    /**
     * Add an entry to the calculation history
     * @param {string} entry - The history entry to add
     */
    addToHistory(entry) {
        // Remove empty history message if present
        const emptyHistory = this.historyList.querySelector('.empty-history');
        if (emptyHistory) {
            this.historyList.removeChild(emptyHistory);
        }

        // Create history item
        const historyItem = document.createElement('div');
        historyItem.className = 'history-item';
        historyItem.textContent = entry;

        // Add click event to reuse the calculation
        historyItem.addEventListener('click', () => {
            // Extract the calculation from the history entry
            const parts = entry.split('=');
            if (parts.length >= 2) {
                const calculation = parts[0].trim();
                this.simulateCommand(calculation);
            }
        });

        // Add to history list (at the beginning)
        this.historyList.insertBefore(historyItem, this.historyList.firstChild);

        // Limit history to 20 items
        const historyItems = this.historyList.querySelectorAll('.history-item');
        if (historyItems.length > 20) {
            this.historyList.removeChild(historyItems[historyItems.length - 1]);
        }

        // Save history to localStorage
        this.saveHistory();
    }

    /**
     * Clear the calculation history
     */
    clearHistory() {
        // Clear history list
        this.historyList.innerHTML = '<p class="empty-history">No calculations yet.</p>';

        // Clear from localStorage
        localStorage.removeItem('vocalcalc-history');
    }

    /**
     * Save history to localStorage
     */
    saveHistory() {
        const historyItems = this.historyList.querySelectorAll('.history-item');
        const history = Array.from(historyItems).map(item => item.textContent);
        localStorage.setItem('vocalcalc-history', JSON.stringify(history));
    }

    /**
     * Load history from localStorage
     */
    loadHistory() {
        const savedHistory = localStorage.getItem('vocalcalc-history');
        if (savedHistory) {
            const history = JSON.parse(savedHistory);

            // Clear current history
            this.historyList.innerHTML = '';

            // Add history items
            if (history.length > 0) {
                history.forEach(entry => {
                    const historyItem = document.createElement('div');
                    historyItem.className = 'history-item';
                    historyItem.textContent = entry;

                    // Add click event to reuse the calculation
                    historyItem.addEventListener('click', () => {
                        // Extract the calculation from the history entry
                        const parts = entry.split('=');
                        if (parts.length >= 2) {
                            const calculation = parts[0].trim();
                            this.simulateCommand(calculation);
                        }
                    });

                    this.historyList.appendChild(historyItem);
                });
            } else {
                this.historyList.innerHTML = '<p class="empty-history">No calculations yet.</p>';
            }
        }
    }

    /**
     * Simulate a voice command (for example commands)
     * @param {string} command - The command to simulate
     */
    simulateCommand(command) {
        // Update command display
        this.updateCommandDisplay(`You said: ${command}`);

        // Trigger the calculation
        if (typeof calculator !== 'undefined') {
            calculator.processCommand(command);
        }
    }

    /**
     * Show a loading state in the result display
     */
    showLoading() {
        this.resultDisplay.textContent = 'Calculating...';
    }

    /**
     * Show an error in the result display
     * @param {string} error - The error message
     */
    showError(error) {
        // Format the error message
        let displayError = error;

        // If it's a network error, provide more helpful information
        if (error.includes('Network error') || error.includes('Failed to fetch')) {
            displayError = 'Network Error: Server may be unavailable. Please check if the server is running.';
            // Also show a toast with more detailed information
            this.showToast('Make sure the Flask server is running on port 5000', 'error');
        }

        // Update the display
        this.resultDisplay.textContent = displayError;
        this.resultDisplay.classList.add('shake');
        this.resultDisplay.style.color = 'var(--error-color)';

        // Remove shake class and reset color after animation completes
        setTimeout(() => {
            this.resultDisplay.classList.remove('shake');

            // Reset color after a bit longer
            setTimeout(() => {
                this.resultDisplay.style.color = '';
            }, 2000);
        }, 500);
    }

    /**
     * Show a success animation in the result display
     */
    showSuccess() {
        this.resultDisplay.classList.add('bounce');

        // Remove bounce class after animation completes
        setTimeout(() => {
            this.resultDisplay.classList.remove('bounce');
        }, 500);
    }

    /**
     * Show a toast notification
     * @param {string} message - The message to display
     * @param {string} type - The type of toast (success, error, warning, info)
     */
    showToast(message, type = 'info') {
        appSettings.showToast(message, type);
    }
}

// Create global UI instance
const ui = new UI();

// Load history when the page loads
document.addEventListener('DOMContentLoaded', () => {
    ui.loadHistory();
});
