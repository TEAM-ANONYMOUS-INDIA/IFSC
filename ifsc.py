import requests
import re
from colorama import Fore, Style, init

# Initialize colorama for colored text
init(autoreset=True)

def validate_ifsc(ifsc):
    """Validates IFSC format"""
    return bool(re.match(r"^[A-Z]{4}0[A-Z0-9]{6}$", ifsc))

def fetch_ifsc_details(ifsc):
    """Fetches IFSC details from an API"""
    if not validate_ifsc(ifsc):
        return Fore.RED + "❌ Invalid IFSC code format! Please enter a valid 11-character IFSC code."

    api_url = f"https://ifsc.razorpay.com/{ifsc}"
    
    try:
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return f"""
{"-"*40}
🔍 IFSC Code: {data.get('IFSC')}
🏦 Bank: {data.get('BANK')}
📍 Branch: {data.get('BRANCH')}
📌 Address: {data.get('ADDRESS')}
🏛 City: {data.get('CITY')}
🏙 State: {data.get('STATE')}
📞 Contact Number: {data.get('CONTACT', 'Not Available')}
🔢 MICR Code: {data.get('MICR', 'Not Available')}
🏦 Bank Code: {data.get('BANKCODE')}
🏧 RTGS Supported: {"✅ Yes" if data.get('RTGS') else "❌ No"}
💳 NEFT Supported: {"✅ Yes" if data.get('NEFT') else "❌ No"}
📲 IMPS Supported: {"✅ Yes" if data.get('IMPS') else "❌ No"}
🏦 UPI Enabled: {"✅ Yes" if data.get('UPI') else "❌ No"}
{"-"*40}
"""
        elif response.status_code == 404:
            return Fore.RED + "❌ IFSC code not found! Please check and try again."
        else:
            return Fore.YELLOW + "⚠️ Unexpected error occurred. Try again later!"
    except requests.exceptions.Timeout:
        return Fore.RED + "⏳ API request timed out! Please try again later."
    except requests.exceptions.ConnectionError:
        return Fore.RED + "❌ No internet connection! Please check your network."
    except Exception as e:
        return Fore.RED + f"⚠️ Error: {str(e)}"

if __name__ == "__main__":
    print(Fore.CYAN + "-"*40)
    print(Fore.GREEN + "🔍 IFSC Code Checker - TEAM ANONYMOUS INDIA")
    print(Fore.CYAN + "-"*40)

    ifsc_code = input(Fore.YELLOW + "Enter IFSC Code: ").upper().strip()
    print(fetch_ifsc_details(ifsc_code))

    print(Fore.MAGENTA + "\n© TEAM ANONYMOUS INDIA")