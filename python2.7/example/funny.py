
from turtle import Turtle
import time
start =time.clock()

t=Turtle()
t.setpos(-200,0)
for i in range(36):
	t.forward(400)
	t.right(170)

end=time.clock()
print "Running duration: %f s" % (end-start)
raw_input('Input:')