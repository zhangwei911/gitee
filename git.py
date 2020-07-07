from selenium import webdriver
from time import sleep
#驱动路径 记得前面加r 防止字符转义
#!!!注意这里必须把驱动程序中的路径写完整，后面必须加上这个chromedriver.exe  否则会报错 执行不成功
driver = webdriver.Chrome('C:\\Users\\dell\\Desktop\\chromedriver_win32\\chromedriver.exe')
#用driver打开百度页面  后面的地址是百度的地址
driver.get('https://gitee.com/login')
# 将窗口最大化
driver.maximize_window()
username = input("请输入账号:")
# 查找页面的“设置”选项，发送一个你要搜索的值，并进行点击
driver.find_element_by_id('user_login').send_keys(username)
userpassword = input("请输入密码:")
driver.find_element_by_id('user_password').send_keys(userpassword)
#并进行点击
driver.find_element_by_class_name('submit').submit()
sleep(3)
driver.get('https://gitee.com/projects/new')
sleep(3)
driver.find_element_by_id('import-link').click()
sleep(1)
giturl = input("请输入git库地址:")
driver.find_element_by_id('project_import_url').send_keys(giturl)
# sleep(2)
driver.find_element_by_xpath('//*[@id="project_public_1"]/..').click()
sleep(2)
driver.find_element_by_id('submit-pro').submit()
#退出驱动程序
driver.quit()
