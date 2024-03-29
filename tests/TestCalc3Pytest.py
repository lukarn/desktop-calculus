import json
import time
import csv

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

with open("../testdata/med2.csv", "r") as f:
    reader = csv.reader(f)
    med2_csv = list(reader)

with open("../testdata/med5.csv", "r") as f:
    reader = csv.reader(f)
    med5_csv = list(reader)

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

    def test_12add(self):
        for i in range(0, 2):  # (0, 29) max
            assert calc.add_2(data_long["num1"][i], data_long["num2"][i]) == data_long["add"][i], "test failed"

    def test_13add(self):
        for i in range(0, 2):  # (0, 29) max
            print(add_csv[i][0], "+", add_csv[i][1], "= ", add_csv[i][2])
            assert calc.add_2(add_csv[i][0], add_csv[i][1]) == add_csv[i][2], "test failed"

    def test_14med2(self):
        for i in range(0, 3):  # (0, 29) max
            print(med2_csv[i][1], " ; ", med2_csv[i][3], "  median = ", med2_csv[i][4])
            assert calc.med_2(med2_csv[i][1], med2_csv[i][3]) == med2_csv[i][4], "test failed"

    def test_15med5(self):
        for i in range(0, 29):  # (0, 29) max
            print(med5_csv[i][1], " ; ", med5_csv[i][3], " ; ", med5_csv[i][5], " ; ", med5_csv[i][7], " ; ",
                  med5_csv[i][9], "  median = ", med5_csv[i][10])
            assert calc.med_5(med5_csv[i][1], med5_csv[i][3], med5_csv[i][5], med5_csv[i][7],
                              med5_csv[i][9]) == med5_csv[i][10], "test failed"
