
"""
A Python3 script to automate swiping right to anything and everything on [web-based] Tinder. UI elements and workflows are accurate as of 2018-NOV-01.
"""

# Import the relevant libraries and dependencies.
import time
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


# Define the Swiper Class and it's various functions.
class Swiper():


    def __init__(self):
        """
        Initialise the Chrome web driver. One may need to append the chromedrover.exe path to ones PATH.
        """
        self.driver = webdriver.Chrome()


    def fb_login(self):
        """
        Login to Facebook using username and password.
        """

        # Navigate to Facebook.
        print("Login to Facebook.")
        self.driver.get('https://www.facebook.com/')

        time.sleep(3)

        # Insert email address.
        print("Entering username.")
        a = self.driver.find_element_by_id('email')
        EmailAddress = "<YOUR EMAIL ADDRESS>"  # Hardcode email for speed.
        a.send_keys(EmailAddress)
        # a.send_keys(input('Opened Facebook. Please enter username/email: ')) # Accept email address from the console.
        print("Username entered. Moving on to password.")

        # Insert password.
        print("Entering password.")
        b = self.driver.find_element_by_id('pass')
        Password = '<YOUR PASSWORD>' # Hardcode password for speed.
        b.send_keys(Password)
        # b.send_keys(getpass(prompt='Username entered. Please enter password: ')) # Accept password from the console.
        print("Password entered. Logging in.")

        # Click on the Facebook login button.
        print("Clicking the login button.")
        c = self.driver.find_element_by_id('loginbutton')
        c.click()

        # Check whether Facebook login was successful by finding the home button.
        time.sleep(3)
        print("Confirming Facebook login.")

        try: 
            self.driver.find_element_by_id('u_0_c')
        except:
            return False
        return True
    

    def tinder_login(self):
        """
        Login to Tinder using the previos Facebook login as a SSO.
        """
        # Navigate to Tinder and wait for the page to load fully.
        self.driver.get('https://tinder.com')
        time.sleep(5)
        print("Clicking on sign in with Facebook.")

        # Click on the "Login using Facebook" button, making use of the Facebook SSO login.
        self.driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div[2]/div/div[3]/div/button/span").click()
        time.sleep(3)

        # Selenium scripts open a testing environment in chrome. Every login therefore acts like a brand new login. One must click through the tutorial.
        try: 
            print("Dismissing tutorial prompts")

            print("Prompt 1 - Location")
            self.driver.find_element_by_xpath('//*[@id="content"]/div/span/div/div[2]/div/div/div[3]/button[1]').click()
            time.sleep(1)

            print("Prompt 2 - Notifications")
            self.driver.find_element_by_xpath('//*[@id="content"]/div/span/div/div[2]/div/div/div[3]/button[1]').click()
            time.sleep(1)
        except:
            print('Something went wrong during login.')
            return False
        print("Ready to start swiping.")
        return True



    def swipe_tinder(self):
        """
        With Tinder loaded, begin swiping right.
        """

        # Initialise the chain of actions to come.
        ActionChains(self.driver)
        print("Swipe until there are no more profiles.")

        # Swipe right to anything and everything. Stop swiping by catching the exception of not finding a profile. Upon exception, close the browser.
        try:
            while self.driver.find_element_by_xpath('//*[@id="content"]/div/span/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[4]'):
                self.driver.find_element_by_xpath('//*[@id="content"]/div/span/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[4]').click()
                time.sleep(0.2)
        except:
            print("No more profiles found. Quitting.")
            self.driver.quit()


# Let's begin ... Are you a Boy or a Girl?
if __name__ == "__main__":
    swiper = Swiper()
    if(swiper.fb_login()):
        if swiper.tinder_login():
            swiper.swipe_tinder()
    else:
        print("Facebook login failed, Quitting")
        swiper.driver.quit()