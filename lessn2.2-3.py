from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time



link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

num1 = int(browser.find_element_by_id("num1").text)
num2 = int(browser.find_element_by_id("num2").text)

summ = str(num1 + num2)
print(summ)
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(summ)
time.sleep(0.5)
browser.find_element_by_tag_name("[type='submit']").click()
