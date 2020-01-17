from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time
import csv

def scroll_to_down(driver):
    SCROLL_PAUSE_TIME = 2

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
    # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break

        last_height = new_height


options = Options()
options.set_headless()

url = input("paste profile url: ")

firefox = webdriver.Firefox(options=options)
'''
firefox.get('https://www.instagram.com')
time.sleep(1)
face_book_login = firefox.find_element_by_class_name('sqdOP.L3NKy.y3zKF')
face_book_login.click()

email = firefox.find_element_by_id('email')
password = firefox.find_element_by_id('pass')

email.send_keys('')
password.send_keys("")
login = firefox.find_element_by_id('loginbutton')
login.click()
time.sleep(2)
'''
firefox.get(url)

#scroll_to_down(firefox)

time.sleep(2)
soup = BeautifulSoup(firefox.page_source, 'lxml')

firefox.close()

profile_name = soup.find('h1').text
username = soup.find("h1", class_="rhpdm").text
profile_picture = soup.find('img', class_="_6q-tv").attrs['src']
followers_info = soup.find_all('span', class_="g47SY")
info = []
for i in followers_info:
    info.append(i.text)
a, b, c = info[0], info[1], info[2]

with open('profiles.csv', mode="a+") as file:
    profile_writer = csv.writer(file, delimiter=',',)
    profile_writer.writerow([profile_name, username, profile_picture, a, b, c])
