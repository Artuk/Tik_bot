import selenium.common.exceptions
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

a = 0
driver = webdriver.Firefox()


def authorization_and_preparing():
    driver.get('https://www.tiktok.com')
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="header-login-button"]'))).click()
    WebDriverWait(driver, 2).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[5]/div[3]/div/div/div/div[1]/div/div/div[1]/div[2]/div/div'))).click()
    WebDriverWait(driver, 2).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[5]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[1]/a'))).click()
    WebDriverWait(driver, 2).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[5]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[1]/input'))).send_keys('') # В скобках send_keys вставьте логин от своего аккаунта
    WebDriverWait(driver, 2).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[5]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[2]/div/input'))).send_keys(
        '')# В скобках send_keys вставьте пароль от своего аккаунта
    WebDriverWait(driver, 2).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[5]/div[3]/div/div/div[1]/div[1]/div[2]/form/button'))).click()
    sleep(17) # Это время которое вам дается на прохождение капчи
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/nav/ul/li[1]/div/a').click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[2]/button[2]'))).click()

def action():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--headless")
    second_driver = webdriver.Firefox(options=firefox_options)

    try:
        second_driver.get('') # Это ссылка на ваш профиль в тик ток для получения оттуда количества подписчиков
        driver.execute_script('document.querySelector(".public-DraftEditorPlaceholder-inner").remove();')
        WebDriverWait(driver,3).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.css-qpucp9-DivInputEditorContainer.e1rzzhjk3 .public-DraftEditor-content'))).click()
        followers_element = second_driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[1]/h3/div[2]/strong')
        ActionChains(driver).send_keys('Пишу комментарии пока не наберу 1000 подписчиков.          ', followers_element.text,'/1000').perform()
        WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[4]/div/div[2]/div[2]/div/div[2]'))).click()
        WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[4]/div/div[1]/button[3]'))).click()
        sleep(randint(15,30))
    except selenium.common.exceptions.JavascriptException:
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[4]/div/div[1]/button[3]').click()
    second_driver.quit()

authorization_and_preparing()

while a < 100:
    action()
    a += 1

