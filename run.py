import tkinter as tk
from tkinter import filedialog, messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.request import Request, urlopen
from plyer import notification
from bs4 import BeautifulSoup
import time

def browse_chromedriver():
    """Open a file dialog to select the ChromeDriver executable."""
    filename = filedialog.askopenfilename(title="Select ChromeDriver", filetypes=(("Executable Files", "*.exe"),))
    chromedriver_entry.delete(0, tk.END)
    chromedriver_entry.insert(0, filename)

def run_script():
    """Run the presentation notification script with the provided inputs."""
    chromedriver_path = chromedriver_entry.get()
    url_param = url_param_entry.get()

    if not chromedriver_path or not url_param:
        messagebox.showerror("Input Error", "Please provide both the ChromeDriver path and URL parameter.")
        return

    # Initialize the WebDriver using the Service class
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service)

    # Open the URL
    url = f'https://pollev.com/{url_param}'
    driver.get(url)

    # Allow time for the page to load and click the button
    click_skip_button(driver)

    # Wait for the new content to load
    time.sleep(3)

    while True:
        # Get the HTML of the resulting page
        html_page = driver.page_source
        soup = BeautifulSoup(html_page, 'html.parser')

        # Check the presentation status
        element = check_presentation_status(soup)

        if element:
            print("Presentation has not started.")
        else:
            print("Presentation has begun!")
            notify_presentation_started()
            break  # Exit the loop when the presentation starts

        # Wait 10 seconds before checking again
        time.sleep(10)

    # Close the driver
    driver.quit()

def click_skip_button(driver):
    """Find and click the 'Skip for now' button."""
    try:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Skip for now']]"))
        )
        button.click()
    except Exception as e:
        print("Error clicking button:", e)

def check_presentation_status(soup):
    """Check if the presentation has started by searching for the specific <h1> element."""
    element = soup.find('h1', class_="text-xl font-semibold", text=lambda t: t and f"Waiting for {url_param_entry.get()}'s presentation to begin" in t)
    return element

def notify_presentation_started():
    """Send desktop notification when the presentation starts."""
    notification.notify(
        title="Presentation Started",
        message="mkogan's presentation has begun!",
        timeout=10  # Notification will stay for 10 seconds
    )

# Create the GUI
root = tk.Tk()
root.title("Presentation Notification Setup")

tk.Label(root, text="ChromeDriver Path:").pack(pady=10)
chromedriver_entry = tk.Entry(root, width=50)
chromedriver_entry.pack(pady=5)
tk.Button(root, text="Browse", command=browse_chromedriver).pack(pady=5)

tk.Label(root, text="URL Parameter:").pack(pady=10)
url_param_entry = tk.Entry(root, width=50)
url_param_entry.pack(pady=5)

tk.Button(root, text="Start", command=run_script).pack(pady=20)

root.mainloop()
