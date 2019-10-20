#/usr/bin/python3
import unittest
from models.base import Base

class BaseTestClass(unittest.TestCase):

    """Unittest cases for Base class - test task 1 """

    def test_ClassBase(self):
        """ test is instance of the class Object """
        b0 = Base(9)
        self.assertIsInstance(b0, object)

    def test_ID(self):
        """test without "id" - increase __nb_objects"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_ID2(self):
        """test "id" 8"""
        b2 = Base(8)
        self.assertEqual(b2.id, 8)

    def test_ID_None(self):
        """test 'id' None - increase __nb_objects"""
        b3 = Base(None)
        self.assertEqual(b3.id, 2)
        self.assertEqual(b3.id, Base._Base__nb_objects)

    def test_Id_Test(self):
        b4 = Base("Yenn")
        self.assertEqual(b4.id, "Yenn")

    def test_Id_No_Equal(self):
        """test 'id' It is not a number and undefined"""
        b5 = Base(float('nan'))
        self.assertNotEqual(b5.id, b5.id) 

