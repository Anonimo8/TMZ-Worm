from os import system
from os import popen
from datetime import datetime

def clear():
    return system("cls")

def date_time():
    return datetime.now()

def PyNumVerify():
    system("title PyNumVerify v1.0 by ttomiid")
    system("MODE 70,20")
    api_key_file = open("configs/API_KEY.txt", "r", encoding="utf8")
    api_key = api_key_file.read()
    api_key_file.close()
    num =input("Telephone: ")

    clear()

    numVerifyLog_file = open(f"Results/{num}.log", "w", encoding="utf8")
    numVerifyCMD = f'curl -s "https://apilayer.net/api/validate?access_key={api_key}&number={num}&country_code=&format=1"'
    output_numVerifyCMD = popen(numVerifyCMD).read()
    numVerifyLog_file.write(f"""
    {date_time()}
    {output_numVerifyCMD}
    """)
    
    numVerifyLog_file.close()

    return print(f"""
    {output_numVerifyCMD}
    """)

try:
    PyNumVerify()
    print('\n\n')
    input('Press enter to continue...')
    clear()

except FileNotFoundError as fnfe:
    system("mkdir configs")
    api_key_file = open("configs/API_KEY.txt", "w", encoding="utf8")
    api_key = input("API Key: ")
    api_key_file.write(api_key)
    api_key_file.close()
    system("mkdir Results")
    PyNumVerify()
    input("Press enter to continue...")
except FileExistsError as fee:
    clear()
except KeyboardInterrupt as ki:
    system("cls")
    print("Exiting...")
except Exception as e:
    print(f"An error occurred {e}", type(e))