
def main():
    for i in range(20):
        if(i % 2 == 1):
            print("Hello" + str(i))

class myObj:
    def __init__(self, value = 200):
        self.val = value
        print(self.val)


main()
test = myObj()
test2 = myObj(100)
