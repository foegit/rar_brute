import random
import time
from threading import Thread
import brute
import rarfile

class CheckThread(Thread):
    find = False
    def __init__(self, id, rar, passwords):
        Thread.__init__(self)
        self.passwords = passwords
        self.rar = rar
        self.id = id
        self.finding = False

    def run(self):
      start_time = time.time()
      print('Thread #{}: start'.format(self.id))
      n = len(self.passwords)
      right_pwd = None
      for (i, password) in enumerate(self.passwords):
        if CheckThread.find:
          break
        time_per_iter = (time.time() - start_time) / (i + 1)
        time_left = (n - i) * time_per_iter
        print("Thread #{}: ({}/{}) time left {:06.2f}s, speed {:0.2f} || {}".format(self.id,
          i, n, time_left, time_per_iter, password))
        try:
          self.rar.extractall(pwd=password)
          print("\n[!] Find password: {}\n".format( password))
          CheckThread.find = True
          right_pwd = password
        except:
          pass
      end_time = time.time()
      print('Thread #{}: Stop. Work time: {:0.2f}'.format(self.id, end_time - start_time), 'ms')
      return right_pwd


def chunkify(lst, n):
  return [lst[i::n] for i in range(n)]


def create_threads(passwords, thread_num, rar_filename):
  chunck = chunkify(passwords, thread_num)
  for i in range(thread_num):
    rar = rarfile.RarFile(rar_filename)
    my_thread = CheckThread(id = i, passwords = chunck[i], rar = rar)
    my_thread.start()


rarfile.UNRAR_TOOL = 'C:\\Program Files (x86)\\WinRAR\\unrar'

prf = rarfile.RarFile('ok.rar')

# prf.extractall(pwd='ok')

def generate_pass_file(filename, start_length, lenght):
  passwords = list(brute.brute(
    start_length=start_length, symbols=False, length=lenght, spaces=False))

  f = open(filename, 'a+')
  for i in passwords:
    f.write(i + '\n')


filename = 'db_pwd.txt'
# generate_pass_file(filename, start_length=3, lenght=4)

f = open(filename, 'r+')
passwords = f.read().split('\n')
create_threads(passwords, 4, "Variant07_1.rar")

