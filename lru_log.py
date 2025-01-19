import argparse
from create_log import create_logger


class LRUCache:
    def __init__(self, limit=42):
        self.limit = limit
        self._value = {}
        self.logger = None

    def get(self, key):
        # ключ не был установлен
        if key not in self._value:
            self.logger.info('Попытка получения значения по несуществующему ключу "%s"', key)
            return None

        # получаем значение и перезаписываем ключ в конец словаря
        get_val = self._value.pop(key)
        self.logger.info('Получение значения "%s" по ключу "%s"', get_val, key)
        self._value[key] = get_val
        self.logger.debug('Использование элемента с ключом "%s"', key)

        return get_val

    def set(self, key, value):
        # удаляем ключ при перезаписи значения
        if key in self._value:
            self.logger.info('Попытка перезаписи значения ключа "%s"', key)
            self._value.pop(key)
            self.logger.debug('Удаление существующего ключа "%s"', key)

        self._value[key] = value
        self.logger.info('Установка значения "%s" по ключу "%s"', value, key)
        self.logger.debug('Использование элемента с ключом "%s"', key)

        # превышение лимита
        if len(self._value) > self.limit:
            self.logger.warning('Количество элементов превышает лимит')
            # получение и удаление неиспользуемого (первого) элемента
            unused_key = next(iter(self._value))
            self._value.pop(unused_key)
            self.logger.info('Очистка кэша')
            self.logger.debug('Удаление неиспользумего элемента с ключом "%s"', unused_key)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', action='store_true', help='Доп.логирование в stdout')
    parser.add_argument('-f', action='store_true', help='Применение кастомного фильтра')
    args = parser.parse_args()

    logger = create_logger(args.s, args.f)

    cache = LRUCache(3)
    cache.logger = logger

    cache.set("k1", "val1")
    cache.set("k2", "val2")
    cache.set("k3", "val3")

    cache.set("k1", "new_val1")

    cache.set("k4", "val4")

    cache.get("k1")
    cache.get("k2")
