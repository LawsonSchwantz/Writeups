1. Run nmap to discover all open ports and services from the web server.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/308f221b-7241-4f90-bf83-17ab52359d89)

2. I open the ip address in the browser and there is an information that the web uses HttpFileServer 2.3.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/13714112-46a8-4e83-9383-5bb51003b480)

3. Googling for find any vulnerabilities and found this [link](https://www.exploit-db.com/exploits/39161) that are related to HttpFileServer 2.3.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/a8bc1a51-a55d-4992-944b-b02e59b48e4c)

4. For the payload, I use from this [link](https://www.rapid7.com/db/modules/exploit/windows/http/rejetto_hfs_exec/) with metasploit. Set LHOST for our ip address (tun0) and RHOSTS for target IP.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/134947b0-5a7d-4d08-b166-64080bdb4466)

5. Run shell and get the flag in user.txt file.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/acf16788-91f1-462c-b6b4-52f130335529)

6. Cheking one by one directories and found nothing, I decided to check the system info for any information. I found that the system use Microsoft Windows Server 2012 R2.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/e6dbef7a-98fa-4c63-8dd3-19eaf67523bd)

7. Run `background` to maintain the session and still no clue what should do. use `search suggester` to find any sugggester.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/6b3639d3-2684-46c9-a0d7-354e5bd8a138)

8. Run the suggester for find any suitable payloads.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/1979b0a0-8d21-4aae-9a59-51d59207ea50)

9. Too many payloads, so I searched for root escalation vulnarability in Windows R2 and found this [link](https://www.exploit-db.com/exploits/39719).
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/2586d985-da9e-4787-b7d9-0a1ef53e75e6)

10. It related to MS16-032. Back to the list payloads and it's in number two. Set LHOST for our IP address (tun0) and the sessions for our active session (in this case is session one).
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/45d03b01-02be-4dd9-bbba-c511b372418e)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/ab82f06d-6ca2-47cb-8ee5-8952f6da0d41)

11. Run and the root flag can be found in root.txt file.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/a92a4867-4303-40db-be0c-ad7fa7e6dd18)











