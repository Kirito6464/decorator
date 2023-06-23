import datetime


def logger(old_function):
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        call_time = datetime.datetime.now()
        with open('main.log', 'a', encoding='utf-8') as file:
            file.write(f'время вызова - {call_time}\n'
                       f'название функции - {old_function.__name__}\n'
                       f'аргументы функции - {args, kwargs}\n'
                       f'результат - {result}\n\n')
        return result

    return new_function


def logger_func(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            call_time = datetime.datetime.now()
            with open(path, 'a', encoding='utf-8') as file:
                file.write(f'время вызова - {call_time}\n'
                           f'название функции - {old_function.__name__}\n'
                           f'аргументы функции - {args, kwargs}\n'
                           f'результат - {result}\n\n')
            return result

        return new_function

    return __logger
