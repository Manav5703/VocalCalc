import unittest

# Discover and run all tests
loader = unittest.TestLoader()
start_dir = '.'
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner()
runner.run(suite)
