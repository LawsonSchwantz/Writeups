1. Run nmap to discover any open ports.
![image](https://github.com/user-attachments/assets/7e98a8f2-84dd-4741-9ab6-a9e7e78a0b1c)
2. Realize that the server use oscommerce-2.3.4 service, I search for the payload and there is a RCE payload from the searchploit result.
![image](https://github.com/user-attachments/assets/22865d58-38ab-462d-a462-cf9290cc1437)
3. Import the python payload script using **searchsploit -m** command. <br>
![image](https://github.com/user-attachments/assets/24507773-eaf1-473a-b48d-26188c41ea00)
4. Run the payload into the server.
![image](https://github.com/user-attachments/assets/3bea30b3-0c2e-4e05-a56d-81ab99bb1859)
5. The root flag is found in C:\Users\Administrator\Desktop\root.txt.txt file.
![image](https://github.com/user-attachments/assets/1f41c26d-ff11-4672-8a80-0bc3488c6678)
6. For the NTLM, I copy the registry value into a file named SAM, SYSTEM, and SECURITY with reg.exe file. <br> 
![image](https://github.com/user-attachments/assets/aebae00e-5117-4a07-9c1a-1aeeecaa0751)
7. Download the file by opening http://blueprint.thm:8080/oscommerce-2.3.4/catalog/install/includes path on my browser.
![image](https://github.com/user-attachments/assets/60d28a20-fe99-45c6-9be2-554218404d91)
8. Dump the hash by using samdump2 tool.
![image](https://github.com/user-attachments/assets/c22137ea-92a6-476a-a2e3-b1014cf87871)
9. Crack the lab hash using this [tool](https://crackstation.net/) and I successfully obtain the decrypted NTLM lab user hash.
![image](https://github.com/user-attachments/assets/a0248a86-10f2-4b7b-ad16-79cfa87b52d2)
























