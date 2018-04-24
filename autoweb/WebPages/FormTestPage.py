from WebPages.IndexPage import IndexPage

class FormTest(IndexPage):
    selectbox = ('xpath','//*[@id="s1Id"]')
    selectboxV = ('xpath', '//*[@id="s1Id"]/option[2]')

    def clickselect(self):
        selectbox = self.element_element(self.selectbox,self.selectboxV)
        self.click(selectbox)