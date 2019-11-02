import json
import time
import csv
from commons.methods import *
from commons.param import *
from pages.Calc import *


# desktop test exercises - application: Kalkulator 3 (OS Win10 PL) - from some recruitment process

# test data import
with open("../testdata/add_test.json", "r") as read_file:
    data = json.load(read_file)
with open("../testdata/add_test_long.json", "r") as read_file:
    data_long = json.load(read_file)

with open("../testdata/add.csv", "r") as f:
    reader = csv.reader(f)
    add_csv = list(reader)

# page object for all tests
calc = Calc("Calculus")


class TestCalc3Pytest:

    def test_01print_con_ids(self):
        calc.get_ids(2)
        time.sleep(delay)

    def test_04add(self):
        calc.click_8()
        calc.click_plus()
        calc.click_9()
        calc.click_equal()
        assert calc.get_result() == "17", "test failed"

    def test_05add(self):
        send_keys("1234")
        calc.click_plus()
        send_keys("4321")
        calc.click_equal()
        assert calc.get_result() == "5555", "test failed"

    def test_06add(self):
        send_keys(data["num1"][0])
        calc.click_plus()
        send_keys(data["num2"][0])
        calc.click_equal()
        assert calc.get_result() == data["add"][0], "test failed"

    def test_07add(self):
        send_keys(data["num1"][1])
        send_keys("{VK_ADD}")
        send_keys(data["num2"][1])
        send_keys("{ENTER}")
        assert calc.get_result() == data["add"][1], "test failed"

    def test_08add(self):
        send_keys(data["num1"][2])
        calc.click_plus()
        send_keys(data["num2"][2])
        calc.click_equal()
        assert calc.get_result() == data["add"][2], "test failed"

    def test_09add(self):
        assert calc.add_2(data["num1"][3], data["num2"][3]) == data["add"][3], "test failed"

    def test_10add(self):
        assert calc.add_2(data["num1"][4], data["num2"][4]) == data["add"][4], "test failed"

    # def test_11add(self):
    #     # failure test - screenshot after failure
    #     send_keys(random_pesel("m"))
    #     calc.click_plus()
    #     send_keys(random_pesel("w"))
    #     calc.click_equal()
    #     assert calc.get_result() == data["add"][4], "test failed"

    def test_12add(self):
        for i in range(0, 2):  # (0, 29) max
            assert calc.add_2(data_long["num1"][i], data_long["num2"][i]) == data_long["add"][i], "test failed"

    def test_13add(self):
        for i in range(0, 29):  # (0, 29) max
            print(add_csv[i][0], "+", add_csv[i][1], "= ", add_csv[i][2])
            assert calc.add_2(add_csv[i][0], add_csv[i][1]) == add_csv[i][2], "test failed"
