from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
#在搜索框中输入文本
driver.find_element_by_css_selector("input[name='wd']").send_keys('python')