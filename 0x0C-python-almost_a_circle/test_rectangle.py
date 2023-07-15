#!/usr/bin/python3
""" Module for testing the Rectangle class """
import unittest
import os
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleMethods(unittest.TestCase):
    """ Test suite for the Rectangle class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_new_rectangle(self):
        """ Test creating a new rectangle """
        new = Rectangle(1, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_new_rectangle_2(self):
        """ Test creating a new rectangle with all attributes """
        new = Rectangle(2, 3, 5, 5, 4)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_new_rectangles(self):
        """ Test creating new rectangles """
        new = Rectangle(1, 1)
        new2 = Rectangle(1, 1)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def test_is_Base_instance(self):
        """ Test if Rectangle is an instance of Base """
        new = Rectangle(1, 1)
        self.assertEqual(True, isinstance(new, Base))

    def test_incorrect_amount_attrs(self):
        """ Test error raised when incorrect number of arguments is passed """
        with self.assertRaises(TypeError):
            new = Rectangle(1)

    def test_incorrect_amount_attrs_1(self):
        """ Test error raised when no arguments are passed """
        with self.assertRaises(TypeError):
            new = Rectangle()

    def test_access_private_attrs(self):
        """ Test accessing private attributes """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__width

    def test_access_private_attrs_2(self):
        """ Test accessing private attributes """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__height

    def test_access_private_attrs_3(self):
        """ Test accessing private attributes """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__x

    def test_access_private_attrs_4(self):
        """ Test accessing private attributes """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__y

    def test_valid_attrs(self):
        """ Test passing a string value """
        with self.assertRaises(TypeError):
            new = Rectangle("2", 2, 2, 2, 2)

    def test_valid_attrs_2(self):
        """ Test passing a string value """
        with self.assertRaises(TypeError):
            new = Rectangle(2, "2", 2, 2, 2)

    def test_valid_attrs_3(self):
        """ Test passing a string value """
        with self.assertRaises(TypeError):
            new = Rectangle(2, 2, "2", 2, 2)

    def test_valid_attrs_4(self):
        """ Test passing a string value """
        with self.assertRaises(TypeError):
            new = Rectangle(2, 2, 2, "2", 2)

    def test_value_attrs(self):
        """ Test passing invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(0, 1)

    def test_value_attrs_1(self):
        """ Test passing invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(1, 0)

    def test_value_attrs_2(self):
        """ Test passing invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(1, 1, -1)

    def test_value_attrs_3(self):
        """ Test passing invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(1, 1, 1, -1)

    def test_area(self):
        """ Test the return value of the area method """
        new = Rectangle(4, 5)
        self.assertEqual(new.area(), 20)

    def test_area_2(self):
        """ Test the return value of the area method """
        new = Rectangle(2, 2)
        self.assertEqual(new.area(), 4)
        new.width = 5
        self.assertEqual(new.area(), 10)
        new.height = 5
        self.assertEqual(new.area(), 25)

    def test_area_3(self):
        """ Test the return value of the area method """
        new = Rectangle(3, 8)
        self.assertEqual(new.area(), 24)
        new2 = Rectangle(10, 10)
        self.assertEqual(new2.area(), 100)

    def test_display(self):
        """ Test the printed string """
        r1 = Rectangle(2, 5)
        res = "##\n##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_2(self):
        """ Test the printed string """
        r1 = Rectangle(2, 2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.width = 5
        res = "#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_str(self):
        """ Test the __str__ return value """
        r1 = Rectangle(2, 5, 2, 4)
        res = "[Rectangle] (1) 2/4 - 2/5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_2(self):
        """ Test the __str__ return value """
        r1 = Rectangle(3, 2, 8, 8, 10)
        res = "[Rectangle] (10) 8/8 - 3/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r1.id = 1
        r1.width = 7
        r1.height = 15
        res = "[Rectangle] (1) 8/8 - 7/15\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_3(self):
        """ Test the __str__ return value """
        r1 = Rectangle(5, 10)
        res = "[Rectangle] (1) 0/0 - 5/10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
