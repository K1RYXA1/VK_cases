import unittest

from custommeta import CustomClass, MyClass


class TestCustomMeta(unittest.TestCase):

    def test_public_cls_attr(self):

        self.assertEqual(CustomClass.custom_x, 50)

        with self.assertRaises(AttributeError):
            print(CustomClass.x)

    def test_protected_cls_attr(self):

        self.assertEqual(MyClass.custom__protect, 'cls_protect')

        with self.assertRaises(AttributeError):
            print(CustomClass._protect)

    def test_private_cls_attr(self):

        self.assertEqual(MyClass.custom__MyClass__private, 'cls_private')

        with self.assertRaises(AttributeError):
            print(CustomClass._MyClass__private)

    def test_dynamic_cls_attr(self):
        CustomClass.new_attr = 'new'

        self.assertEqual(CustomClass.custom_new_attr, 'new')

        with self.assertRaises(AttributeError):
            print(CustomClass.new_attr)

    def test_public_obj_attr(self):

        inst = CustomClass()
        self.assertEqual(inst.custom_val, 99)

        with self.assertRaises(AttributeError):
            print(inst.val)

        inst = CustomClass('wow')
        self.assertEqual(inst.custom_val, 'wow')

        with self.assertRaises(AttributeError):
            print(inst.val)

    def test_protected_obj_attr(self):

        inst = MyClass()

        self.assertEqual(inst.custom__obj_protect, 'obj_protect')

        with self.assertRaises(AttributeError):
            print(inst._obj_protect)

    def test_private_obj_attr(self):

        inst = MyClass()

        self.assertEqual(inst.custom__MyClass__obj_private, 'obj_private')

        with self.assertRaises(AttributeError):
            print(inst._MyClass__obj_private)

    def test_dynamic_obj_attr(self):

        inst = CustomClass()
        inst.dynamic_attr = 'I am new'

        self.assertEqual(inst.custom_dynamic_attr, 'I am new')

        with self.assertRaises(AttributeError):
            print(inst.dynamic_attr)

    def test_method(self):

        inst = CustomClass()
        self.assertEqual(inst.custom_line(), 100)

        with self.assertRaises(AttributeError):
            inst.line()

    def test_magic_method(self):

        inst = CustomClass()
        self.assertEqual(str(inst), "Custom_by_metaclass")

    def test_error(self):

        inst = CustomClass()

        with self.assertRaises(AttributeError):
            print(inst.yyy)
