user_input = input("Enter a list of integers separated by spaces: ")

numbers = [int(num) for num in user_input.split()]

processed = ['over' if num > 100 else num for num in numbers]

print("Processed list:")
print(processed)
