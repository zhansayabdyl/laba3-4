import unittest
from app import app


class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Ипотечный калькулятор'.encode('utf-8'), response.data)

    def test_calculate_mortgage(self):
        response = self.app.post('/calculate', data={'principal': 100000, 'annual_rate': 5, 'years': 10})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Ежемесячный платеж:'.encode('utf-8'), response.data)

    def test_invalid_input(self):
        response = self.app.post('/calculate', data={'principal': 'abc', 'annual_rate': 'def', 'years': 'xyz'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Пожалуйста, введите корректные значения.'.encode('utf-8'), response.data)


if __name__ == '__main__':
    unittest.main()
