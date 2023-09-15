1. Run nmap to discover some open ports and services from the web server.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/ce8cf887-54a0-4369-8904-1a31ea201642)

2. Only 2 ports are opened and run port 8443 on https protocol. It shows that there is an error 403 which mean that we are not allowed to access that port.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/b6f8c0b7-0c51-47a1-8494-092081d631c5)

3. Back to the nmap result, we can discover that the web server using kubernetes as their OS.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/385c0bc1-6582-4218-ac5c-18ba7ca860df)

4. Now we want to check if the kubelet API is exist. We can add -p- in our nmap command to see all ports open in the web server. There we discover that there is a ssl opened in port 10250.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/2314e72a-441e-402b-948c-df9a664c7710)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/6b748eb8-5b5c-43a2-8a8d-c6433153d5f8)

5.When we opened the port, it says 404 not found which mean we can't find anything here.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/bc070816-dcec-44c6-977f-dd43ae40d076)

6. To see what pods that the web server has, we use **kubeletctl** to check it.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/1a38bb67-6584-4fcd-ae44-66f40434b4e8)

7. To check which pods are vulnerable, we use **scan rce**. The result is there are two pods are vulnerable called nginx and kube-proxy (indicates with + sign)
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/6029920a-ee83-48b6-a86e-54262ddb3f24)

8.We check the kube-proxy pod first using **exec** command from the kubeletctl and found nothing there.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/f28861af-dd0d-4098-9858-164f5622cc8e)

9. Check the nginx pod and found that we can execute our bash command there.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/da7670f9-c722-4c3b-8152-759aef2abaf4)

10. Therefore we takeover the target terminal with **bin/bash** command and found the flag in root/user.txt
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/c2ffb4ff-f5f5-4e9a-b48a-819296524ab9)

11. Next, we want to find the serviceaccount folder that indicates the identity of the services. I ask to chatGPT and it says that there are 2 main factors that shows service identity are tokens and ca.crt that are located in var/...
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/98f80731-c636-4421-9d1f-7fe1279945e9)

12. This is what looks like.
ca.crt: <br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/7e66c5be-2158-429a-ba1c-aeadc5481cd8)

token: <br>
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/ff488e04-ecd2-49b0-847d-d53d508538e5)

13. Copy the token and ca.crt content to our local terminal. Unfortunately, the terminal doesn't have netcat so we have to do manually.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/2c01a160-509e-43f9-a241-f3175b1d5c94)

14. Write the token into enviroment variable and run **kubectl get pods** command to check the pods that are running in the background and we discover only nginx is running.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/d300d733-4116-4138-ab32-4544f4d8512e)

15. Next we want to know what this terminal can do. We use **auth can-i** to see the privileges. The result is the terminal can get, create, and list pods from another target.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/5ec92aff-2eca-4baf-b239-b47bd7abd3e9)

16. Now we open the .yaml file to check the terminal configuration. From there we get the information that the image that the terminal uses is nginx 1.14.2 and the namespace is set to default.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/e3e8ff41-687c-4cdb-9185-6cbf6395b307)

17. From that two important informations, we can build a nefarious pod to give us the whole privilege of the terminal such as root privileges with the script below (mount in /mnt folder). 
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/adc1dc49-f234-4c27-b013-b8226a11dcb3)

18. We use **apply** to execute the payload.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/30e8d8cd-0d7a-41f4-86e6-e23457b715df)

19. We can see that now there are two pods that are running in the background.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/ad6311fe-cb6e-47ca-b032-ad613df64189)

20. Access the "nginxnewpod" to get the full privileges and we get the flag in /mnt/root/root.txt.
![image](https://github.com/LawsonSchwantz/Writeups/assets/74954683/434f44d6-048f-4f8a-99a5-cc81d72c0532)


























































