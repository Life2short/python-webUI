from WebPages.IndexPage import IndexPage


class LinkTest(IndexPage):
    linkByContent = ('id','linkById')
    linkByHtml = ('id','linkByHtml')
    Search = ('xpath','/html/body/a[12]/span')


    def clickContent(self):
        Contentbox = self.elementlocated(self.linkByContent)
        self.click(Contentbox)

    def Search(self):
        searchbox = self.elementlocated(self.Search)
        self.click(searchbox)

