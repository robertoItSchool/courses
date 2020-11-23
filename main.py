list_users = ['roberto', 'roberto', 'roberto']
list_websites = ['amazon', 'netflix', 'spotify']
list_passwords = ['123456', 'abcdefg', 'a12abeee']

dict = {
  'amazon': {'user': 'roberto', 'password': '123456'},
  'netflix': {'user': 'roberto', 'password': 'abcdefg'},
  'spotify': {'user': 'roberto', 'password': 'a12abeee'}
}


def get_user_and_password(website_name):
  try:
    user = dict[website_name]['user']
    password = dict[website_name]['password']
    return user, password
  # if an exception of type KeyError occurs, execute the code in except
  except KeyError:
    return '', ''



for website in list_websites:
  print(get_user_and_password(website))
