# EGCERT-CTFs2023-Sign_Gate_Challenge_Writeup
The challenge gives us a host and a port to connect to "nc 209.38.200.9 7725".  
It also gives us a message that says the gate keeper will let you go if you sign his message and he can verfiy that it's his signature on it.  
The message given is "Crypt0N19h7".  

Connecting to the host using ncat or python's socket returns an interface that gives you two options:  
1- Sign a message.  
2- Verfiy a signature.  

Here we will use option 1 to get the signature of the gate keeper, and somehow use it to sign "Crypt0N19h7" as if he signed it, then we send it back using option 2 and recieve the flag.  

First let's change the message from bytes to long.  
Crypt0N19h7 --> 81538619852414955053213751.  
factorizing the message using Alperton online factorization.  
81538619852414955053213751 = 16896045279 * 4825899700550569.  

The trick here is that if M = m1 * m2.  
where s1 is the signature of m1.  
and s2 is the signature of m2.  

S the signature of M can be calculated as follows:  
S = (s1 * s2) mod n.

And here is an example to better understand the idea.  
![image](https://github.com/MohamedAwad9k8/EGCERT-CTFs2023-Sign_Gate_Challenge_Writeup/assets/75997594/a8ffa089-d1e3-411f-95b6-71a109a50b9d)
.  
.  
![image](https://github.com/MohamedAwad9k8/EGCERT-CTFs2023-Sign_Gate_Challenge_Writeup/assets/75997594/242667c8-c1f1-4548-a857-0fd9430c2203)

And here's how cheerful the flag looks in my terminal
![image](https://github.com/MohamedAwad9k8/EGCERT-CTFs2023-Sign_Gate_Challenge_Writeup/assets/75997594/0adae823-40fa-4be7-b0ec-8c1503ff8f20)
