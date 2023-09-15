with open("msg.enc") as f:
    ct = bytes.fromhex(f.read())

flag = ""
for char in ct:
    for val in range(33,128):
        if((123 * val + 18) % 256 == char):
            flag += chr(val)
            break

print(flag)
