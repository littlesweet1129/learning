# Write a Python program which accepts a sequence of 
# comma-separated numbers from user and generate a list and a 
# tuple with those numbers

class NumberSequence():
    def __init__(self, string):
        self.string = string
        self.split_string = self.string.split(',')

    def to_list(self):
        print(self.split_string)
    
    def to_tuple(self):
        print(tuple(self.split_string))

string = input('number of sequence: ')
number_sequence = NumberSequence(string)
number_sequence.to_list()
number_sequence.to_tuple()

