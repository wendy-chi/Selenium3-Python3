from selenium import webdriver
ChromeDriverServer = "C:\Program Files (x86)\Google\Chrome\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(ChromeDriverServer)
driver.get('https://phptravels.com/demo/')