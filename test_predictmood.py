import unittest
from unittest import mock

from predictmood import predict_message_mood


class TestPredictMessageMood(unittest.TestCase):

    def test_less_lower_limit(self):
        with mock.patch("predictmood.SomeModel") as mock_model:
            mock_model.return_value.predict.return_value = 0.2
            mood = predict_message_mood("Чапаев и пустота")

            # проверяем пределы по умолчанию
            self.assertEqual(mood, "неуд")
            calls = [
                mock.call("Чапаев и пустота")
            ]
            self.assertEqual(calls, mock_model.return_value.predict.mock_calls)

            mood = predict_message_mood("Чапаев и Чапаев", 0.25, 0.6)

            # проверяем заданные нами пределы
            self.assertEqual(mood, "неуд")
            calls = [
                mock.call("Чапаев и пустота"),
                mock.call("Чапаев и Чапаев")
            ]
            self.assertEqual(calls, mock_model.return_value.predict.mock_calls)

            mock_model.return_value.predict.return_value = 1.199999999
            mood = predict_message_mood("Что?", 1.2, 1.6)

            # проверяем значение prediction с точностью 9 знаков
            self.assertEqual(mood, "неуд")

    def test_lower_limit(self):
        with mock.patch("predictmood.SomeModel") as mock_model:
            mock_model.return_value.predict.return_value = 0.25
            mood = predict_message_mood("Что?", 0.25, 0.6)

            # проверяем значение prediction равное нижнему пределу
            self.assertEqual(mood, "норм")
            calls = [
                mock.call("Что?")
            ]
            self.assertEqual(calls, mock_model.return_value.predict.mock_calls)

            mock_model.return_value.predict.return_value = 1.1999999999
            mood = predict_message_mood("Что?", 1.2, 1.6)

            # проверяем значение prediction с точностью 10 знаков
            self.assertEqual(mood, "норм")

            mock_model.return_value.predict.return_value = 1.2000000001
            mood = predict_message_mood("Что?", 1.2, 1.6)

            # проверяем значение prediction с точностью 10 знаков
            self.assertEqual(mood, "норм")

    def test_high_upper_limit(self):
        with mock.patch("predictmood.SomeModel") as mock_model:
            mock_model.return_value.predict.return_value = 0.8
            mood = predict_message_mood("Пустота", 0.7, 0.75)

            # проверяем значение prediction больше верхнего предела
            self.assertEqual(mood, "отл")
            calls = [
                mock.call("Пустота")
            ]
            self.assertEqual(calls, mock_model.return_value.predict.mock_calls)

            mock_model.return_value.predict.return_value = 1.201000001
            mood = predict_message_mood("Что?", 1.2, 1.201)

            # проверяем значение prediction с точностью 9 знаков
            self.assertEqual(mood, "отл")

    def test_upper_limit(self):
        with mock.patch("predictmood.SomeModel") as mock_model:
            mock_model.return_value.predict.return_value = 0.8
            mood = predict_message_mood("Пустота", 0.7, 0.8)

            # проверяем значение prediction равное верхнему пределу
            self.assertEqual(mood, "норм")
            calls = [
                mock.call("Пустота")
            ]
            self.assertEqual(calls, mock_model.return_value.predict.mock_calls)

            mock_model.return_value.predict.return_value = 1.2010000001
            mood = predict_message_mood("Что?", 1.2, 1.201)

            # проверяем значение prediction с точностью 10 знаков
            self.assertEqual(mood, "норм")

    def test_within_limit(self):
        with mock.patch("predictmood.SomeModel") as mock_model:
            mock_model.return_value.predict.return_value = 0.75
            mood = predict_message_mood("Не пустота", 0.7, 0.8)

            # проверяем значение prediction внутри заданных пределов
            self.assertEqual(mood, "норм")
            calls = [
                mock.call("Не пустота")
            ]
            self.assertEqual(calls, mock_model.return_value.predict.mock_calls)
