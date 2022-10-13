import pytest

#fixture are used as setup and tear down method for test cases-conftest file generalize
# fixture and make it available to all test cases
@pytest.fixture(scope="class")
def setup():
    print("I will execute first")
    yield
    print("I will execute last")


#datadriven fixture is use to loading the data into test cases
@pytest.fixture()
def dataload():
    print("loading the data")
    return ["Praful", "Shinde", "Manas"]

#parameterizing test with multiple data sets using fixture
#datadriven and parameterization can be done with return statement in tuple format
#when you define fixture scope to class only,it will run once before class is initiated and at the end

@pytest.fixture(params=[("chrome","Praful","Shinde"),("firefox","Akash","Jamgade"),("IE")])
def crossBrowser(request):
    return request.param



#how to generate html report i python
#how to install pytest-html for reporting
#command is pip install pytest-html

#how to run generate html report (--html=pro.html)
#command is py.test test_fixtureDemo.py --html=pro.html -v -s

