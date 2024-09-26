# utf-8
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,datetime
import json


def start(num, target, content, execTime):

    try:
        #指定目标地址
        url = "https://docs.qq.com/form/page/" + target

        #初始化浏览器，登陆账号
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
        #driver.get("https://docs.qq.com")
        driver.get(url)
        driver.delete_all_cookies()

        with open('tenDocsCookies.json', 'r') as f:
            cookies = json.load(f)
            for cookie in cookies:
                driver.add_cookie(cookie)

        driver.refresh()
        driver.implicitly_wait(2)

        #确定开始抢票的时间，准备开始
        print("正在开始...")
        clock = execTime.split(":")
        currentTime = datetime.datetime.now()
        executeTime = datetime.datetime(currentTime.year, currentTime.month, currentTime.day, int(clock[0]), int(clock[1]), 0)
        waitPeriod = executeTime - currentTime
        time.sleep(waitPeriod.seconds)

        #计时结束，开始抢票
        while datetime.datetime.now() < executeTime:
            time.sleep(1)

        start = time.time()
        driver.get(url)
        driver.implicitly_wait(0.5)

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
        #elements[0].send_keys(sName)
        #elements[1].send_keys(sID)
        if elements.__len__() == num:
            for i in range(num):
                elements[i].send_keys(content[i])
        else :
            return False

        button = driver.find_element(By.XPATH, "//button[text()='提交']")
        #driver.execute_script("arguments[0].click();", button)
        button.click()
        driver.implicitly_wait(1)
        locator = (By.XPATH, "//button[contains(.,'确认')]")
        button = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
        button.click()

        print("抢票用时：")
        print(time.time() - start)
        driver.quit()
        return True
    except Exception as e:
        print(e)
        return False
