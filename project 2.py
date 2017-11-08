from visual import *
import random
print "J and K slow down or speed up the electron. N and M change the strength (and direction) of the magnetic field. L fires the electron. X ends the game. an outward magnetic field (toward you) is red and an inward magnetic field is blue. Hit the Goal for maximum fun times!"
# The list of all particles
particles=[]
# The timestep length (might need to be adjusted)
dt=0.01
field=0;
speed=25;
# ================== Some useful functions
#
# The following function makes a particle
# at the given position and with the given
# velocity
#
def makeparticle(position,velocity):
# Adjust radius and color the way you like 
    newparticle=sphere(pos=position,radius=0.3,color=color.red)
    newparticle.velocity=vector(velocity)
    particles.append(newparticle)

#
# The following removes the particle in the argument
#
def destroyparticle(thisparticle):
    particles.remove(thisparticle)
    thisparticle.visible=false
    del thisparticle

# =========================================
#
# The following can be modified to handle your
# keys. You to call it inside your time loop
#
import random
global field;

charge1=sphere(pos=(0,-5),radius=0.5,charge=(0,0,field))


def listenkeys():
    global field;
    global speed;
    if scene.kb.keys:
        s=scene.kb.getkey()
# This is where you have to add all your keys
# In this demo, "q" lifts the launcher, 'a' lowers it
# j and k change the speed of the particle
        if (s=='j'):
            speed+=-1;
            print(speed)
            print("electron speed updated")
            print(speed)

        if (s=='k'):
            speed+=1;
            print("electron speed updated")
            print(speed)
#N decreasaes the field strength by 1 and M increases the field strengh by 1
        if (s=='n'):
             field+=-0.25;
             charge1.charge=field
             print("magnetic field value updated")
             print(field)
             
             
        if (s=='m'):
            field+=0.25;
            charge1.charge=field
            print("magnetic field value updated")
            print(field)
            
        if charge1.charge > 0 :
            charge1.color=color.red
        if charge1.charge < 0:
            charge1.color=color.blue
        if charge1.charge is 0 :
            charge1.color=color.white

# 'l' launches a particle
        if (s=='l'):
            makeparticle((-5,launchdevice.pos.y,0),(speed,0,0))

# 'x' quits
        if (s=='x'):
            exit()
            
#  =========================================


#
crashwall=box(pos=(5,0,0), size=(0.2,8,1), color=color.green)
launchdevice=box(pos=(-6,0,0), size=(2,0.4,0.4), color=color.magenta)

scene.autoscale = False

#
# Move them
#
while 1:
    global field;
    # Synchronized
    rate(100)
    # Catch keystrokes
    listenkeys()
    # Loop over all existing particles
    for thisparticle in particles:
        # The acceleration
        acc=vector(0,0,0)
        # Sum up all accelerations on the particle

        acc+=cross(-thisparticle.velocity,(0,0,field))

        # dv=a*dt
        thisparticle.velocity+=acc*dt
        # dx=v*dt
        thisparticle.pos+=thisparticle.velocity*dt
        # =====
        # Now destroy particles, if needed
        if thisparticle.pos.x > 5:
            destroyparticle(thisparticle)
        if thisparticle.pos.x < -7 :
            destroyparticle(thisparticle)
        if (thisparticle.pos.x > 5) and (-4<thisparticle.pos.y<4) :
            print "You're TV!"


