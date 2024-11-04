# Pollev Desktop Notifications
This script automatically checks for the start of a presentation on the specified webpage and sends a desktop notification when the presentation begins.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Downloading ChromeDriver](#downloading-chromedriver)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Discalimer](#disclaimer)
- [License](#license)

## Prerequisites

Make sure you have the following installed on your system:

- Python 3.6 or higher
- pip (Python package installer)
- Google Chrome
- Windows

## Installation

1. **Clone this repository** or download the script file directly.

2. Install the required packages.

``` pip install -r requirements.txt ```

## Downloading ChromeDriver

To use the Selenium WebDriver for Chrome, you need to download ChromeDriver that matches your version of Chrome:

Check your Chrome version:

Open Chrome and go to <a href = "chrome://settings/help"> chrome://settings/help </a> to see your version.
Download ChromeDriver:

1. Visit the <a href="https://googlechromelabs.github.io/chrome-for-testing/"> ChromeDriver download page </a>. <br>
2. Download the appropriate version for your operating system. <br>
3. Place the chromedriver.exe file in a convenient location on your computer (e.g., C:\Users\<YourUsername>\Desktop\chromedriver-win64\). The path of the executable will be needed when running the program. <br>

## Usage

Run the script:
```
python run.py
```

A UI will open, prompting you to provide the path to the ChromeDriver and the URL parameter e.g. for pollev.com/mypoll, the URL parameter would be "mypoll".

Click "Start" to run the script, which will open the specified webpage and click the "Skip for now" button. It will continuously check for the presentation status every 10 seconds, notifying you when it begins.

## Troubleshooting

<b> Selenium WebDriver Issues </b> - Ensure that the ChromeDriver version matches your installed Chrome version. <br>

<b>Permissions </b> - If you encounter permission errors, ensure that your Python environment has the required permissions to execute scripts and access the ChromeDriver. <br>

<b> Notification Issues </b> - Ensure that notifications are enabled on your operating system for the script to display alerts. <br>

## Disclaimer
This project is intended for educational purposes only. Users are reminded to adhere to academic integrity guidelines while using this script. Do not use this tool to disrupt or interfere with online presentations or events. Always respect the terms of service of the websites you access.

## License
This project is open source and available under the MIT License.



