1. Run Nmap to discover any open ports (80 for web server, 3389 for RDP).
![image](https://github.com/user-attachments/assets/5b50a1b1-6f9b-4235-af3c-e1ebb2c3c9d1)
2. Open the website and it shows blog page.
![image](https://github.com/user-attachments/assets/bb152d9a-cb59-45fd-ab39-bb2b9b875c1d)
3. Robots.txt is showed inside the server and consist of possible user password.
![image](https://github.com/user-attachments/assets/e5c16412-3948-465e-a998-a1c7b4a33f19)
4. Check for the administrator name, it shows that the name is Solomon Grundy from the poem content in one of the blog inside the server.
![image](https://github.com/user-attachments/assets/a90d665a-a5ff-4594-b6a5-c16317e19fe5)
5. The email format is shown in the first blog, so for this case the email is SG@anthem.com.
![image](https://github.com/user-attachments/assets/1bb7cf68-e91a-44a5-8d56-07a120e5dd6c)
6. The first flag is shown inside the view-source meta content in the first blog.
![image](https://github.com/user-attachments/assets/d37b1eb8-8065-451b-8dea-46a899f186e9)
7. The second flag is shown inside the view-source search placeholder in the first or second blog.
![image](https://github.com/user-attachments/assets/a3b6040b-eb59-4bd1-84f0-45c3201e7752)
8. The third flag is shown in Jane Doe user profile.
![image](https://github.com/user-attachments/assets/bd5cbae9-749a-447f-8327-a67634f9f7c9)
9. The last flag is shown inside the view-source meta content in the second blog.
![image](https://github.com/user-attachments/assets/b4465011-10df-452e-a754-5423bfd4bfd6)
10. Log in to the server RDP using xfreerdp from linux with the known credentials from above.
![image](https://github.com/user-attachments/assets/dfa36cb2-5c55-43b6-a8cb-3d2f57087e02)
11. The user flag is found in user.txt.
![image](https://github.com/user-attachments/assets/8b471bce-2c8d-4728-bd53-51cc84d16dab)
12. For admin flag, there is hidden folder named backup that can be view by changing the permission to show hidden files/folders in view menu above file explorer.
![image](https://github.com/user-attachments/assets/ae3cc937-cfcc-4163-b66c-3233ff8c054a)
13. Inside the backup folder, there is a file named restore.txt but can't be opened because of the permission problem.
![image](https://github.com/user-attachments/assets/f94d48b5-eacf-48ae-92a8-317707101f35)
14. In here, I change the file permission as follows: <br>
a. Open Properties -> Choose security menu -> Click Edit Options. <br>
![image](https://github.com/user-attachments/assets/ef33ca9f-1eca-4954-8a52-6cd7ce3dffa1) <br>
b. Click Add button. <br>
![image](https://github.com/user-attachments/assets/b91f04ef-7c10-4f07-a9fd-74262615302f) <br>
c. Choose Advance button -> Change the object types into users only -> Click Find Now -> Choose the SG user. <br>
![image](https://github.com/user-attachments/assets/d4a09a5a-b341-4c44-80ec-0ba51c5025db) <br>
d. Click OK until all the windows page is closed. <br>
![image](https://github.com/user-attachments/assets/f4301011-98df-4cba-94e4-49fbece7ba3e) <br>
15. Open the restore.txt again and it shows the admin password. 
![image](https://github.com/user-attachments/assets/75514d5c-971f-48d0-b83e-3b361036366e)
16. Log in to the server RDP using xfreerdp from linux with the known credentials from above as the admin user.
![image](https://github.com/user-attachments/assets/73569228-33ca-4457-b266-5fbc925b13df)
17. The admin flag is found in root.txt.
![image](https://github.com/user-attachments/assets/f9681791-476c-4971-8d34-9cfb5881e3bb)





































