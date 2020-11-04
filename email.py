class EmailUser:
  _email_list = []
  __max_number_of_emails = 10

  def __init__(self, username, full_name):
    self._username = username
    self._full_name = full_name
    try:
      f = open(self._username)
      f.close()
    except FileNotFoundError:
      self.__save()

  def get_username(self):
    return self._username

  def add_email(self, subject, message):
    self._email_list.append({"subject": subject, "message": message})
    self.__save_email(subject, message)
    self._delete_old_emails()

  def get_emails(self):
    f = open(self._username)
    return f.read()
    return self._email_list

  def _delete_old_emails(self):
    if len(self._email_list) > self.__max_number_of_emails:
      self._email_list = self._email_list[1:]

  def __save(self):
    f = open(self._username, 'w')
    f.write('username: ' + self._username + '\n')
    f.write('full_name: ' + self._full_name + '\n')

  def __save_email(self, subject, message):
    f = open(self._username, 'a')
    f.write('subject: ' + subject + ' , message: ' + message + '\n')
    f.close()


class PremiumEmailUser(EmailUser):
  def __init__(self, username, full_name):
    self._username = username
    self._full_name = full_name

  def _delete_old_emails(self):
    return
