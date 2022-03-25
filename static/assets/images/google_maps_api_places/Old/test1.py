import pexpect

img_link = pexpect.spawn('script - Copy.py')
img_link.expect("file name + extention:")
img_link.sendline('Alice.jpg')