def speaker(env):
	try:
		yield env.timeout(random.randint(25,35))
	except simpy.Interrupt as interrupt:
		print(interrupt.cause,env.now)

def moderator(env):
	for i in range(3):
		speaker_proc = env.process(speaker(env))
		yield env.timeout(30)
		if not speaker_proc.triggered:
			speaker_proc.interrupt("No time left")


import simpy
import random
env = simpy.Environment()
env.process(moderator(env))
env.run()
