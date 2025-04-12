1. Run nmap to discover any open ports from the server.
![image](https://github.com/user-attachments/assets/27289e85-bcff-445f-8c4e-a73723b63d18)
2. Only port 80 and 3389 (RDP) are opened, next I enumerate the server and found /retro path inside the server.
![image](https://github.com/user-attachments/assets/fe899add-f5c9-49e6-8fa4-ea6c907c11a7)
3. Open the retro page and it shows several blogs inside the page.
![image](https://github.com/user-attachments/assets/9e26e015-149e-44c4-a9f1-cbe19a79c10e)
4. There is a login feature inside the website. <br>
![image](https://github.com/user-attachments/assets/be1769de-502e-4147-abdb-30830c575b24)
5. I analyze the blogs where they are written by a user name Wade.
![image](https://github.com/user-attachments/assets/cc98bc63-9e57-46ec-aa85-2a1fc89a78cf)
6. It found that the user is comment in one of the blog which is the password of the user.
![image](https://github.com/user-attachments/assets/64b9159e-3358-4fa4-9055-dd250c73b2e7)
7. I directly login into the website and it shows wordpress page.
![image](https://github.com/user-attachments/assets/78ae446d-c1b5-4122-b44b-a4400a5f9c11)
8. Analyze each feature and no vulnerability is found inside. Realize that the server has RDP service, I tried to login into the RDP service with the provided credential. <br>
![image](https://github.com/user-attachments/assets/db14c285-6488-4389-8a86-4634f59140bd)
9. Successfully login into the RDP, the user flag can be found in user.txt from the user desktop.
![image](https://github.com/user-attachments/assets/530bf031-620f-42a9-b836-48d411a0bc90)
10. For the admin privilege, I check first the system configuration that use in the server.
![image](https://github.com/user-attachments/assets/4979111f-8dc3-4fde-ac50-9cedf46221f4)
11. Searching for privilege escalation vulnerability from the server OS version, I discover this [script](https://github.com/WindowsExploits/Exploits/tree/master/CVE-2017-0213) and used it inside the target Windows machine. <br>
![image](https://github.com/user-attachments/assets/130c50fa-36df-4198-9f03-ebda3922a6a6)
![image](https://github.com/user-attachments/assets/77fa4ce5-e276-4cd4-bc7f-49c82e9b9396)
12. Execute the script and the system will open a new terminal with admin privilege.
![image](https://github.com/user-attachments/assets/63c0b5c7-035e-4319-8e90-1641187d905c)
13. The root flag is stored in C:\Users\Administrator\Desktop\root.txt.
![image](https://github.com/user-attachments/assets/8ed9bf08-be7f-4af4-a853-448b689198ab)



















































