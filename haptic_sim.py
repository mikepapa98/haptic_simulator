import pygame

#Initialize Screen
pygame.init()
screen_size = screen_width, screen_height = 1000, 500
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Haptic Simulation")

#Initialize Electrodes
elec_pos = pos_x, pos_y = int(screen_width / 7), int(screen_height / 4)
elec_rad = rad = 25

#Colors
black = 0, 0, 0
white = 255, 255, 255
gray = 75, 75, 75

#Framerate
fps = 60
frame = 0

#Letters
null = [ [0,0] ]
a = [ [1,1] ] 
b = [ [1,1] , [1,2] ]
c = [ [1,1] , [2,1] ]
d = [ [1,1] , [2,1] , [2,2] ]
e = [ [1,1] , [2,2] ]
f = [ [1,1] , [1,2] , [2,1] ]
g = [ [1,1] , [1,2] , [2,1] , [2,2] ]
h = [ [1,1] , [1,2] , [2,2] ]
i = [ [1,2] , [2,1] ]
j = [ [1,2] , [2,1] , [2,2] ]
k = [ [1,1] , [1,3] ]
l = [ [1,1] , [1,2] , [1,3] ]
m = [ [1,1] , [1,3] , [2,1] ]
n = [ [1,1] , [1,3] , [2,1] , [2,2] ]
o = [ [1,1] , [1,3] , [2,2] ]
p = [ [1,1] , [1,2] , [1,3] , [2,1] ]
q = [ [1,1] , [1,2] , [1,3] , [2,1] , [2,2] ]
r = [ [1,1] , [1,2] , [1,3] , [2,2] ]
s = [ [1,2] , [1,3] , [2,1] ]
t = [ [1,2] , [1,3] , [2,1] , [2,2] ]
u = [ [1,1] , [1,3] , [2,3] ]
v = [ [1,1] , [1,2] , [1,3] , [2,3] ]
w = [ [1,2] , [2,1] , [2,2] , [2,3] ]
x = [ [1,1] , [1,3] , [2,1] , [2,3] ]
y = [ [1,1] , [1,3] , [2,1] , [2,2] , [2,3] ]
z = [ [1,1] , [1,3] , [2,2] , [2,3] ]



def activate(letter):
    screen.fill(black)
    for y in range(-1,6):
        deactivate()
        for x in range(len(letter)):
            if (pos_x * letter[x][0] + pos_x * y >= pos_x and pos_x * letter[x][0] + pos_x * y <= screen_width - pos_x):
                pygame.draw.circle(screen,white,(pos_x * 7 - pos_x * letter[x][0] - pos_x * y, pos_y * letter[x][1]), rad)
                pygame.display.flip()
        pygame.time.delay(500)

def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

def deactivate():
    for x in range(1,7):
        for y in range(1,4):
            pygame.draw.circle(screen,gray,(pos_x * x, pos_y * y), rad)
            pygame.display.flip()


def main(run):

    while run:
        #Set Framerate
        clock = pygame.time.Clock()
        clock.tick(fps)

        #Turn Electrodes OFF
        deactivate()

        #Framerate
        #frame += 1
        #print(frame)

        #Check for Exit
        check_quit()

        #Check Keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            run = False
        if keys[pygame.K_a]:
            letter = activate(a)
        if keys[pygame.K_b]:
            letter = activate(b)
        if keys[pygame.K_c]:
            letter = activate(c)
        if keys[pygame.K_d]:
            activate(d)
        if keys[pygame.K_e]:
            activate(e)
        if keys[pygame.K_f]:
            activate(f)
        if keys[pygame.K_g]:
            activate(g)
        if keys[pygame.K_h]:
            activate(h)
        if keys[pygame.K_i]:
            activate(i)
        if keys[pygame.K_j]:
            activate(j)
        if keys[pygame.K_k]:
            activate(k)
        if keys[pygame.K_l]:
            activate(l)
        if keys[pygame.K_m]:
            activate(m)
        if keys[pygame.K_n]:
            activate(n)
        if keys[pygame.K_o]:
            activate(o)
        if keys[pygame.K_p]:
            activate(p)
        if keys[pygame.K_q]:
            activate(q)
        if keys[pygame.K_r]:
            activate(r)
        if keys[pygame.K_s]:
            activate(s)
        if keys[pygame.K_t]:
            activate(t)
        if keys[pygame.K_u]:
            activate(u)
        if keys[pygame.K_v]:
            activate(v)
        if keys[pygame.K_w]:
            activate(w)
        if keys[pygame.K_x]:
            activate(x)
        if keys[pygame.K_y]:
            activate(y)
        if keys[pygame.K_z]:
            activate(z)
        

def setup():
    deactivate()
    main(True)

if __name__ == '__main__':
    setup()

