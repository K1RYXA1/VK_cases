import unittest

from custom_list import CustomList


class TestDecorator(unittest.TestCase):  # pylint: disable=too-many-public-methods

    def test_add_positive_int(self):
        i = 10
        ex = CustomList([5, 1, 3, 7, 22])
        result_1 = i+ex
        result_2 = ex+i

        self.assertEqual(result_1, CustomList([15, 11, 13, 17, 32]))
        self.assertEqual(result_2, CustomList([15, 11, 13, 17, 32]))

        self.assertEqual(ex, CustomList([5, 1, 3, 7, 22]))

        # экземпляр имеет 0 элементов
        ex = CustomList([])
        result_1 = i+ex
        result_2 = ex+i

        self.assertEqual(result_1, CustomList([]))
        self.assertEqual(result_2, CustomList([]))

        self.assertEqual(ex, CustomList([]))

    def test_add_negative_int(self):
        i = -10
        ex = CustomList([5, 1, 3, 7, 22])
        result_1 = i+ex
        result_2 = ex+i

        self.assertEqual(result_1, CustomList([-5, -9, -7, -3, 12]))
        self.assertEqual(result_2, CustomList([-5, -9, -7, -3, 12]))

        self.assertEqual(ex, CustomList([5, 1, 3, 7, 22]))

        # экземпляр имеет 0 элементов
        ex = CustomList([])
        result_1 = i+ex
        result_2 = ex+i

        self.assertEqual(result_1, CustomList([]))
        self.assertEqual(result_2, CustomList([]))

        self.assertEqual(ex, CustomList([]))

    def test_add_short_list(self):
        lst = [10]
        ex = CustomList([5, 1, 3, 7, 22])
        result_1 = lst+ex
        result_2 = ex+lst

        self.assertEqual(result_1, CustomList([15, 1, 3, 7, 22]))
        self.assertEqual(result_2, CustomList([15, 1, 3, 7, 22]))

        self.assertEqual(ex, CustomList([5, 1, 3, 7, 22]))

    def test_add_long_list(self):
        lst = [10, 20, 30]
        ex = CustomList([5, 1])
        result_1 = lst+ex
        result_2 = ex+lst

        self.assertEqual(result_1, CustomList([15, 21, 30]))
        self.assertEqual(result_2, CustomList([15, 21, 30]))

        self.assertEqual(ex, CustomList([5, 1]))

        # экземпляр имеет 0 элементов
        ex = CustomList([])
        result_1 = lst+ex
        result_2 = ex+lst

        self.assertEqual(result_1, CustomList([10, 20, 30]))
        self.assertEqual(result_2, CustomList([10, 20, 30]))

        self.assertEqual(ex, CustomList([]))

    def test_add_similar_list(self):
        lst = [10, 20]
        ex = CustomList([5, 1])
        result_1 = lst+ex
        result_2 = ex+lst

        self.assertEqual(result_1, CustomList([15, 21]))
        self.assertEqual(result_2, CustomList([15, 21]))

        self.assertEqual(ex, CustomList([5, 1]))

    def test_add_empty_list(self):
        lst = []
        ex = CustomList([5, 1, 3, 7, 22])
        result_1 = lst+ex
        result_2 = ex+lst

        self.assertEqual(result_1, CustomList([5, 1, 3, 7, 22]))
        self.assertEqual(result_2, CustomList([5, 1, 3, 7, 22]))

        self.assertEqual(ex, CustomList([5, 1, 3, 7, 22]))

    def test_add_short_customlist(self):
        a = CustomList([10])
        ex = CustomList([5, 1, 3, 7, 22])
        result_1 = a+ex
        result_2 = ex+a

        self.assertEqual(result_1, CustomList([15, 1, 3, 7, 22]))
        self.assertEqual(result_2, CustomList([15, 1, 3, 7, 22]))

        self.assertEqual(ex, CustomList([5, 1, 3, 7, 22]))
        self.assertEqual(a, CustomList([10]))

    def test_add_long_customlist(self):
        a = CustomList([10, 20, 30])
        ex = CustomList([5, 1])
        result_1 = a+ex
        result_2 = ex+a

        self.assertEqual(result_1, CustomList([15, 21, 30]))
        self.assertEqual(result_2, CustomList([15, 21, 30]))

        self.assertEqual(ex, CustomList([5, 1]))
        self.assertEqual(a, CustomList([10, 20, 30]))

    def test_add_similar_customlist(self):
        a = CustomList([10, 20])
        ex = CustomList([5, 1])
        result_1 = a+ex
        result_2 = ex+a

        self.assertEqual(result_1, CustomList([15, 21]))
        self.assertEqual(result_2, CustomList([15, 21]))

        self.assertEqual(ex, CustomList([5, 1]))
        self.assertEqual(a, CustomList([10, 20]))

    def test_add_empty_customlist(self):
        a = CustomList([])
        ex = CustomList([5, 1, 3, 7, 22])
        result_1 = a+ex
        result_2 = ex+a

        self.assertEqual(result_1, CustomList([5, 1, 3, 7, 22]))
        self.assertEqual(result_2, CustomList([5, 1, 3, 7, 22]))

        self.assertEqual(ex, CustomList([5, 1, 3, 7, 22]))
        self.assertEqual(a, CustomList([]))

    def test_sub_positive_int(self):
        i = 10
        ex = CustomList([5, 1, 3, 7, 22])
        result_1 = ex-i
        result_2 = i-ex

        self.assertEqual(result_1, CustomList([-5, -9, -7, -3, 12]))
        self.assertEqual(result_2, CustomList([5, 9, 7, 3, -12]))

        self.assertEqual(ex, CustomList([5, 1, 3, 7, 22]))

        # экземпляр имеет 0 элементов
        ex = CustomList([])
        result_1 = i-ex
        result_2 = ex-i

        self.assertEqual(result_1, CustomList([]))
        self.assertEqual(result_2, CustomList([]))

        self.assertEqual(ex, CustomList([]))

    def test_sub_negative_int(self):
        i = -10
        ex = CustomList([5, 1, 3, 7, 22])
        result_1 = i-ex
        result_2 = ex-i

        self.assertEqual(result_1, CustomList([-15, -11, -13, -17, -32]))
        self.assertEqual(result_2, CustomList([15, 11, 13, 17, 32]))

        self.assertEqual(ex, CustomList([5, 1, 3, 7, 22]))

        # экземпляр имеет 0 элементов
        ex = CustomList([])
        result_1 = i-ex
        result_2 = ex-i

        self.assertEqual(result_1, CustomList([]))
        self.assertEqual(result_2, CustomList([]))

        self.assertEqual(ex, CustomList([]))

    def test_sub_short_list(self):
        lst = [10]
        ex = CustomList([5, 1, 3, 7, 22])
        result_1 = lst-ex
        result_2 = ex-lst

        self.assertEqual(result_1, CustomList([5, -1, -3, -7, -22]))
        self.assertEqual(result_2, CustomList([-5, 1, 3, 7, 22]))

        self.assertEqual(ex, CustomList([5, 1, 3, 7, 22]))

    def test_sub_long_list(self):
        lst = [10, 20, 30]
        ex = CustomList([5, 1])
        result_1 = lst-ex
        result_2 = ex-lst

        self.assertEqual(result_1, CustomList([5, 19, 30]))
        self.assertEqual(result_2, CustomList([-5, -19, -30]))

        self.assertEqual(ex, CustomList([5, 1]))

        # экземпляр имеет 0 элементов
        ex = CustomList([])
        result_1 = lst-ex
        result_2 = ex-lst

        self.assertEqual(result_1, CustomList([10, 20, 30]))
        self.assertEqual(result_2, CustomList([-10, -20, -30]))

        self.assertEqual(ex, CustomList([]))

    def test_sub_similar_list(self):
        lst = [10, 20]
        ex = CustomList([5, 1])
        result_1 = lst-ex
        result_2 = ex-lst

        self.assertEqual(result_1, CustomList([5, 19]))
        self.assertEqual(result_2, CustomList([-5, -19]))

        self.assertEqual(ex, CustomList([5, 1]))

    def test_sub_empty_list(self):
        lst = []
        ex = CustomList([5, 1, 3, 7, 22])
        result_1 = lst-ex
        result_2 = ex-lst

        self.assertEqual(result_1, CustomList([-5, -1, -3, -7, -22]))
        self.assertEqual(result_2, CustomList([5, 1, 3, 7, 22]))

        self.assertEqual(ex, CustomList([5, 1, 3, 7, 22]))

    def test_sub_short_customlist(self):
        a = CustomList([10])
        ex = CustomList([5, 1, 3, 7, 22])
        result_1 = a-ex
        result_2 = ex-a

        self.assertEqual(result_1, CustomList([5, -1, -3, -7, -22]))
        self.assertEqual(result_2, CustomList([-5, 1, 3, 7, 22]))

        self.assertEqual(ex, CustomList([5, 1, 3, 7, 22]))
        self.assertEqual(a, CustomList([10]))

    def test_sub_long_customlist(self):
        a = CustomList([10, 20, 30])
        ex = CustomList([5, 1])
        result_1 = a-ex
        result_2 = ex-a

        self.assertEqual(result_1, CustomList([5, 19, 30]))
        self.assertEqual(result_2, CustomList([-5, -19, -30]))

        self.assertEqual(ex, CustomList([5, 1]))
        self.assertEqual(a, CustomList([10, 20, 30]))

    def test_sub_similar_customlist(self):
        a = CustomList([10, 20])
        ex = CustomList([5, 1])
        result_1 = a-ex
        result_2 = ex-a

        self.assertEqual(result_1, CustomList([5, 19]))
        self.assertEqual(result_2, CustomList([-5, -19]))

        self.assertEqual(ex, CustomList([5, 1]))
        self.assertEqual(a, CustomList([10, 20]))

    def test_sub_empty_customlist(self):
        a = CustomList([])
        ex = CustomList([5, 1, 3, 7, 22])
        result_1 = a-ex
        result_2 = ex-a

        self.assertEqual(result_1, CustomList([-5, -1, -3, -7, -22]))
        self.assertEqual(result_2, CustomList([5, 1, 3, 7, 22]))

        self.assertEqual(ex, CustomList([5, 1, 3, 7, 22]))
        self.assertEqual(a, CustomList([]))

    def test_less_than(self):
        # экземпляр а меньше по длине, но больше по сумме
        a = CustomList([1000])
        ex = CustomList([10, 1, 3])

        self.assertTrue(ex < a)
        self.assertFalse(a < ex)

        # экземпляр а равен по длине, но меньше по сумме
        a = CustomList([1, 2, 3])

        self.assertTrue(a < ex)
        self.assertFalse(ex < a)

        # экземпляр а больше по длине, но меньше по сумме
        a = CustomList([1, 2, 3, 2])

        self.assertTrue(a < ex)

        # экземпляр а больше по длине и больше по сумме
        a = CustomList([1, 2, 3, 20])

        self.assertTrue(ex < a)

        # экземпляр а меньше по длине, но равен по сумме
        a = CustomList([7, 7])

        self.assertFalse(ex < a)

        # экземпляр а имеет 0 элементов
        a = CustomList([])

        self.assertTrue(a < ex)

    def test_less_or_equel(self):
        # экземпляр а меньше по длине, но больше по сумме
        a = CustomList([1000])
        ex = CustomList([10, 1, 3])

        self.assertTrue(ex <= a)
        self.assertFalse(a <= ex)

        # экземпляр а равен по длине, но меньше по сумме
        a = CustomList([1, 2, 3])

        self.assertTrue(a <= ex)
        self.assertFalse(ex <= a)

        # экземпляр а равен по длине и равен по сумме
        a = CustomList([11, 0, 3])

        self.assertTrue(a <= ex)
        self.assertTrue(ex <= a)

        # экземпляр а меньше по длине, но равен по сумме
        a = CustomList([7, 7])

        self.assertTrue(ex <= a)

        # экземпляр а имеет 0 элементов
        a = CustomList([])

        self.assertTrue(a <= ex)

    def test_equel(self):
        # экземпляр а меньше по длине, но больше по сумме
        a = CustomList([1000])
        ex = CustomList([10, 1, 3])

        self.assertFalse(a == ex)

        # экземпляр а идентичен
        a = CustomList([10, 1, 3])

        self.assertTrue(a == ex)

        # экземпляр а равен по длине и равен по сумме
        a = CustomList([11, 0, 3])

        self.assertTrue(a == ex)

        # экземпляр а меньше по длине, но равен по сумме
        a = CustomList([14])

        self.assertTrue(a == ex)

        # экземпляр а больше по длине, но равен по сумме
        a = CustomList([5, 1, 2, 5, 1])

        self.assertTrue(a == ex)

        # экземпляр а имеет 0 элементов
        a = CustomList([])

        self.assertFalse(ex == a)

    def test_not_equel(self):
        # экземпляр а меньше по длине, но больше по сумме
        a = CustomList([1000])
        ex = CustomList([10, 1, 3])

        self.assertTrue(a != ex)

        # экземпляр а идентичен
        a = CustomList([10, 1, 3])

        self.assertFalse(a != ex)

        # экземпляр а равен по длине и равен по сумме
        a = CustomList([11, 0, 3])

        self.assertFalse(a != ex)

        # экземпляр а меньше по длине, но равен по сумме
        a = CustomList([14])

        self.assertFalse(a != ex)

        # экземпляр а больше по длине, но равен по сумме
        a = CustomList([5, 1, 2, 5, 1])

        self.assertFalse(a != ex)

        # экземпляр а больше по длине и больше по сумме
        a = CustomList([10, 1, 2, 5, 1])

        self.assertTrue(a != ex)

        # экземпляр а имеет 0 элементов
        a = CustomList([])

        self.assertTrue(ex != a)

    def test_great_or_equel(self):
        # экземпляр а меньше по длине, но больше по сумме
        a = CustomList([1000])
        ex = CustomList([10, 1, 3])

        self.assertTrue(a >= ex)
        self.assertFalse(ex >= a)

        # экземпляр а равен по длине, но меньше по сумме
        a = CustomList([1, 2, 3])

        self.assertTrue(ex >= a)
        self.assertFalse(a >= ex)

        # экземпляр а равен по длине и равен по сумме
        a = CustomList([11, 0, 3])

        self.assertTrue(a >= ex)
        self.assertTrue(ex >= a)

        # экземпляр а меньше по длине, но равен по сумме
        a = CustomList([14])

        self.assertTrue(a >= ex)

        # экземпляр а имеет 0 элементов
        a = CustomList([])

        self.assertTrue(ex >= a)

    def test_great_than(self):
        # экземпляр а меньше по длине, но больше по сумме
        a = CustomList([1000])
        ex = CustomList([10, 1, 3])

        self.assertTrue(a > ex)
        self.assertFalse(ex > a)

        # экземпляр а равен по длине, но меньше по сумме
        a = CustomList([1, 2, 3])

        self.assertTrue(ex > a)
        self.assertFalse(a > ex)

        # экземпляр а больше по длине, но меньше по сумме
        a = CustomList([1, 2, 3, 2])

        self.assertTrue(ex > a)

        # экземпляр а больше по длине и больше по сумме
        a = CustomList([1, 2, 3, 20])

        self.assertTrue(a > ex)

        # экземпляр а меньше по длине, но равен по сумме
        a = CustomList([7, 7])

        self.assertFalse(ex > a)

        # экземпляр а имеет 0 элементов
        a = CustomList([])

        self.assertTrue(ex > a)

    def test_str_format(self):
        a = CustomList([1, 2, 3])

        self.assertEqual(str(a), 'Элементы: 1, 2, 3; Сумма элементов: 6')

        a = CustomList([])

        self.assertEqual(str(a), 'Элементы: ; Сумма элементов: 0')
