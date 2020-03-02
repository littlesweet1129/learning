# Write a Python program that accepts an integer (n) and
# computes the value of n+nn+nnn

class Computer():
    def __init__(self, n):
        self.n = n

    def get_n_nn_nnn(self):
        print(self.n+10*self.n+self.n+100*self.n+10*self.n+self.n)

number = int(input('input: '))
computer = Computer(number)
computer.get_n_nn_nnn()