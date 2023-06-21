class BrowserHistory(object):

    def __init__(self, homepage):

        #This is to allow us to track both back and forward
        self.history, self.future = [], []
        self.current = homepage
        

    def visit(self, url):
        # Append current url into the history browse

        self.history.append(self.current)

        #visit this url by changing current URL to this new URL
        self.current = url

        #Clears the future stack since we have redescribed what the 'furthest url' is.

        self.future = []
        """
        :type url: str
        :rtype: None
        """
        

    def back(self, steps):

        while steps > 0 and self.history:
            self.future.append(self.current)
            self.current = self.history.pop()
            steps -= 1
        return self.current
        """
        :type steps: int
        :rtype: str
        """
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps > 0 and self.future:
            self.history.append(self.current)
            self.current = self.future.pop()
            steps -= 1
        return self.current
        