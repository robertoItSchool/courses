class Credentials:
  # we need to give an user & password
  def __init__(self, user, password):
    # save the variables to the object
    self.user = user
    self.password = password


# extent Credentials
class EmptyCredentials(Credentials):
  def __init__(self):
    # call the parent (Credentials) constructor
    super().__init__('', None)


dict = {
  'amazon': Credentials('roberto', '123456'),
  'netflix': Credentials('roberto', 'abcdefg'),
  'spotify': Credentials('roberto', 'ab12eeee')
}


def get_user_and_password(website_name):
  try:
    return dict[website_name]
  # if an exception of type KeyError occurs, execute the code in except
  except KeyError:
    return EmptyCredentials()


if __name__ == '__main__':
  new = Credentials('value1', 'value2')
  print(new.__dict__)

