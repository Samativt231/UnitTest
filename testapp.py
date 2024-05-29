import unittest
from app import app

class TestVolumeCalculations(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_connection(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Вычисление объемов геометрических фигур".encode('utf-8'), response.data)

    def test_cube_volume(self):
        response = self.app.post('/', data=dict(
            figure='cube',
            param1='3',
            param2='',
            precision='2'
        ))
        self.assertIn(b'27.00', response.data)

    def test_sphere_volume(self):
        response = self.app.post('/', data=dict(
            figure='sphere',
            param1='2',
            param2='',
            precision='2'
        ))
        self.assertIn(b'33.51', response.data)

    def test_cylinder_volume(self):
        response = self.app.post('/', data=dict(
            figure='cylinder',
            param1='2',
            param2='5',
            precision='2'
        ))
        self.assertIn(b'62.83', response.data)

    def test_missing_param2_for_cylinder(self):
        response = self.app.post('/', data=dict(
            figure='cylinder',
            param1='2',
            param2='',
            precision='2'
        ))
        self.assertIn("Введите второй параметр для цилиндра.".encode('utf-8'), response.data)