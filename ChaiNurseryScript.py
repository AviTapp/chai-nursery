print "Child's first name:"
f_name = raw_input()
print "last name:"
l_name = raw_input()
print "Date of birth:"
dob = raw_input()
print f_name, l_name, dob
bio = " ".join([l_name, f_name, dob])
print bio
bio = bio + " \n"
info = open('info.txt', 'w')
info.write(bio)
info.close()

print "Is there a child you would like to add to the list?"
run = 