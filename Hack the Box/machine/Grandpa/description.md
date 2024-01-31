1.Run Nmap to discover any open ports inside the web server.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/f0cff4f2-4d49-4398-9473-b275243bcc66)

2. Same as the [Granny](https://github.com/LawsonSchwantz/Writeups/tree/main/Hack%20the%20Box/machine/Granny) one which is IIS 6 vulnerability so I use the same payload from this [link](https://github.com/g0rx/iis6-exploit-2017-CVE-2017-7269/blob/master/iis6%20reverse%20shell).
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/9a7dbcef-ace0-4c1c-b6d5-b217d2c81e03)

Attacker Terminal: <br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/efd0e664-7ca3-4e0f-aeb5-52eeb7b35e0a)

3. Same as the Granny case, user directory cannot be access directly.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/d4acbf9d-a22d-48ae-9a44-96f7566c5edb)

4. Again, I use the payloadftp.txt that I've made before and send it to victim terminal through ftp.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/acc900a7-65f0-4f50-a8e7-3d50af179421)

5. Execute the reverse shell payload with churrasco.exe and I got the root privelege.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/e7a730b5-88ea-44c0-8fb1-c449cb8fb3db)

Attacker Terminal:<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/b485c7d0-caa5-45ce-8f65-c8db2cf9e0ba)

6. The user flag is located in Harry/Desktop/user.txt.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/65e45066-65c7-491e-989e-e45eb78ac3d3)

7. The root flag is located in Administrator/Desktop/root.txt.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/e9f9eb58-39a5-4203-b6e9-86ec9f2e0aa3)






