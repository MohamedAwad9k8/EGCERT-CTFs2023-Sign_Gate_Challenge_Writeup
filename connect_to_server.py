from pwn import *

ip_address = '209.38.200.9'
port = 7725

# Connect to the server using pwn
conn = remote(ip_address, port)

#Changing the message from bytes to long
# Crypt0N19h7 --> 81538619852414955053213751 
#factorizing the message using Alperton online factorization

#81538619852414955053213751 = 16896045279 * 4825899700550569
#We send both messages m1 and m2, and reciece both their signatures s1 and s2
# Note: The signature of M = m1 * m2 is (s1 * s2) % n

# Receive and process the response from the server
response = conn.recv(1024)
print(response.decode().strip())
output = response.decode().strip()
n = output[212:366] # from 212 to 365
print(n)

conn.sendline("1".encode())
response = conn.recv(1024)
print(response.decode().strip())
conn.sendline("16896045279".encode())
response = conn.recv(1024)
print(response.decode().strip())
s1 = response.decode().strip()[0:154]
print(s1)

conn.sendline("1".encode())
response = conn.recv(1024)
print(response.decode().strip())
conn.sendline("4825899700550569".encode())
response = conn.recv(1024)
print(response.decode().strip())
s2 = response.decode().strip()[0:154]
print(s2)

s = (int(s1) * int(s2)) % int(n)

conn.sendline("2".encode())
response = conn.recv(1024)
print(response.decode().strip())
conn.sendline(str(s).encode())
response = conn.recv(1024)
print(response.decode().strip())
