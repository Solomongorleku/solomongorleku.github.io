from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver")


@when('open the data test app')
def openApp(context):
    context.driver.get("http://localhost:3000/")


@when('fill first name')
def fillFirstname(context):
    context.driver.find_element(By.NAME, "firstName").send_keys("Solomon")


@when('fill middle name')
def fillMiddlename(context):
    context.driver.find_element(By.NAME, "middleName").send_keys("Ofoli")

@when('fill last name')
def fillLastname(context):
    context.driver.find_element(By.NAME, "lastName").send_keys("Gorleku")


@when('fill phone number')
def fillPhonenumber(context):
    context.driver.find_element(By.NAME, "phoneNumber").send_keys("0549695760")


@when('fill date of birth')
def fillDOB(context):
    context.driver.find_element(By.NAME, "dob").send_keys("11-30-2021")


@when('fill address')
def fillAddress(context):
    context.driver.find_element(By.NAME, "address").send_keys("Accra")


@when('click add new user')
def clickAddUser(context):
    add_new_user = context.driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/a")
    add_new_user.click()



@then('new user should be added to the user list')
def userList(context):
    user_List = context.driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/main/div[1]")
    status = user_List.is_displayed()
    assert status is True

@then('close browser')
def closeBrowser(context):
    context.driver.close()