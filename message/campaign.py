from selenium.webdriver.common.by import By

message = "Hi, " \
          "I am teaching programming for more than 4 years." \
          " In my understanding basic programming come from basic math." \
          "Actually its come from kindergarten math. We all know x , y math." \
          "In Bangla We called 'চলক' , In programming we called it variable." \
          "You see 6 class math. We are going to learn like that. to know more" \
          "about me I give yoy my github profile. Its give you a perception about " \
          "my creditability.'https://github.com/sushen'. If you think I can help you to learn" \
          "I will be glad to spend time with you."

import time

from driver.driver import Driver
from googlesheet.connection import Connection
from login.login import Login

driver = Driver().driver
driver.get("https://facebook.com")


Login().login(driver)

work_sheet = Connection().connect_worksheet("Student")
group_list = work_sheet.col_values(1)
print(group_list)


def visit_link_list(driver, link_list):
    list_index = []
    for link in link_list:
        list_index.append(link)
        print(f"\n* {len(list_index)} : {link}\n")
        driver.get(link)
        time.sleep(2)
        driver.implicitly_wait(4)

        driver.find_element(By.XPATH, "//span[contains(text(),'Message')]").click()
        driver.find_element(By.XPATH, "//p[@class='m8h3af8h kjdc1dyq']").send_keys(message)
        driver.find_element(By.XPATH, "//div[@aria-label='Press enter to send']//*[name()='svg']").click()

        time.sleep(4)

        driver.find_element(By.XPATH, "//div[@aria-label='Close chat']").click()

        print(input("Next :"))

    print(f"\nWe visit {len(link_list)} link")
    return len(link_list)


visit_link_list(driver, group_list)

