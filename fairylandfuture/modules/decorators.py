# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-10 10:20:53 UTC+8
"""

import time

from typing import Literal, Type, TypeVar, Generic


_T = TypeVar("_T")


class SingletonDecorator(Generic[_T]):
    """
    A decorator class that turns a class into a Singleton by ensuring that only one instance of the class exists.

    :param cls: The class to be transformed into a Singleton.
    :type cls: object

    Usage::

        @SingletonDecorator
        class MyClass:
            pass

        my_instance1 = MyClass()
        my_instance2 = MyClass()

        assert my_instance1 is my_instance2  # True because both are the same instance
    """

    _instance = None

    def __init__(self, cls: Type):
        self._cls = cls

    def __call__(self, *args, **kwargs):
        if not self._instance:
            self._instance = self._cls(*args, **kwargs)
        return self._instance

    def __instancecheck__(self, instance):
        return isinstance(instance, self._cls)


class TimingDecorator(Generic[_T]):
    """
    A decorator class for timing the execution duration of a function and printing the elapsed time.

    :param func: The function to be timed.
    :type func: object

    Usage::

        @TimingDecorator
        def my_function():
            # Function implementation

    Note:
        Customize `output` method in a subclass to handle the timing message output.
    """

    def __init__(self, func: Type):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        results = self.func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Calculating hours, minutes, and seconds from elapsed time
        hour, minute, second = self._calculate_time_parts(elapsed_time)

        elapsed_str = f"Running for {hour:02d}:{minute:02d}:{second:06.3f}"
        self.output(elapsed_str)

        return results

    @staticmethod
    def _calculate_time_parts(elapsed_time):
        if elapsed_time < 60:
            return 0, 0, elapsed_time
        elif elapsed_time < 3600:
            return 0, int(elapsed_time / 60), elapsed_time % 60
        else:
            hour = int(elapsed_time / 3600)
            return hour, int((elapsed_time - (hour * 3600)) / 60), elapsed_time % 60

    def output(self, msg: str) -> None:
        raise NotImplementedError("Customize the output in the subclass.")


class ActionDecorator(Generic[_T]):
    """
    A decorator class that logs the start and end of a function's execution, indicating success or failure.

    :param action: An optional action name to log.
    :type action: str

    Usage::

        @ActionDecorator(action="Process Data")
        def process_data():
            # Function implementation

    Note:
        Customize `output` method in a subclass to handle the action message output.
    """

    def __init__(self, action: Literal[str] = None):
        self.action = action

    def __call__(self, *args, **kwargs):
        func: Type = args.__getitem__(0)

        def wrapper(*args, **kwargs):
            if not self.action:
                self.action = func.__name__
            try:
                self.output(msg=f"{self.action} running starts.")
                results = func(*args, **kwargs)
                self.output(msg=f"{self.action} running success.")
                return results
            except Exception as err:
                self.output(msg=f"{self.action} running failure.")
                raise err

        return wrapper

    def output(self, msg: str) -> None:
        raise NotImplementedError("Customize the output in the subclass.")


class TryCatchDecorator(Generic[_T]):
    """
    A decorator class that wraps a function in a try-except block, catching and re-raising any exceptions.

    :param func: The function to be wrapped.
    :type func: object

    Usage::

        @TryCatchDecorator
        def my_function():
            # Function implementation
    """

    def __init__(self, func: Type):
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            results = self.func(*args, **kwargs)
            return results
        except Exception as error:
            raise error


class TipsDecorator(Generic[_T]):
    """
    A decorator class designed to provide optional tips or messages during the execution of a function.

    :param tips: An optional tip or message related to the function's purpose or execution.
    :type tips: str

    Usage::

        @TipsDecorator(tips="Check the input data carefully.")
        def data_processing():
            # Function implementation
    """

    def __init__(self, tips: Literal[str] = None):
        self.tips = tips

    def __call__(self, *args, **kwargs):
        func: Type = args.__getitem__(0)

        def wrapper(*args, **kwargs):
            try:
                self.output(self.tips)
            except NotImplementedError:
                pass

            try:
                results = func(*args, **kwargs)
                return results
            except Exception as err:
                raise err

        return wrapper

    def output(self, msg: str) -> None:
        """
        Outputs a message. This should be customized in a subclass to handle the message output.

        :param msg: The message to output.
        :type msg: str
        """
        raise NotImplementedError("Customize the output in the subclass.")
