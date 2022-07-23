from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import yaml
import time
import logging
import os

CONFIG_PATH="./config/" # 若此项为空, 则读取下列配置
HEADLESS = False

USERNAME = ""
PASSWORD = ""
REASON = "其他必要事项"
FULL_REASON = "吃饭"
TRACK = "达美乐"
PROVINCE = "北京市"
CITY = "市辖区"
DISTRICTS = "海淀区"
STREET = "海淀街道"

# 以下配置不建议更改以避免未知错误-------------------------------
START = 1
END = 7



class Pkusubmit():

    def __init__(self):
        self.driver=None
        # self.start_driver()
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s %(levelname)s %(message)s',
            datefmt='%H:%M:%S')
        self.log = logging
        self.username = USERNAME
        self.password = PASSWORD
        self.reason = REASON
        self.start = START
        self.end = END
        self.full_reason = FULL_REASON
        self.track = TRACK
        self.province = PROVINCE
        self.city = CITY
        self.districts = DISTRICTS
        self.street = STREET

    def start_driver(self):
        ff_op = webdriver.FirefoxOptions()
        ff_op.headless = HEADLESS
        self.driver = webdriver.Firefox(options=ff_op)

    def teardown(self, method):
        try:
            self.driver.quit()
        except:
            pass

    def read_config(self,config_path):
        d=yaml.safe_load(config_path)
        self.username=d["username"]
        self.password=d["password"]
        self.reason=d["reason"]
        self.start=d["start"]
        self.end=d["end"]
        self.full_reason=d["full_reason"]
        self.track=d["track"]
        self.province=d["province"]
        self.city=d["city"]
        self.districts=d["districts"]
        self.street=d["street"]


    def submit(self):
        self.driver.get(
            "https://iaaa.pku.edu.cn/iaaa/oauth.jsp?appID=portal2017&appName=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6%E6%A0%A1%E5%86%85%E4%BF%A1%E6%81%AF%E9%97%A8%E6%88%B7%E6%96%B0%E7%89%88&redirectUrl=https%3A%2F%2Fportal.pku.edu.cn%2Fportal2017%2FssoLogin.do"
        )
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, "user_name"))).send_keys(self.username)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, "password"))).send_keys(self.password)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "logon_button"))).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "keyword"))).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, "keyword"))).send_keys("学生出入校")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, "keyword"))).send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, "stuCampusExEnReq"))).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(.,\' 出入校申请\')]"))).click()
        time.sleep(7)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(.,\'确定\')]"))).click()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[2]/div/div/div/div/input"))).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, f"//span[contains(.,'{self.reason}')]"))).click()


        start_end=[]
        for i in [self.start,self.end]:
            if i==1:
                start_end.append('')
            else:
                start_end.append(f'[{i}]')
        # 起点选择燕园
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@type=\'text\'])[3]"))).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, f"//div[3]/div/div/ul/li{start_end[0]}"))).click()

        # 终点选择校外
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@type=\'text\'])[4]"))).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, f"//div[4]/div/div/ul/li{start_end[1]}"))).click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@type=\'text\'])[5]"))).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR,
                 ".el-col-md-12 .el-textarea__inner"))).send_keys(f"{self.full_reason}")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[2]/ul/li[3]"))).click()
        if self.end==7:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR,
                    "div:nth-child(8) > .el-col:nth-child(2) .el-input__inner"
                    ))).click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//li[contains(.,'{self.province}')]"))).click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR,
                    "div:nth-child(8) > .el-col:nth-child(3) .el-input__inner"
                    ))).click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//li[contains(.,'{self.city}')]"))).click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR,
                    "div:nth-child(8) > .el-col:nth-child(4) .el-select__caret"
                    ))).click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//li[contains(.,'{self.districts}')]"))).click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "(//input[@type=\'text\'])[10]"))).send_keys(f"{self.street}")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR,
                 ".el-col-md-24 > .is-required .el-textarea__inner"))).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR,
                 ".el-col-md-24 > .is-required .el-textarea__inner"
                 ))).send_keys(f"{self.track}")

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CLASS_NAME,
                'el-button.el-button--primary.el-button--small'
            ))).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CLASS_NAME,
                'el-button.el-button--default.el-button--small.el-button--primary'
            ))).click()

        self.log.info('填报完成')

    def main(self,config_path=''):
        if config_path:
            self.read_config(config_path)
        self.log.info(f'{self.username} start')
        success_flag = False
        while(5):
            if(success_flag):
                break
            try:
                self.start_driver()
                self.submit()
                self.teardown()
                success_flag=True
                self.log.info(f'{self.username} success')
            except:
                self.teardown()
        return success_flag


if __name__=='__main__':

    p = Pkusubmit()

    if CONFIG_PATH:
        for i in os.listdir(CONFIG_PATH):
            if i[-4:]=='.yml':
                p.main(i)
    else:
        p.main()
