import rarfile
from string import ascii_letters, digits

def test4(rar, alphabet):
  n = len(alphabet)
  iteration = n

  for a in alphabet:
    for b in alphabet:
      for c in alphabet:
        for d in alphabet:
          psw = a+b+c+d
          print();
          try:
            rar.extractall(pwd=psw)
            print('Password found:' + psw)
            return psw
          except:
            print('sorry: ' + psw)

rarfile.UNRAR_TOOL = 'C:\\Program Files\\WinRAR\\unrar'

rf = rarfile.RarFile('arch.rar')
prf = rarfile.RarFile('Variant07_1.rar')
ipass = rarfile.RarFile('ipass.rar')

# ipass.setpassword('1111')
# ipass.extractall(pwd='1111')
# print('\r\n\x93\xaa\xa0\xa7\xa0\xad \xad\xa5\xa2\xa5\xe0\xad\xeb\xa9 \xaf\xa0\xe0\xae\xab\xec.')

alphabet = ascii_letters + digits
test4(prf, 4, alphabet)

# print(len(alphabet))

# print(ipass.needs_password())
# print(ipass.namelist())
# print(ipass.testrar())
# print(ipass.open('ipass', mode='r', psw='1111'))




# ipass.setpassword('1111')
# print(ipass.namelist)
