import simpy

env  = simpy.Environment()
res  = simpy.Resource(env, capacity=1) 

def print_stats(res,processId): 
	print('%d of %d slots are allocated. log by processId: %d' % (res.count, res.capacity,processId)) 
	print('  Users: %s log by processId: %d' %(res.users,processId)) 
	print('  Queued events: %s log by processId: %d' % (res.queue,processId)) 

def user(res,processId): 
	print_stats(res,processId) 
	with res.request() as req: 
		yield req 
		print_stats(res,processId) 
	print_stats(res,processId) 


procs = [env.process(user(res,i)) for i in range(2)] 
env.run()

"""
Result:

0 of 1 slots are allocated. log by processId: 0
  Users: [] log by processId: 0
  Queued events: [] log by processId: 0
1 of 1 slots are allocated. log by processId: 1
  Users: [<Request() object at 0x7f720f7c0b70>] log by processId: 1
  Queued events: [] log by processId: 1
1 of 1 slots are allocated. log by processId: 0
  Users: [<Request() object at 0x7f720f7c0b70>] log by processId: 0
  Queued events: [<Request() object at 0x7f720f7c0b38>] log by processId: 0
0 of 1 slots are allocated. log by processId: 0
  Users: [] log by processId: 0
  Queued events: [<Request() object at 0x7f720f7c0b38>] log by processId: 0
1 of 1 slots are allocated. log by processId: 1
  Users: [<Request() object at 0x7f720f7c0b38>] log by processId: 1
  Queued events: [] log by processId: 1
0 of 1 slots are allocated. log by processId: 1
  Users: [] log by processId: 1
  Queued events: [] log by processId: 1

"""
 
