from replit import clear
from art import logo

def add(n1, n2):
  return n1+n2

def sub(n1, n2):
  return n1-n2

def mult(n1, n2):
  return n1*n2

def div(n1, n2):
  return n1/n2

operations = {
  "+": add,
  "-": sub,
  "*": mult,
  "/": div,
}

ans = "yes"
chain_calc = "yes"



while ans=="yes":

  clear()
  print(logo)
  num1 = float(input("Enter your first number: "))

  print("\nPlease choose from the following operations: ")
  for key in operations:
    print(key)

  while chain_calc=="yes":

    choice = input("\nPick an operation from the list above: ")
    num2 = float(input("\nEnter your next number: "))

    for operator in operations:
      if operator == choice:
        function = operations[operator]
        result = function(num1, num2)
        print(f"\n{num1} {operator} {num2} = {result}\n-> The answer is {result}")
  
    chain_calc = input("\nDo you want to continue with this current calculation?  ")
    if chain_calc=="yes":
      num1 = result
  ans = input("\nWould you like to continue?  ")
  if ans=="yes":
    chain_calc="yes"
