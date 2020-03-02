# Write a Python program to display the first 
# and last colors from the following list

class Colors():
    def __init__(self, colors):
        self.colors = colors

    def get_first_last(self):
        print('first color: ', self.colors[0])
        print('last color: ', self.colors[-1])

colors = input('list of colors: ').split(',')
col = Colors(colors)
col.get_first_last()