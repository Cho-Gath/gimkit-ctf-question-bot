import os
from time import sleep

import pickle
from selenium import webdriver

import locations


def safe_click(driver, button):
    while True:
        try:
            button = driver.find_element_by_css_selector(button)
            button.click()
            break
        # except NoSuchElementException or StaleElementReferenceException or ElementNotInteractableException:
        except Exception:
            sleep(0.2)


def safe_find_text(driver, element):
    while True:
        try:
            text = driver.find_element_by_css_selector(element).text
            return text
        except Exception:
            sleep(0.2)


with open('./vocab_set.pickle', 'rb') as file:
    vocab_set = pickle.load(file)

driver = webdriver.Firefox(executable_path=os.getenv("geckodriver_path"), service_log_path=os.devnull)

game_code = input('Game Code: ')

driver.get('https://www.gimkit.com/join?gc=' + game_code)

while True:
    question = safe_find_text(driver, locations.question)
    if question in vocab_set.keys():
        answer = vocab_set[question]
        for button in locations.button_list:
            if safe_find_text(driver, button) == answer:
                safe_click(driver, button)
                break
    else:
        clicked_answer = safe_find_text(driver, locations.top_left_button)
        result = safe_find_text(driver, locations.result_text)
        if result[0] == '+':
            vocab_set[question] = clicked_answer
        else:
            safe_click(driver, locations.view_correct_answer_button)
            vocab_set[question] = safe_find_text(driver, locations.correct_answer_text)
        with open('./vocab_set.pickle', 'wb') as file:
            pickle.dump(question, file)
    safe_click(driver, locations.continue_button)
