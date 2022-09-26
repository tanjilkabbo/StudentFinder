import re
import time

import winsound
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class SearchKeyword:
    def pageStart(self, driver):
        time.sleep(2)
        driver.implicitly_wait(30)
        pageStartAction = ActionChains(driver)
        pageStartAction.send_keys(Keys.HOME)
        pageStartAction.perform()

    def scrollDown(self, driver):
        time.sleep(2)
        driver.implicitly_wait(30)
        scrollDownAction = ActionChains(driver)
        scrollDownAction.send_keys(Keys.PAGE_DOWN)
        scrollDownAction.perform()

        # print(input("Press any Key: "))

    def scrollUp(self, driver):
        time.sleep(2)
        driver.implicitly_wait(30)
        scrollUpAction = ActionChains(driver)
        scrollUpAction.send_keys(Keys.PAGE_UP)
        scrollUpAction.perform()

    def scrollAndSearchUsingXpath(self, driver):
        for search in range(2):
            time.sleep(5)
            driver.implicitly_wait(30)
            self.scrollDown(driver)
        for search in range(2):
            time.sleep(5)
            driver.implicitly_wait(30)
            self.scrollUp(driver)
        grpupPostXpath = "//div[@aria-label='Actions for this post']"
        grpupPostXpathAria = driver.find_elements(By.XPATH, grpupPostXpath)
        # print(grpupPostXpathAria)
        print("First " + str(len(grpupPostXpathAria)) + " Post are searching by bot")

        index = []
        for postLoad in grpupPostXpathAria:
            time.sleep(4)
            driver.implicitly_wait(30)
            index.append(postLoad)
            grpupPostXpathAria[len(index)-1].click()
            grpupPostXpathAria[len(index)-1].click()
        self.pageStart(driver)

    def searchWordUsingXpath(self, driver):
        search_interested_word_xpath = "//div[contains(text(),interested)]"
        searchWordhAria = driver.find_elements(By.XPATH, search_interested_word_xpath)
        # print(searchWordhAria)
        # print(str(len(searchWordhAria)) + " interested Word Found")

        if driver.find_elements(By.XPATH, search_interested_word_xpath):
            print(str(
                searchWordhAria[0]) + " :is the Elements" + "\n" + search_interested_word_xpath + " :For this xpath")
            # print(searchWordhAria[0].text)
            allText = searchWordhAria[0].text

            text = allText

            index = []
            for m in re.finditer(r"\binterested\b", text):
                if m.group(0):
                    index.append(m)
                    print("Present")

                    freq = 500
                    # duration is set to 100 milliseconds
                    dur = 100
                    winsound.Beep(freq, dur)
                else:
                    print("Absent")
                print(str(len(index)) + " no 'interested' Word Found")

            if len(index) != 0:
                print("Total " + str(len(index)) + " 'interested' Word Found")
                print(input("Press any Key: "))
            else:
                print("No 'interested' Word Found")

    # def searchWordUsingXpath(self, driver, word="interested"):
    #     search_interested_word_xpath = f"//div[contains(text(),{word})]"
    #     searchWordhAria = driver.find_elements(By.XPATH, search_interested_word_xpath)
    #     # print(searchWordhAria)
    #     # print(str(len(searchWordhAria)) + " interested Word Found")
    #
    #     if driver.find_element(By.XPATH, search_interested_word_xpath):
    #         print(str(searchWordhAria[0]) + " :is the Elements" + "\n" + search_interested_word_xpath + " :For this xpath")
    #         # print(searchWordhAria[0].text)
    #         allText = searchWordhAria[0].text
    #
    #         text = allText
    #
    #         index = []
    #         for m in re.finditer(f"\b{word}\b", text):
    #             if m.group(0):
    #                 index.append(m)
    #                 print("Present")
    #
    #                 freq = 500
    #                 # duration is set to 100 milliseconds
    #                 dur = 100
    #                 winsound.Beep(freq, dur)
    #             else:
    #                 print("Absent")
    #             print(str(len(index)) + f" no {word} Word Found")
    #
    #         if len(index) != 0:
    #             print("Total " + str(len(index)) + f" {word} Word Found")
    #             print(input("Press any Key: "))
    #         else:
    #             print(f"No {word} Word Found")


# from driver.driver import Driver
# driver = Driver().driver
#
# driver.get("https://www.facebook.com")
# from login.login import Login
# Login().login(driver)
# driver.get("https://www.facebook.com/groups/308915099815447")
#
# SearchKeyword().scrollAndSearchUsingXpath(driver)
# SearchKeyword().searchWordUsingXpath(driver)




