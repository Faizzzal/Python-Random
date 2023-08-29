try:
    f=open('sample.txt','r')
    print(f)
except Exception as e:
    print(e) 
print("hello")    
#finally:
#    print('ERROR')