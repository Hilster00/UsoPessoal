class c:
   @classmethod
   def c1(cls,nome):
       r=""
       for i in nome:
           r+=str(ord(i))+"-"
       return r
   @classmethod
   def c2(cls,nome):
       r=""
       for i in nome.upper():
           if i in "ABC":
               r+="2"
           elif i in "DEF":
               r+="3"
           elif i in "GHI":
               r+="4"
           elif i in "JKL":
               r+="5"
           elif i in "NMO":
               r+="6"
           elif i in "PQRS":
               r+="7"
           elif i in "TUV":
               r+="8"
           elif i in "WXYZ":
               r+="9"
           elif i == "+":
               r+="0"
           else:
               r+="1"
           r+="-"
       return r
   @classmethod
   def c3(cls,n):
       r=""
       for i in range(1,len(n)+1,2):
           a=n[i-1:i+1]
           r+=chr(int(a))
       return r
   @classmethod
   def c4(cls,n):
       r=list()
       for i in n:
           if i == "2":
               r.append(["A","B","C"])
           elif i =="3":
               r.append(["D","E","F"])
           e
   @classmethod
   def t_(cls,n):
       return n.replace("-","")
p=input(":")
print(c.c1(p))
print(c.c2(p))         
print(c.c3(c.t_(c.c1(p))))
