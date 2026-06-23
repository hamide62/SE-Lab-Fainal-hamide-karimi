import unittest
from main import app

class TestStudentAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_all_students(self):
        # Arrange: آماده‌سازی (در اینجا تنظیمات اولیه در setUp انجام شده)
        
        # Act: انجام عملیات (درخواست گرفتن لیست دانشجویان)
        response = self.app.get('/api/students')
        
        # Assert: بررسی نتیجه (آیا کد وضعیت 200 یا همان موفقیت است؟)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Ali', response.data)

if __name__ == '__main__':
    unittest.main()
