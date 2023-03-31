from selenium import webdriver
from time import sleep

USERNAME = 'your email address'
PASSWORD = 'your password'
error_flg = False

def load():
    counter = 0
    while True:
        driver.refresh()
        # scroll to bottom
        driver.execute_script("obj = document.body;obj.scrollTop = obj.scrollHeight;")
        s = input('press enter to reload? >')==''
        if s == True:
            counter += 1
            print('you have loaded ' + str(counter) + ' times')
        else:
            break

    return False

try:
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')	
    driver.get('https://admissions.42.fr')
    email_input = driver.find_element_by_id('user_email')
    password_input = driver.find_element_by_id('user_password')
    email_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    submit_button = driver.find_element_by_name('commit')
    submit_button.submit()
    sleep(0.5)
    load()
except Exception:
    print('error: ' + Exception)
    error_flg = True
finally:
    driver.close()
