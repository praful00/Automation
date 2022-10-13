import pytest
#Fixtures are functions, which will run before each test function to which it is applied.
# Fixtures are used to feed some data to the tests such as database connections,URLs to test and some sort of input data.
# Therefore, instead of running the same code for every test, we can attach fixture function to the tests and it will run and return the data to the test before executing each test.
from pytest_demo.baseclass import logtest


@pytest.mark.usefixtures("setup")
class Testpro(logtest):

    def test_fixturedemo(self, dataload):
        log = self.getlogger()
        log.info(dataload[0])
        log.info(dataload[1])

    #def test_fixturedemo1(self, dataload):
        #print("I will execute third")
        #print(dataload[0])
        #print(dataload[1])
        #print(dataload[2])

