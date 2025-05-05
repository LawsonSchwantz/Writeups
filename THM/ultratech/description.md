1. Run nmap to discover any open ports from the server.
![image](https://github.com/user-attachments/assets/ccca0931-282f-4442-8a4c-4034723837fc)
2. There are 2 open http ports from the nmap result. Next I enumerate the 8081 port server first to discover any interesting path.
![image](https://github.com/user-attachments/assets/d6174b2b-80d6-40b4-aca0-8bc3edf4de58)
3. Found auth path, when I opened the page, it shows only the error message to specify login and password.
![image](https://github.com/user-attachments/assets/b3f287b9-b34c-44c3-8324-37caa219334e)
4. I opened the 31331 port server and it shows a website page.
![image](https://github.com/user-attachments/assets/ab3929ab-8725-446a-9cc2-9f21d7c563ac)
5. I enumerate the 31331 port server with dirsearch and found that there is robots.txt file inside the server.
![image](https://github.com/user-attachments/assets/99e289c7-c014-41e1-827a-54dacd51fb31)
6. Open the robots.txt file in the browser and found sitemap file path.
![image](https://github.com/user-attachments/assets/3aef73e6-b453-4242-8eb7-867949e43b44)
7. Inside the sitemap file, I found 3 different html file which is index, what, and partner.
![image](https://github.com/user-attachments/assets/cf6215d9-2972-4d7b-b216-35a1b866fea1)
8. Open each of the file and the content can be see from the picture below. <br>
what.html: <br>
![image](https://github.com/user-attachments/assets/5a934b6b-a591-4047-926a-38eb5df2a238)
partner.html: <br>
![image](https://github.com/user-attachments/assets/71989d54-f9da-49d5-9df2-0f4e5261df26)
9. I check the source code from each page and found a js file name api.js.
![image](https://github.com/user-attachments/assets/85b5c0fc-2a21-4f23-b0b4-c8753625ea28)
10. Inside the file, there is a new path named ping which need an input value inside the IP parameter. From here, I tried to do code injection from the IP parameter. Here I input "whoami" as the IP value. <br>
![image](https://github.com/user-attachments/assets/ffea679d-578b-4081-9503-f1827a55719f)
11. The code injection works, next I input "ls" to check any file inside the directory. It shows there is a database file inside. <br>
![image](https://github.com/user-attachments/assets/a6415705-4da6-4558-a646-dfe7283448e2)
12. Open the database file and it shows root and admin credentials in md5 hash.
![image](https://github.com/user-attachments/assets/7de10421-6402-4cce-b34a-dd82c1d05e99)
13. I crack each of the password with this [tool](https://crackstation.net/) and the results are shown below. <br>
root password: <br>
![image](https://github.com/user-attachments/assets/6271e13e-450c-427d-9464-e1eb5bba2430)
admin password: <br>
![image](https://github.com/user-attachments/assets/efda8390-6f00-49a2-a0f3-8382964f77fa)
14. Get the root password, I login using SSH protocol. Next, I check the id for any information and found that the user is inside docker.
![image](https://github.com/user-attachments/assets/ae330ec8-c79e-476c-808d-a90cb811ac22)
15. Searching technique to use root insde docker and found this command.
![image](https://github.com/user-attachments/assets/32f7c3fc-0d8d-488c-abe5-3ff747671a96)
16. Run the command inside the target terminal. <br>
<b>Command: docker run -v /:/mnt --rm -it bash chroot /mnt sh <b> <br>
![image](https://github.com/user-attachments/assets/fb888fb6-7995-4159-86ce-01f183ecdfbe)
17. Successfully becomes root, the ssh key is found inside /root/.ssh/id_rsa.pub file. <br>
![image](https://github.com/user-attachments/assets/f81de5cc-296f-4715-aaf9-4138ea527c63)










