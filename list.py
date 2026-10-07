num = [3,6,2,8,4,10]
large = num[0]
smallest = num[0]
for ele in num:
    if(ele>=large):
        large = ele 
    if(ele<=smallest):
        smallest = ele 

print("largest element is : ",large) 
print("smallest element is : ",smallest)               