from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

element_x = browser.find_element_by_id("input_value").text
textbox = browser.find_element_by_id("answer")
outcome = calc(element_x)
textbox.send_keys(outcome)

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
browser.find_element_by_id("robotCheckbox").click()
browser.find_element_by_id("robotsRule").click()
button.click()