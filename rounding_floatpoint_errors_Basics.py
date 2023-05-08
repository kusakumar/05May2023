"""
round() Function
The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
The default number of decimals is 0, meaning that the function will return the nearest integer

Syntex: round(float_num, num_of_decimals)
Parameters
float_num: the float number to be rounded.
num_of_decimals: (optional) The number of decimals to be considered while rounding.
It is optional, and if not specified, it defaults to 0, and the rounding is done to the nearest integer.
The second argument is optional and defaults to 0 when not specified, and in such case, it will round to the nearest integer, and the return type will also be an integer.
"""
# testing round()

float_num1 = 10.60 # here the value will be rounded to 11 as after the decimal point the number is 6 that is >5

float_num2 = 10.40 # here the value will be rounded to 10 as after the decimal point the number is 4 that is <=5

float_num3 = 10.3456 # here the value will be 10.35 as after the 2 decimal points the value >=5

float_num4 = 10.3445 #here the value will be 10.34 as after the 2 decimal points the value is <5

print("The rounded value without num_of_decimals is :", round(float_num1))
print("The rounded value without num_of_decimals is :", round(float_num2))
print("The rounded value with num_of_decimals as 2 is :", round(float_num3, 2))
print("The rounded value with num_of_decimals as 2 is :", round(float_num4, 2))
print()
# testing round() on a integer

num = 15
print("The output is", round(num))
num2 = -2.8
num3 = -1.5
print("The value after rounding is", round(num2))
print("The value after rounding is", round(num3))
print()

##floating point errors
def sqrt(num):
    root = 0.0
    while root * root < num:
        root += 0.01
    return root
print(sqrt(4))
print(sqrt(9))
print()
print(1.2 - 1.0)
print()
print(.1 + .1 + .1 == .3)
print(round(.1, 1) + round(.1, 1) + round(.1, 1) == round(.3, 1))
print(0.1 + 0.2 + 0.3 == 0.6)
print(round(.1 + .1 + .1, 10) == round(.3, 10))  #0.1 cannot get any closer to the exact value of 1/10 and 0.3 cannot get any closer to the exact value of 3/10
print(round(0.1 + 0.2 + 0.3, 5)  == round(0.6, 5))
print()
###escape characters:

print("kusa\nkumar")
print("kusa\\nkumar")
print("kusa\tkumar")
print("kusa\\\\\\kumar")
print("\'kusa\' \'kumar\'")
print("\"kusa\" \"kumar\"")