1. Run nmap to discover any open ports and services from the web server.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/40d73772-c5bc-4f4d-929b-998e34ba0622)

2. Try to open the ip address in web browser and it directs to shoppy.htb.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/10e94db5-91b3-4d1c-b3a0-125e4f384cca)

3. I need to add shoppy.htb to /etc/hosts with the corresponding IP and the website looks like this.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/34d77028-c8f6-40cf-823e-e4992c0a8240)

Website:<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/57626ee2-0749-4c5d-a271-41e8398af1ab)

4. It says that there is a shoppey beta that will release in 53 days. I guess that ther is a subdomain in the IP address. To check it, I run `wfuzz -u http://10.10.11.180 -H "Host: FUZZ.shoppy.htb" -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt`
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/e7f43f5f-aea0-42dd-a4b6-288d0af20999)

5. The average response are 169 character only, to filter, I can add --hh 169 which means ignore any word with the character length of 169 and run `wfuzz -u http://10.10.11.180 -H "Host: FUZZ.shoppy.htb" -w /usr/share/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt --hh 169` (the top5000.txt doesn't give any result)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/e507529e-c4c3-4448-a77a-dc1ea25210d0)

6. From wfuzz I get one match named **mattermost**. The website looks like this.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/7f939765-e3fa-46b4-89d6-73d51bee288b)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/8e292a95-313b-46ad-a391-7bec0c3ef5b8)

7. Because it's start from login page, I have to find any interesting things in the main website (shoppy.htb) with feroxbuster. I found 2 admin endpoints which caught our attention.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/cd8cab5f-752f-46d6-a4f0-8d3330b4a1ba)

8. When I opened, it redirects to login page. 
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/14f52f2c-d748-446c-beb7-6d2795b6f213)

9. First thought is SQL Injection so let's try this payload `username=admin' OR 1=1 -- &password=aaa`
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/f4a7c690-f863-4013-a905-318d833101cf)

10. It returns error 504. Try all SQL Injection payload and it doesn't work. Next idea is NoSQL Injection with this payload `username[$ne]=admin&password[$ne]=aaa` but still not work. Try one by one NoSQL Injection payload and finally, one payload is working `username=admin' || '1'=='1&password=aaa`. I're redirecting to admin page after that.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/66bb38c7-b403-4aca-ac55-53b88c0f1867)

Admin Dashboard:
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/cd15260d-4171-4f90-8b88-4933fd0254ff)

11. Next one is check the search feature. It exports the user's id, username, and password in MD5 that I searched.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/df1fbc85-020e-46c6-90fc-3c383701ae0a)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/8b875f06-f447-45f7-a8b0-87226f5438f7)

12. Still related to NoSQL Injection, I try this payload `admin' || '1'=='1` to get all data from database. 
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/cd09f001-092d-433a-bee4-75e1b3245271)

13. I get user John and his MD5 password hash and decrack it with this [tool](https://crackstation.net/).

Data: <br>
user: josh <br>
password: remembermethisway

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/4d702db9-dc13-4378-a55e-972d191b3f24)

14. Back to mattermost subdomain and do login with user Josh. I see a chat page.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/62f67dcd-7724-4fee-a452-e225b3c035e3)

15. Analyze the channel and discover an important message about account disclosure.

Data: <br>
user: Jaeger <br>
password: Sh0ppyBest@pp!

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/b1f9cc3e-f40d-4bcd-b610-7a5aa5313681)

16. Do login to user jaeger with ssh and found the user flag in user.txt.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/4ce8603e-aabf-45d6-ab52-ba0720936d06)

17. It's not over, I still analyze another channel to find another useful information. The results are there are two chats that discuss about docker and deploy a password manager.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/0cda35a2-79ac-4f97-b7d8-ef2cc8cc947a)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/f97f2ebd-9f02-4ec3-916d-edfee709e221)

18. Check sudo permission that Jaeger has.<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/d5b119f6-fa3f-4d15-997f-d09603e46266)

19. Right, that's what Josh said. I can run `sudo -u deploy /home/deploy/password-manager` to execute the file. Try to input Jaeger password and it's says Access Denied!<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/4be9630d-d203-49fe-9247-d7fb04329859)

20. I can use scp for copy the file to our terminal.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/88579041-3748-44c7-873b-b6eeab1229cf)

21. Check the file type with `file` and it's ELF 64 Bit.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/c86b12df-c694-4d67-a763-23d7fdf43f35)

22. I're decompiling the file using IDA and found the password in the main function.

Master Password: Sample<br>

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/86811ea3-60c2-4d24-b65f-5114bc8c1d13)

23. Run again the password-manager and input the passowrd. Thus, I get new user's creds.

Data: <br>
username: deploy<br>
password: Deploying@pp!

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/98075ce2-d462-46b4-87b0-e1b20484cf5a)

24. Login the deploy user with ssh. Related to the information before, Josh using docker for his deployment so I check any attributes related to docker (container & images).<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/3578e3b9-969c-4eb2-8cab-bb1191c1a4c8)

25. Found 1 image name alpine and I can copy the root directory content from deploy terminal to alpine using command `docker run -it -v /root:/root alpine`. The root flag can be find in /root/root.txt.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/44e3b93e-1072-497c-85d2-8a4fe39bfc4a)













