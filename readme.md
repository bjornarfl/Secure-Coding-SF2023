# Secure Coding Practice
 A sample web application containing vulnerabilities from OWASP Top 10. All information in this repository is entirely fictional.
 During Sikkerhetsfestivalen 2023, the application can be accessed here: scat-sf23.eu-west-1.elasticbeanstalk.com (at least until someone eventually breaks it.)

## The Case:
 Bikes as a Service* (BaaS) is a startup that offers easy-to-use bike rental across Oslo. Your task is to review the security of their Web Portal. Using your knowledge of OWASP Top 10, can you find any vulnerabilities?

 *BaaS as a concept for a fictional organization was originally created by Adam Shostack, to teach people how to perform threat modelling. I have repurposed this concept and scenario for this practical assignment.

 ## Missions:
  ### Elevation of Privilege (Easy):
   1. Find a way to change the username of another user (Hint: A01 Broken Access Control)
   2. Using the trick from task 1, can you find any users of particular interest?
   3. Log in on the account you found in task 2 (Hint: A07 Identification and Authentication Failures)
   4. You got access! But now what? Can you find anything new you have access to?
   5. Give yourself a free lifetime subscription to the bike rental service

 ### Harder Challenges
  1. Find a way to force the application into an error-state
  2. Use the credit card of another user to pay for your subscription (without admin privileges)
  3. Give the profile page some background music
     
## The Web Portal
 The Web Portal allows users to:
 - Create and update their profiles, including contact information, payment information, and their subscription to the bike rental service,
 - See a history of past bike rentals, and search for specific previous bike rentals.

 The application is built using Python and the web application framework «Django». Django handles functionality such as authentication and session management out of the box.

 ### Important files:
 - **BaaS/models.py** – Defines the database tables using Djangos object relational mapping (ORM)
 - **BaaS/urls.py** – Handles the routing of requests
 - **BaaS/views.py** – Handles the business logic of each request and renders responses using html from the templates folder
 - **BaaS/forms.py** – Handles validation of user input
 - **ebdjango/settings.py** – Defines the Django configuration for the web server

## How to run the application locally
 For readability, the repository has been stripped of several files that are not relevant for the practical assignment, such as static files or migration files. These files are however needed to actually run the application.
 If you want to run the application locally, you can download the securecoding.zip folder. It contains all necessary files, including further instructions on how to run the application.
