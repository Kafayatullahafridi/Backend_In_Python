# text = "FastAPI"
# text[0]#F
# text[3]#t
# text[-1]#I
# text[-3]#A
# text = "Programming"
# print(text[0:3])# Pro
# print(text[3:7])# gram
# print(text[0:])# Programming
# print(text[::-1])# gnimmargorP

# word = "backend"
# count = 0
# for letter in word:
#     print(letter)
#     count+=1
# print(count)

# text = "Python"
# text[0] = "J"#TypeError: 'str' object does not support item assignment
# email = "kayfi@example.com"

# print('@'in email)
# print('.com'in email)
# print('gmail'in email)

# username = "   KAYFI   "
# name = username.strip().lower()
# print(name)
# url = "https://example.com/users"
# if url.startswith('https://') and url.endswith('/users'):
#     print('valid url')
# else:
#     print('invalid ')

# text = "I am learning Java"
# new = text.replace('Java',"Pythton")
# print(new)
password = "   Python123   "
normal = password.strip().lower()
print(normal)
lenth = len(normal)
print(lenth)
p = 'python'
if lenth>=8 and  p.lower() in normal:
    print('Valid password')

email = "   KAYFI@Example.COM   "
valid = email.strip().lower()
if '@' in valid:
    print('Valid')