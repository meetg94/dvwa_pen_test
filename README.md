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

2. #### Determining the Number of Columns
Next, we determined the number of columns in the original SQL query. We used the ORDER BY clause and incremented the number until we got an error. We found that the original SQL query has 2 columns.

3. #### Extracting Database Information
We then used the UNION SELECT statement to extract information about the database structure. We retrieved a list of all tables in the database and then a list of all columns in the users and guestbook tables.

##### Commands Used:
```
1' UNION SELECT table_name,2 FROM information_schema.tables #
1' UNION SELECT column_name,2 FROM information_schema.columns WHERE table_name = 'guestbook' #
1' UNION SELECT column_name,2 FROM information_schema.columns WHERE table_name = 'users' #
```