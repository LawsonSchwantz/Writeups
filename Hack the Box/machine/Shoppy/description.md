1. Run nmap to discover any open ports and services from the web server.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/8a09e7fe-58ff-4b91-84bc-7cf16d2bac51)

2. Try to open the ip address in web browser and it directs to shoppy.htb.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/1146f2c1-249d-476f-b22d-21a1c0e12662)

3. We need to add shoppy.htb to /etc/hosts with the corresponding IP and the website looks like this.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/45558ca9-0933-4803-b18a-d39d102c2e90)

Website:<br>
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/b4b29ca1-aaed-45b9-8aa2-f64f38697181)

4. It says that there is a shoppey beta that will release in 53 days. We guess that ther is a subdomain in the IP address. To check it, we run `wfuzz -u http://10.10.11.180 -H "Host: FUZZ.shoppy.htb" -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt`
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/ccfbe1a1-fadb-45d8-8483-a035acb08f05)

5. The average response are 169 character only, to filter, we can add --hh 169 which means ignore any word with the character length of 169 and run `wfuzz -u http://10.10.11.180 -H "Host: FUZZ.shoppy.htb" -w /usr/share/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt --hh 169` (the top5000.txt doesn't give any result)
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/0dc5ba0e-ed48-4395-b5d2-b9cac4870890)

6. From wfuzz we get one match named **mattermost**. The website looks like this.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/bf329604-4dec-4759-ad4d-51ba643d0025)
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/c0731c8b-8c41-41ac-8d23-3204bff460e0)

7. Because it's start from login page, we have to find any interesting things in the main website (shoppy.htb) with feroxbuster. We found 2 admin endpoints which caught our attention.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/d703c74e-1216-472f-821f-b5d4852f4a93)

8. When we opened, it redirects to login page. 
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/300a1e16-d683-4f9c-b6bd-887a8f507664)

9. First thought is SQL Injection so let's try this payload `username=admin' OR 1=1 -- &password=aaa`
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/9b86f97c-6251-45fd-9190-4071933bcaa6)

10. It returns error 504. Try all SQL Injection payload and it doesn't work. Next idea is NoSQL Injection with this payload `username[$ne]=admin&password[$ne]=aaa` but still not work. Try one by one NoSQL Injection payload and finally, one payload is working `username=admin' || '1'=='1&password=aaa`. We're redirecting to admin page after that.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/757aea75-d340-42b4-9665-7d16f81c8311)

Admin Dashboard:
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/688b73fd-7de8-47e6-920b-7caddb68c52f)

11. Next one is check the search feature. It exports the user's id, username, and password in MD5 that we searched.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/b3a12ae8-eec1-42ab-ba0f-c5c507db8821)
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/6b8075ef-4ee5-4d23-8d61-0cdc670e2fea)

12. Still related to NoSQL Injection, we try this payload `admin' || '1'=='1` to get all data from database. 
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/e24d084b-fda5-43b1-8091-794f90f08269)

13. We get user John and his MD5 password hash and decrack it with this [tool](https://crackstation.net/).

Data: <br>
user: josh <br>
password: remembermethisway

![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/1132f869-15c0-427e-b899-f5f76e202646)

14. Back to mattermost subdomain and do login with user Josh. We see a chat page.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/f6de7238-7ee5-4dd1-9a5b-a6649e20041b)

15. Analyze the channel and discover an important message about account disclosure.

Data: <br>
user: Jaeger <br>
password: Sh0ppyBest@pp!

![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/1d7ab60d-fa80-4c97-a11b-d91dd2c49021)

16. Do login to user jaeger with ssh and found the user flag in user.txt.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/5e18aeaf-c3a4-47eb-affd-5f1a0d221cd9)

17. It's not over, we still analyze another channel to find another useful information. The results are there are two chats that discuss about docker and deploy a password manager.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/122e453d-c7cb-46ec-ad5d-c9b36d630e76)
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/bd04bf81-a033-4fe2-a964-ed60434def93)

19. Check sudo permission that Jaeger has.<br>
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/06e85719-0aa3-49b2-a6b1-eb228425786d)

20. Right, that's what Josh said. We can run `sudo -u deploy /home/deploy/password-manager` to execute the file. Try to input Jaeger password and it's says Access Denied!
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/a8cab13b-fc0b-45a7-88e6-99558c7a0f6a)

21. We can use scp for copy the file to our terminal.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/1be878c3-1bb6-4f25-97e7-215bffd93da6)

22. Check the file type with `file` and it's ELF 64 Bit.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/a6c00f97-c239-4b97-b0db-7d084f711105)

23. We're decompiling the file using IDA and found the password in the main function.

Master Password: Sample<br>

![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/81e9b4b3-9a48-42aa-9a64-a7b112e1ea7f)

23. Run again the password-manager and input the passowrd. Thus, we get new user's creds.

Data: <br>
username: deploy<br>
password: Deploying@pp!

![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/d7af1b82-e134-43fc-bb4a-0c8ecc7b0f09)

24. Login the deploy user with ssh. Related to the information before, Josh using docker for his deployment so we check any attributes related to docker (container & images).<br>
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/fec78cdd-bdfb-4570-b56a-be4e471b7103)

25. Found 1 image name alpine and we can copy the root directory content from deploy terminal to alpine using command `docker run -it -v /root:/root alpine`. The root flag can be find in /root/root.txt.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/c8e0dc7c-7d80-49f9-9c50-dad687db7b9e)













