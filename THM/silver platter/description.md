1. Run nmap to discover any open ports from the server.
![image](https://github.com/user-attachments/assets/5527e1b1-c834-43a7-9f09-2fd18442ed0f)
2. It shows that port 22,80, and 8080 are opened, let's open the port 80 first. It shows a page that has four main menu. My main focus is at the contact menu where consists of user information and the service which is in Silverpeas. <br>
![image](https://github.com/user-attachments/assets/12d405b0-e363-420b-bf2b-f7f2567d3620)
3. Try to open port 8080 and it shows not found error message. 
![image](https://github.com/user-attachments/assets/4b8de31e-4b09-4a79-a99e-b69bb236dd09)
4. Next thing is I enumerate the website with gobuster.
![image](https://github.com/user-attachments/assets/7f94dd5d-85f8-4688-b0e1-7d2c13f9027d)
5. Nothing interesting found between the two path where it returns forbidden error message. Then I realize that the service is located in Silverpeas. The next thing is I tried to open /silverpeas path inside the website and it shows a Silverpeas login page. <br>
![image](https://github.com/user-attachments/assets/2fc6fb84-e6fd-4540-a525-e86f631bf976)
6. Trying to bypass the authentication and I found this [vuln](https://github.com/advisories/GHSA-4w54-wwc9-x62c) that related to Silverpeas. It basically remove the password parameter inside the login request so server only process the username. <br>
Before: <br>
![image](https://github.com/user-attachments/assets/cb33ec22-8a4a-47b4-9c23-8f3a4ff12b8d)
After: <br>
![image](https://github.com/user-attachments/assets/3aea1478-0a6d-4b28-938d-e1fe0755204a)
7. Successfully login, it shows Silverpeas service in French language.
![image](https://github.com/user-attachments/assets/6e281035-1d03-4d9f-829e-7eba5d959faa)
8. I check the service one by one but found nothing. Finding another CVE or vuln related to Silverpeas service and I found this [vuln](https://github.com/RhinoSecurityLabs/CVEs/tree/master/CVE-2023-47323?source=post_page-----71008786f53e---------------------------------------) which able to see all secret messages from the Silverpeas mail service. <br>
![image](https://github.com/user-attachments/assets/d21eefff-9243-44f8-9fd4-ec15d5fe0464)
9. Similar to IDOR vuln, I changed the ID value and found an user credential data in ID 6.
![image](https://github.com/user-attachments/assets/50cac439-06f0-4a26-8af9-348ca01dadb9)
10. Login with the ssh protocol as the port 22 is opened with the provided credential.
![image](https://github.com/user-attachments/assets/d5ee951a-76dc-498b-b055-126117917a71)
11. The user flag is found in user.txt file. <br>
![image](https://github.com/user-attachments/assets/191cfd2a-6169-4384-8927-b78d4dfbbd67)
12. For root privilege, I check the user id group and it shows that the user is in admin group.
![image](https://github.com/user-attachments/assets/d8fc9fd8-352d-4b7b-9f4f-3d8991eacd4c)
13. With this privilege, I able to check the log that related to the authentication inside this machine. It results that user tyler has access root privilege from the log. Inside the log there is the username and password information related to user tyler. <br>
<b> Command: cat /var/log/auth* | grep -i root <br> </b>
![image](https://github.com/user-attachments/assets/aa36b753-75c3-4114-979e-d16c5b944c99)
14. Next I use the tyler user with the password that I get in the previous step and check the root privilege.
![image](https://github.com/user-attachments/assets/53d78a61-16df-4d35-b639-de426ed8ca29)
15. With user tyler I can escalate my privilege with any command so I use sudo su to change the user into root privilege. The root flag is found in /root/root.txt file. <br>
![image](https://github.com/user-attachments/assets/b69a1028-1407-4b9d-99c6-96ef8748a048)















