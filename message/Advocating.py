"""
We test our advocacy in this page : https://www.facebook.com/groups/341334433330410/permalink/1266678044129373/
"""
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from message.message_text import MessageText
from datetime import datetime
import time
from driver.driver import Driver
from googlesheet.connection import Connection
from login.login import Login
import re


message = "Are you using broadband internet ?"
# print(first_message)


driver = Driver().driver
action = ActionChains(driver)
driver.get("https://facebook.com")


Login().login(driver)

driver.get("https://www.facebook.com/groups/ProgrammingForBeginners/permalink/1220644232066258/")

driver.implicitly_wait(10)
top_comments = driver.find_element(By.XPATH, "//span[contains(.,'Top comments')]")
print(top_comments)
top_comments.click()

driver.implicitly_wait(10)
all_comments = driver.find_element(By.XPATH, "//span[normalize-space()='All comments']")
print(all_comments)
all_comments.click()

driver.implicitly_wait(10)
previous_comments = driver.find_element(By.XPATH, "//span[contains(text(),'previous comments')]")
print(previous_comments)
previous_comments.click()

time.sleep(5)
driver.implicitly_wait(10)
main_comments = driver.find_elements(By.XPATH, "//div[@role='article']")
print(len(main_comments))

main_comments_reply_button = driver.find_elements(By.XPATH, "//div[@role='button'][normalize-space()='Reply']")
print(len(main_comments_reply_button))

comment_index = []
for comment in main_comments:
    comment_index.append(comment)
    print(f"Index : {len(comment_index)}")
    print(comment.text)
    re.finditer(r"\binterested\b", comment.text)
    # TODO : Base on regular expression create condition
    action.move_to_element(comment).click(comment).perform()
    main_comments_reply_button[len(comment_index)-1].click()
    action.send_keys(message).perform()
    # time.sleep(5)
    print("......................")
    print(input("Stop :"))


# time.sleep(10)
# driver.implicitly_wait(10)
# all_comments_fb_profile = driver.find_elements(By.XPATH, "//span[@class='x3nfvp2']")
# print(len(all_comments_fb_profile))
#
# action = ActionChains(driver)
#
# for fb_profile in all_comments_fb_profile:
#     action.move_to_element(fb_profile).perform()
#     time.sleep(4)
#     print(fb_profile.text)
#     if fb_profile.text == 'Garrowolf Sauber':
#         # action.move_to_element(fb_profile)
#         action.move_to_element(fb_profile).\
#             key_down(Keys.CONTROL).\
#             click(fb_profile).\
#             key_up(Keys.CONTROL).\
#             send_keys(Keys.TAB).\
#             send_keys(Keys.TAB).\
#             send_keys(Keys.TAB).\
#             send_keys(Keys.TAB).\
#             send_keys(Keys.TAB). \
#             pause(2). \
#             perform()
#         time.sleep(2)
#         # action.click().perform()
#
#         print(input("Stop :"))


print(input("Stop :"))
time.sleep(60)

driver.implicitly_wait(10)
