import unittest
from WebPages.FormTestPage import IndexPage,FormTest
import CommonLibrary.CommonConfiguration as cc
import time
from TestCaseInfo import TestCaseInfo
from TestReport import TestReport
from datetime import datetime
import LogUtility

class TestForm(unittest.TestCase):
    Url = cc.baseUrl()
    def setUp(self):
        self.page = IndexPage(browser_type='chrome').get(self.Url, maximize_window=True)
        self.testCaseInfo = TestCaseInfo(id=1, name="Test selenium Python", owner='zhang')
        self.testResult = TestReport()
        LogUtility.CreateLoggerFile("Test_selenium_Python")

    def tearDown(self):
        self.testResult.WriteHTML(self.testCaseInfo)
        self.page.quit()

    def testSelect(self):
        try:
            self.testCaseInfo.starttime = cc.getCurrentTime()
            # 进入select页面
            self.page.clickFormTest()
            self.page.alert()
            self.page = FormTest(self.page)
            # 选择下拉框
            self.page.clickselect()
            text = self.page.alert('text')
            #断言alert提示框信息
            assert ('change' in text)
            self.page.alert()
            time.sleep(2)
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