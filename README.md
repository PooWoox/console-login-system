# login-system
A simple login system created with python and Google Sheets. This is a project I just worked on for putting into practice my knowledge and logics. Below is basically everything about it, a tutorial on how to connect Google Sheets to your projects and my 'plans' for this on the future.

--------------------------------------------------------

ABOUT IT.

The login system is really basic, it runs basically inside a while loop that will only stop when the variable 'session' is equal to 'online'. When started the user has the option to Register or Login. For registering an username will be asked first, no character restrictions at all, then the password is requested, along with a confirmation of the first one typed. No characters restriction for now either.

If the password is not confirmed correctly when asked, the user will be prompted with a message to retype it for the first time and then confirm again. After successfully confirming the user is created and added to the first blank row on this Google Sheets sheet  shorturl.at/suN02 and gets "logged in" as 'session' value is changed to 'online'. Program stops as the process is over.

If the option chosen is to log in, the user will be requested to type the username and password. When inputing both information a function will check if the username can be found on the spreadsheet, if it is found it gets the row number and confirm if the password inputed by the user now is the same password on the same row. If both information provided matches the records on the spreadsheet, 'session' will be changed to 'online' and the user is now "logged in". If the username is not found or the password doesn't match the one registered before, user will be notified of it and the program will restart.

For now this is really basic, I didn't want to dive in making character restrictions for now as I wanted to focus more on the logics behind getting and confirming the login values. At first I was storing the data on the same format as dics on a text file, I then looked for ways to connect to an excel file as I thought it would be more interesting, this way I found how to connect to Google Sheets and decided to go with it.

For connecting to Google Sheets you need this JSON file I uploaded here, it has private keys that of course shouldn't be shared as I did here, don't worry, I created it using a google account just for that.

--------------------------------------------------------

HOW TO CONNECT YOUR OWN GOOGLE SHEETS TO THIS PROJECT OR YOUR OWN PROJECTS.

For connecting, first you need to go to https://console.cloud.google.com. There you should create a new project, name as you wish and save it. Now you will need 2 APIs from cloud console to get to work, search for Google Drive API first and activate it. After activating go to it and click on the button for creating credentials. There you will set the options as follows: 

1st. Google Drive API
2nd. Web server(e.g. node.js, Tomcat)
3rd. Application data
4th. No, I'm not using them

Then name yourself, role I guess could be any but "Project Editor" would fit nicely. On this page you will be fine for downloading the JSON file with your credentials.

The second API is Google Sheets API, find it on the same website and activate it. 

Now run 'pip install gspread oauth2client' on your machine, make sure both gspread and oauth2cliend are added to python before starting. On your code you can import as I did and run the same scope, creds, client and sheet variables as I did.

--------------------------------------------------------

POSSIBLE FUTURE IMPROVEMENTS.

- Password restrictions (minimum, maximum, special characters and other security stuff)
- Username restrictions (min and max characters and fix being able to create usernames that already exists)
- Possibly implementing it to a website using flask for other practice purposes.


    Thanks for reading, I will appreciate tips and other comments on how to improve this or make anything I wrote even more simple.
