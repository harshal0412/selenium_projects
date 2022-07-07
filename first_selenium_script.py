"""
Error: “chromedriver” cannot be opened because the developer cannot be verified.
Solution: xattr -d com.apple.quarantine /Users/admas/Downloads/chromedriver
"""
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/admas/Downloads/chromedriver')
# driver = webdriver.Firefox()

driver.get('http://demostore.supersqa.com')
print(driver.title)