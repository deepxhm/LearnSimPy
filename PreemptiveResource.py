
import simpy

def resource_user(name, env, resource, wait, prio): 
	yield env.timeout(wait) 
	with resource.request(priority=prio) as req: 
		print('%s requesting at %s with priority=%s' % (name, env.now, prio)) 
		yield req 
		print('%s got resource at %s' % (name, env.now)) 
		try: 
			yield env.timeout(3) 
		except simpy.Interrupt as interrupt: 
			by = interrupt.cause.by 
			usage = env.now - interrupt.cause.usage_since 
			print('%s got preempted by %s at %s after %s' % (name, by, env.now, usage)) 

env = simpy.Environment() 
res = simpy.PreemptiveResource(env, capacity=1) 
p1 = env.process(resource_user(1, env, res, wait=0, prio=0)) 
p2 = env.process(resource_user(2, env, res, wait=1, prio=0)) 
p3 = env.process(resource_user(3, env, res, wait=2, prio=-1)) 
env.run() 
"""
Result:

1 requesting at 0 with priority=0 
1 got resource at 0 
2 requesting at 1 with priority=0 
3 requesting at 2 with priority=‐1 
1 got preempted by <Process(resource_user) object at 0x...> at 2 after 2 
3 got resource at 2 
2 got resource at 5 

"""
