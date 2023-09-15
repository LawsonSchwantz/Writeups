1. Run nmap to discover some open ports and services from the web server.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/06bc8094-0cfc-4865-a091-f5194dd4eb66)

2. Try to open the ip address in the browser and it shows only http default page.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/0e09f15b-da32-42cb-b8e4-52d29dc52d81)

3. Using burp suite to find any interesting information and we found the backend server with named `office.paper`.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/2490612e-5c7a-4b7a-a07e-9b08ab4a38fc)

4. To open it, we add this server to /etc/hosts with the corresponding ip address.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/995aa100-5bb2-4f7b-bf2b-fb8e288b16dc)

5. The web server looks like this
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/4d8efffd-5ea7-4a46-afa3-c7a46ae5e9d8)

6. I check the uppermost post and it says that there is a secret content that Michael needs to look at.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/b3b50d4d-6b68-4bcd-a832-ea82652ea6ff)

7. This indicates that the website using wordpress to running their services. Next, we can check the wordpress version using Wappalyzer and it shows that it uses WordPress 5.2.3.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/2f44097b-ccbe-424b-8157-9158d4467724)

8. Try googling for vulnerability and found this [Link](https://wpscan.com/wordpress/523). Scroll a bit to find this [Vulnerability](https://wpscan.com/vulnerability/3413b879-785f-4c9f-aa8a-5a4a1d5e0ba2) about unauthenticated view private posts (similar to the message). We can execute the payload `office.paper/?static=1`
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/1a30c8ea-78af-49cb-9786-160acc1ecb71)

9. We found a subdomain inside the message.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/853783e7-71a7-4a82-a2f6-d20f89bc6577)

10. Again, add the subdomain to /etc/hosts with the corresponding ip address.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/b5844e34-391e-42fc-b920-66ac21613c82)

11. It shows signup page and we must register a new account.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/c07c4801-e775-4503-9903-3c67787411a9)

12. After registering, we're redirecting to a chat model page where on the left there is a channel named general. The main chat is about that someone has added bot to the server named recyclops.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/c818a24e-b1fd-47cf-83c8-4ceb2f008ecd)

13. The basic command is `recyclops help`. Let's try it.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/99c1241b-1177-4199-b7b7-4c7dea17492a)

14. We found that the files and list command are the most interesting one. Let's try send `list ..` to check it (similar to ls .. in linux).
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/89436769-7799-4a5e-831f-1cc00e1349d1)

15. There is a user.txt in there. Try to grab it with file command and it says access denied.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/611f3bc8-879e-4c29-9c56-3924a5748692)

16. We need to find another way to open that file. Analyze the `list ..` content and discover a hubot file. Try to find a thing related to hubot and get this [link](https://github.com/RocketChat/hubot-rocketchat). 
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/7d77ee90-1fc7-43a0-9bee-ae6fd42c113b)

17. It says that the main thing is the .env file, so run `list ../hubot` to see what file inside hubot folder and we found the .env file.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/0544926c-91f4-4ebf-8805-9ae3f76d7416)

18. To open we run `file ../hubot/.env`.

User = recyclops
Password = Queenofblad3s!23

![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/a84015c9-27f1-4231-ae33-eb58ea2acb89)

19. Login to user recyclops with ssh and it says permission denied.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/ec3e670c-1217-4748-9f19-beec08b98821)

20. There must be another user inside. Run `list ../..` to the content of home folder. We found there is a user name Dwight.

User = dwight
Password = Queenofblad3s!23

![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/53e0747d-3b2d-471c-87ab-ca4d7b382f42)

21. Login to user dwight with ssh and we found the user flag in user.txt.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/2058f834-dfa0-425d-96db-de3a6077037d)

22. Now we want to find the root flag. So, we run `sudo su` to take a root privilege but unfortunately, Dwight doesn't have the sudo privilege.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/1a4fd081-237e-460a-9908-c6d4827b5d0d)

23. To get the root privilege, we can use linpeas from this [link](https://github.com/carlospolop/PEASS-ng/releases/tag/20220612). We copy `linpeas.sh` file to dwight's terminal using scp (Run chmod 777 before copying it).
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/9d51702a-36bb-4afa-86f9-a9bd933723f9)
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/659eca2c-7503-494e-9e4e-08dd9cb054ba)

24. Run `linpeas.sh` and discover that the sudo privilege is vulnerable to CVE-2021-3560.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/37ddade9-8ee2-4680-aac8-e1429b8f42c0)
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/e2ca7cbe-a7ef-44b2-b45e-d7e6e3245f02)

25. Googling that related to CVE-2021-3560 script and found this [payload](https://github.com/secnigma/CVE-2021-3560-Polkit-Privilege-Esclation). Change the username and password parameter as we like.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/2de78b53-bacd-4b64-80f0-6fc73f6ba01d)

26. Run `poc.sh` (Before that, run chmod 777 to give the file execute permission for all users).
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/8879b1df-9357-482d-aa9a-c61903465df1)

27. Switch to superuser privilege and we successfully get the sudo privilege. Root flag is located in /root/root.txt.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/f7a4d921-2cfd-46ef-bc02-eb80608c0d0f)












