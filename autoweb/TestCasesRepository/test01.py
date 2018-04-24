import time
import unittest
from WebPages.baidu_result_page import BaiDuMainPage, BaiDuResultPage
import CommonLibrary.CommonConfiguration as cc


class TestBaiDu(unittest.TestCase):
    Url = cc.baseUrl()

    def setUp(self):
        self.page = BaiDuMainPage(browser_type='chrome').get(self.Url, maximize_window=True)

    def tearDown(self):
        self.page.quit()

    # def sub_setUp(self):
    #     # 初始页面是main page，传入浏览器类型打开浏览器
    #     self.page = BaiDuMainPage(browser_type='chrome').get(self.Url, maximize_window=True)


    # def sub_tearDown(self):
    #     self.page.quit()

    def test_search(self):
        # self.sub_setUp()
        datas = [{'search':'python'},{'search':'java'}]
        for d in datas:
            with self.subTest(data=d):
                self.page.search(d['search'])
                time.sleep(2)
                self.page = BaiDuResultPage(self.page)  # 页面跳转到result page
                links = self.page.result_links
                for link in links:
                    print(link)

    # def test_end(self):
    #     self.sub_tearDown()

if __name__ == "__main__":
    unittest.main()