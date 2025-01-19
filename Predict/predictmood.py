from random import randint, random

# Функция оценки сообщения
# Реализовать функцию predict_message_mood, которая принимает на вход строку message и пороги хорошести. Функция возвращает:

# "неуд", если предсказание модели меньше bad_threshold;
# "отл", если предсказание модели больше good_threshold;
# "норм" в остальных случаях.
# Функция predict_message_mood создает экземпляр класса SomeModel и вызывает у этого экземпляра метод predict с аргументом message.


class SomeModel:
    def predict(self, _message: str) -> float:
        return randint(0, 100)+random()


def predict_message_mood(
    message: str,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    model = SomeModel()
    prediction = model.predict(message)
    eps = 1e-10
    match prediction:
        case prediction if prediction < bad_thresholds-eps:
            return "неуд"
        case prediction if prediction > good_thresholds+eps:
            return "отл"
        case _:
            return "норм"

