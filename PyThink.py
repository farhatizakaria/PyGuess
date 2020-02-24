import random as rand

def pythink():
        Count = 0
        computerNum = rand.randint(1,10)
        
    
        while True:
            GuessNum = int(input("Write an integer number between 1 and 10 "))
            if type(GuessNum) is int and GuessNum is not 1 and GuessNum is not 10:
                
                
                if computerNum == GuessNum:
                    print("You got it!")
                    print(computerNum)
                    print("Number of count ",Count)
                    break
                else:
                    print("Nope!")
                    Count += 1
                    continue
            else:
                print("Guess num error/type")
        

def main():
    
    pythink()

if __name__ == '__main__':
    main()
