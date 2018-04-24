from WebPages.baidu_main_page import BaiDuMainPage

class BaiDuResultPage(BaiDuMainPage):
    loc_result_links = ('XPATH', '//div[contains(@class, "result")]/h3/a')

    @property
    def result_links(self):
        return self.findElements(self.loc_result_links)