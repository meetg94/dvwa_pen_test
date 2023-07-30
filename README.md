# DVWA: Penetration Testing

## Introduction

This project involves setting up a vulnerable web application for 
penetration testing practice. The Damn Vulnerable Web Application (DVWA) 
hosted on a Metasploitable 2 virtual machine is used.

## Setup Procedure

### Virtual Environment Setup

1. #### VirtualBox Installation: Downloaded and installed VirtualBox, a 
powerful x86 and AMD64/Intel64 virtualization product for enterprise as 
well as home use.

2. #### Metasploitable 2 VM Setup: Downloaded the Metasploitable 2 VM, 
which is an intentionally vulnerable Linux virtual machine. Imported the 
Metasploitable 2 VM into VirtualBox.

3. #### Verify Network Connection: Verified the network connection of the 
Metasploitable VM by pinging a public IP address (8.8.8.8).

### Accessing DVWA

1. #### Find Metasploitable IP Address: Found the IP address of the 
Metasploitable VM by running the ifconfig command in the Metasploitable 
terminal.

2. #### Access DVWA: Accessed DVWA by navigating to 
http://<metasploitable-ip-address>/dvwa on a web browser on the host 
machine.


## Penetration Testing

### SQL Injection
SQL Injection is a code injection technique that attackers can use to exploit vulnerabilities in a web application's database query. In this project, we've used SQL Injection to extract data from the DVWA's database.

1. #### Identifying the Vulnerability
We started by testing for a SQL Injection vulnerability. We entered a single quote (') into the User ID field and observed the application's response. The application returned a SQL error message, indicating that it is vulnerable to SQL Injection.

![SQL Injection Screenshot](https://user-images.githubusercontent.com/86708110/256084274-161ec019-8b2f-4ff0-bde8-88d521019003.png)

2. #### Determining the Number of Columns
Next, we determined the number of columns in the original SQL query. We used the ORDER BY clause and incremented the number until we got an error. We found that the original SQL query has 2 columns.

![SQL Injection Screenshot](https://user-images.githubusercontent.com/86708110/256084282-1d965870-994e-4bf3-af82-18e44b7f1b87.png)

3. #### Extracting Database Information
We then used the UNION SELECT statement to extract information about the database structure. We retrieved a list of all tables in the database and then a list of all columns in the users and guestbook tables.

##### Commands Used:
```
1' UNION SELECT table_name,2 FROM information_schema.tables #
1' UNION SELECT column_name,2 FROM information_schema.columns WHERE table_name = 'guestbook' #
1' UNION SELECT column_name,2 FROM information_schema.columns WHERE table_name = 'users' #
```

![SQL Injection Screenshot](https://user-images.githubusercontent.com/86708110/256084300-bfb77880-04a3-4005-ab35-fc073d1fde9d.png)

##### Session Cookies:
Session cookies are critical for maintaining a user's state during navigation across a website. They are used to keep users logged in, track their activities, and deliver personalized content. However, if not handled securely, session cookies can be exploited by attackers to impersonate users and gain unauthorized access to their accounts.

In this project, we used a session cookie to maintain our session with the DVWA. The session cookie, specifically the PHPSESSID, was required to perform the Blind SQL Injection attack. We extracted the PHPSESSID from our browser's developer tools and included it in our Python script to send authenticated requests to the DVWA.

##### Extracting PHPSESSID:
1. Open the DVWA in your browser.
2. Open the developer tools (F12 in most browsers).
3. Navigate to the 'Application' or 'Storage' tab.
4. Under 'Cookies', select the DVWA URL.
5. Find the PHPSESSID and copy its value.

##### Extracting Hashed Password:

We used a blind SQL Injection technique to extract the hashed password of the 'admin' user. We iterated over each character of the password, and for each character, we iterated over a list of possible characters. We used a SQL query to check if the character at the current position matches the current character from the list. If the application's response indicated a match, we added the character to the final password.

We created a python script (sqppwdinject.py) to automate the process.

![SQL Injection password script](https://user-images.githubusercontent.com/86708110/257036338-7478179c-c16b-4c5f-a100-d7b731fce31b.png)

4. #### Python Script
We created a Python script to automate the process of extracting the hashed password. The script sends GET requests to the DVWA server with the SQL Injection payloads and analyzes the responses to check for matches, and constructs the final password. The script uses the requests library for sending GET requests and handling the HTTP responses.
