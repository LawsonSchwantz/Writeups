1. Run Nmap to check any open ports and the services from the target IP.
![image](https://github.com/user-attachments/assets/58e315fb-58a9-48c5-a403-4f7d6d5a16d6)
2. It shows that port 80 is open, let's add it into /etc/hosts file. <br>
![image](https://github.com/user-attachments/assets/da47ecbb-27c7-4a61-a1fb-900d1467faaf) <br>
3. Opening the website and it shows dashboard page that capture events from the service. 
![image](https://github.com/user-attachments/assets/b0e7274b-06c5-42a1-a698-9b5aa7854d3f) <br>
4. Change it to the "security snapshot" feature and it gives 1st data page from the capture activity. 
![image](https://github.com/user-attachments/assets/73ce99ec-de59-4ae3-9309-fe825ec9730f) <br>
5. Because it starts from 1, I try to change it to 0 and it shows interesting capture data.
![image](https://github.com/user-attachments/assets/f746c70b-6f67-4e14-8c00-3800357ac8c0) <br>
6. From the pcap file, the user logs in into the server and the credentials are shown inside the file.
![image](https://github.com/user-attachments/assets/bbad1d9c-2d16-4fd6-8835-1cc6f7e4643c) <br>
**Username: nathan <br>
Password: Buck3tH4TF0RM3!**
7. Logs in using SSH protocol and the user flag is found in user.txt.
![image](https://github.com/user-attachments/assets/93bf5134-d4dd-4dde-b7dd-d20e34f21152) <br>
8. Now I run linpeas.sh inside the target machine to discover any vulnerability inside the machine.
![image](https://github.com/user-attachments/assets/59d262b0-7048-440f-a2c2-5a7ab661d1b9) <br>
9. It shows that there is capability vulnerability from the server and check it from GTFOBins. It gives privilege escalation payload below.
![image](https://github.com/user-attachments/assets/afe263c7-cffe-483c-915d-5d428a0a0e80) <br>
10. Run the payload and I successfully gain the root privilege. The root flag is stored in /root/root.txt.
![image](https://github.com/user-attachments/assets/7cbc8145-0590-4d67-b330-7161aa49312a) <br>
































