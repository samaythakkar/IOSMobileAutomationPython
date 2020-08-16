from pytest_bdd import scenario, given, when, then
from features.business_logic.po_appiumtest_loginpage import ATLoginaPage
from features.business_logic.po_appiumtest_smileypage import ATSmileyPage
from pytest_bdd import parsers
import pytest

atloginpage = ATLoginaPage()
atSmileyPage = ATSmileyPage()
@scenario('test_cases/appiumtest.feature', 'Check the smiley display')
def test_login_appiumtest():
    print('Scenario--> test_login_to_adam_sea')

@given("User is on Application home page")
def go_to_homepage():
    pass

@when(parsers.cfparse("User login with '{user}'"))
def user_login(user):
    atloginpage.login(user)

@then("User should see the smiley")
def user_should_see_the_smiley():
    assert atSmileyPage.is_smiley_visible()

