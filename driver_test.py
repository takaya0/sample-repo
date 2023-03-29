import chromedriver_binary  # <- これでChromeDriverをPATHに自動追加してくれる
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
target_url = 'https://odaibako.net/u/mazo773sissy'
target_class_name = 'longtext_box'

message = '夜に変態衣装に着替えて、外に出る。\nその後証拠写真を撮りツイートする'


def main():
    driver = webdriver.Chrome()
    driver.get(target_url)

    work_box = driver.find_element(By.CLASS_NAME, target_class_name)
    work_box.send_keys(message)
    submit_butotn = driver.find_element(By.CLASS_NAME, 'submit_button')
    submit_butotn.click()
    time.sleep(3)
    modal_submit_button = driver.find_element(
        By.CLASS_NAME, 'modal-submit-button')
    modal_submit_button.click()
    time.sleep(3)
    driver.close()


if __name__ == '__main__':
    main()
