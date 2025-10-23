Link Programmer
This program is a simple tool that lets you create a custom webpage with 10 colorful, clickable buttons. You use a web-based form (powered by Gradio) to set the button names and website links, then download an HTML file (like buttons.html) that displays your buttons. Each button has a unique color and a pill shape, and clicking them opens your chosen websites in new browser tabs. This is great for creating a quick dashboard of your favorite links!
Screenshots
Below are examples of what you’ll see:

The Input Form: Where you enter button names and links.
The Generated Webpage: The final page with your custom buttons.

Features

Easy-to-Use Form: A clean web form where you type button names, website links, and a filename for your webpage.
Custom Buttons: Set names and links for 10 buttons, with defaults like "Google" and "https://www.google.com" provided.
Stylish Output: The generated webpage has a centered layout, Arial font, light gray background (#f0f0f0), and 10 pill-shaped buttons in different colors.
Quick Setup for Windows: A setup_and_run.bat file sets everything up and runs the program automatically.

Prerequisites

Python 3.6 or higher: Download from python.org. During installation, check "Add Python to PATH" so your computer can find it.
Windows: The setup_and_run.bat file is made for Windows. If you’re using Mac or Linux, see the manual setup below.

How to Use

Get the Files:

Download this repository (a "repository" is just a folder with the project files) by clicking the green "Code" button on GitHub and selecting "Download ZIP".
Unzip the folder to a place like your Desktop or Documents.
Make sure setup_and_run.bat and link_programmer.py are in the same folder.


Run the Program (Windows):

Double-click setup_and_run.bat in the folder.
The batch file will:
Create a virtual environment (a safe space for the program’s tools) called venv in the folder.
Install Gradio (the tool that makes the web form).
Run link_programmer.py to open the form in your browser.
Close the virtual environment when done.




Run the Program (Mac/Linux):

Open a terminal (on Mac, search for "Terminal"; on Linux, use your terminal app).
Navigate to the folder with cd /path/to/folder.
Create and activate a virtual environment:python3 -m venv venv
source venv/bin/activate


Install Gradio:pip install gradio


Run the program:python3 link_programmer.py




Use the Web Form:

The terminal will show a web address (e.g., http://127.0.0.1:7860). Copy and paste it into a browser like Chrome, Firefox, or Edge.
You’ll see (like in the first screenshot):
A heading: "Custom Link Programmer".
10 pairs of text boxes for button names (e.g., "LH7860") and website links (e.g., "localhost:7860").
A text box for the output filename (default: buttons.html).
A blue, pill-shaped "Save Custom Link Maker" button.




Customize Your Buttons:

Type new names and website links for each button. Leave boxes blank to keep defaults (e.g., "Google" and "https://www.google.com").
Enter a filename (e.g., my_links) or keep buttons.html. The .html will be added if you forget it.


Download the Webpage:

Click "Save Custom Link Maker".
A download link will appear. Click it to save your HTML file (e.g., buttons.html or my_links.html).


View Your Webpage:

Open the downloaded file in a browser (double-click it). You’ll see 10 colorful, pill-shaped buttons (like in the second screenshot) that open your chosen websites when clicked.



Where the Generated File is Located

The HTML file (e.g., buttons.html or my_links.html) is downloaded through your browser.
It usually goes to your Downloads folder (e.g., C:\Users\<YourName>\Downloads on Windows).
To find it:
Check your browser’s Downloads list (in Chrome, press Ctrl+J; in Firefox, go to Menu > Downloads).
Look in your Downloads folder or wherever your browser saves files.


The program also creates a temporary file in your computer’s temp folder (e.g., C:\Users\<YourName>\AppData\Local\Temp), but you don’t need to find this; the downloaded file is what you use.

Notes

Website Links: Use valid web addresses (e.g., https://example.com). Some defaults like localhost:7860 only work if you have a local server running.
Port Issues: If the form doesn’t load, port 7860 might be busy. Edit link_programmer.py:
Click link_programmer.py on GitHub.
Click the pencil icon, find demo.launch(), change to demo.launch(port=7861), and commit with a message like “Change Gradio port”.


Permissions: If you see errors, right-click setup_and_run.bat and select "Run as administrator".
Browsers: The generated webpage works in Chrome, Firefox, Edge, or similar.

Troubleshooting

Python Not Found: Open Command Prompt (search "cmd" in Windows) and run python --version. If it fails, install Python and ensure “Add to PATH” is checked.
Gradio Won’t Install: Ensure you’re online. Contact someone familiar with Python if needed, as this is unsupported.
Form Doesn’t Load: Check the terminal for the URL or errors. Try a different browser or port (e.g., 7861).
No Download Link: Ensure inputs are valid and click "Save Custom Link Maker" again. Check the browser console (F12 > Console) for errors.

Support
This program is provided as-is with no support. There are no guarantees it will work perfectly, and no updates or fixes will be provided. Use it at your own risk. For help with Python or Gradio, check:

Python Documentation
Gradio Documentation

Customization

Change Defaults: Open link_programmer.py in a text editor (like Notepad), find the default_links list, and edit names/URLs. Upload the updated file via GitHub.
Change Button Colors: In link_programmer.py, find html_content and edit .pill-button-X styles (e.g., change #007bff to another color code).
Change Form Style: In link_programmer.py, edit the css section in gr.Blocks to adjust the form’s look.

License
This project is unlicensed. You can use, modify, or share it freely, but no warranty or support is provided.
