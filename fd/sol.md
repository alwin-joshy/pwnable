# Solution

The binary reads a number from argv and subtracts this from 0x1234. It then treats this
as a file descriptor and reads from it. If the number we pass in is 0x1234, it reads
from FD 0 i.e. stdin. It compares what it reads from the file descriptor with a password,
and if this matches, it gives you the flag
