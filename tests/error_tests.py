import unittest
from bookshelf import app


class ErrorTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_pagenotfound_statuscode(self):
        result = self.app.get('/bg/missing-page/')

        self.assertEqual(result.status_code, 404)

    def test_pagenotfound_data(self):
        result = self.app.get('/bg/missing-page/')

        self.assertIn('Not Found', result.data.decode('utf-8'))

    def test_unhandledexception_code(self):
        result = self.app.put('/books')

        self.assertEqual(result.status_code, 500)

    def test_unhandledexception_data(self):
        result = self.app.put('/books')

        self.assertIn('Something Went Wrong', result.data.decode('utf-8'))
