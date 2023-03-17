import sys
import time
context = {}
SeriesOfInputs = []



def main():
    userInput = input("Please Follow the Instructions Given (y) to continue (q) to break: ")
    if userInput == 'y':
        products()
    else:
        RageQuit()
        
        
def products():
    productsInfo = input('These are the available products that we have.. kindly provide us with your needs: ')
    


def RageQuit():
    print('Data has been saved')
    time.sleep(1)
    print('exiting in')
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    sys.exit()



while True:
    main()
