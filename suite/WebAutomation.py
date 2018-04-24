
import subprocess
from datetime import datetime
import CommonLibrary.LogUtility as LogUtility
import CommonLibrary.EmailUtils as EmailUtils
import CommonLibrary.CommonConfiguration as cc


class RunTests(object):
    """description of class"""

    def __init__(self):
        # self.testcaselistfile =cc.TestCases_PATH + "testcases.txt"
        self.testcaselistfile = "testcases.txt"
    def LoadAndRunTestCases(self):
        try:
            f = open(self.testcaselistfile)
            testfiles = [test for test in f.readlines() if not test.startswith("#")]
            f.close()
            for item in testfiles:
                subprocess.call("nosetests " +cc.TestCases_PATH+"\\"+ str(item).replace("\\n", ""), shell=True)
        except Exception as err:
            LogUtility.logger.debug("Failed running test cases, error message: {}".format(str(err)))
        # finally:
        #     EmailUtils.send_report() #发送邮件

    def CreateRunFolder(self):
        try:
            time = datetime.now()
            subprocess.call("mkdir " + cc.Logs_PATH + "\\" + "TestRun_" + time.strftime("%Y_%m_%d_%H_%M_%S"), shell=True)
        except Exception as err:
            LogUtility.logger.debug("Failed creating run folder, error message: {}".format(str(err)))


if __name__ == "__main__":
    newrun = RunTests()
    newrun.CreateRunFolder()
    newrun.LoadAndRunTestCases()