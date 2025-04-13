/**
 * VocalCalc - Settings Module
 * Handles user settings and preferences
 */

class Settings {
    constructor() {
        // Default settings
        this.defaults = {
            theme: 'auto',
            language: 'en-US',
            confidenceThreshold: 0.5,
            speechRate: 1.0,
            speechPitch: 1.0,
            speechVolume: 1.0
        };
        
        // Load settings from localStorage or use defaults
        this.settings = this.loadSettings();
        
        // Initialize settings UI
        this.initSettingsUI();
        
        // Apply initial settings
        this.applySettings();
    }
    
    /**
     * Load settings from localStorage
     * @returns {Object} The loaded settings or defaults
     */
    loadSettings() {
        const savedSettings = localStorage.getItem('vocalcalc-settings');
        return savedSettings ? JSON.parse(savedSettings) : { ...this.defaults };
    }
    
    /**
     * Save settings to localStorage
     */
    saveSettings() {
        localStorage.setItem('vocalcalc-settings', JSON.stringify(this.settings));
    }
    
    /**
     * Initialize settings UI elements
     */
    initSettingsUI() {
        // Theme select
        this.themeSelect = document.getElementById('theme-select');
        this.themeSelect.value = this.settings.theme;
        this.themeSelect.addEventListener('change', () => {
            this.settings.theme = this.themeSelect.value;
            this.applyTheme();
            this.saveSettings();
        });
        
        // Language select
        this.languageSelect = document.getElementById('language-select');
        this.languageSelect.value = this.settings.language;
        this.languageSelect.addEventListener('change', () => {
            this.settings.language = this.languageSelect.value;
            this.saveSettings();
        });
        
        // Confidence threshold
        this.confidenceThreshold = document.getElementById('confidence-threshold');
        this.confidenceValue = document.getElementById('confidence-value');
        this.confidenceThreshold.value = this.settings.confidenceThreshold;
        this.confidenceValue.textContent = this.settings.confidenceThreshold;
        this.confidenceThreshold.addEventListener('input', () => {
            this.settings.confidenceThreshold = parseFloat(this.confidenceThreshold.value);
            this.confidenceValue.textContent = this.settings.confidenceThreshold;
            this.saveSettings();
        });
        
        // Speech rate
        this.speechRate = document.getElementById('speech-rate');
        this.rateValue = document.getElementById('rate-value');
        this.speechRate.value = this.settings.speechRate;
        this.rateValue.textContent = this.settings.speechRate.toFixed(1);
        this.speechRate.addEventListener('input', () => {
            this.settings.speechRate = parseFloat(this.speechRate.value);
            this.rateValue.textContent = this.settings.speechRate.toFixed(1);
            this.saveSettings();
        });
        
        // Speech pitch
        this.speechPitch = document.getElementById('speech-pitch');
        this.pitchValue = document.getElementById('pitch-value');
        this.speechPitch.value = this.settings.speechPitch;
        this.pitchValue.textContent = this.settings.speechPitch.toFixed(1);
        this.speechPitch.addEventListener('input', () => {
            this.settings.speechPitch = parseFloat(this.speechPitch.value);
            this.pitchValue.textContent = this.settings.speechPitch.toFixed(1);
            this.saveSettings();
        });
        
        // Speech volume
        this.speechVolume = document.getElementById('speech-volume');
        this.volumeValue = document.getElementById('volume-value');
        this.speechVolume.value = this.settings.speechVolume;
        this.volumeValue.textContent = this.settings.speechVolume.toFixed(1);
        this.speechVolume.addEventListener('input', () => {
            this.settings.speechVolume = parseFloat(this.speechVolume.value);
            this.volumeValue.textContent = this.settings.speechVolume.toFixed(1);
            this.saveSettings();
        });
        
        // Reset button
        const resetButton = document.getElementById('reset-settings');
        resetButton.addEventListener('click', () => {
            this.resetSettings();
        });
        
        // Save button
        const saveButton = document.getElementById('save-settings');
        saveButton.addEventListener('click', () => {
            this.saveSettings();
            this.closeSettingsModal();
            this.showToast('Settings saved successfully', 'success');
        });
    }
    
    /**
     * Apply all settings
     */
    applySettings() {
        this.applyTheme();
    }
    
    /**
     * Apply theme setting
     */
    applyTheme() {
        const theme = this.settings.theme;
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        
        if (theme === 'auto') {
            if (prefersDark) {
                document.body.classList.add('dark-theme');
                this.updateThemeIcon(true);
            } else {
                document.body.classList.remove('dark-theme');
                this.updateThemeIcon(false);
            }
        } else if (theme === 'dark') {
            document.body.classList.add('dark-theme');
            this.updateThemeIcon(true);
        } else {
            document.body.classList.remove('dark-theme');
            this.updateThemeIcon(false);
        }
    }
    
    /**
     * Update theme toggle icon
     * @param {boolean} isDark - Whether the theme is dark
     */
    updateThemeIcon(isDark) {
        const themeToggle = document.getElementById('theme-toggle');
        if (themeToggle) {
            const icon = themeToggle.querySelector('i');
            if (isDark) {
                icon.className = 'fas fa-sun';
            } else {
                icon.className = 'fas fa-moon';
            }
        }
    }
    
    /**
     * Reset settings to defaults
     */
    resetSettings() {
        this.settings = { ...this.defaults };
        
        // Update UI
        this.themeSelect.value = this.settings.theme;
        this.languageSelect.value = this.settings.language;
        
        this.confidenceThreshold.value = this.settings.confidenceThreshold;
        this.confidenceValue.textContent = this.settings.confidenceThreshold;
        
        this.speechRate.value = this.settings.speechRate;
        this.rateValue.textContent = this.settings.speechRate.toFixed(1);
        
        this.speechPitch.value = this.settings.speechPitch;
        this.pitchValue.textContent = this.settings.speechPitch.toFixed(1);
        
        this.speechVolume.value = this.settings.speechVolume;
        this.volumeValue.textContent = this.settings.speechVolume.toFixed(1);
        
        // Apply settings
        this.applySettings();
        
        // Show toast
        this.showToast('Settings reset to defaults', 'info');
    }
    
    /**
     * Close settings modal
     */
    closeSettingsModal() {
        const settingsModal = document.getElementById('settings-modal');
        settingsModal.classList.remove('active');
    }
    
    /**
     * Show a toast notification
     * @param {string} message - The message to display
     * @param {string} type - The type of toast (success, error, warning, info)
     */
    showToast(message, type = 'info') {
        const toastContainer = document.getElementById('toast-container');
        
        // Create toast element
        const toast = document.createElement('div');
        toast.className = `toast ${type}`;
        
        // Add icon based on type
        let icon;
        switch (type) {
            case 'success':
                icon = 'fa-check-circle';
                break;
            case 'error':
                icon = 'fa-exclamation-circle';
                break;
            case 'warning':
                icon = 'fa-exclamation-triangle';
                break;
            case 'info':
            default:
                icon = 'fa-info-circle';
                break;
        }
        
        toast.innerHTML = `
            <i class="fas ${icon}"></i>
            <span>${message}</span>
        `;
        
        // Add to container
        toastContainer.appendChild(toast);
        
        // Remove after 3 seconds
        setTimeout(() => {
            toast.classList.add('fade-out');
            setTimeout(() => {
                toastContainer.removeChild(toast);
            }, 300);
        }, 3000);
    }
    
    /**
     * Get a specific setting
     * @param {string} key - The setting key
     * @returns {any} The setting value
     */
    getSetting(key) {
        return this.settings[key];
    }
}

// Create global settings instance
const appSettings = new Settings();
