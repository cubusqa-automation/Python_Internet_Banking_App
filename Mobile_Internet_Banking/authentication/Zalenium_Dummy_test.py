import sys
import time
import os

sys.path.insert(0, os.path.join(os.getcwd(), '..', '..'))

from Mobile_Internet_Banking.helper.TestData import *


class Test_Zalenium_Dummy:
    def test_zalenium_dummy(self):

        time.sleep(30)
        test_data = TestData()
        general_data = test_data.get_general_test_data()
        print(general_data.report_Machine)

        #bashCommand = "sudo docker cp authentication_container:/Mobile_Internet_Banking/Allure_Report ~/Documents"
        #os.subprocess.call(bashCommand)

        time.sleep(5)
