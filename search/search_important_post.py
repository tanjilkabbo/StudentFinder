import time

from driver.driver import Driver
from googlesheet.connection import Connection
from login.login import Login

driver = Driver().driver
driver.get("https://facebook.com")


Login().login(driver)

work_sheet = Connection().connect_worksheet("PythonFacebookGroupList")
group_list = work_sheet.col_values(1)
print(group_list)


def visit_link_list(link_list):
    for link in link_list:
        print(link)
        driver.get(link)
        time.sleep(2)
        driver.implicitly_wait(4)
    print(f"\nWe visit {len(link_list)} link")
    return len(link_list)


visit_link_list(group_list)

