from random import randint, random


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

