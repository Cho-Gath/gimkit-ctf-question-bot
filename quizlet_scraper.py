import pickle
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Firefox()
driver.get('https://google.com')

input('pause')

count = 1
in_a_row = 0
vocab_set = {}
while True:
    element = f'div.SetPageTerms-term:nth-child({count})'
    try:
        driver.find_element_by_css_selector(element)
    except NoSuchElementException:
        count += 1
        if in_a_row > 5:
            break
        in_a_row += 1
        continue
    key = driver.find_element_by_css_selector(element + ' > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)').text
    value = driver.find_element_by_css_selector(element + ' > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1) > span:nth-child(1)').text
    vocab_set[key] = value
    count += 1
    in_a_row = 0
name = input('name of set: ')
with open(f'{name}.pickle', 'wb') as f:
    pickle.dump(vocab_set, f)
