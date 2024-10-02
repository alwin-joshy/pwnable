from pwn import *
import math


target = 0x21DD09EC
packet = math.floor(target / 5)
last = target - (packet * 4)

payload = p32(packet) * 4 + p32(last)

s = ssh(host="pwnable.kr", user="col", password="guest", port=2222)
p = s.process(argv=["./col", payload], executable="./col")

p.interactive()

