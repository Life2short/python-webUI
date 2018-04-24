from WebPages.IndexPage import IndexPage

class FileUpload(IndexPage):
    filebox_1 = ('xpath','//*[@id="file"]')
    submitbox_1 = ('xpath','/html/body/form[1]/input[3]')

    def sendfile(self,filepath):
        filebox = self.findElement(self.filebox_1)
        submitbox = self.findElement(self.submitbox_1)
        self.clean(filebox)
        self.type(filebox,filepath)
        self.click(submitbox)