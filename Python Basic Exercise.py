#Exercise No 1. Simple variable Assignment
name="Farah"
age=19
print(f"{name} age is {age}")
#Exercise 2. Multiple variable assigment.
num1=23
num2=34
result=num1+num2
print(f"{num1}+{num2}={result}")
#Exercise 3. Variable Types
price=120.7
quantity=4
total_cost=price*quantity
print(f"Price={price}")
print(f"Quantity={quantity}")
print(f"Total Cost={total_cost}")
#Exercise No 4. String Concatenation
first_name="Farah"
last_name="Maqbool"
full_name=first_name+" "+last_name
print(f"{full_name}")
#Exercise No 5. Boolean variable
is_adult=19
print(is_adult==18)
#Exercise No 6. Interactive user input.
user_input=input("Enter your Name: ")
print(f"Thanks for Enrolling {user_input}")
#Exercise No 7. Temerature Conversion.
Celsius_Temperature=45
Fahrenheit_Temperature=(Celsius_Temperature* 9/5)+32
print(f"In Celsius Temperature={Celsius_Temperature} and in Fahrenheit temperature={Fahrenheit_Temperature}")
#Exercise No 8. Swapping Variables
a=23
b=34
a,b=b,a
print("The value of A is 23 but after swaping the value of A is",a)
print("The value of B is 34 but after swapping the value of B is",b)
#Exercise No 9. Calculator
user_num1=int(input("Enter Number: ")) 
user_num2=int(input("Enter Number: "))
user_operator=input("Enter Operator (+,-,/,*): ")
if user_operator=="+":
    print(f"{user_num1}+{user_num2}={user_num1+user_num2}")
elif user_operator=="-":
    print(f"{user_num1}-{user_num2}={user_num1-user_num2}")    
elif user_operator=="*":
    print(f"{user_num1}X{user_num2}={user_num1*user_num2}")   
elif user_operator=="/":
    print(f"{user_num1}/{user_num2}={user_num1/user_num2}")
else:
    print("Invalid Condition")         