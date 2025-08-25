# Write a python program to count the number of vowels in a string

s = input('Enter a string: ')
v = 'aeiouAEIOU'
count = 0
for i in s:
    if i in v:
        count += 1

print(f'Total number of vowels in \'{s}\' is {count}')        