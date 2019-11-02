import pyscreenshot
import pytest
from pywinauto import Application

from commons.methods import getdate
from pages.Calc import *


# global no_test
no_test = 0


def pytest_report_header():
    return "PROJECT HEADER TEST"


@pytest.fixture(autouse=True)
def after_failure(request):
    failed_before = request.session.testsfailed
    yield
    if request.session.testsfailed != failed_before:
        print("executing test failed!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", request.node.nodeid)
        # grab fullscreen
        im = pyscreenshot.grab()
        # save image file
        im.save("../screenshots/screenshot" + getdate() + ".png")


@pytest.fixture(autouse=True)
def run_around_tests():
    # Code before each test case
    global no_test
    no_test = no_test + 1
    print("\nThis is the begining of test case no {0} ________________________________________________".format(no_test))
    calc = Calc("Calculus")
    calc.click_wyczysc()
    yield
    # Code after each test case
    print("\nThis is the end of test case no {0} _____________________________________________________".format(no_test))


@pytest.fixture(scope="module", autouse=True)
def setup_teardown_module():
    print("\n===========test suite beginning=========================================")
    Application(backend="win32").start("C:\\Kalkulator3\\bin\\Calculus.exe")
    yield
    Desktop(backend="win32").window(best_match="Calculus").set_focus()
    send_keys('%{F4}')
    print("\n===========test suite end================================================")
