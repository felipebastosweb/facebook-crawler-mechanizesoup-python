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
    
    """
    Submit One Click Login
    """
    def one_click_login(self):
        self.browser.select_form('form[method="post"]')
        response = self.browser.submit_selected()
        return response
    
    """
    Open Profile Page
    """
    def open_profile(self, username):
        self.browser.open_relative('/%s' % username)
        return self.browser.get_current_page()
    
    """
    Open Friends Page
    """
    def open_friends_page(self):
        self.browser.open_relative('friends/center/friends/?mff_nav=1&fb_ref=tn')
        return self.browser.get_current_page()
    
    """
    Open Friends Request Page
    """
    def open_friends_requests_page(self):
        self.browser.open_relative('/?soft=requests')
        return self.browser.get_current_page()
    
    """
    Open Sugestions Friends Page
    """
    def open_suggestions_friends_page(self):
        self.browser.open_relative('/friends/center/suggestions/?mff_nav=1&fb_ref=tn')
        return self.broser.get_current_page()
    
    """
    Open Notifications Page
    """
    def open_notifications_page(self):
        self.browser.open_relative('/home.php?soft=notifications')
        return self.browser.get_current_page()
