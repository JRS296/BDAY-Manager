# BDAY-Manager
BDAY Manager - GDSC Technical Round 3 
Name: - Jonathan Rufus Samuel
Roll: 20BCT0332
Course: CSE with Specialization in IOT (batch of '24)

Q: Task 2 - Write a birthday manager program. The program must read from a csv file of stored friends’ details, and send them an email with a personalised message. It should also have the functionality to add and delete friends’ details to the csv. [Use a database for plus points]


# Features Successfully Implemented: 
1) Mail System - Works In accordance to given requirements, searches through database (which contains data from CSV file) for birthdays that happen to be on the specific day that the program is run. To demonstrate, an entry (key #11) with the name 'Dummy' is used. This entry has a birthday on the 7th of February. And so, the mail system sends a Mail as required. This can be further demonstrated by the manual Database editing feature, hence we can add another name with it's birthday as required, to see the working of the mail system. This mail system works on the SMTP protocol, and the module smtplib is used for the same.

2) Database Display: As mentioned before, the given csv file 'test.csv' is loaded into the inbuilt database management system SQLite3. This is then displayed in the menu as option #2, and shows the complete database at that instance.

3) Editing of given Database: Three sub-options have been made available: Addition of a friend, Deletion of a Friend (Ouch) and Editing of details of a Friend. Unfortunately, only the Addition feature works as required. The issue has been identified and added into the issues section of GitHub. Can be fixed with a bit of guidance on how SQL is to be used under python.

4) Updation of CSV file from DB and Download: The instance of Database is saved into the working CSV file directory (here test.csv). This is also made available in the downloads section of the PC, with the name of the file user-defined.


# Acknowledgements
Would like to thank the GDSC Recruitment team for this opportunity, had a lot of fun working on this project, and managed to learn few things along the way. Cheers!

Jonathan Rufus Samuel 
(20BCT0332)
