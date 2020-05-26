
import time

from selenium import webdriver

BYPASS_COOKIE = {"name": "9a3d48f2292d7083178ebfc7720beb9260588988dd10ff7e",
                 "value": '{"override_universal_recaptcha": "0"}',
                 "domain": '.pizzahut.com'}

createAccoutn = "create-account"

browser = webdriver.Chrome('/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/chromedriver')
browser.get('https://staging-m-sprint.pizzahut.com')

browser.add_cookie(BYPASS_COOKIE)
print(browser.get_cookies())

browser.get('https://staging-m-sprint.pizzahut.com/index.php')

# element = browser.find_element_by_xpath("//a[@data-analytics-action='Join']")
element = browser.find_element_by_xpath("//a[@data-analytics-action='Join Hut Rewards > Top']")
element.click()


time.sleep(6)
browser.quit()
