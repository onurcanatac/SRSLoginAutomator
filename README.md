# SRS Login Automator
As a personal hobby project, I implemented a webscraper using Python and Selenium. This program automates the SRS (Student Website of Bilkent University) login process.

1. Program opens a new Google Chrome window by a driver, and goes to the SRS login page.
2. Enters users student ID and password and clicks to the login button.
3. Website is programmed to send an email to the user which contains a code (number). The code is required in the new webpage which comes up after login button is pressed.
4. Program opens a new window in Google Chrome and logs into users email using his/her email adress and email password.
5. Finds the last email sent which contains the code in the message.
6. Fetches the message part of the email and parses the code from the email message.
7. Returns to the SRS window and enters the code to the required area.
8. Done!
