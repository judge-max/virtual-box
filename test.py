from selenium import webdriver
import time

def submit(prob_id, code):
    driver_path = r'C:/Users/caspe/Downloads/chromedriver_win32/chromedriver.exe'
    driver = webdriver.Chrome(driver_path)

    driver.get("https://tioj.ck.tp.edu.tw/users/sign_in")

    USERNAME = 'ESCape'
    PASSWORD = 'escape'

    driver.find_element_by_id("user_username").send_keys(USERNAME)
    driver.find_element_by_id("user_password").send_keys(PASSWORD)
    driver.find_element_by_name("commit").click()

    driver.get("https://tioj.ck.tp.edu.tw/problems/"+str(prob_id)+"/submissions/new")
    driver.find_element_by_id("code-input").send_keys(code)
    driver.find_element_by_name("commit").click()

    while len(driver.find_element_by_xpath("//*[@id='page-content']/div/div[2]/div/div[4]").text) == 0:
        time.sleep(0.5)
        driver.refresh()

    result = driver.find_element_by_xpath("//*[@id='page-content']/div/div[2]/div/div[4]").text

    return result

code = '''#include <bits/stdc++.h>
using namespace std;
signed main() {
    cout << "Hello Tmt World XD!" << endl;
    return 0;
}'''
print(submit(1001, code))