1. Run Nmap to discover any interesting information from the open ports of the web server.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/5b6fb91f-c046-4f5c-af16-552bbb50876a)

2. The Nmap give results some suggestion of host script that are related to smb. Let's find some vulnerable script that related to smb with nmap and it gives result it's vulnerable to remote code execution.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/d37a0c4b-054b-461d-9133-44a9d00c14f1)

3. To do so, I use metasploit for the payload and input the victim IP Address. 
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/791aace6-385b-40a2-be7c-edc493da5429)

4. Run the script and it successfuly enters the meterpreter. To use the windows shell, just type shell in the meterpreter.<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/9c986d98-4dc7-4e3f-9239-17b2a21d9cbf)

5. The user flag is found in /John/Dekstop/user.txt.<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/9a8f3b1e-d51e-4aab-904e-a77a05b56299)

6. The root flag is found in /Administrator/Desktop/root.txt.<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/907c970e-4419-4c4f-a4ea-348eec254803)









