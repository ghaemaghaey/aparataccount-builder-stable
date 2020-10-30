import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyperclip
harf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
names = ['ali','mohammad','abbas','abolfazl','darya','soltan','zahra','mahsa','abdollah','reza','ghaem','nayeb','nima'
,'sadra','ahmad','fateme','hojat','haji','mahdi','hadi','maryam','soghra','karim','safooreh','hasan','sajjad','sadegh','saber',]#sum =28
codes = ['9','8','7','6','5','4','3','2','1']
driver = webdriver.Chrome()
while True:
    try:
        for i in range(29):
            file = open('users.txt', 'a+')
            for a in range(1):
                codesnumber1 = random.choice(codes)
                codesnumber2 = random.choice(harf)
                codesnumber3 = random.choice(codes)
                codesnumber4 = random.choice(harf)
                code = codesnumber1+codesnumber2+codesnumber3+codesnumber4
            print(code)
            driver.get('https://mail.tm/en')
            sleep(3)
            driver.find_element_by_xpath('//*[@id="accounts-menu"]').click()
            driver.find_element_by_xpath('//*[@id="accounts-list"]/div/div[5]/a').click()
            sleep(1)
            driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div/div[2]/div[2]/span[1]/button').click()
            sleep(4)
            driver.find_element_by_xpath('//*[@id="email"]').click()
            driver.get('https://www.aparat.com/signup')
            sleep(5)
            username = driver.find_element_by_id('account')
            username.send_keys(pyperclip.paste()+Keys.ENTER)
            driver.get('https://mail.tm/en')
            sleep(7)
            driver.get('https://mail.tm/en')
            driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/main/div/div[2]/ul/li/a').click()
            sleep(3)
            ifream = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/main/div/div[3]/div[2]/div/div/iframe')
            driver.switch_to.frame(ifream)
            driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/a').click()
            driver.switch_to.default_content()
            driver.switch_to_window(driver.window_handles[1])
            sleep(5)
            try:
                driver.find_element_by_id('newpassword').send_keys('1520642814Ghh')
                driver.find_element_by_id('newpassword-confirm').send_keys('1520642814Ghh'+Keys.ENTER)
            except:
                driver.switch_to.window(driver.window_handles[0])
                driver.close()
                driver.switch_to.window(driver.window_handles[1])
                driver.find_element_by_id('newpassword').send_keys('1520642814Ghh')
                driver.find_element_by_id('newpassword-confirm').send_keys('1520642814Ghh'+Keys.ENTER)
            sleep(3)
            driver.get('https://www.aparat.com/user/profile/change_username/username/')
            usernameOUT = names[i]+code
            driver.find_element_by_id('newUsernameInput').send_keys(usernameOUT+Keys.ENTER)
            file.write(usernameOUT)
            file.write('\n')
            try:
                driver.switch_to_window(driver.window_handles[0])
                driver.close()
            except:
                driver.switch_to_window(driver.window_handles[0])
                driver.close()
                driver.switch_to_window(driver.window_handles[0])
                driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.delete_all_cookies()
            file.close()
    except:
        print('erore')
        driver.delete_all_cookies()
        