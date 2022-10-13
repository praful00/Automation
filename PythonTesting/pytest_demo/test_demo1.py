#pytest file name should start with test_ keyword
#method name should start with test name
#every code should wrapped in one method
#we can run single method out of n number of method by using py.test -k and method name(-k keyword is regular expression)
#-k stand for method names execution, -s logs in output, -v stand for more info metadata
#you can mark(tag) tests @pytest.mark.smoke and then run with -m keyword
#you can skip tests with @pytest.mark.skip

import pytest


#@pytest.mark.smoke
from pytest_demo.baseclass import logtest


@pytest.mark.usefixtures("setup")
class Testpraful(logtest):
    def test_firstdemo(self):
        log = self.getlogger()
        log.info("Hello Praful")
        print("Hello Praful")

    def test_test1(self):
        print("Hello Akash")

    def test_test2(self):
        print("Hello Shubham")



