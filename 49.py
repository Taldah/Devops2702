from selenium import webdriver
from time import sleep
#driver = webdriver.Chrome(executable_path=)
driver = webdriver.Chrome()
#driver.get("https://github.com")
driver.get("file:C://Users//taltech//OneDrive//Documents//tip_calc//index.html")
billamt = driver.find_element(by="id", value="billamt")
billamt.send_keys("100")
s = driver.find_element(by="xpath", value="//*[@id=\"serviceQual\"]/option[5]")
s.click()
people = driver.find_element(by="id", value="peopleamt")
people.send_keys("5")
driver.find_element(by="id", value="calculate").click()
expected = "2.00"
actual = driver.find_element(by="id", value="tip").text
#assert expected != actual
sleep(10)
driver.close()