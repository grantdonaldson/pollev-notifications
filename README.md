# Pollev Desktop Notifications
This script automatically checks for the start of a presentation on the specified webpage and sends a desktop notification when the presentation begins.

# Presentation Notification Script

This script automatically checks for the start of a presentation on the specified webpage and sends a desktop notification when the presentation begins. It now includes a graphical user interface (GUI) for easier input of the ChromeDriver path and the URL parameter.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Downloading ChromeDriver](#downloading-chromedriver)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)

## Prerequisites

Make sure you have the following installed on your system:

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. **Clone this repository** or download the script file directly.

2. Install the required packages.

<code> pip install -r requirements.txt </code>

## Downloading ChromeDriver
To use the Selenium WebDriver for Chrome, you need to download ChromeDriver that matches your version of Chrome:

Check your Chrome version:

Open Chrome and go to chrome://settings/help to see your version.
Download ChromeDriver:

Visit the ChromeDriver download page.
Download the appropriate version for your operating system.
Place the chromedriver.exe file in a convenient location on your computer (e.g., C:\Users\<YourUsername>\Desktop\chromedriver-win64\).

## Usage

Run the script:

<code> python run.py </code>
A GUI will open, prompting you to provide the path to the ChromeDriver and the URL parameter (http://pollev.com/<URL PARAMETER>).

Click "Start" to run the script, which will open the specified webpage and click the "Skip for now" button. It will continuously check for the presentation status every 10 seconds, notifying you when it begins.

## Troubleshooting
Selenium WebDriver Issues: Ensure that the ChromeDriver version matches your installed Chrome version.
Permissions: If you encounter permission errors, ensure that your Python environment has the required permissions to execute scripts and access the ChromeDriver.
Notification Issues: Ensure that notifications are enabled on your operating system for the script to display alerts.



