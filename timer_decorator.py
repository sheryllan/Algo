import time

def timer(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()

        print(f'{f.__name__} took {end - start} seconds')
        return result
    return wrapper


