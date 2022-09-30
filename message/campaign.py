from selenium.webdriver.common.by import By

from message.message_text import MessageText

message = MessageText()

# print(first_message)

import time

from driver.driver import Driver
from googlesheet.connection import Connection
from login.login import Login

driver = Driver().driver
driver.get("https://facebook.com")


Login().login(driver)

"""
Documentation :
https://docs.gspread.org/en/v5.4.0/oauth2.html#oauth-client-id          
"""

work_sheet = Connection().connect_worksheet("BanglaStudent")
group_list = work_sheet.col_values(1)
# print(group_list)


def send_message(current_loop_position, message_number):
    driver.find_element(By.XPATH, "//span[contains(text(),'Message')]").click()
    driver.find_element(By.XPATH, "//p[@class='m8h3af8h kjdc1dyq']").send_keys(message.ai_text(message_number))
    driver.find_element(By.XPATH, "//div[@aria-label='Press enter to send']//*[name()='svg']").click()
    time.sleep(4)

    driver.find_element(By.XPATH, "//div[@aria-label='Close chat']").click()

    work_sheet.update_cell(current_loop_position + 1, 2, message_number + 1)

    after_sell_value = work_sheet.row_values(current_loop_position + 1)
    print(f"Sell Value After: {after_sell_value}")
    return print(f"Message: \n{message.ai_text(message_number)}\n")


def visit_link_list(driver, link_list):
    list_index = []
    for i in range(len(link_list)):
        list_index.append(link_list[i])
        print(f"\n* {len(list_index)} : {link_list[i]}\n")
        driver.get(link_list[i])
        time.sleep(2)
        driver.implicitly_wait(4)

        sell_value = work_sheet.row_values(i + 1)
        print(f"Sell Value Before: {sell_value}")
        # print(i+1)
        # print(input("Stop :"))

        # TODO : Make a time if block to add time logic. if you send message someone within 24 hours you will not
        #  send him message again.

        if sell_value[1] == '0':
            print(f"{sell_value[1]} Value found that means\nHuman are talking to this person.")

        elif sell_value[1] == '1':
            send_message(i, 1)

        elif sell_value[1] == '2':
            send_message(i, 2)

        elif sell_value[1] == '3':
            send_message(i, 3)

        elif sell_value[1] == '4':
            send_message(i, 4)

        else:
            print("Extend message_text.py file for more message")

        print(input("Message Next Person:"))

    print(f"\nWe visit {len(link_list)} link")
    return len(link_list)


visit_link_list(driver, group_list)

