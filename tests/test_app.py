import unittest
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