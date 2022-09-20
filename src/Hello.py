# print("Dead By Daylight")

# TRUE = 1  #할당 연산지

# if TRUE:
#     print ("나는")
#     print ("바보입니다.")

# else:
#     print ("그런데")
#     print ("바보와 천재는 종이 한 장 차이 입니다.")


# import sys

# file_name = input("Enter filename: ")
# file_finish = input("Enter text: ")

# if len(file_name) == 0:
#     print("Next time please enter something")
#     sys.exit()

# try:
#     file = open(file_name, "w")

# except IOError:
#     print("there was an error writing to", file_name)
#     sys.exit()

# print("Enter'", file_finish,)
# print ("When finished")

# while file_text != file_finish:
#     file_text = input("Enter text: ")
#     if file_text == file_finish:
#         #close th file
#             file.close
#             break
#     file.write(file_text)
#     file.write("\n")
#     file.close()


# try:
#     file =open(file_name, "r")

# except IOError:
#     print("There was an error reading file")
#     sys.exit()
# file_text = file.read()
# file.close()
# print (file_text)

# var1 = 1
# var2 = 20

#!/usr/bin/python3

# str = 'Hello World!'

# print (str)          # Prints complete string
# print (str[0])       # Prints first character of the string
# print (str[2:5])     # Prints characters starting from 3rd to 5th
# print (str[2:])      # Prints string starting from 3rd character
# print (str * 2)      # Prints string two times
# print (str + "TEST")


# list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
# tinylist = [123, 'john']

# print (list)
# print (list[0])      
# print (list[1:3])     
# print (list[2:])      
# print (tinylist * 2)  
# print (list + tinylist)

#!/usr/bin/python3

# tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
# tinytuple = (123, 'john')

# print (tuple)           
# print (tuple[0])        
# print (tuple[1:3])      
# print (tuple[2:])       
# print (tinytuple * 2)   
# print (tuple + tinytuple) 

#!/usr/bin/python3

# tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
# list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
# tuple[2] = 1000    
# list[2] = 1000     


dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dict['one'])       
print (dict[2])           
print (tinydict)          
print (tinydict.keys())   
print (tinydict.values()) 