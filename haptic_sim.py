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
a = [ [2,1] ] 
b = [ [2,1] , [2,2] ]
c = [ [2,1] , [1,1] ]
d = [ [2,1] , [1,1] , [1,2] ]
e = [ [2,1] , [1,2] ]
f = [ [2,1] , [2,2] , [1,1] ]
g = [ [2,1] , [2,2] , [1,1] , [1,2] ]
h = [ [2,1] , [2,2] , [1,2] ]
i = [ [2,2] , [1,1] ]
j = [ [2,2] , [1,1] , [1,2] ]
k = [ [2,1] , [2,3] ]
l = [ [2,1] , [2,2] , [2,3] ]
m = [ [2,1] , [2,3] , [1,1] ]
n = [ [2,1] , [2,3] , [1,1] , [1,2] ]
o = [ [2,1] , [2,3] , [1,2] ]
p = [ [2,1] , [2,2] , [2,3] , [1,1] ]
q = [ [2,1] , [2,2] , [2,3] , [1,1] , [1,2] ]
r = [ [2,1] , [2,2] , [2,3] , [1,2] ]
s = [ [2,2] , [2,3] , [1,1] ]
t = [ [2,2] , [2,3] , [1,1] , [1,2] ]
u = [ [2,1] , [2,3] , [1,3] ]
v = [ [2,1] , [2,2] , [2,3] , [1,3] ]
w = [ [2,2] , [1,1] , [1,2] , [1,3] ]
x = [ [2,1] , [2,3] , [1,1] , [1,3] ]
y = [ [2,1] , [2,3] , [1,1] , [1,2] , [1,3] ]
z = [ [2,1] , [2,3] , [1,2] , [1,3] ]



def activate(letter):
    screen.fill(black)
    for y in range(-1,6):
        deactivate()
        for x in range(len(letter)):
            if (pos_x * letter[x][0] + pos_x * y >= pos_x and pos_x * letter[x][0] + pos_x * y <= screen_width - pos_x):
                pygame.draw.circle(screen,white,(pos_x * 7 - pos_x * letter[x][0] - pos_x * y, pos_y * letter[x][1]), rad)
                pygame.display.flip()
        pygame.time.delay(500)
    deactivate()

def deactivate():
    for x in range(1,7):
        for y in range(1,4):
            pygame.draw.circle(screen,gray,(pos_x * x, pos_y * y), rad)
            pygame.display.flip()

def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

def keys(run = True):
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        run = False
    if key[pygame.K_a]:
        letter = activate(a)
    if key[pygame.K_b]:
        letter = activate(b)
    if key[pygame.K_c]:
        letter = activate(c)
    if key[pygame.K_d]:
        activate(d)
    if key[pygame.K_e]:
        activate(e)
    if key[pygame.K_f]:
        activate(f)
    if key[pygame.K_g]:
        activate(g)
    if key[pygame.K_h]:
        activate(h)
    if key[pygame.K_i]:
        activate(i)
    if key[pygame.K_j]:
        activate(j)
    if key[pygame.K_k]:
        activate(k)
    if key[pygame.K_l]:
        activate(l)
    if key[pygame.K_m]:
        activate(m)
    if key[pygame.K_n]:
        activate(n)
    if key[pygame.K_o]:
        activate(o)
    if key[pygame.K_p]:
        activate(p)
    if key[pygame.K_q]:
        activate(q)
    if key[pygame.K_r]:
        activate(r)
    if key[pygame.K_s]:
        activate(s)
    if key[pygame.K_t]:
        activate(t)
    if key[pygame.K_u]:
        activate(u)
    if key[pygame.K_v]:
        activate(v)
    if key[pygame.K_w]:
        activate(w)
    if key[pygame.K_x]:
        activate(x)
    if key[pygame.K_y]:
        activate(y)
    if key[pygame.K_z]:
        activate(z)
    return run


def main(run = True):

    while run:
        #Set Framerate
        clock = pygame.time.Clock()
        clock.tick(fps)
        
        #Framerate
        #frame += 1
        #print(frame)

        #Check for Exit
        check_quit()

        #Check Keys
        run = keys()
        

def setup():
    deactivate()
    main()

if __name__ == '__main__':
    setup()

