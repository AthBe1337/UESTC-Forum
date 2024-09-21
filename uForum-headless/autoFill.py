# utf-8
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,datetime
import json


def start(fID, sName, sID, stime):
    #指定目标地址
    url = "https://docs.qq.com/form/page/" + fID

    #初始化浏览器，登陆账号
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

    with open('/home/ubuntu/uestcForum/tenDocsCookies.json', 'r') as f:
        cookies = json.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)

    driver.refresh()
    driver.implicitly_wait(2)

    #确定开始抢票的时间，准备开始
    clock = stime.split(":")
    currentTime = datetime.datetime.now()
    executeTime = datetime.datetime(currentTime.year, currentTime.month, currentTime.day, int(clock[0]), int(clock[1]), 0)
    waitPeriod = executeTime - currentTime
    print("等待中...")
    time.sleep(waitPeriod.seconds)

    #计时结束，开始抢票
    #while datetime.datetime.now() < executeTime:
    #    time.sleep(1)

    driver.get(url)
    driver.implicitly_wait(2)
    start = time.time()

    # 等待元素出现
    timeout = 10  # 设置超时时间，单位为秒
    locator = (By.XPATH, "//textarea[@placeholder='请输入']")
    elements = []
    while not elements:
        try:
            elements = WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located(locator))
        except:
            pass
    if elements.__len__() == 0:
        print("未找到元素")
        return
    elements[0].send_keys(sName)
    elements[1].send_keys(sID)

    button = driver.find_element(By.XPATH, "//button[text()='提交']")
    #driver.execute_script("arguments[0].click();", button)
    button.click()
    locator = (By.XPATH, "//button[contains(.,'确认')]")
    button = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
    button.click()

    print("抢票用时：")
    print(time.time() - start)
    driver.quit()
    return
