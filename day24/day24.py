#filesystem
'''
file = open('my_file.txt')
contents = file.read()
print(contents)
file.close()
'''

# #no need to close
# with open('my_file.txt') as file:
#     contents = file.read()
#     print(contents)

#overwrite what is in the file.
with open('my_file.txt', mode='w') as file:
   file.write('Spatulas are amazing')

#append to the file.  If the file doesn't exist, it will be created from scratch
with open('my_file.txt', mode='a') as file:
   file.write('\nI have a Hopsy and a Barley!')

with open('new_file.txt', mode='w') as file:
    file.write('new text')   
   

