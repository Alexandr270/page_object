from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element_by_css_selector("#login_link")
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present('//a[@id="login_link"]'), "Login link is not presented"
