import unittest
import sys 
import os

# Add the parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


class TestApp(unittest.TestCase):

    def test_hello_route(self):
        client = app.test_client()
        res = client.get("/")

        # Replace assert with unittest assertions
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Hello, Kubernetes CI/CD", res.data)


if __name__ == "__main__":
    unittest.main()
