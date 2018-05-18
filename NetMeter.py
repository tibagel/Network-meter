import os
import psutil
import time

net = psutil.net_io_counters(pernic=True)['wlp3s0']
Ib_sent = net.bytes_sent
Ib_received = net.bytes_recv


def GetHumanReadable(size,precision=2):
    suffixes=['B','KB','MB','GB','TB']
    suffixIndex = 0
    while size > 1024 and suffixIndex < 4:
        suffixIndex += 1 #increment the index of the suffix
        size = size/1024.0 #apply the division
    return "%.*f%s"%(precision,size,suffixes[suffixIndex])

while True:
	net = psutil.net_io_counters(pernic=True)['wlp3s0']
	sent = net.bytes_sent - Ib_sent
	received = net.bytes_recv - Ib_received
	print(GetHumanReadable(sent) + '/s')
	print(GetHumanReadable(received) + '/s')
	Ib_sent += sent
	Ib_received += received
	time.sleep(1)
	os.system('clear')
