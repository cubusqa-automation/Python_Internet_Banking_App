import pymongo
import os

from Mobile_Internet_Banking.helper.TestData_Properties import *


class TestData:

    @staticmethod
    def get_general_test_data():
        try:
            general_Test_Data = General_Properties()
            mongodb_client = pymongo.MongoClient(general_Test_Data.mongodb_connection_string, ssl=True,
                                                 tlsAllowInvalidCertificates=True, tlsAllowInvalidHostnames=True)
            mongodb_database = mongodb_client.DATABASE_CUBUSQA_TESTDATA
            mongodb_collection = mongodb_database.Collection_QABox_TestData
            general_data = dict(mongodb_collection.find_one({'key': 'general_TestData'}))

            general_Test_Data.deployment_Type = general_data.get("deployment_Type").lower()
            general_Test_Data.deployment_Environment = general_data.get("deployment_Environment").lower()
            general_Test_Data.remote_Machine = general_data.get("remote_Machine")
            general_Test_Data.admin_Browser = general_data.get("admin_Browser").lower()
            general_Test_Data.admin_CUDeposite_Browser = general_data.get("admin_CUDeposite_Browser").lower()
            general_Test_Data.olb_Browser = general_data.get("olb_Browser").lower().lower()
            general_Test_Data.mobile_Browser = general_data.get("mobile_Browser").lower()
            general_Test_Data.quickPay_PreLogin_Browser = general_data.get("quickPay_PreLogin_Browser").lower()
            general_Test_Data.admin_URL = general_data.get("olb_URL").lower()
            general_Test_Data.olb_URL = general_data.get("olb_URL")
            general_Test_Data.mobile_URL = general_data.get("mobile_URL")
            general_Test_Data.quickPay_PreLogin_URL = general_data.get("quickPay_PreLogin_URL")

            return general_Test_Data

        except Exception as e:
            print(e)

    @staticmethod
    def get_authentication_test_data():
        try:
            general_Test_Data = General_Properties()
            authentication_Test_Data = Authentication_Properties()

            mongodb_client = pymongo.MongoClient(general_Test_Data.mongodb_connection_string, ssl=True,
                                                 tlsAllowInvalidCertificates=True, tlsAllowInvalidHostnames=True)
            mongodb_database = mongodb_client.DATABASE_CUBUSQA_TESTDATA
            mongodb_collection = mongodb_database.Collection_QABox_TestData
            authentication_data = dict(mongodb_collection.find_one({'key': 'authentication_TestData'}))

            authentication_Test_Data.loginFlow_MemberNo = authentication_data.get("loginFlow_MemberNo")
            authentication_Test_Data.loginFlow_UserName = authentication_data.get("loginFlow_UserName")
            authentication_Test_Data.loginFlow_Password = authentication_data.get("loginFlow_Password")
            authentication_Test_Data.loginFlow_SSN = authentication_data.get("loginFlow_SSN")
            authentication_Test_Data.loginFlow_DOB = authentication_data.get("loginFlow_DOB")
            authentication_Test_Data.retrieveUserName_MemberNo = authentication_data.get("retrieveUserName_MemberNo")
            authentication_Test_Data.retrieveUserName_Password = authentication_data.get("retrieveUserName_Password")
            authentication_Test_Data.retrieveUserName_SSN = authentication_data.get("retrieveUserName_SSN")
            authentication_Test_Data.retrieveUserName_DOB = authentication_data.get("retrieveUserName_DOB")
            authentication_Test_Data.resetPassword_UserName = authentication_data.get("resetPassword_UserName")
            authentication_Test_Data.resetPassword_SSN = authentication_data.get("resetPassword_SSN")
            authentication_Test_Data.resetPassword_DOB = authentication_data.get("resetPassword_DOB")
            authentication_Test_Data.resetPassword_New_Confirm_Password = authentication_data.get("resetPassword_New_Confirm_Password")

            return authentication_Test_Data

        except Exception as e:
            print(e)

