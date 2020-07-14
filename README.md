# Institute-Web-Nominee-Assignment

This portal is made for as part of the assignment for the Institute Web Nominee Position.
Flask is used for backend stuff like user login and form submission. Bootstrap is used
for the frontend stuff.

To run this web app, clone this repository and run `python app.py` in the terminal. This app uses the following python libraries:
- Flask
- Flask-Mail
- Pandas
- Datetime
- Passlib  

Now open a browser and go to `http://localhost:5000/`

## Databases
The two files `users.csv` and `userData.csv` are used as databases for this app.
The former contains the registered users's credentials. For now there are two dummy users,
the passowrd stored in the file is hashed. The credentials are as follows:  
- User 1
    - LDAP : 180070032
    - Passowrd: xxxx
- User 2
    - LDAP: 18D070032
    - Password: yyyy
    
The second file `userData.csv` contains the information filled by the user in the
form that he/she fills.

## Usage
First fill in the necessary email credentials at the lines with
comments in `app.py` file to test this app. Then save and run this file.

Use either of these credentials to log in, and then a form will be displayed.
After logging in, the login timestamp will be updated in `users.csv` file.
This will be used to allow a user fill the form once a day. Now fill the form with the necessary information. After submitting this form,
you will be redirected to the login page. The submitted form data is stored/updated
in the `userData.csv` file.   
If the user checks any symptoms, an email will be sent to the concerned authorities.

## Demo Video
Here, I set my email ID as the target email id if any user reports symptoms.  
<!-- blank line -->
<figure class="video_container">
  <iframe src="https://youtu.be/DUmj8yPjxSM" frameborder="0" allowfullscreen="true"> </iframe>
</figure>
<!-- blank line --


 
