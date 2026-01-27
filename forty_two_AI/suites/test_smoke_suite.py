from forty_two_AI.Page_objects.home_page import home_page
from forty_two_AI.Page_objects.login_page import login_page


class Test_login_forty_two:

    def test_forty_two_login(self, page):
        phone_number = '9446655459'
        LP = login_page(page)
        Hp = home_page(page)
        LP.login(phone_number)
        Hp.assessment_logic()



