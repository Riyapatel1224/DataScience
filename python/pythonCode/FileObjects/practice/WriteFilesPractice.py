# with open('FileObjects/test2.txt','w') as f:
#     f.write('test') #  1st write operation

# with open('FileObjects/practice/test.txt','r') as rf: #  read mode file object is created
#     with open('FileObjects/practice/test_copy.txt','w') as  wf: #  write mode file object is created
#         for line in rf: 
#             wf.write(line) # copy text from test.txt to test_copy.txt


# with open('FileObjects/practice/image.jpg','rb') as rf:
#     with open('FileObjects/practice/image_copy.jpg','wb') as wf:
#         for line in rf:
#             wf.write(line)


with open('FileObjects/practice/image.jpg','rb') as rf:
    with open('FileObjects/practice/image_copy.jpg','wb') as wf:
        chunk_size=20000
        rf_chunk=rf.read(chunk_size)
        while chunk_size > 0:
            wf.write(rf_chunk)
            rf_chunk=rf.read(chunk_size)
            