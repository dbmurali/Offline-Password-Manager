# Password Manager

A simple and secure Password Manager built with Python and Tkinter. This application allows you to generate, store, retrieve, and copy passwords for various websites or accounts. The application saves your credentials (website, email, and password) in a local JSON file, ensuring that your data is easily accessible but also securely stored.

## Features:

### 1. **Password Generation**:
   - Generate a random password with the click of a button.
   - The generated password can be copied to the clipboard for convenience.
   
### 2. **Save Passwords**:
   - Enter a website, email, and generated password, and store the information in a local JSON file.
   - The app ensures that the entered details are saved in a structured format, making it easy to manage passwords for multiple sites.

### 3. **Search for Stored Passwords**:
   - You can search for saved credentials by entering the website name or user ID.
   - The application will fetch the associated email and password, displaying them in a popup message.

### 4. **Copy Password to Clipboard**:
   - After generating or retrieving a password, you can copy it to your clipboard with a button click, making it easy to paste it elsewhere (like logging into a website).

### 5. **Screenshots**:
 #### 1. **Application Interface**:
   ![Application Interface](https://github.com/dbmurali/Offline-Password-Manager/blob/28b66d3712f17f1b713c413d384aecba5ae13dbe/Application%20Interface.png)

 #### 2. **Password Generation**:
   ![Password Generation](https://github.com/dbmurali/Offline-Password-Manager/blob/28b66d3712f17f1b713c413d384aecba5ae13dbe/Password%20generation.png)

 #### 3. **Search Functionality**:
   ![Search Functionality](https://github.com/dbmurali/Offline-Password-Manager/blob/28b66d3712f17f1b713c413d384aecba5ae13dbe/Search%20Functionality.png)

 #### 4. **Error Message**:
   ![Error Message](https://github.com/dbmurali/Offline-Password-Manager/blob/28b66d3712f17f1b713c413d384aecba5ae13dbe/Error%20screen.png)

## How It Works:

1. **Password Generation**: 
   - The app uses a random password generator function to create strong and secure passwords.
   
2. **Saving Passwords**:
   - When you add a new password, the app saves it in a JSON file (`data_file.json`). If the file does not exist, it is created automatically.
   
3. **Searching and Displaying Passwords**:
   - When searching for a password, the app looks for the website name in the saved JSON data and retrieves the associated email and password. If the website name is not found, an error message is displayed.

4. **Clipboard Functionality**:
   - You can copy the generated password to your clipboard, so you don't need to manually type it out.

## Requirements:
- Python 3.x
- `pyperclip` for copying to clipboard
- Tkinter (pre-installed with Python)

