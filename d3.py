# python_basics.py


def demonstrate_data_types_and_variables():
    print("=== Data Types and Variables ===")
    
    # Integers
    age = 30
    print(f"Age is {age}, type: {type(age)}")

    # Floats
    price = 19.99
    print(f"Price is {price}, type: {type(price)}")

    # Strings
    name = "Alice"
    print(f"Name is {name}, type: {type(name)}")

    # Booleans
    is_student = False
    print(f"is_student is {is_student}, type: {type(is_student)}")

    # Type casting
    age_str = str(age)
    print(f"Converted age to string: {age_str}, type: {type(age_str)}")

def demonstrate_operators():
    print("\n=== Operators ===")
    x = 10
    y = 3

    # Arithmetic
    print("x + y =", x + y)
    print("x - y =", x - y)
    print("x * y =", x * y)
    print("x / y =", x / y)
    print("x // y =", x // y)  # integer division
    print("x % y =", x % y)
    print("x ** y =", x ** y)

    # Comparison
    print("x == y?", x == y)
    print("x > y?", x > y)

    # Logical
    print("(x > 5) and (y < 5)?", (x > 5) and (y < 5))
    print("(x < 5) or (y < 5)?", (x < 5) or (y < 5))
    print("not (x == 10)?", not (x == 10))

def demonstrate_control_flow():
    print("\n=== Control Flow ===")
    num = 7

    # if-elif-else
    if num < 5:
        print(f"{num} is less than 5")
    elif num == 5:
        print(f"{num} is exactly 5")
    else:
        print(f"{num} is greater than 5")

    # for loops
    print("For loop from 0 to 2:")
    for i in range(3):
        print("i =", i)

    # while loop
    print("While loop counting down from 3:")
    count = 3
    while count > 0:
        print("count =", count)
        count -= 1

def demonstrate_data_structures():
    print("\n=== Data Structures ===")
    # Lists
    fruits = ["apple", "banana", "cherry"]
    print("Fruits list:", fruits)
    fruits.append("orange")
    print("After append:", fruits)

    # Tuples (immutable)
    colors = ("red", "green", "blue")
    print("Colors tuple:", colors)

    # Sets
    unique_numbers = {1, 2, 2, 3, 4}
    print("Set of unique numbers:", unique_numbers)

    # Dictionaries
    person = {"name": "Bob", "age": 25}
    print("Person dict:", person)
    person["job"] = "Engineer"
    print("Updated person dict:", person)

def demonstrate_functions():
    print("\n=== Functions ===")
    
    def greet(name):
        return f"Hello, {name}!"

    msg = greet("Charlie")
    print(msg)

def demonstrate_error_handling():
    print("\n=== Error Handling ===")
    try:
        result = 10 / 0
        print("Result is:", result)
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)

def main():
    demonstrate_data_types_and_variables()
    demonstrate_operators()
    demonstrate_control_flow()
    demonstrate_data_structures()
    demonstrate_functions()
    demonstrate_error_handling()

if __name__ == "__main__":
    main()
