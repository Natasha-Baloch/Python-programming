marks = []
for m in range(5):
    num = int(input("Enter Student marks : "))
    marks.append(num)


total = sum(marks)
print(f"The total is : {total}")
print(f"The Average is : {total/5}")
print(f"The highest number is : {max(marks)}")
print(f"The smallest number is : {min(marks)}")
marks.sort()
print(f"The marks in Ascending order : {marks}")