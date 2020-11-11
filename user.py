import os

class User:
  # constructor of class, receives its username
  def __init__(self, username):
    self.username = username
    self.file_path = 'user_' + self.username # we generate the file path here

  def save(self):
    try:
      # try to open file, will succeed if it already exists
      file = open(self.file_path)
      file.close()
      return 'User already exists' # return the message so we can check it
    except FileNotFoundError:
      # if the file does not exists and we can't open it we create it
      file = open(self.file_path, 'w')
      file.close()
      return 'User added' # return the message so we can check it

  def remove(self):
    try:
      os.remove(self.file_path) # try to remove the file with name user_...
      print('Removed user')
      return True
    except:
      print('User does not exist')
      return False

  def rename(self, new_username):
    success = self.remove() # delete the current file
    if not success:
      return
    self.username = new_username
    self.file_path = 'user_' + self.username # change the file path variable
    self.save() # save the new file
