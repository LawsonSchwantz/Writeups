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
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/15f46a78-2d9b-4779-a2f0-ca312abf2927)

8. Try googling for vulnerability and found this [Link](https://wpscan.com/wordpress/523). Scroll a bit to find this [Vulnerability](https://wpscan.com/vulnerability/3413b879-785f-4c9f-aa8a-5a4a1d5e0ba2) about unauthenticated view private posts (similar to the message). We can execute the payload `office.paper/?static=1`
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/b117ecac-c0f5-49aa-87ab-cb2b2e3f67b4)

9. We found a subdomain inside the message.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/13636bb2-1260-4625-ac33-4ca2d72c7c4c)

10. Again, add the subdomain to /etc/hosts with the corresponding ip address.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/14477553-02ea-4903-b513-eb6df2309bf0)

11. It shows signup page and we must register a new account.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/c65b9c0c-81c4-4f69-a380-219a5752baa1)

12. After registering, we're redirecting to a chat model page where on the left there is a channel named general. The main chat is about that someone has added bot to the server named recyclops.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/d47c1c39-ff12-4f6e-885b-8b462ef772b8)

13. The basic command is `recyclops help`. Let's try it.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/7f98cc53-0971-44fb-bc48-a2fc6444feec)

14. We found that the files and list command are the most interesting one. Let's try send `list ..` to check it (similar to ls .. in linux).
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/d29fccc1-fde9-4757-9060-53ea45331c04)

15. There is a user.txt in there. Try to grab it with file command and it says access denied.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/4f9861a0-dcab-4c32-a268-90ae1cbfbbbe)

16. We need to find another way to open that file. Analyze the `list ..` content and discover a hubot file. Try to find a thing related to hubot and get this [link](https://github.com/RocketChat/hubot-rocketchat). 
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/d7cb6e10-1ce2-44ef-818e-1637ce8fb2ae)

17. It says that the main thing is the .env file, so run `list ../hubot` to see what file inside hubot folder and we found the .env file.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/6c3f07f2-36dc-4c11-a602-98086edbf7c7)

18. To open we run `file ../hubot/.env`.

User = recyclops
Password = Queenofblad3s!23

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/c1da82f0-8b8f-48a8-8d70-6be1ca6ed39c)

19. Login to user recyclops with ssh and it says permission denied.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/f275adf1-a315-401b-a409-5439cb3dd5c9)

20. There must be another user inside. Run `list ../..` to the content of home folder. We found there is a user name Dwight.

User = dwight
Password = Queenofblad3s!23

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/a8306763-8815-4c00-963a-ae0c76b06167)

21. Login to user dwight with ssh and we found the user flag in user.txt.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/78ea0c34-f2d7-4f79-a6b2-29f44ebc3e39)

22. Now we want to find the root flag. So, we run `sudo su` to take a root privilege but unfortunately, Dwight doesn't have the sudo privilege.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/b879fa14-bd7e-45bd-ae04-08e9455795b1)

23. To get the root privilege, we can use linpeas from this [link](https://github.com/carlospolop/PEASS-ng/releases/tag/20220612). We copy `linpeas.sh` file to dwight's terminal using scp (Run chmod 777 before copying it).
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/81b692f5-e89a-4c12-8493-b71902d57be4)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/413967f4-4c85-4ebe-b093-a25704e15dec)

24. Run `linpeas.sh` and discover that the sudo privilege is vulnerable to CVE-2021-3560.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/72532c9e-62e1-492a-9f87-e6d8d40ba4b5)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/72dbd24b-0083-4f6b-81c7-6ab89eb72fb1)

25. Googling that related to CVE-2021-3560 script and found this [payload](https://github.com/secnigma/CVE-2021-3560-Polkit-Privilege-Esclation). Change the username and password parameter as we like.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/70c56500-5f95-4198-9257-e8d9a07f934b)

26. Run `poc.sh` (Before that, run chmod 777 to give the file execute permission for all users).
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/3e6a9ca5-66e1-4081-9bb1-8e49c221300c)

27. Switch to superuser privilege and we successfully get the sudo privilege. Root flag is located in /root/root.txt.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/5532fea6-902c-4096-a31b-e4e4d08eabf5)













