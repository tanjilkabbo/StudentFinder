import time

from selenium.webdriver.common.by import By

from driver.driver import Driver
from login.login import Login

driver = Driver().driver
driver.get("https://facebook.com")


Login().login(driver)


def open_group_list(index=0):
    # TODO: get file from google sheet
    with open('../TextFile/groupList.txt') as file:
        lines = file.readlines()
        print("We have to work with " + str(len(lines)) + " link")

    for groupLinkList in lines:
        driver.get(groupLinkList)
        print(groupLinkList + "link")
        time.sleep(2)
        driver.implicitly_wait(4)

        # Automatically click join button
        if driver.find_elements(By.XPATH, "//span[contains(text(),'Joined')]"):
            join_button_object = driver.find_element(By.XPATH, "//span[contains(text(),'Joined')]")
            print(join_button_object)
            join_button_object.click()

            # print(input("Stop :"))
            url = driver.current_url
            print(url)


        # print(input("Visit Next : "))


open_group_list()
