from selenium import webdriver

# Create a new instance of the Firefox driver
driver = webdriver.Chrome()

# go to the google home page
driver.get("http://www.google.com")
inputElement = driver.find_element_by_name("q")
