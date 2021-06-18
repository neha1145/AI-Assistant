from selenium import webdriver
from Speak import *
from TakeCommand import *
from PrintGUI import *

def google_search(root):
    #speak('What should i search ?')
    driver = webdriver.Chrome('C:/Program Files/Google/Chrome/Application/chromedriver.exe')
    driver.get('https://www.google.com')
    SearchBox=driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    speak('What do you want to search in google ?')
    SearchBox.send_keys(takeCommand(root).lower())
    SearchButton= driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
    SearchButton.click()
    try:
        SearchResult=driver.find_element_by_xpath('//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[1]/div/div[1]/div/div[2]').text
        print_gui(root,SearchResult)
        speak(SearchResult)
    except Exception as e:
        print_gui(root,' ')