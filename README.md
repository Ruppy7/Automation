# Random-quote-gen

# Stoic Quote Fetcher

This repository contains a Python script that fetches a random stoic quote from the "stoic-quotes.com" API and displays it on a graphical window using tkinter. The script is designed to run at computer startup.

## Prerequisites

- Python 3 and above installed on your system.
- The `requests` library installed. If you don't have it, install it using `pip install requests`.

## Usage

1. Save the Python script and the corresponding .bat file in the same directory.

2. Double-click on the .bat file to run the Python script.

3. The script will fetch a random stoic quote from the API and display it on your screen in a centered graphical window.

## Windows Task Scheduler

To run the script automatically at computer startup, follow these steps:

1. Open the Windows Task Scheduler by searching for "Task Scheduler" in the Start menu.

2. In the right-hand Actions pane, click on "Create Basic Task."

3. Follow the wizard to create a basic task. Name it (e.g., Stoic Quote Fetcher) and set the trigger to "When the computer starts."

4. Choose "Start a Program" as the action and browse to select the .bat file created for running the Python script.

5. Complete the wizard, and the task will be scheduled to run at computer startup.

Now, whenever your computer starts up, the Python script will fetch a random stoic quote from the API and display it on your laptop screen in a centered graphical window.

## Note

- Ensure that your PC has an internet connection as soon as the computer starts.

- The script is set to display the quote in a 600x400 window centered on your screen.
