1. Run nmap to discover any open ports from the server target.
![image](https://github.com/user-attachments/assets/f90abc9f-bf3f-450c-a918-00389b8a00f6)
![image](https://github.com/user-attachments/assets/3d80583d-64f8-4823-9af6-d09fa11f6ee4)
2. Given from the description for the initial credential: **rose / KxEPkKe6R8su**.
3. Because port 445 is open, I tried to use the provided credential into server SMB service and it works.
![image](https://github.com/user-attachments/assets/a829b55f-3682-4276-b6ec-24b2fa1e2347)
4. Logs in as rose with smbclient and check the shares inside the account.
![image](https://github.com/user-attachments/assets/9c27146a-0807-403b-9000-f80095be2370)
5. There are 2 files inside the "Account Department" share and download it into my VM.
![image](https://github.com/user-attachments/assets/b1b4cab3-353e-4e13-8d71-7b45fcf88cff)
6. Inside the account.xlsx file specifically in ShareStrings.xml.
![image](https://github.com/user-attachments/assets/f6c041ff-1887-47f2-92df-d39d46805060)
7. From the XML file, there is a superadmin SQL user with the password and logs in using "impacket-mssqlcleint".
**User: sa
Pass: MSSQLP@ssw0rd!** <br>
![image](https://github.com/user-attachments/assets/6d358fca-d7b0-4857-95ac-697060e91449)
8. Now I want to run cmd command inside the SQL server. To do that, I must enable first the xp_cmdshell command. 
![image](https://github.com/user-attachments/assets/f07213d5-091d-4fec-9447-ae42ad300b75)
9. After enabling the command, generate reverse shell payload which is in Powershell language with help of base64 encoding.
![image](https://github.com/user-attachments/assets/759b1f0f-2513-4259-9276-c7bd83ab4d62)
10. Insert the reverse shell payload inside the machine with xp_cmdshell command and set listener from my  VM.
![image](https://github.com/user-attachments/assets/d3db0093-052e-430c-b340-44922ac48da9)
![image](https://github.com/user-attachments/assets/b6902c35-dddf-4985-809d-588f50982c68)
11. Check the directory inside the target machine for any interesting files and found "sql-Configuration.INI" file.
![image](https://github.com/user-attachments/assets/34186a61-6449-4426-9ca3-938b925a3694)
12. Open the file and it contains several information such as credentials data.
![image](https://github.com/user-attachments/assets/c05842be-e4e7-4b9f-a705-84fedbfc579f)
13. From the file, I found one password ("WqSZAF6CysDQbGb3") and I check user lists that are used inside the machine.
![image](https://github.com/user-attachments/assets/05bb3d74-b6ba-4234-8727-a18bbdf03d73)
14. Bruteforce the user lists with the known password to find any users that has the known password.
![image](https://github.com/user-attachments/assets/db9e5416-a772-4ec7-a459-95d937931505)
15. From the result, it shows that ryan has the known password. Logs in to the evil-rm server and the user flag is found in user.txt.
![image](https://github.com/user-attachments/assets/6477e286-4610-433b-926d-84c163f148ad)
16. Because it's Active Directory (AD), I run sharphound.exe to check any relation between each user inside the server.
![image](https://github.com/user-attachments/assets/2a0e4061-54cd-47fa-909f-eea17715fdc7)
17. Import it to BloodHound and it shows that there is "WriteOwner" relationship between user ryan and ca_svc.
![image](https://github.com/user-attachments/assets/0784e75a-e3aa-47a0-87cc-0a8db0eb65bb)
![image](https://github.com/user-attachments/assets/ef9b551c-2a66-4bb3-b5ad-05433137a1ec)
18. Bloodhound gives information that Shadow Password Attack can be done inside the machine.
![image](https://github.com/user-attachments/assets/168845a3-6574-4ed3-a269-d5f7c17419d4)
19. Before executing the attack, I must change the ryan user permission so I can access the ca_svc user privilege.
![image](https://github.com/user-attachments/assets/c425a46e-3ca6-4c79-bd8f-467c968bdb7b)
![image](https://github.com/user-attachments/assets/2031f72c-addb-4c13-a6ba-152165d1369b)
20. I user certipy.ad to obtain the ca_svc NT Hash as the picture below.
![image](https://github.com/user-attachments/assets/731b3cf8-de45-4bd6-b8c7-08147ffa86be)
21. Using the NT hash, I'm able to check any vulnerability inside the machine. It shows that the vulnerability located in ESC4. <br>
**Command: certipy-ad find -u ca_svc@sequel.htb -hashes 3b181b914e7a9d5508ea1e20bc2b7fce -stdout -vulnerable -dc-ip 10.10.11.5**
![image](https://github.com/user-attachments/assets/e45bc444-bfc7-4575-941a-788278fb4534)
22. Using the vulnerability, I'm able to use the 'DunderMuffinAuthentication' template and obtain the administrator certificate.
![image](https://github.com/user-attachments/assets/9382011b-a148-4836-b8e9-1591a21b1640)
![image](https://github.com/user-attachments/assets/ff77a274-da25-46bf-ab8a-8f712465ead9)
23. Authenticate using pfx file into the target domain and I'm obtain the administrator NTLM Hash.
![image](https://github.com/user-attachments/assets/c8bed7cb-2cee-40f7-b796-315d3ef9d60a)
24. With the NTLM Hash, logs in as the Administrator using evil-rm and the flag is stored in root.txt
![image](https://github.com/user-attachments/assets/1234343f-c6a3-4cbf-91fb-547d5c33cb13)

























































































