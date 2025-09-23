names = input("Enter first names separated by spaces: ")

name_list = names.split()

a_count = 0

for name in name_list:
    a_count += name.lower().count('a')  

print(f"Total occurrences of 'a': {a_count}")
