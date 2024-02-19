# #Question 1: FizzBuzz
# Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for 
# multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print "FizzBuzz"
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# Question 2: Fibonacci Sequence
# Write a program to generate the Fibonacci sequence up to 100.
n1, n2 = 0, 1

while n1 <= 100:
    print(n1)
    fn = n1 + n2

    n1 , n2 = n2 , fn


# Question 3: Power of Two
# Write a program that takes an integer as input and returns true if the input is a power of two.
# Examples: 
# 8=> returns true
# 6=> returns false
def check_power(user_input):

    if  (user_input & (user_input-1)) == 0 and  user_input != 0:
        return True
    else:
        return False

print("Enter a number: ")
user_input = int(input())
print(check_power(user_input))



# Question 4: Capitalize Words
# Write a program that accepts a string as input, capitalizes the first letter of each word in the 
# string, and then returns the result string.
def Capitalize_words(words):
    words_list = words.split(' ')
    new_list = [word.capitalize() for word in words_list]
    return ' '.join(new_list) 

print("Enter a sentence: ")
words = input()
print(Capitalize_words(words))



# Question 5: Reverse Integer
# Write a program that takes an integer as input and returns an integer with reversed digit ordering.
def swapping(num):
    sign = -1 if num < 0 else 1
    num = abs(num)

# covert the number to a list
    digits = [int(digit) for digit in str(num)]

#swapping
    if len(digits) > 1:
        digits[0], digits[-1] = digits[-1], digits[0]
#joining reversed number
    reversed_num = int(''.join(map(str, digits)))
    reversed_num *= sign

    return reversed_num

num = int(input("Enter an integer: "))
result = swapping(num)
print(f"The integer with swapped first and last digits is: {result}")



# Question 6: Count Vowels
# Write a program that counts the number of vowels in a sentence.
# eg " Hello World " => returns 2
def count_vowels(sentence):
    vowels = 'aeiouAEIOU'
    return  sum([1 for char in sentence if char in vowels])

sentence = input("Enter a sentence:")
print(count_vowels(sentence))
