import shutil
import os
import sys


def copy_file():
    file_in = str(sys.argv).split('\'')[1]
    args = file_in.split('.')
    if len(args) == 2:
        file_out = args[0] + '_copy.' + args[1]
    else:
        file_out = args[0] + '_copy'
    if os.path.exists(file_in) & (not os.path.exists(file_out)):
        shutil.copy(file_in, file_out)


if __name__ == '__main__':
    copy_file()
