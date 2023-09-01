from selenium import webdriver

def test_ui():
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/')
    # driver.
    assert True == True