from subprocess import Popen
import os

if __name__ == '__main__':
    Popen('python3 manage.py runserver', shell=True)
    os.system('python3 manage.py bot')