1. Run nmap to discover any open ports from the server.
![image](https://github.com/user-attachments/assets/5268d333-1815-431a-8198-a2ac9b48fe00)
2. Inside the application, it shows a feature to check file metadata.
![image](https://github.com/user-attachments/assets/025da50f-a168-407e-ba8e-6c7aa6ba6310)
3. Nothing can be exploited from this feature, next one is enumerate the application.
![image](https://github.com/user-attachments/assets/829a0edf-c296-44c8-9a03-2722cdc9c455)
4. There is JS folder inside and as I opened it, there is a script named image-extractor.js that consist of port information that use from the server (6177).
![image](https://github.com/user-attachments/assets/eee564a7-b564-406a-b48a-a26add1023b9)
5. Inside the port 6177, there are several endpoints that can be access from the server. One of them is /meta.
![image](https://github.com/user-attachments/assets/a06fdb59-be45-434e-b42e-ec3cb37b56ee)
6. Using metasploit to search payload to abuse tika 1.17 server vulnerability.
![image](https://github.com/user-attachments/assets/f11d206f-83d7-4b60-8af7-28c0ec870940)
7. Execute the payload to obtain machine shell.<br>
![image](https://github.com/user-attachments/assets/79ef16e7-b37f-48aa-9870-4cc9be8d0af6)
8. The user flag is found in C:\Users\CyberLens\Desktop\user.txt.
![image](https://github.com/user-attachments/assets/2bac3c8a-773e-4dd1-a596-9f7f34dce4be)
9. For the admin flag, first I change the registry query configuration to always install application with elevated permission
![image](https://github.com/user-attachments/assets/6a9d3462-3f33-437f-bdb4-e7d1c6fe90f9)
10. Make a reverse shell payload and send it into target machine with python.
![image](https://github.com/user-attachments/assets/fb220438-4cdc-4391-afc2-09d8f1edb87c)
![image](https://github.com/user-attachments/assets/05ce8a43-3b8b-4b61-b877-d4ff8c553ae7)
11. Execute the reverse shell file with msiexec and set listener in our hosts machine.<br>
**Command: msiexec /quiet /qn /i C:\\root\\reverse.msi**
![image](https://github.com/user-attachments/assets/2f5ba0b3-912a-4ced-b616-029de2abd76a)
![image](https://github.com/user-attachments/assets/4d73e2fe-5440-4f4a-a813-498925f6e531)
12. The Admin flag is found in C:\Users\Administrator\Desktop\admin.txt.
![image](https://github.com/user-attachments/assets/a755a89d-b0db-4004-8e94-420b99feb916)




