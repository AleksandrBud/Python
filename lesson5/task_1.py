import os

def create_dir():
    for i in range(1, 10):
        os.mkdir(os.getcwd()+"/dir_"+str(i))

def rem_dir():
    for i in range(1, 10):
        path = os.getcwd()+"/dir_"+str(i)
        if os.path.exists(path):
            os.rmdir(path)

def rem_dir(i_dir):
    if os.path.exists(i_dir):
        os.rmdir(i_dir)
    else:
        print('Папка не существует')

