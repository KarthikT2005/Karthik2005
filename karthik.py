string = "do what i say to the world"
for word in string.split():
    if len(word) % 3 == 0:
        print(word)
# Find the length of the string if the length of the string is
# more than 3 print the first letter of the word output : w
# convert string into list

string = "there is a string"
for word in string.split():
    if len(word)>3:
        print(word[0])

string = "session is going to start"
print(string)
result = [i for i in string.split()if len(i) == 2]
print(result)
print(result[::-1])

for i in(0,20):
    if i % 2 == 0:
        print("buzz")
    else:
        print("not divisible by 2")
