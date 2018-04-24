import time
import unittest
from WebPages.linkByContentPage import LinkTest,LinkTestContent
import CommonLibrary.CommonConfiguration as cc
from TestCaseInfo import TestCaseInfo
from TestReport import TestReport
from datetime import datetime
import LogUtility


class Testlink(unittest.TestCase):
    Url = cc.baseUrl()
    def setUp(self):
        self.page = LinkTest(browser_type='chrome').get(self.Url, maximize_window=False)
        self.testCaseInfo = TestCaseInfo(id=1, name="Test selenium Python", owner='zhang')
        self.testResult = TestReport()
        LogUtility.CreateLoggerFile("Test_selenium_Python")

    def tearDown(self):
        self.testResult.WriteHTML(self.testCaseInfo)
        self.page.quit()

    def test_linktest(self):
        try:
            self.testCaseInfo.starttime = cc.getCurrentTime()
            self.page.clicklinktest()
            #点击LinkTest链接
            self.page = LinkTest(self.page)
            self.page.clickContent()
            #点击LinkTestContent链接
            self.page = LinkTestContent(self.page)
            text = self.page.chektext()
            #断言
            assert ('Link By Content Test' in text)
            #返回LinkTest页面
            self.page.back()
            self.page = LinkTest(self.page)
            #获取LinkTest页面标题
            title = self.page.getTitle()
            assert ('Link Test' in title)

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