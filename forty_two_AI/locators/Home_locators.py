import re

class home_page_locators:
    home_page_text = "Discover Where You Truly Belong"
    get_started_btn = "Get Started"
    start_assessment = "Start Assessment"
    options = "(//div[button])[2]//button"
    next_btn=re.compile(r"^(Next|submit)$", re.IGNORECASE)
    question_txt = "//h1[text()]"