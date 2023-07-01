
#print("Please Enter a string like ,"a2d3f4", then look output carefully")
# str1 = input("enter a string")
# mid = ''
# output = ''

# for i in str1:
#     if i.isalpha():
#         mid = mid+i
#     if i.isdigit():
#         last_element = mid[-1]
#         multi = last_element*int(i)
#         output = output+multi

# print(mid)
# print(output)


####### rewarse a string

# #1

# s = input("enter a string")
# print(s[::-1])

#2

#optimal solution

# def reverse(s):
    
#     str2 = ''

#     for i in s:
#         str2 = i+str2

#     print(str2)

# string1 = input("Enter a string to be reverse")
# reverse(string1)



#reverse each character of the sting
# s=input("Enter Some String: ")
# l=s.split()
# print(l)
# l1=[]
# i=0
# while i<len(l):
#     print(l[i][::-1])
#     l1.append(l[i][::-1])
#     i=i+1
# print(' '.join(l1))


# print the occurence of each character of sting

s = input("enter a sting")
print(s)
d = {}
for i in s:
    if i in d.keys():
        d[i] = d[i]+1

    else:
        d[i] = 1
print(d)


print("this is demo for git vesion chceck")


