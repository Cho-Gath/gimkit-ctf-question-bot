import os
from time import sleep

import pickle
import keyboard
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementNotInteractableException

import locations

def safe_click(driver, button):
    clicked = False
    while not clicked:
        try:
            button.click()
            clicked = True
        except NoSuchElementException or StaleElementReferenceException or ElementNotInteractableException:
            sleep(0.2)

def safe_find_text(driver, element):
    while True:
        try:
            text = driver.find_element_by_css_selector(element).text
            return text
        except NoSuchElementException or StaleElementReferenceException or ElementNotInteractableException:
            sleep(0.2)

with open('./vocab_set.pickle', 'rb') as file:
    vocab_set = pickle.load(file)

driver = webdriver.Firefox(executable_path=os.getenv("geckodriver_path"),service_log_path=os.devnull)

game_code = input('Game Code: ')

driver.get('https://www.gimkit.com/join?gc=' + game_code)

input('waiting')

while(True):
    answer = vocab_set[safe_find_text(driver, locations.question)]
    for button_selector in locations.button_list:
        button = driver.find_element_by_css_selector(button_selector)
        if button.text == answer:
            safe_click(driver, button)
            break
