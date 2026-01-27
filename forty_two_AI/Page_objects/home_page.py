import random
import time
from playwright.sync_api import expect
from forty_two_AI.locators.Home_locators import home_page_locators


class home_page:
    def __init__(self,page):
        self.page = page


    def assessment_logic(self):
        hpl = home_page_locators()
        home_page_text = self.page.get_by_text(hpl.home_page_text)
        expect(home_page_text).to_be_visible(timeout=2000)
        self.page.get_by_role("button",name=hpl.get_started_btn).click()
        self.page.get_by_role("button", name=hpl.start_assessment).first.click()
        for i in range(120):
            options = self.page.locator(hpl.options)
            expect(options.first).to_be_visible(timeout=30000)
            count = options.count()
            print(f"the count of each run are {count}")
            random_index = random.randrange(count)
            options.nth(random_index).click()
            self.page.get_by_role("button", name=hpl.next_btn).click()
            time.sleep(1.5)


