import os
import subprocess
from text_config import get_config
config = get_config()

if __name__ == '__main__':
	print 'start text!'
	procs = []
	proc_web = subprocess.Popen(['python','text_web.py'],stdout=subprocess.PIPE)
	procs.append(proc_web)
	proc_worker = subprocess.Popen(['python','text_worker.py'],stdout=subprocess.PIPE)
	procs.append(proc_worker)
	for proc in procs:
		proc.communicate()