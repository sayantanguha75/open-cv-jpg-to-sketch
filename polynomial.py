x=int(input("Enter the degree of the first polynomial : "))
result=''
list1=[]
nlist1=[]
x=x+1
for i in range(x,0,-1):
    i=str(i-1)
    y=input(f"Enter the coefficient for x^{i} : ")
    list1.append(y)
    n=y+"^"+i+"+"
    result += n
result=result[:-1]
nlist1 = list(map(int, list1))

x1=int(input("Enter the degree of the second polynomial : "))
result1=''
list2=[]
nlist2=[]
x1=x1+1
for j in range(x1,0,-1):
    j=str(j-1)
    y1=input(f"Enter the coefficient for x^{j} : ")
    list2.append(y1)
    n1=y1+"^"+j+"+"
    result1 += n
result1=result1[:-1]
nlist2 = list(map(int, list2))

# sum_list = []
# max_len = max(len(list1), len(list2))
# list1 = list1 + ['0'] * (max_len - len(list1))
# list2 = list2 + ['0'] * (max_len - len(list2))
# for num1, num2 in zip(list1, list2):
#     sum_list.append(int(num1) + int(num2))

# print(sum_list)
sum_list = []
max_len = max(len(list1), len(list2))

list1 = [0] * (max_len - len(list1)) + list1
list2 = [0] * (max_len - len(list2)) + list2

for num1, num2 in zip(list1[::-1], list2[::-1]):
    sum_list.append(int(num1) + int(num2))

sum_list = sum_list[::-1]

print(sum_list)
polynomial = ""
degree = len(sum_list) - 1

for i, coefficient in enumerate(sum_list):
    power = degree - i
    if coefficient != 0:
        if coefficient > 0 and i != 0:
            polynomial += " + "
        elif coefficient < 0:
            polynomial += " - "
        if abs(coefficient) != 1 or power == 0:
            polynomial += str(abs(coefficient))
        if power >= 1:
            polynomial += "x"
        if power >= 2:
            polynomial += "^" + str(power)

print(polynomial)
