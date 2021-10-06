import os

file = open('a.jpg', 'rb')
# print(file)
file.close()
file = open('time.txt', 'r', encoding='utf8')
print(file)
file.close()

# with open("time.txt", "r", encoding="utf8") as file:
#     s = file.read()
#     file.seek(10)
#     t=file.read(10)
#     print(s)
#     print(t)
# with open("time.txt", "a", encoding="utf8") as file:
#     file.write('\n')
#     file.write('sdaaaaaaaaaaaaaaaaa')

print(os.getcwd())
print(os.listdir)
