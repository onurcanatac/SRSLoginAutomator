from asyncio.windows_events import NULL
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

#enter required info of the user
studentID = ""
srsPassword = ""

mailAdress = ""
mailPassword = ""

#create driver and get it into SRS
url = 'https://stars.bilkent.edu.tr/srs/'
browser = webdriver.Chrome()
browser.get(url)

browser.maximize_window()

#find ID textbox and put the ID in it
bilkentIDtextspace = browser.find_element_by_xpath('//*[@id="LoginForm_username"]')
bilkentIDtextspace.send_keys(studentID)

#find the password input variable and put the SRS password in it
srsPassScript = 'document.getElementsByName("LoginForm[password]")[0].setAttribute("value", "' + srsPassword + '")'
browser.execute_script(srsPassScript)

#click to the login button
button = browser.find_element_by_xpath('//*[@id="login-form"]/fieldset/div/div[1]/div[3]/button')
button.click()

#open new window and get into Bilkent webmail 
browser.execute_script('''window.open("https://webmail.bilkent.edu.tr/","_blank");''')

#switch the driver to that window
windows = browser.window_handles
browser.switch_to.window(windows[1])

#enter the email adress of student
MailNametextspace = browser.find_element_by_xpath('//*[@id="rcmloginuser"]')
MailNametextspace.send_keys(mailAdress)

#put mail password into the password input variable
mailPassScript = 'document.getElementsByName("_pass")[0].setAttribute("value", "' + mailPassword + '")'
browser.execute_script(mailPassScript)

#click to mail login button and log into the email
MailLoginButton = browser.find_element_by_xpath('//*[@id="rcmloginsubmit"]')
MailLoginButton.click()

#wait for a little bit of time in order to avoid the emails with late timing
time.sleep(3)

#find the latest received mail and double click onto it, a page comes up with only that mail in it 
PasswMail = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[4]/table[2]/tbody/tr[1]') # get all of the rows in the table

action = ActionChains(browser)
PasswMail.click()
action.double_click(PasswMail).perform()

#get the full message in that email as text
starsCodeText = browser.find_element_by_xpath('//*[@id="message-part1"]/div').text

#find numbers in the text as digits an get the first one (which is the SRS verificaiton code)as a string
starsCode = [int(word) for word in starsCodeText.split() if word.isdigit()]
starsCodeStr = str(starsCode[0])

#switch the driver back to the SRS window
browser.switch_to.window(windows[0])

#enter the verification code to the required textbox
starsCodeTextspace = browser.find_element_by_xpath('//*[@id="EmailVerifyForm_verifyCode"]')
starsCodeTextspace.send_keys(starsCodeStr)

#click to the verify button which puts us into the SRS system
verifyButton = browser.find_element_by_xpath('//*[@id="verifyEmail-form"]/fieldset/div/div[1]/div[2]/button')
verifyButton.click()