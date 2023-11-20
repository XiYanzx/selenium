from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.page_load_strategy = 'normal'
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
web = webdriver.Chrome(options=chrome_options)
web.get('https://www.52pojie.cn/index.php')
time.sleep(4)

# 点击QQ登录按钮
web.find_element(By.XPATH, '//*[@id="lsform"]/div/div[2]/p[1]/a').click()
time.sleep(5)

window_handles = web.window_handles
# 切换iframe
iframe = web.find_element(By.XPATH,'//*[@id="ptlogin_iframe"]')
web.switch_to.frame(iframe)

web.find_element(By.XPATH,'//*[@id="qlogin_list"]/a').click()
time.sleep(2)
web.switch_to.default_content()
web.find_element(By.XPATH,'//*[@id="um"]/p[2]/a[1]').click()
time.sleep(5)
web.switch_to.default_content()
time.sleep(3)
num = web.find_element(By.XPATH,'//*[@id="ct"]/div[1]/div/ul[2]/li[1]').text
print(num)
web.quit()






