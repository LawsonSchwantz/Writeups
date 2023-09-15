1. Run nmap to discover some ports and services from the web server.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/59f9a342-47d6-473b-b184-7ebe6f967818)

2. If we open port 80, we can see the furniture store website.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/3331a13a-5e76-484f-aeeb-8f92b5238627)

3. Try using feroxbuster and found nothing inside the website.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/c5d98cfe-19af-4cc9-a9f3-7797f3294419)

4. Take a look back to our nmap results, there are NFS and mountd service inside the host. We can use showmount to see the content and it looks like this. <br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/c77f17ab-ef35-438d-87b2-786ecf5b7cc0)

5. First we mount the /var/www/html content using NFS to our folder (mnt).
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/38e08ac0-311f-4ed2-80d2-a5372f5bd344)

6. Next we check each content inside. Unfortunately, we can't open the file because our UID isn't 2017 (My linux's UID is 1000).
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/cc22bd32-6b9e-4804-9a5b-adfa882299af)

7. To open it, we can make a new user (bebek) with the UID of 2017 and run su with bash to run with our new user account. Don't forget to run with bash to get a good view from the terminal.<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/a4c63ab8-38fa-4903-857c-2717002a2fa0)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/d19fc05e-09fc-487b-a153-ae3969b1f9a0)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/559468f2-ccc5-4dc9-9b35-e028f1e0675d)

8. Now we get the access to open the file localy. We can also open it via web like this examples of how css folder looks like.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/47451dc7-e026-447a-9005-9a8eb4193710)

9. From this, the first thing that I think is reverse shell attack. We can use this [script](https://github.com/Wh1ter0sEo4/reverse_shell_php) and change a bit in IP address and the port based on our device.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/cd54383e-ae22-4327-9fc3-05f86130dcd1)

10. Use netcat -lnvp to receive the response and run the script directly in the browser (reverse_shell.php is the script).
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/930b27cb-113a-4da0-a059-d1ae30c9659f)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/7c056701-25e0-4923-a70d-e68212f577ae)

11. We can get the flag in /home/alex/user.txt.<br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/bcf75d83-2832-4a1a-8a3f-2c4cca26f855)

12. Now we want to find the root flag. Remember, we still have to check /home/ross content. We can mount using NFS to our folder (tmp).
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/ad89bade-256c-4aec-9a91-84e38d99d332)

13. Now we check each content inside. Unfortunately, we can't open the file because our UID isn't 1001.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/c18b141d-6535-41e2-901a-94e69ebd1827)

14. Again, we make a new user with the UID of 1001 (mamabebek) and run su with bash to run with our new user account. <br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/c9a0f125-e953-4003-9a63-bbef97350b9c)

15. The interesting thing from there is the Xauthority file. In short, Xauthority is used as a GUI to access the X window system (X11). X11 allow applications to perform their task on another server besides user computer. To use the system, only authorized user that have the access ([Pentesting X11](https://book.hacktricks.xyz/network-services-pentesting/6000-pentesting-x11)). When we open, it looks like this. <br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/0dfce38e-f371-4129-8ace-6fb6bb9b6f8f)

16. We copy the Xauthority content from our local computer to alex terminal. We can use base64 encoding to copy it (I copy to tmp folder).
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/84918bbf-6e2e-4848-a033-973af7e0ed2e)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/d0471e48-6097-4e58-9326-9f1840f4636f)

17. Now we have to set the Xauthority enviroment variable. We can use export XAUTHORITY=path/.Xauthority to add it.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/af35ed90-6de7-41ec-a0fa-410eb854d655)

18. Then, we check the display that the user ross used. We can run **w** command to see all the session information.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/18994d42-b307-4a85-9de4-4c2341e0ab7f)

19. From the session, the display that user Ross uses is :0. According to this [source](https://book.hacktricks.xyz/network-services-pentesting/6000-pentesting-x11#screenshots-capturing), we use xwd -root -screen -silent -display <user's display> to take the X content to our terminal where xwd (X Window Dump) is a tool to take a screenshot and save it from X window system (X11). We save the file as result.xwd.  
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/1169db95-90fa-4c3c-90f3-e5292aefc75e)

20. We want to move this result.xwd into our local terminal. To do that, we use netcat where alex send to my terminal so I can open the file.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/c8c2b950-426f-4198-aa4b-4b24f288b83b)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/8be68a86-f6fd-47a4-85f0-7f9f2cf01263)

21. The output file is meant to be an image. Convert the file into image file (.png or .jpg or .jpeg). After that, open the file and we get the root password!
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/7d599ee2-dded-4aa1-b212-35af0a471525)

22. Run su inside alex terminal and input the root password. Flag is located in /root/root.txt.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/4995a813-706a-409a-9830-80b693bea18f)


