from selenium.webdriver.common.by import By
from WebPages.BasePage import BasePage


class BaiDuMainPage(BasePage):
    searchbox = ('id', 'kw')
    loc_search_button = ('id', 'su')

    def search(self, searchContent):
        searchBox = self.findElements(self.searchbox)
        self.clean(searchBox[0])
        self.type(searchBox[0], searchContent)
        self.enter(searchBox[0])