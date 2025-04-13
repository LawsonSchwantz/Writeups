1. Run nmap to discover any open ports from the server.
![image](https://github.com/user-attachments/assets/64351b3d-7628-4b06-a658-571e56f61068)
2. Only port 22 and 80 are opened, so I tried to open the website.
![image](https://github.com/user-attachments/assets/2743b081-b136-4919-bb74-830de83f3d16)
3. It only consists of a short message, next I enumerate the website with gobuster.
![image](https://github.com/user-attachments/assets/41222b5a-daf6-4d26-8685-dc703fa46beb)
4. It shows /r inside the path and when I opened the page it shows the message to keep going.
![image](https://github.com/user-attachments/assets/ef6e4eb3-a326-4849-b66d-f5c09a4c6c33)
5. So I enumerate the website again but this time with /r path.
![image](https://github.com/user-attachments/assets/9d0645ef-b700-46cc-b720-5c09de2eec08)
6. It results /a path and when I opened the website it shows the same message. So I keep enumerate the website until it results /r/a/b/b/i/t path. <br>
![image](https://github.com/user-attachments/assets/9384dca9-9be3-43a2-ba27-550b56fd9d31)
7. It shows a picture a girl opens curtain to see things inside room. The next step is checking the source code of the website and it shows credential data for user Alice. <br>
![image](https://github.com/user-attachments/assets/9fd3bd16-3a38-471f-886a-c6f38f67353f)
8. I decided to login from server SSH with the provided credential. Inside the home page, there is a root.txt file but it says permission denied when I tried to open it. <br>
![image](https://github.com/user-attachments/assets/8c1c34d9-f36c-4b98-a381-e1b91cf65f37)
9. From here, I thought that the user.txt is stored in root directory. Moving into the root directory and open the user flag that stored in /root/user.txt file. <br>
![image](https://github.com/user-attachments/assets/cf69f714-c08e-455b-bb67-389e9fd4a8be)
10. For the root privilege, it's quite complicated. First, I check the sudo privilege and it shows that I must run a python file that stored in the Alice home directory. <br>
![image](https://github.com/user-attachments/assets/37693268-e376-4090-8b26-263e1f74ba6d)
11. I checked the python script which consists of code that print list of poem in random. 
![image](https://github.com/user-attachments/assets/2c85bd10-a277-4a61-9779-38e4093c8c99)
12. Checking the /etc/passwd file, I realize that there are 3 users inside this machine (alice, rabbit, hatter).
![image](https://github.com/user-attachments/assets/b88124a9-fef0-4722-bef1-ec7077c58a77)
13. Realizing that the python script use random as their library, I make a custom random.py script which call shell from the machine. <br>
```py
import os
os.system('/bin/bash')
```
I run the script where I want to use rabbit account. <br>
**Command: sudo -u rabbit /usr/bin/python3.6 /home/alice/walrus_and_the_carpenter.py** <br>
![image](https://github.com/user-attachments/assets/e1f30af3-afc0-4b5f-ab7e-cfdf734cd127) <br>
14. Successfully get the rabbit account, inside the home page, there is a elf file named teaParty. <br>
![image](https://github.com/user-attachments/assets/183b348f-d6b9-4b02-8603-adbe89651c35)  <br>
15. Checking the elf file, I moved the file into my local machine with the help of python. <br>
![image](https://github.com/user-attachments/assets/f44b0354-38a6-493f-9466-6fdc96a575e3)
![image](https://github.com/user-attachments/assets/e2f62228-5a2b-41fb-a346-d927ca3838ab)
16. Strings the elf file and it shows that the vuln is located in date variable where application execute any command form date file.
![image](https://github.com/user-attachments/assets/dcf2eb71-361b-4652-876c-b0d88e0eae2d) <br>
17. Here I made a new file of date consist of bash command to open hatter shell. Next is add the rabbit home page into the path configuration. <br>
![image](https://github.com/user-attachments/assets/3af9e9c6-120e-4c8a-b01a-5e34bc708164) <br>
18. Finally run the teaParty file. <br>
![image](https://github.com/user-attachments/assets/5d0d8d0f-e9d5-4a78-86db-f7abe5869161) <br>
19. Successfully obtain the hatter shell, check the home page and found a password.txt file which is the hatter user password. <br>
![image](https://github.com/user-attachments/assets/f5183939-836d-48d1-aeaa-5d037eeb5509) <br>
20. Open a new terminal and login as user hatter with ssh. Then, I inserted the linpeas.sh into the machine to check any vuln inside this machine to escalate my privilege. <br>
![image](https://github.com/user-attachments/assets/efdc0637-32ec-4577-a19b-4aebda55675d)
21. It shows that the server perl is vuln with the capabillities. <br>
![image](https://github.com/user-attachments/assets/c2bcbdf3-713d-407d-8165-93baeb2bf1da) <br>
22. Read from this [link](https://gtfobins.github.io/gtfobins/perl/), I can escalate the privilege by following the command from the link. <br>
![image](https://github.com/user-attachments/assets/67c61132-ef73-4664-93f8-b34b5d52a196)
23. Search the perl inside the server and execute the command from the link above. <br>
![image](https://github.com/user-attachments/assets/a1d6b0ce-df47-4c76-a279-2bfafe4c1be3) <br>
24. Successfully get the root privilege, I can obtain the root flag in /home/alice/root.txt file. <br>
![image](https://github.com/user-attachments/assets/c5ca3c59-340b-42ad-a461-30e5cd801a4a)















