#### 1. Open the file and unfortunately can't use ghidra and IDA to analyze the code :(
![image](https://user-images.githubusercontent.com/74954683/211301750-efefac6c-1873-41d3-a66a-e86c98032f8c.png)
#### 2. So i try to open with dnSpy and yay, it works
![image](https://user-images.githubusercontent.com/74954683/211301864-c4e67dd4-e12b-42b6-8c3e-02c330129043.png)
#### 3. Analyze the file and I discover in function 1() that the function always return false statement but we need to be true in the validation
![image](https://user-images.githubusercontent.com/74954683/211301959-ecfcdbff-25c3-46fb-9c7a-6543f4e017bd.png)
#### 4. So let's set a breakpoint in line 11 and as we can see it returns false statement in both flag
![image](https://user-images.githubusercontent.com/74954683/211300832-f05d0b2a-dc1f-43e3-8391-1d9695c07d58.png)
#### 5. Change the value from the flag2 into true and press continue
![image](https://user-images.githubusercontent.com/74954683/211300859-5f20ccf7-3c72-421f-8662-b762ea998b51.png)
![image](https://user-images.githubusercontent.com/74954683/211300870-750a77bd-d09f-46c6-a703-db4f12a94548.png)
#### 6. Yahoowww, we pass the first validation
![image](https://user-images.githubusercontent.com/74954683/211324976-e878a5b1-ce78-462f-9886-2a766884e3cb.png)
#### 7. Now we must have the second key to pass, first we need to set a breakpoint in line 39 
![image](https://user-images.githubusercontent.com/74954683/211325215-66d7668f-8db6-4a92-b158-cfb34c8acdab.png)
#### 8. Input random text into it and we get the key like this:
![image](https://user-images.githubusercontent.com/74954683/211300956-704ee5f0-2ff3-465e-9516-d3de054f0e2d.png)
#### 9. Input the right key and the screen will be like this:
![image](https://user-images.githubusercontent.com/74954683/211301024-ba7911dc-aace-4ef7-acb6-bac5857f0dd9.png)
#### 10. Press F10 in line 41 and we get the flag
![image](https://user-images.githubusercontent.com/74954683/211301077-42224764-72fc-4314-a4c8-292a1b300f80.png)


