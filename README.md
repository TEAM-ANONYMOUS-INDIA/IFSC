# 🔍 IFSC Code Checker - TEAM ANONYMOUS INDIA

## 📌 Description
This is a simple **IFSC Code Checker** script that fetches bank details using the **Razorpay IFSC API**. It validates the IFSC code format and retrieves information such as bank name, branch, address, MICR code, and supported payment methods (RTGS, NEFT, IMPS, UPI).

## 🚀 Features
- ✅ **Validates IFSC Code Format**
- ✅ **Fetches Bank Details**
- ✅ **Checks RTGS, NEFT, IMPS & UPI Support**
- ✅ **Handles API Errors Gracefully**
- ✅ **Stylish & Colored CLI Output**
- ✅ **Fast & Lightweight**

## 📌 Installation
Ensure you have **Python 3.x** installed and install the required dependency:

```sh
pip install requests colorama
```
🎯 Usage
```
https://github.com/TEAM-ANONYMOUS-INDIA/IFSC
cd IFSC
python3 ifsc.py
```

Enter a valid 11-character IFSC code, and the script will display detailed information.

🔹 Example Output
```

🔍 IFSC Code: HDFC0001234
🏦 Bank: HDFC BANK
📍 Branch: MG ROAD
📌 Address: 123, MG ROAD, MUMBAI, MAHARASHTRA
🏛 City: MUMBAI
🏙 State: MAHARASHTRA
📞 Contact Number: 022-12345678
🔢 MICR Code: 400240003
🏦 Bank Code: HDFC
🏧 RTGS Supported: ✅ Yes
💳 NEFT Supported: ✅ Yes
📲 IMPS Supported: ✅ Yes
🏦 UPI Enabled: ❌ No
```
----------------------------------------

⚠️ Error Handling

Invalid IFSC Format: ❌ Displays an error message.

IFSC Code Not Found: ❌ Returns an error if the code does not exist.

API Timeout or No Internet: ⏳ Handles timeouts and network issues.


📜 License

© TEAM ANONYMOUS INDIA
This script is developed for educational and ethical purposes only.

✨ Contributors

TEAM ANONYMOUS INDIA
