1. Run nmap to discover some ports and services from the web server.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/3422b570-bf30-4c39-83ed-1029bbe598a7)

2. If we open port 80, we can see the furniture store website.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/50b57adf-5b1d-47b1-9200-a869f95d4c80)

3. Try using feroxbuster and found nothing inside the website.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/57f0c892-fe95-4d7d-9a04-a4548bf46ea4)

4. Take a look back to our nmap results, there are NFS and mountd service inside the host. We can use showmount to see the content and it looks like this. <br>
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/c138d906-7ae5-4a81-a3a5-e8aa2e7aa1ae)

5. First we mount the /var/www/html content using NFS to our folder (mnt).
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/b6268262-3359-4d75-898c-b66ab4731cad)

6. Next we check each content inside. Unfortunately, we can't open the file because our UID isn't 2017 (My linux's UID is 1000).
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/b0db0f66-9123-4472-a2f0-6ac49250119f)

7. To open it, we can make a new user (bebek) with the UID of 2017 and run su with bash to run with our new user account. Don't forget to run with bash to get a good view from the terminal.<br>
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/5ed20657-aa8a-474b-9368-bacd6f9ca323)
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/30301250-bcc2-43d6-a0ee-fc6737864824)
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/e3ad5ff4-f542-4cd0-acae-b63bb870e213)

8. Now we get the access to open the file localy. We can also open it via web like this examples of how css folder looks like.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/a804d5dc-f223-4b82-9019-63ab7c7e2b9d)

9. From this, the first thing that I think is reverse shell attack. We can use this [script](https://github.com/Wh1ter0sEo4/reverse_shell_php) and change a bit in IP address and the port based on our device.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/0f81a75d-d327-4157-bfbe-88e13b2d0bd1)

10. Use netcat -lnvp to receive the response and run the script directly in the browser (reverse_shell.php is the script).
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/b961f787-e122-4898-9d35-9c4095eab56f)
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/f17a6287-a42a-42a0-9f99-8d7f69463871)

11. We can get the flag in /home/alex/user.txt.<br>
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/a9c08855-b8b3-451a-939c-56632ad7927e)

12. Now we want to find the root flag. Remember, we still have to check /home/ross content. We can mount using NFS to our folder (tmp).
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/cf6dff66-26ac-4eee-a940-445880621d3c)

13. Now we check each content inside. Unfortunately, we can't open the file because our UID isn't 1001.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/53ab0e63-8e38-4494-b53f-6126d042278a)

14. Again, we make a new user with the UID of 1001 (mamabebek) and run su with bash to run with our new user account.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/5b106bbb-264b-47ca-a8e4-7747ec6d3f30)

15. The interesting thing from there is the Xauthority file. In short, Xauthority is used as a GUI to access the X window system (X11). X11 allow applications to perform their task on another server besides user computer. To use the system, only authorized user that have the access ([Pentesting X11](https://book.hacktricks.xyz/network-services-pentesting/6000-pentesting-x11)). When we open, it looks like this. <br>
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/1a2deaee-fcc7-4c07-b85d-87bae44acec7)

16. We copy the Xauthority content from our local computer to alex terminal. We can use base64 encoding to copy it (I copy to tmp folder).
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/430c023d-4c34-4ab4-a283-46d4de205101)
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/3108f673-ed8c-4420-9d92-dd56d604595c)

17. Now we have to set the Xauthority enviroment variable. We can use export XAUTHORITY=path/.Xauthority to add it.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/afa513bf-13d9-4114-bc55-ebfe5b799c2d)

18. Then, we check the display that the user ross used. We can run **w** command to see all the session information.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/01555cbe-78d4-4637-b60b-6950f52a6e80)

19. From the session, the display that user Ross uses is :0. According to this [source](https://book.hacktricks.xyz/network-services-pentesting/6000-pentesting-x11#screenshots-capturing), we use xwd -root -screen -silent -display <user's display> to take the X content to our terminal where xwd (X Window Dump) is a tool to take a screenshot and save it from X window system (X11). We save the file as result.xwd.  
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/5fe8f901-abe6-41ef-940c-a0ee43f52a15)

20. We want to move this result.xwd into our local terminal. To do that, we use netcat where alex send to my terminal so I can open the file.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/e403122c-a891-4758-a8b7-500346f3e146)
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/1f6c044e-fa7e-4cbb-b6f4-eca4fdc6af64)

21. The output file is meant to be an image. Convert the file into image file (.png or .jpg or .jpeg). After that, open the file and we get the root password!
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/5788a3d5-9dfa-4fd4-baf7-33ee0d7952ec)

22. Run su inside alex terminal and input the root password. Flag is located in /root/root.txt.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/724da30e-15a4-42cc-b170-d61f3cdeed3b)


















