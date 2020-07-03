
import time
import sys

from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Swiper():
    def __init__(self):
        self.driver = webdriver.Firefox()

    def tinder_login(self):
        self.driver.get('http://tinder.com')
        time.sleep(5)   
        print("Clicking on sign in with Number.")

        phone_number = input('The Phone number to sign in with : ')
        #modal_man = self.driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div[1]/div/div[3]/span/div[3]/button")

        # if modal_man is not None:
        #     print("SUCCESS")
        #     element_attribute_value = modal_man.get_attribute('class')
        #     print(element_attribute_value)

        # self.driver.quit()

        self.driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div[1]/div/div[3]/span/div[3]/button").click()
        time.sleep(2)

        self.driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div/div[2]/div/input").send_keys(phone_number)
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div/button").click()

        tinder_code = input("Please enter the code : ")
        if len(tinder_code) != 6:
            tinder_code = input("Your code needs to be 5 digits : ")

        self.driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div[1]/div[3]/input[1]").send_keys(tinder_code[0])
        self.driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div[1]/div[3]/input[2]").send_keys(tinder_code[1])
        self.driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div[1]/div[3]/input[3]").send_keys(tinder_code[2])
        self.driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div[1]/div[3]/input[4]").send_keys(tinder_code[3])
        self.driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div[1]/div[3]/input[5]").send_keys(tinder_code[4])
        self.driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div[1]/div[3]/input[6]").send_keys(tinder_code[5])

        input("Awaiting command to quit")
        self.driver.quit()
        sys.exit(0)


if __name__ == "__main__":
    swiper = Swiper()
    if swiper.tinder_login():
        #swiper.swipe_tinder()
    else:
        print("Login failed, Quitting")
        swiper.driver.quit()