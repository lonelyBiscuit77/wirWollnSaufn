import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Load user input from JSON file
with open('inputLogin.json') as f:
    user_data = json.load(f)

# Get the booking URL from the JSON file
booking_url = user_data['booking_url']

driver = webdriver.Chrome()

driver.get(booking_url)

is_under_26 = user_data['age'] < 26

# continuously check for "buchen" buttons and detect the opening of a second tab
buchen_buttons_found = False
second_tab_opened = False

# loop to attempt pressing "buchen" and detect if a new tab opens
while not second_tab_opened:
    try:
       
        buchen_button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='buchen' and @type='submit']"))
        )
        
        
        if is_under_26:
            buchen_button = driver.find_element(By.XPATH, "(//input[@value='buchen' and @type='submit'])[1]")
        else:
            buchen_button = driver.find_element(By.XPATH, "(//input[@value='buchen' and @type='submit'])[2]")
        
        print("Clicking the correct buchen button automatically...")
        buchen_button.click()
        buchen_buttons_found = True
    except Exception:
        
        print("Waiting for buchen button to appear or be pressed manually...")

    
    if len(driver.window_handles) > 1:
        second_tab_opened = True
        print("New tab detected.")
        break

    if not buchen_buttons_found:
        driver.refresh()
        time.sleep(2)  # adjust this sleep time to control refresh rate


try:
    driver.switch_to.window(driver.window_handles[1])  # switch to the new tab
    print("Switched to the new tab.")
except Exception as e:
    print(f"Failed to switch to the new tab: {e}")

try:
    pw_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Ich habe ein Passwort und möchte mich damit anmelden.']"))
    )
    pw_button.click()
    print("Clicked the password login button.")
except Exception as e:
    print(f"Failed to find or click the password login button: {e}")

try:
    driver.find_element(By.NAME, "pw_email").send_keys(user_data['email'])

    password_field = driver.find_element(By.XPATH, "//input[@type='password']")
    
    password_field.send_keys(user_data['password'])

    print("Login fields filled out.")
except Exception as e:
    print(f"Failed to fill out the login fields: {e}")

try:
    weiter_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='weiter zur Buchung' and @type='submit']"))
    )
    weiter_button.click()
    print("Clicked 'weiter zur Buchung'.")
except Exception as e:
    print(f"Failed to click 'weiter zur Buchung': {e}")

try:
    iban_value = user_data['iban']
    driver.execute_script(f"document.getElementById('BS_F_iban').value = '{iban_value}';")
    print("IBAN filled out successfully.")

    terms_checkbox = driver.find_element(By.NAME, "tnbed")
    terms_checkbox.click()
    print("Terms and conditions accepted.")
except Exception as e:
    print(f"Failed to fill IBAN or check terms: {e}")

try:
    final_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "bs_submit"))
    )
    final_button.click()
    print("Final 'weiter zur Buchung' button clicked.")
except Exception as e:
    print(f"Failed to click final 'weiter zur Buchung' button: {e}")

print("Script completed. Please review the page and close the browser manually.")
time.sleep(300)  # Keep the browser open for 5 minutes (300 seconds), or adjust as needed