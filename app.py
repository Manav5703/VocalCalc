"""Main application module for VocalCalc."""

import os
from flask import Flask, render_template, request, jsonify, make_response
from flask_cors import CORS
from command_parser import CommandParser

# Create the Flask application
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # Enable CORS for API routes

# Add CORS preflight handler
@app.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS')
        return response

# Create command parser instance
command_parser = CommandParser()

@app.route('/')
def index():
    """Render the landing page."""
    return render_template('landing.html')

@app.route('/calculator')
def calculator():
    """Render the calculator application page."""
    return render_template('index.html')

@app.route('/api/calculate', methods=['POST'])
def calculate():
    """API endpoint to process calculation requests."""
    try:
        data = request.get_json()

        if not data:
            response = make_response(jsonify({'error': 'Invalid JSON data'}), 400)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

        if 'command' not in data:
            response = make_response(jsonify({'error': 'No command provided'}), 400)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

        if not data['command'] or not isinstance(data['command'], str):
            response = make_response(jsonify({'error': 'Invalid command format'}), 400)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

        command = data['command'].strip()
        if not command:
            response = make_response(jsonify({'error': 'Empty command provided'}), 400)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

        result, history_entry = command_parser.parse_command(command)

        # Format the response
        response_data = {
            'command': command,
            'result': result,
            'history_entry': history_entry
        }

        response = make_response(jsonify(response_data))
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Content-Type', 'application/json')
        return response
    except Exception as e:
        app.logger.error(f"Error processing calculation: {str(e)}")
        response = make_response(jsonify({'error': f'Server error: {str(e)}'}), 500)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    response = make_response(jsonify({'status': 'healthy'}))
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Content-Type', 'application/json')
    return response

if __name__ == '__main__':
    # Get port from environment variable or use 5000 as default
    port = int(os.environ.get('PORT', 5000))
    # Set debug mode based on environment
    debug_mode = os.environ.get('FLASK_ENV', 'development') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
