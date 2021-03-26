with open("C:/Users/ITPS/Desktop/test.txt", "r") as test :
    with open("C:/Users/ITPS/Desktop/copy.txt", "w") as copy :
        while True :
            test1 = test.readline()

            if test1 == '' :
                break
            else:
                copy.write(test1)