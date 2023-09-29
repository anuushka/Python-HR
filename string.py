#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
def swap_case(s):
    word = ""
    for ch in s:
        if(ch.isupper() == True):
            ch = ch.lower()
            word += ch
        elif(ch.islower() == True):
            ch = ch.upper()
            word += ch 
        elif(ch.isspace() == True):
            word += ch   
        else:
            word += ch
    return word

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
  
#You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
def split_and_join(line):
    w = line.split(" ")
    w = "-".join(w)
    return w
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# Hello firstname lastname! You just delved into python.
# Complete the 'print_full_name' function below.
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last

def print_full_name(first, last):
    print(f'Hello {first} {last}! You just delved into python.')
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#Read a given string, change the character at a given index and then print the modified string.
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#Output the integer number indicating the total number of occurrences of the substring in the original string.
def count_substring(string, sub_string):
    count = 0
    start = 0
    for i in range(len(string)):
        if string.find(sub_string, start) != -1:
            start = string.find(sub_string, start) + 1
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

#In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
#In the second line, print True if  has any alphabetical characters. Otherwise, print False.
#In the third line, print True if  has any digits. Otherwise, print False.
#In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
#In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
import re
if __name__ == '__main__':
    s = input()
    print(bool(re.findall('[a-zA-Z0-9]', s)))
    print(bool(re.findall('[a-zA-Z]', s)))
    print(bool(re.findall('[0-9]', s)))
    print(bool(re.findall('[a-z]', s)))
    print(bool(re.findall('[A-Z]', s)))

'''
Input: 5
Output: 
    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H 
'''
#Replace all ______ with rjust, ljust or center. 
thickness = int(input()) #This must be an odd number
c = 'H'
#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    
#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    
#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#You are given a string S and width w.
#Your task is to wrap the string into a paragraph of width w.
import textwrap
def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    string = wrapper.fill(text=string)
    return string
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


