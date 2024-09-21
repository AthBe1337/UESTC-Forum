# utf-8
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json


def init():
    url = "https://docs.qq.com/"
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)
        ser = Service('/usr/local/bin/chromedriver')
        driver = webdriver.Chrome(service=ser, options=options)
        driver.set_window_size(1366, 768)
        driver.get(url)
        driver.delete_all_cookies()
        driver.refresh()
        driver.implicitly_wait(1)
        elmet = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/header/div/div[4]/button[2]")
        elmet.click()
        driver.implicitly_wait(1)
        elmet = driver.find_element(By.ID, "duiCheckboxId-3")
        elmet.click()
        driver.implicitly_wait(1)
        driver._switch_to.frame(driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div/iframe"))
        elmet = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/img")
        qrCodeSrc = elmet.get_attribute("src")
        print("二维码地址如下，请尽快扫码 \n" + qrCodeSrc + "\n")

        while True:
            ch = input("是否已登录/已过期？(y/n)")
            if(ch == 'y'):
                break
                pass
            elif(ch == 'n'):
                elmet.click()
                driver.implicitly_wait(1)
                qrCodeSrc = elmet.get_attribute("src")
                print("新的二维码地址如下，请尽快扫码 \n" + qrCodeSrc + "\n")

        driver.switch_to.default_content()
        cookies = driver.get_cookies()

        with open('/home/ubuntu/uestcForum/tenDocsCookies.json', 'w') as f:
            json.dump(cookies, f)
            f.close()

        driver.close()

    except Exception as e:
        print(e)
        return False

    return True