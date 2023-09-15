## The code is so long and complicated, it's difficult to find the flag with the manual steps. When I analyze the code, I discover that the memcmp is the place where the flag is stored. 
### 1. Check the file first and we discover that the file using PIE in it
![image](https://user-images.githubusercontent.com/74954683/210346174-383f1d4d-adab-43d4-8344-39b8b6858c46.png)
### 2. Find the memcmp address using objdump like this:
![image](https://user-images.githubusercontent.com/74954683/210345813-f5dd224e-b5d4-4057-96b0-c148e2b255b5.png)
### 3. Analyze it and we found the address (0x13b9)
![image](https://user-images.githubusercontent.com/74954683/210345915-757e3809-a705-4f81-bbab-4c7701f68255.png)
### 4. Because the file using PIE, we need to find the base address with vmmap. We take the address that ends with "4000"
![image](https://user-images.githubusercontent.com/74954683/210346368-6fb26cd3-1865-4bac-a9b2-873ceb81083b.png)
### 5. Set the breakpoint from the result of the multiplication of the base address with the memcmp address (0x13b9 * 0x0000555555554000). After that, run the code and input any characters
![image](https://user-images.githubusercontent.com/74954683/210346584-bf069ed7-a488-4eb8-bb34-e20a575196c8.png)
### 6. The flag is stored $rdi and just use command x/s to get the full flag.
![image](https://user-images.githubusercontent.com/74954683/210347275-b43a92a5-e3c8-45ba-8236-d6c18237ad16.png)
