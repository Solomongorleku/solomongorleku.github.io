from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Launch chrome browser
driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver")


# Open the web app
driver.get("http://localhost:3000/")


# Fill in details of the new user
driver.find_element(By.NAME, "firstName").send_keys("Solomon")
driver.find_element(By.NAME, "middleName").send_keys("Ofoli")
driver.find_element(By.NAME, "lastName").send_keys("Gorleku")
driver.find_element(By.NAME, "phoneNumber").send_keys("0549695760")
driver.find_element(By.NAME, "dob").send_keys("11-30-2021")
driver.find_element(By.NAME, "address").send_keys("Accra")


# Click to add new user
add_new_user = driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/a")
add_new_user.click()


# Check if new user has been added
userList = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/main/div[1]")
status = userList.is_displayed()
assert status is True


# Close the browser
driver.close()
