import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_seconddemo(setup):
    a = 10
    b = 20

    assert a == b

def test_thirdCreditCard(setup):
    a = 10
    b = 10
    assert a == b


@pytest.mark.xfail
def test_fourthCreditCard(setup):
    print("Good Morning")

def test_crossbrowser(crossBrowser):
    print(crossBrowser)