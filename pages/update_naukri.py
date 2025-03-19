from selenium import webdriver
import random
from time import sleep
def update_naukri_profile():
    driver=webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.get("https://www.naukri.com/nlogin/login?URL=//www.naukri.com/mnjuser/profile")
    driver.maximize_window()
    user_name=driver.find_element('css selector','input[id="usernameField"]')
    user_name.clear()
    user_name.send_keys("alamsahdab786@gmail.com")
    user_pass=driver.find_element('css selector','input[id="passwordField"]')
    user_pass.clear()
    user_pass.send_keys("Nagma@123")
    driver.find_element('xpath','//button[text()="Login"]').click()
    driver.find_element('xpath','//div[@class="view-profile-wrapper"]//a').click()
    driver.find_element("css selector",'em[class="icon edit "]').click()
    sleep(2)
    a=driver.find_element("css selector",'input[id="name"]')
    random_num=random.randint(0,3)
    sleep(1)
    if random_num==1:
        a.clear()
        a.send_keys("Md Shadab Alam")
        sleep(3)
    elif random_num==2:
        a.clear()
        a.send_keys("Shadab Alam")
        sleep(3)
    elif random_num==3:
        a.clear()
        a.send_keys("Ms Shadab")
        sleep(3)
    driver.find_element('xpath','//button[text()="Save"]').click()
    sleep(5)

