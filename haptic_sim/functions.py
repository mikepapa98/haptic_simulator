import pygame

def activate(letter):
    screen.fill(black)
    for y in range(-1,6):
        deactivate()
        for x in range(len(letter)):
            if (pos_x * letter[x][0] + pos_x * y >= pos_x and pos_x * letter[x][0] + pos_x * y <= screen_width - pos_x):
                pygame.draw.circle(screen,white,(pos_x * 7 - pos_x * letter[x][0] - pos_x * y, pos_y * letter[x][1]), rad)
                pygame.display.flip()
        pygame.time.delay(delay)
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
