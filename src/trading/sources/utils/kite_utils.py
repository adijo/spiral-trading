from __future__ import absolute_import

#from pyvirtualdisplay import Display
import requests
import urlparse
import unicodedata
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import hashlib
import os

from trading.constants.app_constants import CLIENT_ID, PASSWORD

REQUEST_TOKEN = "request_token"

CLIENT_ID_INPUT_FIELD = "inputone"
PASSWORD_INPUT_FIELD = "inputtwo"
FIRST_SECURITY_QUESTION_XPATH = "//span[@class='first']"
SECOND_SECURITY_QUESTION_XPATH = "//span[@class='second']"
FIRST_SECURITY_QUESTION_INPUT_XPATH = "//input[@name='answer1']"
SECOND_SECURITY_QUESTION_INPUT_XPATH = "//input[@name='answer2']"

# TODO: move to config or env vars
ANSWERS = {
	"abc": "answers here"
}


def get_redirected_url(url):
    #display = Display(visible=0, size=(1024, 768))
    #display.start()
    driver = webdriver.Chrome()
    driver.get(url)
    client_id = driver.find_element_by_id(CLIENT_ID_INPUT_FIELD)
    client_id.send_keys(os.environ[CLIENT_ID])
    password = driver.find_element_by_id("inputtwo")
    password.send_keys(os.environ[PASSWORD])
    password.send_keys(Keys.RETURN)
    first_question = driver.find_element_by_xpath(FIRST_SECURITY_QUESTION_XPATH)
    first_question_input = driver.find_element_by_xpath(FIRST_SECURITY_QUESTION_INPUT_XPATH)
    first_question_input.send_keys(ANSWERS[hash_string(first_question.text)])
    second_question = driver.find_element_by_xpath(SECOND_SECURITY_QUESTION_XPATH)
    second_question_input = driver.find_element_by_xpath(SECOND_SECURITY_QUESTION_INPUT_XPATH)
    second_question_input.send_keys(ANSWERS[hash_string(second_question.text)])
    second_question_input.send_keys(Keys.RETURN)
    #display.stop()
    return parse_url_parameter(driver.current_url, REQUEST_TOKEN)

def parse_url_parameter(url, param):
    parsed = urlparse.urlparse(url)
    return urlparse.parse_qs(parsed.query)[param][0]

def hash_string(s):
    hash_object = hashlib.sha256(s)
    hex_dig = hash_object.hexdigest()
    return hex_dig

