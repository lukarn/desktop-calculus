from pywinauto import Desktop
from pywinauto.keyboard import send_keys


class Calc:

    # LOCATORS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def jeden(self):
        return self.window_name.child_window(title="1")

    def dwa(self):
        return self.window_name.child_window(title="2")

    def trzy(self):
        return self.window_name.child_window(title="3")

    def cztery(self):
        return self.window_name.child_window(title="4")

    def piec(self):
        return self.window_name.child_window(title="5")

    def szesc(self):
        return self.window_name.child_window(title="6")

    def siedem(self):
        return self.window_name.child_window(title="7")

    def osiem(self):
        return self.window_name.child_window(title="8")

    def dziewiec(self):
        return self.window_name.child_window(title="9")

    def zero(self):
        return self.window_name.child_window(title="0")

    def plus(self):
        return self.window_name.child_window(title="+")

    def rownasie(self):
        return self.window_name.child_window(title="Wykonaj")

    def wyczysc(self):
        return self.window_name.child_window(title="wyczyść")

    def wyczysc_his(self):
        return self.window_name.child_window(title="Wyczyść")

    # END OF LOCATORS !!!!!!!!!!!!!!!!!!!!!!!!!

    # parameterized constructor
    def __init__(self, window_name):
        self.window_name = Desktop(backend="win32").window(best_match=window_name)

    def get_result(self):
        result = self.window_name.child_window(auto_id="tbWynik").texts()
        result = result[0]
        return result

    def get_ids(self, level):
        self.window_name.print_control_identifiers(depth=level)

    # click number (0-9)
    def click_1(self):
        self.jeden().click()

    def click_2(self):
        self.dwa().click()

    def click_3(self):
        self.trzy().click()

    def click_4(self):
        self.cztery().click()

    def click_5(self):
        self.piec().click()

    def click_6(self):
        self.szesc().click()

    def click_7(self):
        self.siedem().click()

    def click_8(self):
        self.osiem().click()

    def click_9(self):
        self.dziewiec().click()

    def click_0(self):
        self.zero().click()

    def click_plus(self):
        self.plus().click()

    def click_equal(self):
        self.rownasie().click()

    def click_wyczysc(self):
        self.wyczysc().click()

    def click_wyczysc2(self):
        self.wyczysc2().click()

    def add_2(self, num1, num2):
        self.wyczysc().click()
        send_keys(num1)
        self.click_plus()
        send_keys(num2)
        self.rownasie().click()
        return self.get_result()
