#f= open("sample.txt","r")
#print(f.read(5))
#f.close()

#with open("sample.txt") as my_file:
# text = (my_file.readlines())
#print(text)

#with open("sample.txt","w") as f:
#    text =(f.write("bye"))
#print(f)

with open("sample.txt","a") as f:
    text =(f.write("bye"))
print(f)