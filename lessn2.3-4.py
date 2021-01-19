from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)
browser.find_element_by_tag_name("button[type='submit']").click()
alert = browser.switch_to.alert.accept()
get_x = browser.find_element_by_id('input_value').text
outcome = calc(get_x)
browser.find_element_by_id('answer').send_keys(outcome)
browser.find_element_by_tag_name("button[type='submit']").click()
