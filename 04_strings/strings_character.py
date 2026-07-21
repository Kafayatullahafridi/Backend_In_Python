#Printing every character of a string on a new line.


program =  'Python programing'

for ch in program:
    print(ch, end="")
    
for index,ch in enumerate(program):
    print(index , ch , end=',')
    
    