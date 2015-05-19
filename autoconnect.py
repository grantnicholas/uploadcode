import os
import time
import subprocess
import multiprocessing
import os



def make_link(mac, comm):
    cmd = 'sudo rfcomm bind {0} {1}'.format(str(comm), str(mac))
    os.system(cmd)
    # cmd = ['sudo', 'rfcomm', 'connect', str(comm), str(mac)]
    # subprocess.Popen(cmd)

def cat(comm):
    filename = '/home/grant/Desktop/timesync/{0}.txt'.format(comm)
    while os.path.isfile(filename):
    	time.sleep(.01)
    	filename += 't'
    cmd = 'sudo cat /dev/{0} > {1}'.format(comm,filename)
    os.system(cmd)
    # cmd = ['sudo', 'cat', '/dev/{0} > /home/grant/Desktop/timesync/{0}.txt'.format(comm)]
    # subprocess.Popen(cmd)

class Device:
	def __init__(self, mac, comm):
		self.mac = mac 
		self.comm = comm 


def anon(adev):
	make_link(adev.mac, adev.comm)

def anon2(adev):
	cat(adev.comm)


def main():
    # devices = [Device("00:06:66:69:72:84", "rfcomm1")]
    devices = [Device("00:06:66:69:72:84", "rfcomm3"),
    Device("00:06:66:69:72:6F", "rfcomm0")]
    print devices


    # map(anon, devices)
    # map(lambda adev: adev.comm, devices)


    pool1 = multiprocessing.Pool(3)
    pool1.map(anon, devices)
    # pool1.close()
    time.sleep(5)

    print 'im here'
    pool2 = multiprocessing.Pool(3)
    pool2.map(anon2, devices)
    # pool2.close()


if __name__ == '__main__':
    main()
