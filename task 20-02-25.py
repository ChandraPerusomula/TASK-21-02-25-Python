'''
1.  Print all numbers from 1 to 100 using a for loop?
ANS:-
'''
for i in range(1, 101):
  print(i)


'''
2. Write a program to print the sum of the first n natural
numbers. (n*n+1/ 2).?
ANS:-

'''

def sum_of_natural_numbers(n):
  """Calculates the sum of the first n natural numbers."""
  return (n * (n + 1)) // 2

# Get input from the user
n = int(input("Enter a positive integer n: "))

# Calculate and print the sum
if n > 0:
    result = sum_of_natural_numbers(n)
    print(f"The sum of the first {n} natural numbers is: {result}")
else:
    print("Please enter a positive integer.")

''' 
3.Print all even numbers between 1 and 50 using a while
loop?
ANS:-
'''

num = 2  # Start with the first even number
while num <= 50:
  print(num)
  num += 2  # Increment by 2 to get the next even number

  '''
  4.Write a program to display the multiplication table of a given
number. First 20
Write a program to calculate the factorial of a number using
a while loop?

ANS:
  '''
def multiplication_table(number):
  """Displays the multiplication table of a given number up to 20."""
  for i in range(1, 21):
    result = number * i
    print(f"{number} x {i} = {result}")

def factorial_while(number):
  """Calculates the factorial of a number using a while loop."""
  if number < 0:
    return "Factorial is not defined for negative numbers"
  elif number == 0:
    return 1
  else:
    factorial = 1
    while number > 0:
      factorial *= number
      number -= 1
    return factorial

# Multiplication table example:
num_table = int(input("Enter a number to display its multiplication table: "))
multiplication_table(num_table)

# Factorial example:
num_factorial = int(input("Enter a number to calculate its factorial: "))
result_factorial = factorial_while(num_factorial)
print(f"The factorial of {num_factorial} is: {result_factorial}")


'''  
5. Print all numbers from 1 to 100 that are divisible by 3 and 5
using a for loop?
ANS:

'''
for num in range(1, 101):
  if num % 3 == 0 and num % 5 == 0:
    print(num)