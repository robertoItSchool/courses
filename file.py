# f_write = open('workfile', 'a')
# f_write.write('4th line\n')
# f_write.close()

f_read = open('roberto.judet@itschool.ro')
s = f_read.read()
f_read.close()

print(s)
s = s.split('\n')
for line in s:
  print(line.split(','))

