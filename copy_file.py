#encoding:utf-8
import os 
import time   
import threading
source_dir = 'olavoice'
target_dir = 'olavoice_bat'
count = 0
def copy_file(source_dir, target_dir):
	print source_dir
	for f in os.listdir(source_dir):
		source = os.path.join(source_dir, f)
		target = os.path.join(target_dir, f)
		#是文件
		if os.path.isfile(source):
			if not os.path.exists(target_dir):
				os.makedirs(target_dir)
			open(target, "wb").write(open(source, "rb").read()) 
		#是目录	
		elif os.path.isdir(source):
			copy_file(source, target)

def getdirsize(dir):
    size = 0L
    for root, dirs, files in os.walk(dir):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size
    
#定时器，每隔6小时跑一次，文件夹大小不一致就拷贝
def timer():


	global count
	print getdirsize(source_dir) 
	print getdirsize(target_dir)
	if (getdirsize(source_dir) != getdirsize(target_dir)) or (not os.path.exists(target_dir)):
		copy_file(source_dir, target_dir)
		print count
		count += 1

	gap = 3600 * 1
	t = threading.Timer(gap, timer)
	t.start() 

if __name__ == '__main__':
	timer()