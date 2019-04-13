import  os

def list_dir():
    cur_dir = os.getcwd()
    dirs = [i for i in os.listdir(cur_dir) if os.path.isdir(os.path.join(cur_dir, i))]
    for dir in dirs:
        print(dir)


def list_all():
    cur_dir = os.getcwd()
    dirs = [i for i in os.listdir(cur_dir)]
    for dir in dirs:
        print(dir)