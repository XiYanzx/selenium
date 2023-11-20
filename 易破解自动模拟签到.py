from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def calculate_expression(expression):
    # 替换非标准的减号为标准减号
    expression = expression.replace('−', '-')
    # 替换其他可能的非标准运算符
    expression = expression.replace('×', '*').replace('÷', '/')
    # 移除等号
    expression = expression.replace('=', '')
    # 计算表达式
    try:
        result = eval(expression)
        return result
    except Exception as e:
        print(f"无法计算表达式: {expression}. 错误: {e}")
        return None

chrome_options = Options()
chrome_options.page_load_strategy = 'normal'
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
web = webdriver.Chrome(options=chrome_options)
web.set_window_size(1920,1080)
web.get('https://www.ypojie.com/wp-login.php')
text = web.find_element(By.XPATH, '//*[@id="loginform"]/div[2]/strong').text
print("原始表达式:", text)

# 计算并打印结果
result = calculate_expression(text)
if result is not None:
    print("计算结果:", result)
web.find_element(By.XPATH,'//*[@id="user_login"]').send_keys("czxm2019@163.com")
web.find_element(By.XPATH,'//*[@id="user_pass"]').send_keys("lhm123456..")
web.find_element(By.XPATH,'//*[@id="aiowps-captcha-answer"]').send_keys(result)
web.find_element(By.XPATH,'//*[@id="wp-submit"]').click()
web.find_element(By.XPATH,'/html/body/header/div/div[2]/ul/li[1]/a').click()
web.switch_to.window(web.window_handles[-1])
web.find_element(By.XPATH,'/html/body/div[4]/div/ul/li[1]').click()
print("今日已签到")
web.quit()