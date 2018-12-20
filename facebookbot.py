from mechanicalsoup import StatefulBrowser

"""
Bot for Facebook Mobile site
"""
class FacebookBot:
    url = "https://m.facebook.com/"
    """
    init method
    """
    def __init__(self):
        self.browser = StatefulBrowser()
    """
    Login using email e password
    """
    def login(self, email, password):
        self.browser.open(self.url)
        self.browser.select_form("#login_form")
        self.browser['email'] = email
        self.browser['pass'] = password
        response = self.browser.submit_selected()
        return response
