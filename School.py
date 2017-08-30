class School:
	def __init__(self,env):
		self.env = env
		self.class_ends = env.event()
		self.bell_proc = env.process(self.bell())
		self.pupil_procs = [env.process(self.pupil()) for i in range(1)]


		#self.bell_proc = env.process(self.bell())
	
	def bell(self):
		for i in range(2):
			yield self.env.timeout(45)
			self.class_ends.succeed()
			print("Succeed at %s" % self.env.now, end='')
			self.class_ends = self.env.event()
			print("New at %s" % self.env.now)

	def pupil(self):
		for i in range(2):
			print("  \O/ Pupli Now1 at %s" % self.env.now,end='')
			yield self.class_ends
			#print("  \O/ Pupli Now2 at %s" % self.env.now,end='')

import simpy
env = simpy.Environment()
school = School(env)
env.run()

