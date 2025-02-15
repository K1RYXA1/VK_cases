

class CustomMeta(type):

    def __new__(mcs, cls_name, bases, classdict):
        new_classdict = {}  # Создаем новый словарь для хранения измененных атрибутов класса
        for name, value in classdict.items():
            # Защищаем non-public и private атрибуты
            if not name.startswith('_'):
                new_classdict['custom_' + name] = value
            else:
                new_classdict[name] = value

        # Определяем метод __setattr__ для созданного класса для изменения
        # динамически добавленных атрибутов на уровне экземпляра класса
        def __setattr__(self, name, value):
            if not name.startswith('_'):
                super(self.__class__, self).__setattr__('custom_' + name, value) 
            else:
                super(self.__class__, self).__setattr__(name, value) 
        new_classdict['__setattr__'] = __setattr__

        return super().__new__(mcs, cls_name, bases, new_classdict)

    # Переопределяем метод __setattr__ для изменения
    # динамически добавленных атрибутов на уровне класса
    def __setattr__(cls, name, value):
        super().__setattr__('custom_' + name, value)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"


class MyClass(metaclass=CustomMeta):
    """
    Класс для тестирования non-public и private атрибутов
    """
    _protect = 'cls_protect'
    __private = 'cls_private'

    def __init__(self):
        self._obj_protect = 'obj_protect'
        self.__obj_private = 'obj_private'

    def get_cls_private(self):
        return MyClass.__private

    def get_obj_private(self):
        return self.__obj_private


assert CustomClass.custom_x == 50
   

inst = CustomClass()
assert inst.custom_x == 50
assert inst.custom_val == 99
assert inst.custom_line() == 100
assert str(inst) == "Custom_by_metaclass"

inst.dynamic = "added later"
assert inst.custom_dynamic == "added later"