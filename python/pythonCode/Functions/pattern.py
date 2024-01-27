def pattern(num):
    for i in range(0,num):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")

num=int(input("Enter the height you want for pyramid: "))
pattern(num)
