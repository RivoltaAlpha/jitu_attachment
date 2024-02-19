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
n1 = 0
n2 = 1
while n <= 100:
    print(n1)
    print(n2)
    fn = n1 + n2



# Question 3: Power of Two
# Write a program that takes an integer as input and returns true if the input is a power of two.
# Examples: 
# 8=> returns true
# 6=> returns false

def check_div(user_input):
    if (user_input % 2) == 0:
        return True
    else:
        return False

print("Enter a number: ")
user_input = int(input())

print(check_div(user_input))

# Question 4: Capitalize Words
# Write a program that accepts a string as input, capitalizes the first letter of each word in the 
# string, and then returns the result string.
# Examples: 
# "hi"=> returns "Hi"
# "i love programming"=> returns "I Love Programming"

def Capitalize(words):
    str=input().lower()
    words_list = words.split(' ')
    new_words_list = [word.capitalize() for word in wordsList]
    return ' '.join(newWordsList) 

print("Enter a sentence: ")
sentence = input()

print(Capitalize(sentence))


# Question 5: Reverse Integer
# Write a program that takes an integer as input and returns an integer with reversed digit 
# ordering.
# Examples:
# For input 500, the program should return 5.
# For input -56, the program should return -65.
# For input -90, the program should return -9.
# For input 91, the program should return 19.
# def reversing_numbers(numb):



# Question 6: Count Vowels
# Write a program that counts the number of vowels in a sentence.
# eg " Hello World " => returns 2
def count_vowels(sentence):
    vowels = 'aeiouAEIOU'
    return  sum([1 for char in sentence if char in vowels])

sentence = input("Enter a sentence:")
print(count_vowels(sentence))
