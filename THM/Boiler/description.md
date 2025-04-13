1. Run nmap to discover any open ports from the server.
![image](https://github.com/user-attachments/assets/5e954bb0-6034-4dea-a2e9-867c84523db7)
2. From the nmap results, I can answer this two question.
![image](https://github.com/user-attachments/assets/68cf5d6c-1925-4815-8e15-91800416f059)
3. Login into the ftp service with anonymous user and found a file named .info.txt. The file extension is .txt.
![image](https://github.com/user-attachments/assets/7a69ff1f-0911-414e-8775-d772a72116a6)
4. Realize the port 80 is opened, I enumerate the website and found joomla path.
![image](https://github.com/user-attachments/assets/8a54afff-6d49-4626-8624-d4e5cbe09280)
5. Open the joomla page and it shows a room information.
![image](https://github.com/user-attachments/assets/848dfec0-2890-493e-8dba-6a9beb1939b6)
6. Nothing interesting from the page, next I enumerate again the website but with joomla path.
![image](https://github.com/user-attachments/assets/3a81a641-4d74-49d5-9573-cf0ff7f1af53)
7. Found 2 interesting path which is _files and _test. First I open the _files page and found base64 encoded string.
![image](https://github.com/user-attachments/assets/5728debd-871c-4424-9278-3eb710a1611a)
8. Trying to decode and the information that I obtain isn't helping for solving this case.
![image](https://github.com/user-attachments/assets/d9c03c2a-ff86-4750-a86d-ab482fce9bbd)
9. Next one is checking the _test path and it shows sar2html service page.
![image](https://github.com/user-attachments/assets/da17e72f-dd99-4afc-89de-0ec74da32aef)
10. Try each of the feature and I change the OS value into LINUX and it shows a new GET parameter named plot. The vuln is located in plot parameter where I can execute command injection from the paramater. <br>
![image](https://github.com/user-attachments/assets/77c6645c-a734-4a63-afdb-fadc8c2946ea)
11. I execute ls -la command and found interesting file named log.txt.
![image](https://github.com/user-attachments/assets/fed9423d-c213-4207-8326-35ff86b3ce72)
12. I check the log and it shows credentials data for user basterd.
![image](https://github.com/user-attachments/assets/28ef6d0e-0b5c-40cd-bc88-36d784e49667)
13. Login with the ssh located on port 55007. Check the home directory and found a file named backup.sh. <br>
![image](https://github.com/user-attachments/assets/d88c930d-2912-44cc-b151-aa82344083dd)
14. Check the content and it shows another credential for user Stoner.
![image](https://github.com/user-attachments/assets/c8f1fec3-de80-4016-b80f-cbe9b4353a43)
15. Login into the ssh on port 55007 with user Stoner and the user flag is found in .secret file.
![image](https://github.com/user-attachments/assets/ad3ee626-ca4f-4418-a4a0-ccdec76f3a39)
16. For the root privilege, I check with sudo -l first and it shows trolling message. <br>
![image](https://github.com/user-attachments/assets/86df2d86-f58c-4925-8cda-8e0329232a12)
17. So I check the setuid permission with this command below. <br>
**Command: find / -perm -u=s 2>/dev/null** <br>
![image](https://github.com/user-attachments/assets/a2760c5d-138b-47ed-a923-b13199939aa1)
18. It shows that the find command can be use to escalete into root. I run this command to escalate my privilege. <br>
**Command: /usr/bin/find . -exec /bin/bash -p \; -quit** <br>
![image](https://github.com/user-attachments/assets/e21e1da7-a195-4151-bf7a-06f90906da36)
19. Successfully obtain the root privilege, the root flag is found in /root/root.txt file. <br>
![image](https://github.com/user-attachments/assets/03fddd68-2c23-4171-b075-f2aed746bdaa)












