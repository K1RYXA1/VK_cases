# Реализовать класс CustomList наследованием от list
# При этом:

# CustomList должен наследоваться от встроенного списка list для получения всех методов последнего;
# экземпляры CustomList можно складывать и вычитать друг с другом, с обычными списками и с числами:
# CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7])  # CustomList([6, 3, 10, 7])
# CustomList([10]) + [2, 5]  # CustomList([12, 5])
# [2, 5] + CustomList([10])  # CustomList([12, 5])
# CustomList([2, 5]) + 10  # CustomList([12, 15])
# 10 + CustomList([2, 5])  # CustomList([12, 15])

# CustomList([5, 1, 3, 7]) - CustomList([1, 2, 7])  # CustomList([4, -1, -4, 7])
# CustomList([10]) - [2, 5]  # CustomList([8, -5])
# [2, 5] - CustomList([10])  # CustomList([-8, 5])
# CustomList([2, 5]) - 10  # CustomList([-8, -5])
# 10 - CustomList([2, 5])  # CustomList([8, 5])
# Возвращаться должен новый экземпляр CustomList, элементы которого будут результатом поэлементного сложения/вычитания элементов исходных списков. Сложение/вычитание с числом выполняется как сложение/вычитание каждого элемента списка с данным числом;
# при сложении/вычитании списков разной длины отсутствующие элементы меньшего списка считаются нулями;
# после сложения/вычитания исходные списки не должны изменяться;
# при сравнении (==, !=, >, >=, <, <=) экземмпляров CustomList должна сравниваться сумма элементов списков (сравнение с list и int не нужно);
# должен быть переопределен str, чтобы выводились элементы списка и их сумма;
# можно считать элементы списка CustomList, list и другие операнды всегда всегда целыми числами.

class CustomList(list):

    def __add__(self, value: int | list, /):
        new_instance = self.copy()
        if isinstance(value, int):
            for ind, el in enumerate(new_instance):
                new_instance[ind] = el + value
        else:
            if len(self) < len(value):
                new_instance.extend([0]*(len(value)-len(self)))
            min_len = len(value)
            for ind in range(min_len):
                new_instance[ind] = value[ind] + new_instance[ind]
        return CustomList(new_instance)

    def __radd__(self, value: int | list, /):
        return self.__add__(value)

    def __sub__(self, value: int | list, /):
        new_instance = self.copy()
        if isinstance(value, int):
            for ind, el in enumerate(new_instance):
                new_instance[ind] = el - value
        else:
            if len(self) < len(value):
                new_instance.extend([0]*(len(value)-len(self)))
            min_len = len(value)
            for ind in range(min_len):
                new_instance[ind] = new_instance[ind] - value[ind]
        return CustomList(new_instance)

    def __rsub__(self, value: int | list, /):
        new_instance = self.copy()
        if isinstance(value, int):
            for ind, el in enumerate(new_instance):
                new_instance[ind] = value - el
        else:
            if len(self) < len(value):
                new_instance.extend([0]*(len(value)-len(self)))
            elif len(self) > len(value):
                value = value.copy()
                value.extend([0]*(len(self)-len(value)))
            min_len = len(value)
            for ind in range(min_len):
                new_instance[ind] = value[ind] - new_instance[ind]
        return CustomList(new_instance)

    def __lt__(self, value: 'CustomList', /):
        return sum(self) < sum(value)

    def __le__(self, value: 'CustomList', /):
        return sum(self) <= sum(value)

    def __eq__(self, value: 'CustomList', /):
        return sum(self) == sum(value)

    def __ne__(self, value: 'CustomList', /):
        return sum(self) != sum(value)

    def __gt__(self, value: 'CustomList', /):
        return sum(self) > sum(value)

    def __ge__(self, value: 'CustomList', /):
        return sum(self) >= sum(value)

    def __str__(self, /):
        return f"Элементы: {', '.join(map(str, self))}; Сумма элементов: {sum(self)}"
