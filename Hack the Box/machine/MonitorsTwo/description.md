1. Run nmap to discover any open ports and services from the web server.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/c899fefd-379f-4c16-8202-4f31dfc836ea)

2. Open the IP address in browser and shows cacti website.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/14d48b0b-6529-472e-b1ef-392b75093669)

3. Googling for vulnerability and found this [link](https://www.exploit-db.com/exploits/51166).
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/51eb0207-cfb7-4533-973c-7f2d4e00528c)

4. First I'm trying to use the payload from exploitdb but it didn't work. So I use this [payload](https://github.com/FredBrave/CVE-2022-46169-CACTI-1.2.22/blob/main/CVE-2022-46169.py) and it works!
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/827fb9ab-34ad-4cf0-a0b1-8da42c03a03b)

Shell:
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/fbaa2fb2-65ed-4bec-9b18-02e4a92d72ba)

5. Searching for any information and I found that I'm inside the docker. Next let's check the entrypoint.sh file.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/7e6370bd-1c3c-466c-82fe-5b05d38563b4)

6. It shows that something inserted to cacti.sql. I checked it and discover admin's password in md5 hash.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/da8ad103-a5e1-4e20-b075-4190b609593e)

7. Crack it using this [tool](https://crackstation.net/) and the password is also admin.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/d85de5e5-f864-4db9-98fa-ff97dceed205)

8. Unfortunately, it didn't work.<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/24e79eeb-4bcf-4a03-84c3-fdeaf102889f)

9. I run `find / -perm /4000 2>/dev/null` to search any feature that I can use from the terminal. <br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/76c58328-0b8d-488a-8a1c-a95bbea53a74)

10. There is capsh feature. I can use it to get the root privilege with this command `capsh --gid=0 --uid=0 --`.<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/2d64785b-ea13-40a4-b1f1-4ce9856cacb6)

11. Now I can access the mysql feature. I run `mysql -h db -u root -proot cacti -e 'show tables;'` to look the tables inside cacti database.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/e9d0853c-06fe-4615-9d57-d7bed8b59698)

12. The interesting one is user_auth table. To see the value I run `mysql -h db -u root -proot cacti -e 'SELECT * FROM user_auth'` and found a new user named marcus.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/e5be6a2c-b74a-4e4b-8802-6db3923fdd4c)

13. The password hash can be crack using johntheripper and found the password is **funkymonkey**.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/9ec874de-0323-4fcd-8186-fce4b9e70003)

14. Login to marcus account using ssh and the user flag can be found in user.txt.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/a6bb8979-6ff1-44fb-8b0f-fd30d010ca39)

15. Checking one by one directories and found a message inside marcus's mail. It says that there are three CVEs inside the terminal.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/c97784a5-b727-410c-b57c-81a39087479b)

16. Check the docker version and googling all the three CVEs from the mail. After doing some research, the [CVE-2021-41091](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41091) is the most related thing to docker.<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/0353c967-93bc-42ec-ac12-6cb8f9c7186d)

17. I use the payload from this [link](https://github.com/UncleJ4ck/CVE-2021-41091) and copy it to target terminal using python.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/276ad086-ec4c-47f1-a354-2f45f37890c0)

Target:
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/a686a758-91ac-40bd-8ec5-56d46347fdee)

18. Run the payload and the output shows that there is vulnerable path in there.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/fb8c60a3-0246-474e-93e0-d9f6db45d43a)

19. Check all the file permission and it says root. To give the user and group permission, I run `chmod u+s bash` in the first terminal that I reverse shell before.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/6d68437a-27e1-477e-84ef-29df907bce32)

Target:
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/bb502e8e-9259-4481-a493-d1e520785366)

20. Run `./bash -p` and finally I get the root privilege. The root flag can be found in /root/root.txt.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/66a254e6-1f10-4fb5-a2f0-633d39efa519)































