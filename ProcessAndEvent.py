def speaker(env):
	yield env.timeout(30)
	return "handout"

def moderator(env):
	for i in range(3):
		val = yield env.process(speaker(env))
		print(val, env.now)

import simpy
env = simpy.Environment()
env.process(moderator(env))
env.run()
