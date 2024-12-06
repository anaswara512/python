s="hello world from python"
rev=s[::-1]
print(rev) 
r=""
for char in s:
    if char not in r:
        r=r+char
print(r)
new={}
for i in s:
    if i.isalpha():
        new[i]=new.get(i,0)+1
print(new)
