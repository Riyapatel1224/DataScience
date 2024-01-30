# f = open('/Users/riya/Documents/DataScience/python/pythonCode/FileObjects/test.txt', 'r') 
# print(f.name) # name of the file
# print(f.mode) #  mode in which file is opened
# f.close()    # close the file


# automatically close the file for you and create a variable at the end 
with open('FileObjects/test.txt', 'r') as f:
    f_contents=f.read() #  read all contents of the file
    print(f_contents) #  display content of the file
    
    f1_contents= f.readlines() #  read lines of the file
    print(f1_contents) #  display each line of the file
    
    f2_contents = f.readline() #  read one line from the file
    print(f2_contents)         #  display one line of the file
    
    for line in f:    # loop through each line of the file
        print(line,end='')    #  iterate over each line of the file
    
    f3_contents=f.read(100) #  read first 100 characters of the file
    print(f3_contents) #   display only first 100 characters of the file
    
    size_to_read = 10 #  number of bytes to be read
    f4_contents = f.read(size_to_read) 
    print(f.tell()) #  tell method returns current position of the pointer
    while len(f4_contents) > 0: #  check if there are any data left or not
        print(f4_contents, end='') 
        f4_contents = f.read(size_to_read) # to update the data  in f4_content with new chunk of data
    
    
    size_to_read = 10
    f5_contents = f.read(size_to_read)
    print(f5_contents, end='')
    
    f.seek(0) # set position back to the beggining  of the file
    
    f5_contents = f.read(size_to_read)
    print(f5_contents, end='')
    