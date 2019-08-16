from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("http://kimai.memt.com.br")

find_element_username = driver.find_element_by_id("kimaiusername")
assert find_element_username.get_attribute('value') == ''
find_element_username.send_keys('johann.albino')

find_element_pass = driver.find_element_by_id('kimaipassword')
assert find_element_pass.get_attribute('value') == ''
find_element_pass.send_keys('metrum2002*')

driver.find_element_by_id('loginButton').click()

#driver.find_element_by_id('buzzer').click()

kimaiativo = driver.find_element_by_xpath("//table[1]//tr[1]")
assert kimaiativo.get_attribute('class')

print(kimaiativo)


