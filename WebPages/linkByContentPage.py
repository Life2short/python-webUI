from WebPages.LinkTestPage import LinkTest


class LinkTestContent(LinkTest):
    text = ('xpath','/html/body/h2')
    backlink = ('xpath','/html/body/a')

    def chektext(self):
        textbox = self.findElements(self.text)
        text = self.getText(textbox[0])
        return text

    def back(self):
        backbox = self.findElements(self.backlink)
        self.click(backbox[0])