from email import EmailUser

user1 = EmailUser("roberto.judet@itschool.ro", "Roberto Judet")
print(user1.get_username())
print(user1.get_emails())

i = 3
while i < 6:
  user1.add_email('s' + str(i), 'm ' + str(i))
  i += 1
  print(user1.get_emails())

