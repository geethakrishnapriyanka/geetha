while True:
    a = input("Enter Something: ")
    print(a)
    f=open("p.txt","a")
    f.write(a+'\n')
    f.close()

    f=open("p.txt","r")
    print("============== p.txt ========================")
    print(f.read())
    print("======================================")

    f.close()

    
