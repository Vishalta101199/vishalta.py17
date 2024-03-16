from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver
driver = webdriver.Chrome()  # You can use any webdriver here (e.g., Firefox, Edge, etc.)
driver.maximize_window()

# Navigate to the URL
driver.get("https://jqueryui.com/droppable/")

# Switch to iframe containing draggable elements
driver.switch_to.frame(driver.find_element_by_css_selector(".demo-frame"))

# Locate draggable and droppable elements
draggable_element = driver.find_element_by_id("draggable")
droppable_element = driver.find_element_by_id("droppable")

# Perform drag and drop operation using ActionChains
actions = ActionChains(driver)
actions.drag_and_drop(draggable_element, droppable_element).perform()

# Wait for the drop to be successful (text changes to indicate successful drop)
wait = WebDriverWait(driver, 10)
wait.until(EC.text_to_be_present_in_element((By.ID, "droppable"), "Dropped!"))

# Output success message
print("Drag and drop operation successful!")

# Close the browser
driver.quit()
