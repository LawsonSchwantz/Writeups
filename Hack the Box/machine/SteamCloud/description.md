1. Run nmap to discover some open ports and services from the web server.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/3b2acd0f-64f3-4032-8bf7-5a1dba761976)

2. Only 2 ports are opened and run port 8443 on https protocol. It shows that there is an error 403 which mean that we are not allowed to access that port.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/081b9411-7a2e-45b4-9dc0-a74f0d5729d6)

3. Back to the nmap result, we can discover that the web server using kubernetes as their OS.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/239ef200-ed28-4b12-9559-9aeedfb50129)

4. Now we want to check if the kubelet API is exist. We can add -p- in our nmap command to see all ports open in the web server. There we discover that there is a ssl opened in port 10250.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/2ab6a73f-6b36-485a-b542-9977b0e4d2ef)
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/433757af-a151-4ea1-b2c4-c9bea614ad23)

5.When we opened the port, it says 404 not found which mean we can't find anything here.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/317b2d64-327f-420e-ba38-97bf10cbdbfa)

6. To see what pods that the web server has, we use **kubeletctl** to check it.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/a14f40f2-8a22-4907-b849-b0088df702f5)

7. To check which pods are vulnerable, we use **scan rce**. The result is there are two pods are vulnerable called nginx and kube-proxy (indicates with + sign)
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/1d81fe2e-d7ce-40e7-896f-636c9173a5bf)

8.We check the kube-proxy pod first using **exec** command from the kubeletctl and found nothing there.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/dff28ddf-3308-4be2-b205-da86bbbebfea)

9. Check the nginx pod and found that we can execute our bash command there.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/cf365dac-8c0a-474b-97c5-3e08fd700aa1)

10. Therefore we takeover the target terminal with **bin/bash** command and found the flag in root/user.txt
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/3ceed04a-20ae-4c27-94eb-5f0639d1e522)

11. Next, we want to find the serviceaccount folder that indicates the identity of the services. I ask to chatGPT and it says that there are 2 main factors that shows service identity are tokens and ca.crt that are located in var/...
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/4454defa-c32a-4afe-b922-b175d4d19679)

12. This is what looks like.
ca.crt: <br>
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/da97873c-1f77-487f-a95f-a58a125c9fa3)
token: <br>
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/33f0ae3e-e99f-4d38-8295-9cb4211d56e9)

13. Copy the token and ca.crt content to our local terminal. Unfortunately, the terminal doesn't have netcat so we have to do manually.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/1159417b-81de-4939-9787-14d913759e6c)

14. Write the token into enviroment variable and run **kubectl get pods** command to check the pods that are running in the background and we discover only nginx is running.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/7fbafb38-016b-4eeb-a500-279f3d0258a2)

15. Next we want to know what this terminal can do. We use **auth can-i** to see the privileges. The result is the terminal can get, create, and list pods from another target.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/b6c53da8-7ab7-49f2-8e1f-91561a9103a7)

16. Now we open the .yaml file to check the terminal configuration. From there we get the information that the image that the terminal uses is nginx 1.14.2 and the namespace is set to default.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/4817811f-fef0-4fa1-9254-2cbe559c28b7)

17. From that two important informations, we can build a nefarious pod to give us the whole privilege of the terminal such as root privileges with the script below (mount in /mnt folder). 
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/117ccc54-3286-4e51-a87a-9e8462cd1821)

18. We use **apply** to execute the payload.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/bd0a4ae3-ff42-4ba0-afcf-5ef3e7a94a9c)

19. We can see that now there are two pods that are running in the background.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/bc0a3ed8-f241-4313-90d4-4d2ee4fedc2d)

20. Access the "nginxnewpod" to get the full privileges and we get the flag in /mnt/root/root.txt.
![image](https://github.com/LawsonSchwantz/CTF-Writeups/assets/74954683/b9997db3-5e30-4e8b-89e0-6556da06e9be)

























































