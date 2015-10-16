#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Cody Kochmann
# @Date:   2015-10-16 10:06:16
# @Last Modified by:   codykochmann
# @Last Modified time: 2015-10-16 11:53:14

bashrc_file="~/.bashrc"
bash_aliases_file="~/.bash_aliases"

remote_alias_link="http://bit.ly/codys-aliases"

def append_to_file(filename,input_string):
  with open(filename, 'a') as f:
    f.write(input_string)

def grep(url):
  import os
  return(str(os.popen("wget -qO- %s" % (url)).read()))

def bash(text_to_run):
  import os
  os.system(text_to_run)

remote_bash_aliases_text=grep(remote_alias_link)

append_to_file(bash_aliases_file, remote_bash_aliases_text)

to_append_to_bashrc="""
# automatically loads the bash aliases from ~/.bash_aliases
bash %s
""" % (bash_aliases_file)

append_to_file(bashrc_file, to_append_to_bashrc)

bash("bash %s"%(bash_aliases_file))
bash("alias -p")
print("""
      All aliases have been loaded.
      """)
