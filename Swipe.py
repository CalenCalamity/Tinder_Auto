
import time
import sys, getopt

from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Swiper():
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path = 'bin/geckodriver.exe')

    def tinder_login(self, phone_number):
        self.driver.get('http://tinder.com')
        time.sleep(5)   
        print("Clicking on sign in with Number.")

        if not phone_number:
            phone_number = input('The Phone number to sign in with : ')

        self.driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div[1]/div/div[3]/span/div[3]/button").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div/div[2]/div/input").send_keys(phone_number)
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div/button").click()

        tinder_code = input("Please enter the code : ")

        while len(tinder_code) != 6:
            tinder_code = input("Your code needs to be 6 digits : ")

        self.driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div[1]/div[3]/input[1]").send_keys(tinder_code[0])
        self.driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div[1]/div[3]/input[2]").send_keys(tinder_code[1])
        self.driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div[1]/div[3]/input[3]").send_keys(tinder_code[2])
        self.driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div[1]/div[3]/input[4]").send_keys(tinder_code[3])
        self.driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div[1]/div[3]/input[5]").send_keys(tinder_code[4])
        self.driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div[1]/div[3]/input[6]").send_keys(tinder_code[5])
        self.driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div[1]/button").click()

        time.sleep(4)
        self.driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div/div/div[3]/button[1]").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div/div/div[3]/button[1]").click()
        time.sleep(4)
        
        print("Ready to start swiping.")
        return True

    def swipe(self):
        time.sleep(5)
        actions = ActionChains(self.driver)
        time.sleep(5)
        print("Swipe until there are no more profiles.")
        try:
            while self.driver.find_element_by_xpath("//*[@id=\"content\"]/div/div[1]/div/main/div[1]/div/div/div[1]/div"):
                actions.send_keys(Keys.ARROW_RIGHT).perform()
                time.sleep(2)
        except:
            print("No more profiles found. Quitting.")
            self.driver.quit()

        
    def swipe_tinder(self):
        actions = ActionChains(self.driver)
        time.sleep(5)
        print("Swipe until there are no more profiles.")
        try:
            #Stop swiping by catching the exception of not finding a profile. closes browser
            while self.driver.find_element_by_xpath("//*[@id=\"content\"]/div/span/div/div[1]/div/main/div/div/div/div[1]/div[1]/div/div[3]/div[1]"):
                actions.send_keys(Keys.ARROW_RIGHT).perform()
                time.sleep(2)
        except:
            print("No more profiles found. Quitting.")
            self.driver.quit()


if __name__ == "__main__":
    phone_number = ''
    
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["p="])
    except getopt.GetoptError:
        print('Swipe.py -p <Phone Number>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '--p':
            phone_number = arg

    swiper = Swiper()
    if swiper.tinder_login(phone_number):
        swiper.swipe()
    else:
        print("Login failed, Quitting")
        swiper.driver.quit()