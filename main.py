import gspread
from oauth2client.service_account import ServiceAccountCredentials
from getpass import getpass

# Connection to sheets
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("base.json", scope)
client = gspread.authorize(creds)
sheet = client.open("logins_base").sheet1
data = sheet.get_all_records()

session = 'offline'


def login_check(login_username, login_password):
    try:
        user = sheet.find(login_username)
        user_row = user.row
        row = sheet.row_values(user_row)
        if login_password == row[2]:
            return "yes"
    except:
        return ("Username and password combination not found.")


while session != "online":
    start = input("Type L to login or R to register: ")
    if start == "R":
        create_username = input("Choose your username: ")
        create_password = getpass("Choose your password: ")
        conf_pass = getpass("Confirm your password: ")
        while conf_pass != create_password:
            create_password = getpass("Password confirmed does not match. Please retype your password: ")
            conf_pass = getpass("Retype it for confirmation: ")
        print("Registration complete, you are now logged in.")
        user_data = [len(data) + 1, create_username, create_password]
        session = 'online'
        sheet.append_row(user_data)
    elif start == "L":
        login_username = input("Username: ")
        login_password = getpass("Password: ")
        check = login_check(login_username, login_password)
        if check == "yes":
            session = "online"
            print("You have successfully logged in.")
        else:
            print("Username and password combination not found.")
    else:
        print("Plese type L to login or R to register: ")
