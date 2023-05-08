"""
3.shuffle the string using any explam

"""

string = "Hello kusakumar"
shuffle_string = ""
for i in range(len(string)):
    n=int(input("Enter the number: "))
    shuffle_string += string[n]
print("Shuffled string: ",shuffle_string)
