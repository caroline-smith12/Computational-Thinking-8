###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("summer")

q1 = codesters.Square(100,100,200, 'orange')
q2 = codesters.Square(-100,100,200, 'hot pink')
q3 = codesters.Square(-100,-100,200, 'pink')
q4 = codesters.Square(100,-100,200, 'white')

s1 = codesters.Sprite("cardinal", 100,100)
s1.set_size(0.8)
s2 = codesters.Sprite("lacrosse", -100, -100)
s2.set_size(0.3)
s3 = codesters.Sprite("skiing", 100, -100)
s3.set_size(0.1)
s4 = codesters.Sprite("cutefood", -100,100)
s4.set_size(0.5)

message1 = codesters.Text("Caroline Smith",0,220,"black")
message2 = codesters.Text("I love Fwankie",0,-220,"black")