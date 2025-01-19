import unittest
from unittest import mock

from gen import filter_file


class TestFilterFile(unittest.TestCase):

    def test_upper_case_in_file(self):
        file = 'Музыка громче\nглаза закрыты\nЭто НОНСТоП ночью открытий\nДелай что хОЧЕшЬ я забываюсь'
        mock_open = mock.mock_open(read_data=file)

        with mock.patch("builtins.open", mock_open):
            search_words = ['нонстоп', 'хочешь']
            stop_words = ['хочешь']
            result = filter_file("MyFile", search_words, stop_words)

            self.assertEqual(next(result), 'Это НОНСТоП ночью открытий')

    def test_upper_case_in_search(self):
        file = 'Музыка громче\nглаза закрыты\nЭто нонстоп ночью открытий\nДелай что хочешь я забываюсь'
        mock_open = mock.mock_open(read_data=file)

        with mock.patch("builtins.open", mock_open):
            search_words = ['НОНстоп', 'ХОЧЕШЬ']
            stop_words = ['хочешь']
            result = filter_file("MyFile", search_words, stop_words)

            self.assertEqual(next(result), 'Это нонстоп ночью открытий')

    def test_upper_case_in_stop(self):
        file = 'Музыка громче\nглаза закрыты\nЭто нонстоп ночью открытий\nДелай что хочешь я забываюсь'
        mock_open = mock.mock_open(read_data=file)

        with mock.patch("builtins.open", mock_open):
            search_words = ['нонстоп', 'хочешь']
            stop_words = ['ХОЧЕШЬ']
            result = filter_file("MyFile", search_words, stop_words)

            self.assertEqual(next(result), 'Это нонстоп ночью открытий')

    def test_substring(self):
        file = 'Музыка громче\nглаза закрыты\nЭто нонстоп ночью открытий\nДелай что хочешь я забываюсь'
        mock_open = mock.mock_open(read_data=file)

        with mock.patch("builtins.open", mock_open):
            search_words = ['нон', 'хочешь']
            result = filter_file("MyFile", search_words)

            self.assertEqual(next(result), 'Делай что хочешь я забываюсь')

    def test_double_entry(self):
        file = 'Музыка громче\nглаза закрыты\nЭто нонстоп ночью открытий\nДелай что хочешь я забываюсь'
        mock_open = mock.mock_open(read_data=file)

        with mock.patch("builtins.open", mock_open):
            search_words = ['нонстоп', 'ночью', 'хочешь']
            result = filter_file("MyFile", search_words)

            self.assertEqual(next(result), 'Это нонстоп ночью открытий')
            self.assertEqual(next(result), 'Делай что хочешь я забываюсь')

    def test_stop_words(self):
        file = 'Музыка громче\nглаза закрыты\nЭто нонстоп ночью открытий\nДелай что хочешь я забываюсь'
        mock_open = mock.mock_open(read_data=file)

        with mock.patch("builtins.open", mock_open):
            search_words = ['нонстоп', 'хочешь']
            stop_words = ['ночью']
            result = filter_file("MyFile", search_words, stop_words)

            self.assertEqual(next(result), 'Делай что хочешь я забываюсь')

    def test_stop_iteration(self):
        file = 'Музыка громче\nглаза закрыты\nЭто нонстоп ночью открытий\nДелай что хочешь я забываюсь'
        mock_open = mock.mock_open(read_data=file)

        # проверяем исключение при завершении работы генератора
        with mock.patch("builtins.open", mock_open):
            search_words = []

            with self.assertRaises(StopIteration):
                result = filter_file("MyFile", search_words)
                next(result)

        # проверяем исключение при завершении работы генератора с непустым списком search_words
        with mock.patch("builtins.open", mock_open):
            search_words = ['нонстоп']
            result = filter_file("MyFile", search_words)
            next(result)

            with self.assertRaises(StopIteration):
                next(result)

    def test_overlap_search_and_stop(self):
        file = 'Музыка громче\nглаза закрыты\nЭто нонстоп ночью открытий\nДелай что хочешь я забываюсь'
        mock_open = mock.mock_open(read_data=file)

        with mock.patch("builtins.open", mock_open):
            search_words = ['нонстоп', 'глаза', 'хочешь']
            stop_words = ['нонстоп', 'глаза', 'хочешь']
            result = filter_file("MyFile", search_words, stop_words)

            with self.assertRaises(StopIteration):
                next(result)

    def test_diff_search_word_order(self):
        file = 'Музыка громче\nглаза закрыты\nЭто нонстоп ночью открытий\nДелай что хочешь я забываюсь'
        mock_open = mock.mock_open(read_data=file)

        with mock.patch("builtins.open", mock_open):
            search_words = ['нонстоп', 'глаза', 'музыка']
            result = filter_file("MyFile", search_words)

            self.assertEqual(next(result), 'Музыка громче')
            self.assertEqual(next(result), 'глаза закрыты')
            self.assertEqual(next(result), 'Это нонстоп ночью открытий')

    def test_value_error(self):
        file = 'Музыка громче\nглаза закрыты\nЭто нонстоп ночью открытий\nДелай что хочешь я забываюсь'
        mock_open = mock.mock_open(read_data=file)

        # проверяем работу исключения, если в качестве аргумента переданы не название файла или не файловый объект
        with mock.patch("builtins.open", mock_open):
            search_words = []

            with self.assertRaises(ValueError):
                result = filter_file(55, search_words)
                next(result)

    def test_full_sentance_in_search(self):
        file = 'Музыка громче\nглаза закрыты\nЭто нонстоп ночью открытий\nДелай что хочешь я забываюсь'
        mock_open = mock.mock_open(read_data=file)

        with mock.patch("builtins.open", mock_open):
            search_words = ['музыка', 'громче', 'что']
            result = filter_file("MyFile", search_words)

            self.assertEqual(next(result), 'Музыка громче')
            self.assertEqual(next(result), 'Делай что хочешь я забываюсь')

    def test_full_sentance_in_stop(self):
        file = 'Музыка громче\nглаза закрыты\nЭто нонстоп ночью открытий\nДелай что хочешь я забываюсь'
        mock_open = mock.mock_open(read_data=file)

        with mock.patch("builtins.open", mock_open):
            search_words = ['громче', 'что']
            stop_words = ['музыка', 'громче']
            result = filter_file("MyFile", search_words, stop_words)

            self.assertEqual(next(result), 'Делай что хочешь я забываюсь')

    def test_repeat_words_in_search(self):
        file = 'Музыка громче\nглаза закрыты\nЭто нонстоп ночью открытий\nДелай что хочешь я забываюсь'
        mock_open = mock.mock_open(read_data=file)

        with mock.patch("builtins.open", mock_open):
            search_words = ['громче', 'что', 'громче']
            result = filter_file("MyFile", search_words)

            self.assertEqual(next(result), 'Музыка громче')
            self.assertEqual(next(result), 'Делай что хочешь я забываюсь')
