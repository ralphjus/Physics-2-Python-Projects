from visual import *
import random
print "Q and A move the positive charge left and right. L releases the positive charge. Negative charges are red and positive charges are blue."
# The list of all particles
particles=[]
# The timestep length (might need to be adjusted)
dt=0.01
# ================== Some useful functions
#
# The following function makes a particle
# at the given position and with the given
# velocity
#
def makeparticle(position,velocity):
# Adjust radius and color the way you like 
    newparticle=sphere(pos=position,radius=0.25,color=color.blue)
    newparticle.velocity=vector(velocity)
    particles.append(newparticle)

#
# The following removes the particle in the argument

# =========================================
#
# The following can be modified to handle your
# keys. You to call it inside your time loop
#
def listenkeys():
    global speed;
    if scene.kb.keys and launchdevice.visible is true:
        s=scene.kb.getkey()
# This is where you have to add all your keys
# In this demo, "q" lifts the launcher, 'a' lowers it
        if (s=='q'):
            if launchdevice.pos.x<5:
                launchdevice.pos.x+=0.2;
        if (s=='a'):
            if launchdevice.pos.x>-5:
                launchdevice.pos.x-=0.2;


# 'l' launches a particle
        if (s=='l'):
            makeparticle((launchdevice.pos.x,0,0),(0,0,0))
            launchdevice.visible=false

#  =========================================


#define ball that is used to select position

launchdevice=sphere(pos=(0,0,0), radius=0.25, color=color.blue)

# Make the charges exist

import random
print random.randrange(-5,10)

charge1=sphere(pos=(0,2),radius=0.5,charge=-1, color=color.red)
charge2=sphere(pos=(0,-2),radius=0.5,charge=-1, color=color.red)

#Define strength (KQ/m)

strength = 5;

scene.autoscale = False

#
# Move them
#
while 1:
    global strength;
    # Synchronized
    rate(100)
    # Catch keystrokes
    listenkeys()
    # Loop over all existing particles
    for thisparticle in particles:
        # The acceleration
        acc=vector(0,0,0)
        # Sum up all accelerations on the particle

        acc+=strength*(charge1.charge*(thisparticle.pos-charge1.pos))/(mag(thisparticle.pos-charge1.pos)**3)
        acc+=strength*(charge2.charge*(thisparticle.pos-charge2.pos))/(mag(thisparticle.pos-charge2.pos)**3)

        # dv=a*dt
        thisparticle.velocity+=acc*dt
        # dx=v*dt
        thisparticle.pos+=thisparticle.velocity*dt
