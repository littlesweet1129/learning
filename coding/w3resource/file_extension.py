# Write a Python program to accept a filename from the user 
# and print the extension of that

class File():
    def __init__(self, filename):
        self.filename = filename
    
    def get_extension(self):
        print(self.filename.split('.')[-1])

filename = input('filename: ')
onefile = File(filename)
onefile.get_extension()

