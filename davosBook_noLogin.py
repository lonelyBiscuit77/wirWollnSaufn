import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Load user input from JSON file
with open('input.json') as f:
    user_data = json.load(f)

# Initialize the Selenium WebDriver (Assuming you're using Chrome)
driver = webdriver.Chrome()

# Define the booking URL
booking_url = "https://buchung.hsz.rwth-aachen.de/angebote/Wintersemester/_Extratouren_Davos_Maerz.html"

# Open the Davos booking page
driver.get(booking_url)

# Maximize the window for better visibility
driver.maximize_window()

# Check whether the person is under or over 26 years old
is_under_26 = user_data['age'] < 26

# Wait and refresh the page until "buchen" buttons appear
buchen_buttons_found = False
while not buchen_buttons_found:
    try:
        # Try to locate the buchen button (refresh until it's clickable)
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='buchen' and @type='submit']"))
        )
        buchen_buttons_found = True  # If buttons are found, stop refreshing
        print("Buchen buttons found.")
    except Exception:
        # If the buttons are not found, refresh the page and try again
        print("Buchen buttons not found, refreshing...")
        driver.refresh()
        time.sleep(3)  # Small delay between refreshes

# Select the appropriate "buchen" button based on age
try:
    if is_under_26:
        # First row for under 26 years old
        buchen_button = driver.find_element(By.XPATH, "(//input[@value='buchen' and @type='submit'])[1]")
    else:
        # Second row for above 26 years old
        buchen_button = driver.find_element(By.XPATH, "(//input[@value='buchen' and @type='submit'])[2]")

    print("Clicking the correct buchen button...")
    buchen_button.click()
except Exception as e:
    print(f"Failed to find or click the buchen button: {e}")

# Wait for the second tab to open and switch to it
try:
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)  # Wait for a new tab
    driver.switch_to.window(driver.window_handles[1])  # Switch to the new tab
    print("Switched to the new tab.")
except Exception as e:
    print(f"Failed to switch to the new tab: {e}")

# Wait for the form to load (after switching to the new tab)
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "vorname")))
    print("Form loaded successfully.")
except Exception as e:
    print(f"Failed to load the form: {e}")

# Fill in the form fields
try:
    # Gender (assuming "keine Angabe" is selected, i.e., value="X")
    driver.find_element(By.XPATH, "//input[@type='radio' and @value='X']").click()

    # First Name
    driver.find_element(By.NAME, "vorname").send_keys(user_data['first_name'])
    
    # Surname
    driver.find_element(By.NAME, "name").send_keys(user_data['surname'])
    
    # Street
    driver.find_element(By.NAME, "strasse").send_keys(user_data['street'])
    
    # Zip Code + City
    driver.find_element(By.NAME, "ort").send_keys(f"{user_data['zip']} {user_data['city']}")

    # Status (dropdown)
    status_dropdown = Select(driver.find_element(By.NAME, "statusorig"))
    status_dropdown.select_by_visible_text(user_data['status'])

    # Matriculation Number
    driver.find_element(By.NAME, "matnr").send_keys(user_data['matriculation_number'])

    # E-mail Address
    driver.find_element(By.NAME, "email").send_keys(user_data['email'])

    # Phone Number
    driver.find_element(By.NAME, "telefon").send_keys(user_data['phone'])

    # Fill IBAN using JavaScript to bypass validation
    iban_value = user_data['iban']
    driver.execute_script(f"document.getElementById('BS_F_iban').value = '{iban_value}';")
    
    print("Form filled out successfully, including IBAN.")
except Exception as e:
    print(f"Failed to fill out the form: {e}")

# Check the box for terms and conditions
try:
    terms_checkbox = driver.find_element(By.NAME, "tnbed")
    terms_checkbox.click()
    print("Terms and conditions accepted.")
except Exception as e:
    print(f"Failed to check terms and conditions: {e}")

# Keep the browser open for manual closing
print("Script completed. Please review the page and close the browser manually.")
time.sleep(300)  # Keep the browser open for 5 minutes (300 seconds), or adjust as needed
