from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

#change your user name here !
userName = "HamdiAAA"

def giting(projectName):
    os.system("git init")
    os.system("git add .")
    os.system('git commit -m "let s role !" ')

    #get your web driver for your nav
    PATH = "C:\chromedriver.exe"

    #if it s not chrome change .chrome to your nav
    driver = webdriver.Chrome(PATH)
    driver.get("https://github.com/login")

    #here you chnage this with your logins
    info =  {
        "email" : "your mail goes here",
        "password" : "password ofc here xD ! "
    }

    login_field = driver.find_element_by_id("login_field")
    login_field.send_keys(info["email"])

    password = driver.find_element_by_id("password")
    password.send_keys(info["password"])
    password.send_keys(Keys.RETURN)

    driver.get("https://github.com/new")

    #what to do
    newProject = driver.find_element_by_id("repository_name")
    newProject.send_keys(projectName)
    newProject.send_keys(Keys.RETURN)

    time.sleep(2)
    newProject.send_keys(Keys.ENTER)

    os.system(f"git remote add origin https://github.com/{userName}/{projectName}.git")
    os.system("git branch -M main")
    os.system("git push -u origin main")







