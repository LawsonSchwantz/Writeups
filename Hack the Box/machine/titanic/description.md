1. Run nmap to discover any open ports from the server.
![image](https://github.com/user-attachments/assets/f72b7e3c-e24c-471f-9d02-8fa3c9f09cb5)
2. In book now feature, I can add information such as name, email, phone number, travel date, and cabin type.
![image](https://github.com/user-attachments/assets/6d349333-6c9c-4d90-bd9b-338b1754b8f4)
3. Submitting the data and the server will download a json file into our devices.
![image](https://github.com/user-attachments/assets/7dbdb2b1-be09-42ff-a8af-f61d747cd38c)
4. From here, there is LFI vulnerability.
![image](https://github.com/user-attachments/assets/9457fbf0-6ba3-42c8-bbc6-33ff27047321)
5. Inside the /etc/hosts file, there is subdomain name dev.titanic.htb.
![image](https://github.com/user-attachments/assets/53992a20-54ba-4544-90ee-8d389372115e)
6. Add it into our terminal /etc/hosts and it shows Gitea page.
![image](https://github.com/user-attachments/assets/a1a123a2-7bd4-4296-b5c2-034e79a856c1)
7. Register a new account inside the server, examine "explore" menu, there are 2 repositories inside.
![image](https://github.com/user-attachments/assets/1da682df-2b60-46cf-bc22-06bc7bb8e18d)
8. Inside the docker-config repository, there is a docker-compose.yml which contains information about where the Gitea file is stored.
![image](https://github.com/user-attachments/assets/dda1cb32-52e4-4b8e-8ffc-4114ca6011a9)
9. The other file contains information about database configuration.
![image](https://github.com/user-attachments/assets/97c0c6ce-bbbf-4359-b34b-5de3e5833b09)
10. Because it contains database, the next one is finding the Gitea database file named gitea.db inside the server. From the previous step, I know that the file is stored in /home/developer/gitea folder. <br>
**Command: curl -s "http://titanic.htb/download?ticket=/home/developer/gitea/data/gitea/gitea.db" -o gitea.db**
![image](https://github.com/user-attachments/assets/04d8a68f-7ba9-4877-974c-d9f95c0e2f7c)
11. Access the gitea.db using sqlite3.<br>
![image](https://github.com/user-attachments/assets/3f19662a-5abd-44b8-9a28-8905f8791bea)
12. Check user table and it shows gitea hash and the salt inside each user credentials.
![image](https://github.com/user-attachments/assets/461ed8f3-1a85-466a-9753-c4c4a011e6a6)
13. Now, I must bruteforce the hash to obtain the password. First, I use (this script)[https://github.com/unix-ninja/hashcat/blob/master/tools/gitea2hashcat.py] to change the hash into hashcat readable format.
![image](https://github.com/user-attachments/assets/08aba89f-caf2-4cc8-8c07-37359834f8af)
14. Insert the developer's hashcat result into a txt file.
![image](https://github.com/user-attachments/assets/44b8defd-9568-4241-b0b1-52fd8578cbd5)
15. Crack it using hashcat and I found the plain password.
**Pass Developer Account: 25282528**
![image](https://github.com/user-attachments/assets/34d21f2d-c436-4332-b9ee-38e2add7fff8)
16. Log in using developer account and the user flag is stored inside user.txt file.
![image](https://github.com/user-attachments/assets/eddbd5b6-fcf5-4261-9b7e-9ba829365cd7)
17. For the root, first I run linpeas.sh but results nothing. Next, I check the opt directory and found one script named identify_images.sh
![image](https://github.com/user-attachments/assets/baa04430-f13d-415a-b9ef-cfff22c4a850)
18. From this code, it runs any codes inside images folder. In this case, I make a script to move the root.txt file from root folder to tmp folder.
![image](https://github.com/user-attachments/assets/75eb6c75-8fb0-4a71-b60f-b99f705963fa)
19. Open the root.txt in tmp directory and it shows the root flag.
![image](https://github.com/user-attachments/assets/b45d28a6-819a-4fd2-a585-6d5151f11e7d)











