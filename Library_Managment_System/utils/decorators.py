import functools


class Decorators:
    @staticmethod
    def log_action(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[LOG]Calling : {func.__name__}")
            result = func(*args, **kwargs)
            print(f"[LOG] Done : {func.__name__}")
            return result

        return wrapper


log_action = Decorators.log_action
