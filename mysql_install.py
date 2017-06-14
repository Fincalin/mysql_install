
from __future__ import print_function
import os
import fnmatch
import tarfile

'''
检测指定目录下是否有安装包没有需下载
有的话解压
'''


def unpackage_mysql(dir):
    mysql_package_gz = [name for name in os.listdir(dir) if fnmatch.fnmatch(name, 'mysql-5.6.*-linux-*-x86_64.tar.gz')][0]
    os.chdir(dir)
    if os.path.exists(mysql_package_gz):
        if os.path.exists('mysql-5.6.*-linux-glibc2.5-x86_64'):
            print('unpackage already exists,you can go next!')
        else:
            t = tarfile.open(mysql_package_gz, 'r:gz')
            t.extractall('.')
            print('unpackage done!')
    else:
        print('Please downloads mysql-5.6Version and move it to /usr/local')


def main():
    dir = '/usr/local'
    unpackage_mysql(dir)


if __name__ == '__main__':
    main()