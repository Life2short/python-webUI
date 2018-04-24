from WebPages.BasePage import BasePage


class IndexPage(BasePage):
    LinkTest = ('xpath','/html/body/table/tbody/tr/td[1]/a[1]')
    FormTest = ('xpath','/html/body/table/tbody/tr/td[1]/a[2]')
    FileUpload = ('xpath','/html/body/table/tbody/tr/td[3]/a[6]')

    def clicklinktest (self):
        linktestbox = self.findElements(self.LinkTest)
        self.click(linktestbox[0])

    def clickFormTest(self):
        FormTestbox  = self.findElements(self.FormTest)
        self.click(FormTestbox[0])

    def clickFileUpload(self):
        FileUploadbox = self.findElement(self.FileUpload)
        self.click(FileUploadbox)