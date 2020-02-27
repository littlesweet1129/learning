# Write a Python program which accepts the user's first and last name 
# and print them in reverse order with a space between them
class FullName():
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def print_reverse_name(self):
        print(self.last, ' ', self.first)

first = input('first name:')
last = input('last name:')
fullname = FullName(first, last)
fullname.print_reverse_name()
