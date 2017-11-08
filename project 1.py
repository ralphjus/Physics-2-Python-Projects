from visual import *
import random
print "Q and A move the launcher up and down. J and K slow down or speed up the electron. L fires the electron. X ends the game. Negative charges are red and positive charges are blue. Hit the Goal for maximum fun times!"
# The list of all particles
particles=[]
# The timestep length (might need to be adjusted)
dt=0.01
speed=4;
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
def listenkeys():
    global speed;
    if scene.kb.keys:
        s=scene.kb.getkey()
# This is where you have to add all your keys
# In this demo, "q" lifts the launcher, 'a' lowers it
        if (s=='q'):
            if launchdevice.pos.y<5:
                launchdevice.pos.y+=0.2;
        if (s=='a'):
            if launchdevice.pos.y>-5:
                launchdevice.pos.y-=0.2;
                
# j and k change the speed of the particle
        if (s=='j'):
            speed+=-1;

        if (s=='k'):
            speed+=1;

# 'l' launches a particle
        if (s=='l'):
            makeparticle((-5,launchdevice.pos.y,0),(speed,0,0))

# 'x' quits
        if (s=='x'):
            exit()
            
#  =========================================


#
crashwall=box(pos=(5,0,0), size=(0.2,4,1), color=color.green)
launchdevice=box(pos=(-6,0,0), size=(2,0.4,0.4), color=color.magenta)

# Make the charges exist

import random
print random.randrange(-5,10)

charge1=sphere(pos=(random.randrange(-3,4),random.randrange(-2,2)),radius=0.5,charge=random.randrange(-5,5))
charge2=sphere(pos=(random.randrange(-3,4),random.randrange(-2,2)),radius=0.5,charge=random.randrange(-5,5))
charge3=sphere(pos=(random.randrange(-3,4),random.randrange(-2,2)),radius=0.5,charge=random.randrange(-5,5))
charge4=sphere(pos=(random.randrange(-3,4),random.randrange(-2,2)),radius=0.5,charge=random.randrange(-5,5))

if -1 < charge1.charge < 1 :
    charge1.charge = 1
if charge1.charge > 0 :
    charge1.color=color.red
if charge1.charge < 0:
    charge1.color=color.blue

if -1 < charge2.charge < 1 :
    charge2.charge = 1
if charge2.charge > 0 :
    charge2.color=color.red
if charge2.charge < 0:
    charge2.color=color.blue

if -1 < charge3.charge < 1 :
    charge3.charge = 1
if charge3.charge > 0 :
    charge3.color=color.red
if charge3.charge < 0:
    charge3.color=color.blue

if -1 < charge4.charge < 1 :
    charge4.charge = 1
if charge4.charge > 0 :
    charge4.color=color.red
if charge4.charge < 0:
    charge4.color=color.blue

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
        acc+=strength*(charge3.charge*(thisparticle.pos-charge3.pos))/(mag(thisparticle.pos-charge3.pos)**3)
        acc+=strength*(charge4.charge*(thisparticle.pos-charge4.pos))/(mag(thisparticle.pos-charge4.pos)**3)

        # dv=a*dt
        thisparticle.velocity+=acc*dt
        # dx=v*dt
        thisparticle.pos+=thisparticle.velocity*dt
        # =====
        # Now destroy particles, if needed
        if thisparticle.pos.x is charge1.pos:
            destroyparticle(thisparticle)
            
        if thisparticle.pos.x is charge2.pos:
            destroyparticle(thisparticle)

        if thisparticle.pos.x is charge3.pos:
            destroyparticle(thisparticle)

        if thisparticle.pos.x is charge4.pos:
            destroyparticle(thisparticle)

        if thisparticle.pos.y < -4 :
            destroyparticle(thisparticle)
        if thisparticle.pos.y > 4 :
             destroyparticle(thisparticle)
        if thisparticle.pos.x > 5:
            destroyparticle(thisparticle)
        if thisparticle.pos.x < -7 :
            destroyparticle(thisparticle)
        if (thisparticle.pos.x > 5) and (-2<thisparticle.pos.y<2) :
            print "You're Winner!"


