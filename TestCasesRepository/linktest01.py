import time
import unittest
from WebPages.linkByContentPage import LinkTest,LinkTestContent
import CommonLibrary.CommonConfiguration as cc
from CommonLibrary.TestCaseInfo import TestCaseInfo
from CommonLibrary.TestReport import TestReport
from datetime import datetime
import CommonLibrary.LogUtility as LogUtility


class Testlink(unittest.TestCase):
    Url = cc.baseUrl()
    @classmethod
    def setUpClass(self):
        self.page = LinkTest(browser_type='chrome').get(self.Url, maximize_window=False)
        # self.testCaseInfo = TestCaseInfo(id=1, name="Test selenium Python", owner='zhang')
        self.testResult = TestReport()
        LogUtility.CreateLoggerFile("Test_selenium_Python")
        # self.testCaseInfo.starttime = cc.getCurrentTime()

    @classmethod
    def tearDownClass(self):
        # self.testCaseInfo.endtime = cc.getCurrentTime()
        # self.testCaseInfo.secondsDuration = cc.timeDiff(self.testCaseInfo.starttime, self.testCaseInfo.endtime)
        # self.testResult.WriteHTML(self.testCaseInfo)
        self.page.quit()

    def test_linktest(self):
        try:
            self.testCaseInfo = TestCaseInfo(id=1, name="test_linktest", owner='zhang')
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
            assert ("Link Test" in title), '返回页面错误'

            self.testCaseInfo.result = "Pass"

        except Exception as err:
            self.testCaseInfo.errorinfo = str(err)
            LogUtility.Log(("Got error: " + str(err)))
        finally:
            self.testCaseInfo.endtime = cc.getCurrentTime()
            self.testCaseInfo.secondsDuration = cc.timeDiff(self.testCaseInfo.starttime, self.testCaseInfo.endtime)
            self.testResult.WriteHTML(self.testCaseInfo)
        pass


    def test_linktest_1(self):
        try:
            self.testCaseInfo = TestCaseInfo(id=2, name="test_linktest_1", owner='zhang')
            self.testCaseInfo.starttime = cc.getCurrentTime()
            # self.testCaseInfo.starttime = cc.getCurrentTime()
            # self.page.clicklinktest()
            # # 点击LinkTest链接
            # self.page = LinkTest(self.page)
            self.page.clickContent()
            # 点击LinkTestContent链接
            self.page = LinkTestContent(self.page)
            text = self.page.chektext()
            # 断言
            assert ('Link By Content Test' in text)
            # 返回LinkTest页面
            self.page.back()
            self.page = LinkTest(self.page)
            # 获取LinkTest页面标题
            title = self.page.getTitle()
            assert ('Link Test1' in title), '返回页面错误'

            self.testCaseInfo.result = "Pass"

        except Exception as err:
            self.testCaseInfo.errorinfo = str(err)
            LogUtility.Log(("Got error: " + str(err)))
        finally:
            self.testCaseInfo.endtime = cc.getCurrentTime()
            self.testCaseInfo.secondsDuration = cc.timeDiff(self.testCaseInfo.starttime, self.testCaseInfo.endtime)
            self.testResult.WriteHTML(self.testCaseInfo)
        pass



if __name__ == "__main__":
    unittest.main()