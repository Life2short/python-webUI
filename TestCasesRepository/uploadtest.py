import unittest
from WebPages.FileUploadPage import IndexPage,FileUpload
import CommonLibrary.CommonConfiguration as cc
import time
from CommonLibrary.TestCaseInfo import TestCaseInfo
from CommonLibrary.TestReport import TestReport
from datetime import datetime
import CommonLibrary.LogUtility as LogUtility


class TestUpload(unittest.TestCase):
    Url = cc.baseUrl()
    def setUp(self):
        self.page = IndexPage(browser_type='chrome').get(self.Url, maximize_window=True)
        self.testCaseInfo = TestCaseInfo(id=1, name="Test selenium Python", owner='zhang')
        self.testResult = TestReport()
        LogUtility.CreateLoggerFile("Test_selenium_Python")

    def tearDown(self):
        self.testResult.WriteHTML(self.testCaseInfo)
        self.page.quit()

    def testupload_1(self):
        try:
            self.testCaseInfo.starttime = cc.getCurrentTime()
            uploadfile = cc.Upload_PATH + '/test.txt'
            #进入上传文件页面
            self.page.clickFileUpload()
            self.page = FileUpload(self.page)
            # 选择文件并点击上传
            self.page.sendfile(uploadfile)
            time.sleep(5)
            self.testCaseInfo.result = "Pass"
        except Exception as err:
            self.testCaseInfo.errorinfo = str(err)
            LogUtility.Log(("Got error: " + str(err)))
        finally:
            self.testCaseInfo.endtime = cc.getCurrentTime()
            self.testCaseInfo.secondsDuration = cc.timeDiff(self.testCaseInfo.starttime, self.testCaseInfo.endtime)
        pass

if __name__ == "__main__":
    unittest.main()