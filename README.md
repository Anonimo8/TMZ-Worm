
---

# PyNumVerify v1.0  

[NumVerify API](https://numverify.com/)

**A Phone Number Validation Tool Using API Layer**  

PyNumVerify is a Python tool that allows users to validate phone numbers via the API Layer service. It provides a simple interface for sending requests, viewing responses, and saving logs of validations.  

---

## Features  
- Validates phone numbers using the [API Layer](https://apilayer.com/) service.  
- Automatically saves the validation logs in a `Results` folder for future reference.  
- Handles API keys securely via a configuration file (`configs/API_KEY.txt`).  
- Custom terminal title and dimensions for better usability.  

---

## Requirements  
- **Operating System**: Windows (uses `cls` for clearing the console).  
- **Python**: Version 3.x or higher.  
- **Curl**: Installed and available in the system path.  

---

## Setup and Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/ttomiid/PyNumVerify.git
   cd PyNumVerify
   ```  

2. Install `curl` if it is not already available on your system.  
3. Run the script:  
   ```bash
   python3 PyNumVerify.py
   ```  

---

## Usage  

1. When you first run the script, it will prompt you to input your API key. The key will be securely stored in `configs/API_KEY.txt`.  
2. Input the phone number you wish to validate.  
3. The validation result will be displayed on the terminal and saved as a log file in the `Results` folder.  

---

## Folder Structure  
- **`configs/`**: Contains the `API_KEY.txt` file where your API key is stored.  
- **`Results/`**: Stores log files for each phone number validation, named after the validated phone number.  

---

## Example Output  
### Terminal:  
```plaintext
Telephone: +1234567890  

{
    "valid": true,
    "number": "+1234567890",
    "local_format": "1234567890",
    "international_format": "+1234567890",
    "country_prefix": "+1",
    "country_code": "US",
    "country_name": "United States",
    "location": "New York",
    "carrier": "Verizon",
    "line_type": "mobile"
}
```  

### Log File (`Results/+1234567890.log`):  
```plaintext
2025-01-12 10:00:00.123456  

{
    "valid": true,
    "number": "+1234567890",
    "local_format": "1234567890",
    "international_format": "+1234567890",
    "country_prefix": "+1",
    "country_code": "US",
    "country_name": "United States",
    "location": "New York",
    "carrier": "Verizon",
    "line_type": "mobile"
}
```  

---

## Notes  
- Ensure your API key is valid and has sufficient permissions for phone number validation.  
- This tool is designed for **Windows** systems due to the use of `cls` for clearing the console.  
- If any required directories or files are missing, the script will create them automatically.  

---

## License  
PyNumVerify is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for more details.

--- 
