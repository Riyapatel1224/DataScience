def findArea(name,width,height):
    if (name=="triangle"):
        area=0.5*width*height
        print(area)
    elif (name=="rectangle"):
        area=width*height
        print(area)
    else:
        print("INVALID CHOICE")
    
name= input("Enter shape: ")
width=int(input("Enter width: "))
height=int(input("Enter height: "))
ans = findArea(name,width,height)
