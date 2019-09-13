from selenium import webdriver
import pytest
import time


def test_check_add_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)

    
    button = browser.find_element_by_css_selector(".btn-add-to-basket")

    assert button is not None, "Add button doesn't contain at current link"



