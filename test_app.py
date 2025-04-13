import unittest
import json
from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        """Test that the home page loads correctly."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_health_check(self):
        """Test the health check endpoint."""
        response = self.app.get('/api/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')

    def test_calculate_endpoint_addition(self):
        """Test the calculate endpoint with an addition command."""
        response = self.app.post('/api/calculate',
                                json={'command': 'what is 5 plus 3'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['result'], 8)
        self.assertEqual(data['command'], 'what is 5 plus 3')
        self.assertEqual(data['history_entry'], '5 + 3 = 8')

    def test_calculate_endpoint_error(self):
        """Test the calculate endpoint with an invalid command."""
        response = self.app.post('/api/calculate',
                                json={'command': 'invalid command'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['result'], 'Invalid command')

    def test_calculate_endpoint_missing_command(self):
        """Test the calculate endpoint with a missing command."""
        response = self.app.post('/api/calculate', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'Invalid JSON data')

if __name__ == '__main__':
    unittest.main()
