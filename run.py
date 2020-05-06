# -*- coding: utf8 -*-
import subprocess

print('1) windows')
print('2) linux')
print('\n')

input_text = str(input())
if input_text == '1':
    mac = subprocess.check_output(["iwconfig"])

    f = open("linux_mac.txt", "w")
    f.write(str(mac))
    f.close()
if input_text == '2':
    mac = subprocess.run('ipconfig', stdout=subprocess.PIPE).stdout 

    f = open("windows_mac.txt", "w")
    f.write(str(mac))
    f.close()
else:
    print('error')
    
