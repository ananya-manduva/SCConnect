# Web Scraper

This is a simple Python web scraper to extract contact information (emails, phone numbers, and addresses) from local business websites.

## Installation

1. Clone this repository:
    ```
    git clone https://github.com/your-username/web-scraper.git
    ```

2. Navigate to the project directory:
    ```
    cd web-scraper
    ```

4. Create Virtual Environment (if you don't have one)
   ```
   python -m venv venv
   ```
5. Activate the virtual environment:

- On Windows (Command Prompt):
    ```
    .\venv\Scripts\activate

    ```
- On macOS/Linux:
    ```
    source venv/bin/activate
    ```

5. Install the required dependencies
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the app script to get to scraper website:
    ```
    python app.py
    ```

2. Enter the URL of the local business page when prompted.

3. Filter for Santa Cruz locations: The scraper will only return contact information for businesses with a mention of "Santa Cruz" on the page. It will filter out any businesses located elsewhere.

# Troubleshooting
## Line Endings Warning
 If you see a warning like:
    ```
    warning: in the working copy of 'venv/Scripts/activate', LF will be replaced by CRLF the next time Git touches it
    ```
This is due to Git automatically handling line endings across different operating systems. You can prevent this by configuring Git:

- For Windows-only development:
    ```
    git config --global core.autocrlf false
    ```
For cross-platform development:
    ```
    git config --global core.autocrlf true
    ```
## Dependencies

The script uses the following dependencies:

- requests: To handle HTTP requests and fetch webpage content.
- beautifulsoup4: For parsing HTML and extracting the contact information.
    
