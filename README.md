# PClub DVWA
Damn Vulnerable Web Application (DVWA) for Programming Club, IITK
## Requirements
Languages Used: Python3, JavaScript, CSS, HTML<br />
Modules/Packages used (for python3):
* os
* json
* pathlib
* hashlib
* mysql.connector
* flask
* colorama
* sys
* requests
<!-- -->
Install the dependencies:
```bash
pip install -r requirements.txt
```
## Setup
In your System's MySQL Server, do the following:
* Make a new user on *localhost*
* Grant user all the permissions for database **pclub_secy_task** on *localhost*
<!-- -->
This can be achieved by running the following commands on MySQL:
```mysql
CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL ON pclub_secy_task.* TO 'user'@'localhost';
```
Then create a file in the Directory of PClub-DVWA called ***db_user.json*** and it should contain the following json data:
```json
{"user":user,"password":password}
```
Then run the ***create_data.py*** to Create the required Databases, Tables, Columns and Values in your System's MySQL Server.<br />
## Flags
* /route.txt
* /static/files/amansg22/ariitk.jpeg
* /static/files/kaptaan/flag.txt
* MAC Address of eth0 Interface
## Vulnerabilities
* Path Traversal in : /getFile
* SQL Injection in : /getBlogDetail
* Command Injection in : /ipDetails
## SQL Database
The Database is *pclub_secy_task*. It has 3 tables:
* USERS
* BLOGS
* HINTS
<!-- -->
In USERS Table, there are 3 columns:
* user: CC ID of the Programming Club Secies from Tenure 2022-23
* userhash: SHA3 512 Hash of Users (to avoid SQL Injection on Login Page)
* password: MD5 Hash of Passwords randomly choosen from *rockyou.txt* 
<!-- -->
In BLOGS Table, there are 4 columns:
* id
* title
* content
* link
<!-- -->
In HINTS Table, there is only 1 column:
* hint
## Procedure
* After opening Gallery, we see that sources of the Images is something like */getFile?file=/home/kaptaan/IIT_Kanpur/Clubs/PClub/Secretary-Recruitment/2023-24/PClub-DVWA/static/images/gallery/{image_index}.jpeg*. This lets us know that it is vulnerable to Path Traversal Vulnerability. So we send a **GET** request */getFile?file=/home/kaptaan/IIT_Kanpur/Clubs/PClub/Secretary-Recruitment/2023-24/PClub-DVWA/routes.txt* and we get the First flag and a hing.
* After opening Blogs, we see that the Title, Content and Link of the Blogs are fetched through */getBlogDetails* endpoint. After running ***sqlmap*** on it, we found that **blog** parameter is vulnerable to ***SQL INJECTION*** vulnerability. After that we dump the Database, we found from the HINTS table that the passwords are weak and uses MD5 Hashing Algorithm, after running rockyou, we find every password.
* On logging in with *kaptaan* user, we find that there is a flag.
* On logging in with *amansg22* user, we find that there is logo of ***Aerial Robotics***. After using ***steghide*** on it, we found a QR Code, after scanning the QR Code we get a **base64 encoded string** and decoding it and doing **ROT13** on it, we get the flag.
* On logging in with *ritvikg22* user, we find the link to netcat server and pwn challenge.
* After getting *routes.txt*, we see an endpoint **/ipDetails**. When we open it, we see a Input Tag asking for an IP Address. After entering a valid IP and hitting search, we get the details of the IP Address. When we type a wrong IP we don't see that data. This is vulnerable to command injection and after seeing the Hint we got from routes.txt, we run the following *; ifconfig* to get the MAC Address of etho Interface. From here we get another Flag and IP Address to the Netcat Challenge.