from visual import *
import random
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
def makeparticle(position,speed,anglerange):
# Adjust radius and color the way you like 
    newparticle=sphere(pos=position,radius=0.2,color=color.cyan)
    angle=random.uniform(-anglerange,anglerange)
    newparticle.velocity=vector(speed*cos(angle),speed*sin(angle),0)
    newparticle.interfered=False
    particles.append(newparticle)

#
# The following function moves all particles
# according to their velocity for one timestep
# Stops them when they hit the screen
#
def moveparticles():
    for thisparticle in particles:
        thisparticle.pos+=thisparticle.velocity*dt
        if thisparticle.pos.x>9:
            thisparticle.velocity=vector(0,0,0)

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
def listenkeys(v):
    if scene.kb.keys:
        s=scene.kb.getkey()
# TODO: Implement a key to make a new particle
# at the correct position with the given speed
# and an angle spread so it hits the double slit
# and the frame
# 'x' quits
        if (s=='x'):
            exit()
            
        if (s=='l'):
            makeparticle((-7,0,0),v,0.3)
            

            

            
# ==========================================
# Monte Carlo for x

def montecarlo(a,d,l,lamb):
    cosfreq=math.pi*d/(lamb*l)
    sinfreq=math.pi*a/(lamb*l)
# TODO: for performance reasons, maybe calculate some constants
# ahead of time
    while 1:
        x=random.uniform(-20.,20.)
        if (x==0.):
            return x
        y=random.uniform(0,1)
# TODO: fix the next line to use the correct distribution
        f=(math.cos(cosfreq*x))**2*(math.sin(sinfreq*x)/(sinfreq*x))**2
        if (y<=f):
            return x
    
# ==========================================
def interference(a,d,l,lamb):
    for thisparticle in particles:
        if not thisparticle.interfered:
            if thisparticle.pos.x>0:
                sx=montecarlo(a,d,l,lamb)
                redirect=math.atan2(sx,l)
                speedx=thisparticle.velocity.x
# TODO: redirect the particle so it hits the screen at the
# correct position above, i.e., modify thisparticle.velocity
# such that the speed remains the same, but it is deflected
                thisparticle.interfered=True
                thisparticle.velocity=vector(speedx*cos(redirect),thisparticle.velocity.y,speedx*sin(redirect))

                

# ============================= Main program
# TODO: feel free to adjust the geometry
screen=box(pos=(9.5,0,0),size=(1,20,40),color=color.green)
launchdevice=box(pos=(-7,0,0), size=(2,0.4,0.4), color=color.red)
mask1=box(pos=(0,0,-2,),size=(0.1,6,3.6),color=color.blue)
mask2=box(pos=(0,0,2,),size=(0.1,6,3.6),color=color.blue)
mask3=box(pos=(0,0,0),size=(0.1,6,0.2),color=color.blue)
# Nail down the scene
scene.autoscale = False
#
#
# TODO: suggest some good values to the user
m=input("Mass? try 2. ")
v=input("Speed? try 4. Also increase these variables to increase momentum and watch what happens to the intereference pattern. ")
# Just fudging here, h might as well be 1
lamb=1./(m*v)
while 1:
    rate(100)
    listenkeys(v)
    moveparticles()
# TODO: fix the next line so it uses the
# correct geometry
    interference(0.1,0.25,9.5,lamb)
