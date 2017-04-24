#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##!/usr/bin/Python是告诉操作系统执行这个脚本的时候，调用/usr/bin下的python解释器
##!/usr/bin/env python这种用法是为了防止操作系统用户没有将python装在默认的/usr/bin路径里。当系统看到这一行的时候，首先会到env设置里查找python的安装路径，再调用对应路径下的解释器程序完成操作。
# add env para computer will find python env in environment

r'''
learning.py

A Python 3 tutorial from http://www.liaoxuefeng.com

Usage:

python3 learning.py
'''
#r''' remark?
#means normal string use as \
#so ''' means multi-line comment

import sys
#导入sys库  没有from？ 之前是from sys import argv
#from os.path import exists 

def check_version():
    v = sys.version_info
    if v.major == 3 and v.minor >= 4:
        return True
    print('Your current python is %d.%d. Please use Python 3.4.' % (v.major, v.minor))
    return False

# 要求python版本大于3.4  用sys.version_info来查啊  major minor
# 看他用的if 没有用else哦！！因为如果if满足条件就returnTrue了

if not check_version():
    exit(1)
# if version ok return Turn, not ture ==false, if false exit
# what about 1?

import os, io, json, subprocess, tempfile
from urllib import parse
from wsgiref.simple_server import make_server

# 看看用了哪些module  json是什么？javascript object notation
# 分支进程，临时文件 io os
# urllib 链接
# make_server 提供服务，但不知道 wsgiref是什么。。。 太多不懂了
#wsgi_ref  wsgi pep333.. as ruter spec package contents simple_server
# 看起来import from   和from import可以颠倒啊
#查了下pydoc  
'''
there are 2 steps in import
1\ find module and initialize
2\ define a name in workspace.

so  in two forms ,whether it uses the "from".
if exist from
import package's expecify  module
'''

EXEC = sys.executable
PORT = 39093
HOST = 'local.liaoxuefeng.com:%d' % PORT
TEMP = tempfile.mkdtemp(suffix='_py', prefix='learn_python_')
INDEX = 0

#big char define  all script could use

def main():
    httpd = make_server('127.0.0.1', PORT, application)
    print('Ready for Python code on port %d...' % PORT)
    httpd.serve_forever()

#make_server  use wsgiref  provide server

def get_name():
    global INDEX
    INDEX = INDEX + 1
    return 'test_%d' % INDEX

def write_py(name, code):
    fpath = os.path.join(TEMP, '%s.py' % name)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(code)
    print('Code wrote to: %s' % fpath)
    return fpath

# create a box for write code
#TEMP suffix prefix defined!
# fapth  create a .py under the path
# then open the .py file  with write authority

def decode(s):
    try:
        return s.decode('utf-8')
    except UnicodeDecodeError:
        return s.decode('gbk')

def application(environ, start_response):
    host = environ.get('HTTP_HOST')
    method = environ.get('REQUEST_METHOD')
    path = environ.get('PATH_INFO')
    if method == 'GET' and path == '/':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'<html><head><title>Learning Python</title></head><body><form method="post" action="/run"><textarea name="code" style="width:90%;height: 600px"></textarea><p><button type="submit">Run</button></p></form></body></html>']
    if method == 'GET' and path == '/env':
        start_response('200 OK', [('Content-Type', 'text/html')])
        L = [b'<html><head><title>ENV</title></head><body>']
        for k, v in environ.items():
            p = '<p>%s = %s' % (k, str(v))
            L.append(p.encode('utf-8'))
        L.append(b'</html>')
        return L
    if host != HOST or method != 'POST' or path != '/run' or not environ.get('CONTENT_TYPE', '').lower().startswith('application/x-www-form-urlencoded'):
        start_response('400 Bad Request', [('Content-Type', 'application/json')])
        return [b'{"error":"bad_request"}']
    s = environ['wsgi.input'].read(int(environ['CONTENT_LENGTH']))
    qs = parse.parse_qs(s.decode('utf-8'))
    if not 'code' in qs:
        start_response('400 Bad Request', [('Content-Type', 'application/json')])
        return [b'{"error":"invalid_params"}']
    name = qs['name'][0] if 'name' in qs else get_name()
    code = qs['code'][0]
    headers = [('Content-Type', 'application/json')]
    origin = environ.get('HTTP_ORIGIN', '')
    if origin.find('.liaoxuefeng.com') == -1:
        start_response('400 Bad Request', [('Content-Type', 'application/json')])
        return [b'{"error":"invalid_origin"}']
    headers.append(('Access-Control-Allow-Origin', origin))
    start_response('200 OK', headers)
    r = dict()
    try:
        fpath = write_py(name, code)
        print('Execute: %s %s' % (EXEC, fpath))
        r['output'] = decode(subprocess.check_output([EXEC, fpath], stderr=subprocess.STDOUT, timeout=5))
    except subprocess.CalledProcessError as e:
        r = dict(error='Exception', output=decode(e.output))
    except subprocess.TimeoutExpired as e:
        r = dict(error='Timeout', output='执行超时')
    except subprocess.CalledProcessError as e:
        r = dict(error='Error', output='执行错误')
    print('Execute done.')
    return [json.dumps(r).encode('utf-8')]

if __name__ == '__main__':
    main()
