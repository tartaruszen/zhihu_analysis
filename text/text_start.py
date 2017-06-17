import os

if __name__ == '__main__':
	os.popen('python text_web.py')
	print 'text_web start!'
	os.popen('python text_worker.py')
	print 'text_worker start!'