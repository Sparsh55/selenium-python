# Selenium Automation Script

## Overview

This Python script uses Selenium to validate the search functionality on the Selenium Playground website. The script performs a series of tests to verify URL, title, and search functionality.

## screenshot:-
![image](https://github.com/user-attachments/assets/7d2a0b3b-c956-4d4e-a004-14d4ad30ef9c)

![image](https://github.com/user-attachments/assets/1379df13-59cc-4371-9550-fdac5903892b)



## Prerequisites

- Python 3.x
- Selenium
- pytest
- WebDriver (e.g., [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) for Chrome)

## Installation

1. Clone the repository or download the script files.
2. Open a terminal and navigate to the project directory.
3. Set up a virtual environment:

command:- 
python -m venv venv

## Activate the virtual environment:

On Windows:
.\venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

## Install the required Python packages:

pip install selenium pytest pytest-html

Download and set up the WebDriver for your browser (e.g., ChromeDriver for Chrome).

## Running the Script
Ensure the WebDriver is in your PATH or specify its path in the script.

Run the script using pytest:-

pytest -v --html=report.html

## Approach
The script performs the following tests:

test_open_page(): Opens the Selenium Playground Table Search Demo page.

test_validate_url(): Verifies the actual URL matches the expected URL.

test_validate_title(): Checks that the name of the header is "Table Sort And Search Demo".

test_search_new_york(): Locates the search box, scrolls the window, and performs a search for "New York".

test_validate_results(): Validates that the search results show 5 entries out of 24 total entries using robust assertion statements.

## Browser Compatibility
This script has been tested with:

Google Chrome

Mozilla Firefox

## Code Quality
The code follows PEP8 standards and is structured using pytest for easy maintenance and future enhancements.

## Designed and developed by Sparsh Saxena
