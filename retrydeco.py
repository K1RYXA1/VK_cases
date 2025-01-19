import functools

# Декоратор retry_deco должен:

# принимать опциональными параметрами число перезапусков декорируемой функции и список ожидаемых классов исключений;
# при вызове функции логировать (выводить) название функции, все переданные ей аргументы, номер попытки перезапуска, результат работы функции и ошибку, если было выброшено исключение; формат логирования произвольный (например, функция и аргументы один раз, а номер попытки и исключение/результат сколько потребуется);
# в случае исключения при выполнении функции декоратор должен выполнить новую попытку запуска функции, пока не достигнет заданного числа перезапусков; если исключение из списка ожидаемых классов исключений (параметр декоратора), то перезапускать функцию не надо, тк исключения из списка это нормальный режим работы декорируемой функции.

def retry_deco(repeat = 1, exception=[]):
    
    def retry(func):
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            n = repeat
            try:
                result = func(*args, **kwargs)
                print(f'run {func.__name__} with positional args = {args}, keyword kwargs = {kwargs}, attempt = 1, {result=}')
            
            except tuple(exception) as err:
                
                print(f'run {func.__name__} with positional args = {args}, keyword kwargs = {kwargs}, attempt = 1, {err=}')
            
            except Exception as err:
                for i in range(n):
                    print(f'run {func.__name__} with positional args = {args}, keyword kwargs = {kwargs}, attempt = {i+1}, {err=}')
            
                     
        return wrapper
    
    return retry


