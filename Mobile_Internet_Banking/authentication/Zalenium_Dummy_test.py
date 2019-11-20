import sys
import time
import os
import subprocess

import paramiko

sys.path.insert(0, os.path.join(os.getcwd(), '..', '..'))

from Mobile_Internet_Banking.helper.TestData import *


class Test_Zalenium_Dummy:
    def test_zalenium_dummy(self):

        #time.sleep(30)
        test_data = TestData()
        general_data = test_data.get_general_test_data()
        print(general_data.report_Machine)

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(general_data.report_Machine, username="cubusqa-client", password="@Cu2010bus")
        sftp = ssh.open_sftp()
        localpath = '/Mobile_Internet_Banking/Allure_Report'
        remotepath = '~/Downloads'
        sftp.put(localpath, remotepath)
        sftp.close()
        ssh.close()
