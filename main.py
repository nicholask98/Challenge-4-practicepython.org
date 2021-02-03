'''
Create a program that asks the user for a number and 
then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number 
that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has 
no remainder.)
'''

user_num = int(input('Enter a number:\n'))
divisor_list = []
count = 1
while count <= (user_num / 2):
    if user_num % count == 0:
        divisor_list.append(count)
    count += 1

divisor_list.append(user_num)

print('The divisors of {num} are {div}'.format(num = user_num, div = divisor_list))