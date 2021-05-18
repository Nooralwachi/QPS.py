from datetime import datetime
from collections import defaultdict
def qps(filename):
	queries=defaultdict(int)
	with open(filename, 'r') as f:
		f.readline()
		for line in f:
			Time,Date,Server_ID,Query_ID= line.strip().split()
			# query_date=str(Time)+' '+str(Date)
			queries[Server_ID]+=1
		print(f'Server_ID QPS')
		for server in queries:
			print(f'{server}: {float(queries[server]/3):.1f}')

qps('server_log.txt')