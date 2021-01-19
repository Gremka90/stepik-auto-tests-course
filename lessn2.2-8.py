from selenium import webdriver
import os
path = 'C:\Project\pythonProject\Selenium\Test.txt'
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_tag_name("input[name='firstname']").send_keys('Slava')
browser.find_element_by_tag_name("input[name='lastname']").send_keys('Melnikov')
browser.find_element_by_tag_name("input[name='email']").send_keys('Slava@gmail.com')

current_dir = os.path.abspath(os.path.dirname(path))
file_path = os.path.join(current_dir, 'test.txt')

browser.find_element_by_tag_name("input[type='file']").send_keys(file_path)
browser.find_element_by_tag_name("[type='submit']").click()