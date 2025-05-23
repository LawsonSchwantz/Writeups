1. Run Nmap to discover any open ports from the server.
![image](https://github.com/user-attachments/assets/a872979f-3de7-4cad-a7ff-78a07d1ca7f9)
2. Open the web, nothing inside it after checking all the features.
![image](https://github.com/user-attachments/assets/4a5d667e-da90-42fb-be05-5624b6e4d28d)
3. Check the services inside port 1311.
![image](https://github.com/user-attachments/assets/3762854a-daa4-4367-a4b7-44eed6cbd92c)
4. Change into https protocol and it shows DELL Open Manage login page.
![image](https://github.com/user-attachments/assets/ba791cdd-d04f-43ce-9e65-1c8ebcf5de33)
5. Check the about page to see the version information.
![image](https://github.com/user-attachments/assets/6b397b87-3ca2-41e8-9917-5891ba6d9983)
6. It shows that the version is vulnerable as CVE-2020-5377. I can use this [script](https://github.com/RhinoSecurityLabs/CVEs/tree/master/CVE-2020-5377_CVE-2021-21514) to exploit.<br>
![image](https://github.com/user-attachments/assets/f32a08bb-4d11-4db2-b4f9-1041cd08128f)
7. Run the script and it successfully opened connection into the target terminal.
![image](https://github.com/user-attachments/assets/b0ce54e0-e183-4b9c-8165-c37ea2117fc3)
8. Check web.config file for any interesting information. It shows credentials data for user Tyler. <br>
**Location: C:\inetpub\wwwroot\hacksmartersec\web.config** <br>
![image](https://github.com/user-attachments/assets/020a223a-e69a-4dd1-80cf-92df64e4e169)
9. Log in using ssh with the provided credentials.
![image](https://github.com/user-attachments/assets/28293909-1512-4a82-81d6-a2f4e0ba48d3)
10. The user flag is found in C:\Users\Tyler\Desktop\user.txt.
![image](https://github.com/user-attachments/assets/71035249-538b-4a86-aa72-79e3522d8753)
11. Import privesccheck powershell script to check any vulnerability that can leads to privilege escalation from the server.
![image](https://github.com/user-attachments/assets/54bbe27c-28be-491f-989a-b166fd92114e)
![image](https://github.com/user-attachments/assets/77594fad-14ad-4e89-a825-c778d21d2164)
12. Run the script with command below. <br>
**Command: . .\priv.ps1; Invoke-PrivescCheck -Extended** <br>
![image](https://github.com/user-attachments/assets/daf6e285-bb73-48c0-9238-b005577d41a2)
13. It shows that one of the service is vulnerable where the severity is high.
![image](https://github.com/user-attachments/assets/4cd23fdb-ccc4-45f0-b8f8-543ec5c9a0e4)
14. I can stop the spoofer-scheduler service and change it with my own exploit.
![image](https://github.com/user-attachments/assets/b635b44f-514e-4a3d-a379-99589f15a3c9)
15. I use this [script](https://github.com/Sn1r/Nim-Reverse-Shell?source=post_page-----96f3cd45a7c5---------------------------------------) to insert reverse shell payload inside the modified spoofer-scheduler service later on. <br>
![image](https://github.com/user-attachments/assets/566aeba0-da30-4423-ba9a-eddcaa6e5998)
16. insert reverse shell payload inside my modified spoofer-scheduler service by using nim with command below and send it to the target machine. <br>
**Command: nim c -d:mingw --app:gui -o:spoofer-scheduler.exe rev_shell.nim** <br>
![image](https://github.com/user-attachments/assets/8644faea-dabf-405c-88e0-2582b3ceff90)
![image](https://github.com/user-attachments/assets/5fc68808-3440-473c-a6d5-49300a81d07b)
17. Start the modified spoofer-scheduler service and set the listener in my host machine.
![image](https://github.com/user-attachments/assets/de4fce3f-a1e1-4780-aa13-e18426c9dc60)
![image](https://github.com/user-attachments/assets/20780bbe-734a-4703-8982-e1148f82443c)
18. Succesfully get the admin privilege, the hacking targets is stored in C:\Users\Administrator\Hacking-Targets\hacking-targets.txt.
![image](https://github.com/user-attachments/assets/85a04c57-1e24-48c0-a607-093286247313)


















