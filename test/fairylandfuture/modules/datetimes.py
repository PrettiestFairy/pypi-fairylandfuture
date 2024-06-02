# coding: utf8

from fairylandfuture.modules.datetimes import DateTimeModule

class TestDataTime:
    
    @classmethod
    def run(cls):
        method_list = [func for func in dir(cls) if callable(getattr(cls, func)) and not func.startswith("__")]
        for method in method_list:
            if method.startswith("test_"):
                getattr(cls, method)()
    
    @classmethod
    def test_001(cls):
        print(DateTimeModule.date())
        
    @classmethod
    def test_002(cls):
        print(DateTimeModule.time())


if __name__ == '__main__':
    TestDataTime.run()
