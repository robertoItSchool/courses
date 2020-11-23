list_users = ['roberto', 'roberto', 'roberto']
list_websites = ['amazon', 'netflix', 'spotify']
list_passwords = ['123456', 'abcdefg', 'a12abeee']

dict = {
  'amazon': {'user': 'roberto', 'password': '123456'},
  'netflix': {'user': 'roberto', 'password': 'abcdefg'},
  'spotify': {'user': 'roberto', 'password': 'a12abeee'}
}


def get_user_and_password(website_name):
  i = 0
  for website in list_websites:
    if website_name == website:
      return list_users[i], list_passwords[i]
    i += 1


for website in list_websites:
  print(get_user_and_password(website))
