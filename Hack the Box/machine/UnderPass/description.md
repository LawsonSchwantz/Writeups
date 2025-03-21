1. Run nmap to discover any open TCP ports from the server.
![image](https://github.com/user-attachments/assets/408c476e-4aae-4bb5-a5c6-b5120a6e0f3d)
2. Run nmap to check any open UDP ports from the server. In this case, port 161 inside the server opened.
![image](https://github.com/user-attachments/assets/846c3b20-7250-4008-b121-3da3988175ca)
3. Because port 161 opened, I can check the snmp configuration for any information. 
![image](https://github.com/user-attachments/assets/66723d0f-b0ed-4b03-917a-e9796e3923d6)
4. Add the IP address to /etc/hosts as underpass.htb, it shows that only dalorarius server is allowed to logged in. Now, I enumerate the server.
![image](https://github.com/user-attachments/assets/0f4efc05-b65e-405f-b2e4-1622f7f68fb5)
5. Continue bruteforce the app directory.
![image](https://github.com/user-attachments/assets/1286c1ff-322a-4d59-871b-a68dee095436)
6. There are login pages in /users/ and /operators/ directory.
![image](https://github.com/user-attachments/assets/48765762-e21e-42a0-9a30-bb1bf5108921)
7. Now I want to find any credentials information, so I enumerate doc/ directory and found INSTALL file.
![image](https://github.com/user-attachments/assets/2a74a5b4-dea8-49d4-afa2-1bb1464be55f)
![image](https://github.com/user-attachments/assets/47ebd5a8-532d-4e43-bcdb-820d0c587301)
8. Inside the file, there is a credentials information within the operators login page.
![image](https://github.com/user-attachments/assets/3fe7fea6-fb67-4f6d-ba2a-aa827eea19db)
9. Logged in into the operators page with the provided credentials.
![image](https://github.com/user-attachments/assets/34fe46ea-929b-4476-b39b-def5aedfa82b)
10. There is 1 user inside and consist of MD5 password hash and the username.
![image](https://github.com/user-attachments/assets/0f0141f1-8bd8-48b8-8152-9444397a6612)
11. Crack it with Crackstation and obtain the user's plain password.
**User: svcMosh
Pass: underwaterfriends**
![image](https://github.com/user-attachments/assets/d6c83c16-3a75-4485-bd8e-54d781610b08)
12. Log in using SSH protocol and the user flag is found in user.txt.
![image](https://github.com/user-attachments/assets/a406d693-4fcb-4ba8-861f-9ce4d07c928b)
13. Now I upload linpeas.sh inside the target machine and it shows that there is a executable program in /usr/bin/mosh-server.
![image](https://github.com/user-attachments/assets/95e84464-9951-4cf6-aa53-82d33feeeaac)
14. So I tried to run mosh and it shows below.
![image](https://github.com/user-attachments/assets/c2d42834-fdf0-42f1-b751-24ae3d84ab85)
15. From the help information, it shows that I can use sudo privilege with server parameter as shown below.
**Command: mosh --server="sudo /usr/bin/mosh-server" localhost**
![image](https://github.com/user-attachments/assets/ce8a9f99-9340-44f8-8c74-0882597457a1)
16. Successfully get the root privilege, the root flag is stored in root.txt. <br>
![image](https://github.com/user-attachments/assets/dd090ba0-9186-4107-8de5-ab481d3001b3)




































