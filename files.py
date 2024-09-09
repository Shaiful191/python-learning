# open a file if file not exit it created one
myfile = open('myfile.txt', 'w')  

#get some info
print('Name: ',myfile.name)

# write to file
myfile.write("I love python")
myfile.write(" and JavaScript.")
myfile.close()

# Append to file
myfile = open('myfile.txt','a')
myfile.write(' I also like PHP.')
myfile.close()

# Read from file
myfile = open('myfile.txt','r')
text= myfile.read(100)
print(text)
