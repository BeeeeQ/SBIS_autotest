from selenium.webdriver.common.by import By
from selenium import webdriver
try:
    link = "https://sbis.ru/"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    browser.maximize_window()
    browser.find_element(By.LINK_TEXT, 'Поддержка').click()
    browser.find_element(By.CLASS_NAME, 'sbis_ru-CookieAgreement__close').click()
    browser.find_element(By.XPATH, './/div/h4[text()="Скачать"]').click()
    link_full_base = browser.find_element(By.XPATH, './/div[2]/div/div/a[contains(text(), "Полная версия")]').get_attribute('href')
    link_update_base = browser.find_element(By.XPATH, './/div[2]/div/div/a[contains(text(), "Обновление")]').get_attribute('href')
    link_jinn = browser.find_element(By.XPATH, './/div[3]/div/div/a[contains(text(), "Полная версия")]').get_attribute('href')
    link_2d_scan = browser.find_element(By.XPATH, './/div[4]/div[2]/div/a[contains(text(), "Скачать")]').get_attribute('href')
    link_library_samples = browser.find_element(By.XPATH, './/div[5]/div[2]/div/a[contains(text(), "Скачать")]').get_attribute('href')
    links_list = [link_full_base, link_update_base, link_jinn, link_2d_scan, link_library_samples]
    my_file = open("links_sbis.txt", "w+")
    for index in links_list:
        my_file.write(index + '\n')
    my_file.close()
finally:
    browser.quit()
