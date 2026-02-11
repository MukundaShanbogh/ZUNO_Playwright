from playwright.sync_api import expect
from forty_two_AI.locators.login_locators import login_page_locators


class login_page:
    def __init__(self,page):
        self.page = page


    def login(self,phone_number):
        lgl = login_page_locators()
        self.page.get_by_placeholder(lgl.phone_number).fill(phone_number)
        self.page.get_by_role("button",name= lgl.send_otp_btn).click()
        otp_input = self.page.locator(lgl.Otp_input)
        # print("OTP locator count:", otp_input.count())
        expect(otp_input).to_have_count(4)
        # otp_input.first.click()
        self.page.keyboard.type("1111", delay=50)
        self.page.get_by_role("button",name=lgl.verify_btn).click()
        continue_btn = self.page.get_by_role("button",name=lgl.continue_btn)
        expect(continue_btn).to_be_visible()
        continue_pop_up_txt = self.page.get_by_text(lgl.pop_up_txt)
        for i in range (4):
            try:
                expect(continue_pop_up_txt).to_be_visible(timeout=1000)
                continue_btn.click()
            except Exception:
                print("there is no pop up for the student")




