import sys
import subprocess
import random
import time
import threading
import Queue
 
class AsynchronousFileReader(threading.Thread):
 
    def __init__(self, fd, name):
        threading.Thread.__init__(self)
        self._fd = fd
	self._name = name 

    def run(self):
        for line in iter(self._fd.readline, ''):
            print self._name + " : "+line
  
def consume(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
 
    stdout_reader = AsynchronousFileReader(process.stdout, "stdout")
    stdout_reader.start()

    stderr_reader = AsynchronousFileReader(process.stderr, "stderr")
    stderr_reader.start()
 
    stdout_reader.join()
    stderr_reader.join()
 
    process.stdout.close()
    process.stderr.close()
 
def produce(items=10):
    for i in range(items):
        output = random.choice([sys.stdout, sys.stderr])
        output.write('Line %d on %s\n' % (i, output))
        output.flush()
        time.sleep(random.uniform(.1, 1))
 
if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'produce':
        produce(10)
    else:
        consume(['python', sys.argv[0], 'produce'])

