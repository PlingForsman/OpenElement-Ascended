import threading
from functools import wraps

class State:
    """Controls the state of the program."""

    running = True
    paused = False
    
    def __init__(self) -> None:
        raise RuntimeError("State class is not meant to be initialized")

def threaded(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
        return thread
    
    return wrapper
