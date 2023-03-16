

def main():
    with open("Sales Report.csv") as handler:  
        data = handler.read()
        print(data)
        #TODO DATA IS BEING READ


if __name__ == '__main__':
    main()