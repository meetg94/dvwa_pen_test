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
