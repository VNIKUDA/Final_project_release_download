# Імпортую модулі
import pygame, os, time, json
pygame.init()
pygame.display.init()


# Створюю та підписую вікно
win = pygame.display.set_mode((1240, 700))
pygame.display.set_caption('Akar')
pygame.display.set_icon(pygame.image.load(os.path.join('Assets', 'game_icon.png')))

# Колір заливки екрану
color = (0, 255, 255)

# Змінні відповідальні за продовження головного циклу
run = False
p_menu = False
main_menu = True

# Змінні для налаштувань програми та данні для наступного запуску програми
bright = 100
language = 'English'
control = 'Space-Left-Right'
chekpoint = 0
FPS = 60

'''filename = 'data_base.json'

line = ''
priv_line = ''

data_base = f'bright\n{bright}\nlanguage\n{language}\ncontrol\n{chekpoint}\nFPS\n{FPS}\n'

try:
    global player
    with open(filename) as f:
        lines = f.readlines()

    for i in lines:
        line = i
        if priv_line == 'bright':
            bright = int(line)
        if priv_line == 'language':
            language = line
        if priv_line == 'control':
            control = line
        if priv_line == 'chekpoint':
            chekpoint = line
        if priv_line == 'FPS':
            FPS = int(line)
        priv_line = line

except FileNotFoundError:
    with open(filename, 'a') as file:
        file.write(data_base)'''
# Земля
ground = pygame.Rect(0, 645, 5000, 75)
ground_texture = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'ground.png')), (5000, 75))

animation = 0
temp = 0
temp2 = 0
temp3 = 0
moving_obj = []
objects = []
all_obj = []
mobs = []

all_obj.append(ground)

end = pygame.Rect(4980, 605, 50, 50)
end_p = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Arka.png')), (75, 100))
start = pygame.Rect(0, 0,1,1)
arka = pygame.Rect(0,0,1,1)
all_obj.append(arka)
bg_img = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'game_bg (2).png')), (1240, 700))
p_menu_bg = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Menu_background.png')), (1240, 720))

button = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Button_menu.png')), (350, 110))
button_cont_rect = pygame.Rect(400, 200, 350, 110)
button_cont_text = pygame.font.SysFont('Forte', 50).render('CONTINUE', True, (0,0,0))
button_start_text = pygame.font.SysFont('Forte', 50).render('NEW GAME', True, (0,0,0))
button_sett_rect = pygame.Rect(400, 360, 350, 110)
button_sett_text = pygame.font.SysFont('Forte', 50).render('SETTINGS', True, (0,0,0))
button_main_rect = pygame.Rect(400, 510, 350, 110)
button_main_text = pygame.font.SysFont('Forte', 40).render('MAIN MENU', True, (0,0,0))
p_menu_text = pygame.font.SysFont('Forte', 130).render('PAUSE MENU', True, (255,255,255))
main_menu_text_w = pygame.font.SysFont('Forte', 150).render('Akar', True, (255, 255, 255))
main_menu_text_b = pygame.font.SysFont('Forte', 150).render('Akar', True, (0, 0, 0))
menu_icon = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Menu_icon.png')), (30, 15))

t1 = time.time()
ani = 0
ani_time = 0
def animate(animation, times, coor):
    global ani, ani_time, t1
    if ani_time >= 0 and ani_time < times[ani]:
        win.blit(animation[ani], coor)
    if ani_time >= times[ani]:
        ani_time = 0
        ani += 1
    if ani == len(animation):
        ani = 0
    t2 = time.time()
    t = t2 - t1
    ani_time += t

def pause_m():
    global button_cont_rect, button_sett_rect, button_main_rect, p_menu, run, main_menu, menu_icon
    win.blit(p_menu_text, (180, 20))
    win.blit(button, (button_cont_rect))
    win.blit(button, (button_sett_rect))
    win.blit(button, (button_main_rect))
    win.blit(button_cont_text, (button_cont_rect.x + 30, button_cont_rect.y + 40))
    win.blit(button_sett_text, (button_sett_rect.x + 30, button_sett_rect.y + 40))
    win.blit(button_main_text, (button_main_rect.x + 30, button_main_rect.y + 40))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                p_menu = False
            if event.key == pygame.K_q:
                run = False
        if event.type == pygame.QUIT:
            run = False
            main_menu = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            x, y = event.pos
            if button_cont_rect.collidepoint(x, y) or menu_icon.get_rect().collidepoint(x, y):
                p_menu = False
            if button_main_rect.collidepoint(x, y):
                p_menu = False
                run = False

def sett_menu():
    global p_menu, main_menu

def m_menu():
    global player, run, chekpoint, teleport, arka, all_obj
    win.blit(pygame.transform.scale(pygame.image.load(os.path.join("Assets", 'menu.png.png')), (1240, 720)), (0, 0))
    animate([main_menu_text_w, main_menu_text_b], [0.2, 0.2], (420, 20))
    if chekpoint == 0:
        win.blit(button, (button_sett_rect))
        win.blit(button, (button_main_rect))
        win.blit(button_start_text, (button_sett_rect.x + 20, button_sett_rect.y + 40))
        win.blit(button_sett_text, (button_main_rect.x + 30, button_main_rect.y + 40))
    else:
        win.blit(button, (button_cont_rect))
        win.blit(button, (button_sett_rect))
        win.blit(button, (button_main_rect))
        win.blit(button_cont_text, (button_cont_rect.x + 30, button_cont_rect.y + 40))
        win.blit(button_start_text, (button_sett_rect.x + 20, button_sett_rect.y + 40))
        win.blit(button_sett_text, (button_main_rect.x + 30, button_main_rect.y + 40))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            x, y = event.pos
            if button_sett_rect.collidepoint(x, y) and chekpoint == 0 or button_sett_rect.collidepoint(x, y) and chekpoint != 0:
                while arka.x != 0:
                    for i in all_obj:
                        i.x += 5
                    end.x += 5
                    start.x += 5
                player.x = 10
                player.y = 560
                player.m_down = True
                player.m_up = False
                player.alive = True
                run = True
                chekpoint = 1
            if button_cont_rect.collidepoint(x, y) and chekpoint != 0:
                run = True
        if event.type == pygame.QUIT:
            pygame.quit()

def teleport(coor, obj, objs):
    global start, end
    var1 = obj.x
    obj.y = coor[1]
    if coor[0] >= 0 and coor[0] <= 1240 - obj.w:
        obj.x = coor[0]
        if coor[0] < var1:
            var = var1 - coor[0]
            for i in objs:
                i.x -= var
            start.x -= var
            end.x -= var
        else:
            var = coor[0] - var1
            for i in objs:
                i.x += var
            start.x += var
            end.x += var
        '''if var > obj.x:
            var = var - obj.x
            for i in objs:
                i.x += var
            start.x += var
            end.x += var
        else:
            var = obj.x - var
            for i in objs:
                i.x -= var
            start.x -= var
            end.x -= var'''
    else:
        if coor[0] < 0:
            obj.x = 0
            var = coor[0] * -1 - var1
            for i in objs:
                i.x += var
            start.x += var
            end.x += var

        else:
            obj.x = 1240 - obj.w
            var = coor[0] - var1
            for i in objs:
                i.x -= var
            start.x -= var
            end.x -= var 

def died():
    global player, run, main_menu, objects, clock, all_obj, bg_img
    win.blit(bg_img, (0, 0))
    win.blit(pygame.transform.flip(end_p, True, False), (arka.x, 545))
    win.blit(ground_texture, ground)
    for i in objects:
            i.draw()
    win.blit(p_menu_bg, (0, 0))

    while player.alive != True:
        win.blit(button, (button_sett_rect))
        win.blit(button, (button_main_rect))
        win.blit(pygame.font.SysFont('Forte', 55).render('Restart', True, 'black'), (button_sett_rect.x + 70, button_sett_rect.y + 35))
        win.blit(button_main_text, (button_main_rect.x + 30, button_main_rect.y + 40))
        win.blit(pygame.font.SysFont('Forte', 130).render('You died', True, (255, 255, 255)), (360, 20))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if button_sett_rect.collidepoint(x, y):
                    run = True
                    while arka.x != 0:
                        for i in all_obj:
                            i.x += 5
                        end.x += 5
                        start.x += 5
                    player.x = 10
                    player.y = 560
                    player.m_down = True
                    player.m_up = False
                    player.alive = True
                if button_main_rect.collidepoint(x, y):
                    player.alive = True
                    while arka.x != 0:
                        for i in all_obj:
                            i.x += 5
                        end.x += 5
                        start.x += 5
                    player.x = 10
                    player.y = 560
                    player.m_down = True
                    player.m_up = False
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
        clock.tick(FPS)

# Клас для перешкод
class B():
    class Rect():
        def __init__(self, x, y, w, h, pict, pict_w = 50, pict_h = 50, typ = 'none'):
            global moving_obj, objetcs, all_obj
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.step = []
            self.moving = False
            self.move_time = 0
            self.pict_w = pict_w
            self.pict_h = pict_h
            self.t = 'b.rect'
            self.type = typ

            # Змінні для кожної з сторін прямокутника
            self.left = pygame.Rect(self.x, self.y+6, 1, self.h - 12)
            self.top = pygame.Rect(self.x+6, self.y, self.w-12, 1)
            self.right = pygame.Rect(self.x + self.w -1, self.y+6, 1, self.h - 12)
            self.bottom = pygame.Rect(self.x + 6, self.y + self.h-1, self.w - 12, 1)
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

            if pict != 'flygrass':
                self.pict = pygame.transform.scale(pygame.image.load(os.path.join('Assets', pict)), (self.pict_w, self.pict_h))
                self.p = pict
            else:
                self.pict = [pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Flygrass_middle.png')), (self.pict_w, self.pict_h)), pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Flygrass_left.png')), (self.pict_w, self.pict_h)), pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Flygrass_right.png')), (self.pict_w, self.pict_h))]
                self.p = 'flygrass'
                
            
            # Додавання в список перешкод для колізії
            objects.append(self)
            all_obj.append(self)

        def draw(self):
            self.left = pygame.Rect(self.x, self.y+6, 1, self.h - 12)
            self.top = pygame.Rect(self.x+6, self.y, self.w-12, 1)
            self.right = pygame.Rect(self.x + self.w -1, self.y+6, 1, self.h - 12)
            self.bottom = pygame.Rect(self.x + 6, self.y + self.h-1, self.w - 12, 1)
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
            x = self.x
            y = self.y
            if self.p == 'flygrass':
                self.pict = [pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Flygrass_middle.png')), (self.pict_w, self.pict_h)), pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Flygrass_left.png')), (self.pict_w, self.pict_h)), pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Flygrass_right.png')), (self.pict_w, self.pict_h))]
                num = self.w / self.pict_w
                tem = 0
                for i in range(int(num)):
                    if num == 2:
                        if tem == 0:
                            win.blit(self.pict[1], (x, self.y))
                            tem += 1
                            x += self.pict_w
                        if tem == 1:
                            win.blit(self.pict[2], (x, self.y))
                    if num == 3:
                        if tem == 0:
                            win.blit(self.pict[1], (x, self.y))
                            tem += 1
                            x += self.pict_w
                        if tem == 1:
                            win.blit(self.pict[0], (x, self.y))
                            tem += 1
                            x += self.pict_w
                        if tem == 2:
                            win.blit(self.pict[2], (x, self.y))
                    if num > 3:
                        if tem == 0:
                            win.blit(self.pict[1], (x, self.y))
                            tem += 1
                            x += self.pict_w
                        if tem >= 1 and tem < num - 1:
                            win.blit(self.pict[0], (x, self.y))
                            tem += 1
                            x += self.pict_w
                        if tem == num - 1:
                            win.blit(self.pict[2], (x, self.y))
            else:
                self.pict = pygame.transform.scale(pygame.image.load(os.path.join('Assets', self.p)), (self.pict_w, self.pict_h))
                if self.type.split()[-1] == 'flip':
                    self.pict = pygame.transform.flip(self.pict, False, True)
                num = self.w / self.pict_w
                num2 = self.h / self.pict_h
                for i in range(int(num2)):
                    for a in range(int(num)):
                        win.blit(self.pict, (x, y))
                        x += int(self.pict_w)
                    x -= num * int(self.pict_w)
                    y += int(self.pict_h)
        def move(self, coor, step = 5, timer = 0.3):
            global player, t1, temp, ground
            t2 = time.time()
            if self.step != []:
                a = len(coor) - 1
                b = -1
                while b != a:
                    b += 1
                    if self.y == coor[b] and b == 0 or self.y == coor[b] and b == a or player.rect.colliderect(self.bottom) and self.move_time == 0:
                        self.step *= -1
                        self.y += self.step
                        self.move_time += t2 - t1
                        b = a
                    if self.y == coor[b] and b != 0 and b != a:
                        self.move_time += t2 - t1
                        b = a
                    if player.rect.colliderect(self.top) and self.y == coor[b]:
                        player.y -= self.step
                b = -1
                a = len(player.objs) - 1
                while b != a:
                    b += 1
                    if player.objs:
                        if player.rect.colliderect(player.objs[b].bottom) and player.rect.colliderect(self.top):
                            self.step *= -1
                            self.y += self.step * 2
                            self.move_time += t2 - t1
                            player.y += self.step * 2
                            player.m_up = False
                            b = a

                '''for i in coor:
                    if self.y == i or player.rect.colliderect(self.bottom) and self.move_time == 0:
                        self.step *= -1
                        self.y += self.step
                        self.move_time += t2 - t1'''
                '''if self.y >= coor[0] or self.y <= coor[1] or player.rect.colliderect(self.bottom) and self.move_time == 0:
                    self.step *= -1
                    self.y += self.step
                    self.move_time += t2 - t1'''

                if self.move_time != 0:
                    for i in coor:
                        if player.rect.colliderect(self.top) and player.y + player.h > self.y + 5 and self.y == i:
                            player.y += self.step
                            player.m_down = False
                            player.m_up = True
                            temp = 0

                    if self.move_time < timer:
                        self.move_time += t2 - t1

                    elif self.move_time >= timer:
                        self.move_time = 0
                        self.y += self.step

                if self.move_time == 0:
                        if player.rect.colliderect(self.top) and self.step < 0:
                            player.y += self.step
                            player.m_down = False
                            player.m_up = True
                            temp = 0
                            '''a = len(player.objs) -1
                            b = -1
                            while player.objs != [] and b != a:
                                b += 1
                                if player.rect.colliderect(player.objs[b].left) or player.x + 5 > 1240 - player.w:
                                    player.m_right = False
                                else:
                                    player.m_right = True
                                if player.rect.colliderect(player.objs[b].right) or player.x - 5 < 0:
                                    player.m_left = False
                                else:
                                    player.m_left = True
                                if player.rect.colliderect(self.top) == False and temp == 0 and player.rect.colliderect(ground) == False and player.rect.colliderect(player.objs[b].top):
                                    player.m_down = True
                                    player.m_up = False
                                    temp = 0
                        if player.rect.colliderect(self.left) or player.x + 5 > 1240 - player.w:
                            player.m_right = False
                        else:
                            player.m_right = True
                        if player.rect.colliderect(self.right) or player.x - 5 < 0:
                            player.m_left = False
                        else:
                            player.m_left = True'''
                        
                        self.y += self.step

            else:
                self.step = step
                self.moving = True
    class T():
        def __init__(self, x, y, w =  50, h = 50):
            global all_obj
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.rect = pygame.Rect(self.x , self.y, self.w, self.h)
            self.rect_ = ''
            all_obj.append(self)
        def update(self):
            self.rect = pygame.Rect(self.x , self.y, self.w, self.h)
            
        def close_door(self, x, y, w, h, pict, p_w = 50, p_h = 50):
            global B
            self.rect_ = B.Rect(x, y, w, h, pict, p_w, p_h)
# Клас для спрайтів
class Sprite():
    class Player():
        class Ball():
            def __init__(self, x, y, speed):
                self.x = x
                self.y = y
                self.w = 20
                self.h = 20
                self.speed = speed
                self.pict = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'ball_.png')), (self.w, self.h))
                self.rect = pygame.Rect(self.x, self.y, self.w, self.y)
            def collide(self):
                global mobs
                for mob in mobs:
                    if self.rect.collidrect(mob.rect):
                        mobs.remove(mob)

            def draw(self):
                win.blit(self.pict, (self.x, self.y))

            def move(self, way = 'right'):
                if way == 'left':
                    self.x -= self.speed
                else:
                    self.x += self.speed

        def __init__(self, x, y, w, h, picts):
            self.x = x
            self.y = y
            self.w = w
            self.h = h

            # Завантажую картинки для анімації
            self.mario_r = pygame.transform.scale(picts[0], (self.w-10, self.h-10))
            self.mario_l = pygame.transform.scale(picts[1], (self.w-10, self.h-10))
            self.mario_jr = pygame.transform.scale(picts[2], (self.w-10, self.h-10))
            self.mario_jl = pygame.transform.scale(picts[3], (self.w-10, self.h-10))
            self.mario_wr = pygame.transform.scale(picts[4], (self.w-10, self.h-10))
            self.mario_wl = pygame.transform.scale(picts[5], (self.w-10, self.h-10))
            self.mario_rr = pygame.transform.scale(picts[6], (self.w-10, self.h-10))
            self.mario_rl = pygame.transform.scale(picts[7], (self.w-10, self.h-10))
            self.mario_rr2 = pygame.transform.scale(picts[8], (self.w-10, self.h-10))
            self.mario_rl2 = pygame.transform.scale(picts[9], (self.w-10, self.h-10))
            self.mario_rr3 = pygame.transform.scale(picts[10], (self.w-10, self.h-10))
            self.mario_rl3 = pygame.transform.scale(picts[11], (self.w-10, self.h-10))
            self.mario_rr4 = pygame.transform.scale(picts[12], (self.w-10, self.h-10))
            self.mario_rl4 = pygame.transform.scale(picts[13], (self.w-10, self.h-10))
            self.mario_rr5 = pygame.transform.scale(picts[14], (self.w-10, self.h-10))
            self.mario_rl5 = pygame.transform.scale(picts[15], (self.w-10, self.h-10))

            self.pict = self.mario_r
            self.picts = picts
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
            self.colliding = pygame.Rect(self.x - self.w/2, self.y - self.h/2, self.w * 2, self.h * 2)
            self.m_left = True
            self.m_right = True
            self.m_up = True
            self.m_down = False
            self.objs = []
            self.balls = []
            self.ani = 0
            self.alive = True
            self.time = 0

        def draw(self):
            self.colliding = pygame.Rect(self.x - self.w/2, self.y - self.h/2, self.w * 2, self.h * 2)
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
            win.blit(self.pict, (self.x+5, self.y+5))

        def collide(self):
            global objects, mobs

            self.objs = []

            for object in objects:
                if self.colliding.colliderect(object.rect):
                    self.objs.append(object)

            for mob in mobs:
                if self.colliding.colliderect(mob.rect):
                    self.objs.append(mob)

        def move(self):
            global temp, temp2, temp3, animation, end, start, objects, all_obj, run, chekpoint, t1

            a = len(self.objs) - 1
            b = -1

            while b != a and self.objs != []:
                b += 1
                if self.objs[b].type == 'none':
                    if self.x - 5 < 0 or self.rect.colliderect(self.objs[b].right) == True and self.rect.colliderect(self.objs[b].top) == False:
                        self.m_left = False
                        b = a
                    elif self.x - 5 > 0 or self.rect.colliderect(self.objs[b].top) and self.rect.colliderect(self.objs[b].right) or self.rect.colliderect(self.objs[b].right) == False:
                        self.m_left = True
                    if self.x + 5 > 1245 - self.w or self.rect.colliderect(self.objs[b].left) == True and self.rect.colliderect(self.objs[b].top) == False:
                        self.m_right = False
                        b = a
                    elif self.x + 5 < 1245 - self.w or self.rect.colliderect(self.objs[b].top) and self.rect.colliderect(self.objs[b].left) or self.rect.colliderect(self.objs[b].left) == False:
                        self.m_right = True

                    if self.rect.colliderect(ground) == False and temp == 0 and self.rect.colliderect(self.objs[b].top) == False:
                        self.m_down = True
                        self.m_up = False
                        if animation == 0 or animation == 2 or animation == 4 or animation == 6 or animation == 8 or animation == 10:
                            self.pict = self.mario_jr
                            animation = 2
                        elif animation == 1 or animation == 3 or animation == 5 or animation == 7 or animation == 9 or animation == 11:
                            self.pict = self.mario_jl
                            animation = 3

                    
                    if self.rect.colliderect(self.objs[b].bottom):
                        temp = 0
                        self.m_down = True
                        self.m_up = False

                    if self.rect.colliderect(self.objs[b].top) or self.m_up == True:
                        self.m_up = True
                        self.m_down = False
                        temp = 0
                        b = -1
                        while b != a:
                            b += 1

                            if self.x + 5 <= 10 or self.rect.colliderect(self.objs[b].right) == True:
                                self.m_left = False
                                b = a
                                
                            else:
                                self.m_left = True
                            if self.x + 5 >= 1245 - self.w or self.rect.colliderect(self.objs[b].left) == True:
                                self.m_right = False
                                b = a
                            else:
                                self.m_right = True
                        if animation == 0 or animation == 2:
                            self.pict = self.mario_r
                            animation = 0
                        if animation == 1 or animation == 3:
                            self.pict = self.mario_l
                            animation = 1
                    '''if self.rect.colliderect(self.objs[b].top) and self.y + self.h > self.objs[b].y + 5:
                        while self.y + self.h != self.objs[b].y + 5:
                            self.y -= 5
                            self.m_down = False
                            self.m_up = True
                    if self.rect.colliderect(self.objs[b].top) and self.y + self.h > self.objs[b].y + 5:
                        while self.y + self.h != self.objs[b].y + 5:
                            self.y -= 5
                            self.m_down = False
                            self.m_up = True'''
                    '''if self.objs[b].t == 'sprite.mob':
                    if self.rect.colliderect(self.objs[b].top):
                        self.m_down = False
                        self.m_up = True
                        temp = 1
                        if animation == 0 or animation == 4 or animation == 6 or animation == 8 or animation == 10:
                            self.pict = self.mario_jr
                            animation = 2
                        elif animation == 1 or animation == 5 or animation == 7 or animation == 9 or animation == 11:
                            self.pict = self.mario_jl
                            animation = 3
                    if self.rect.colliderect(self.objs[b].right):
                        self.ani += 1
                        if self.ani >= 1 and self.ani <= 10:
                            animate([player.pict, pygame.image.load(os.path.join('Assets', 'none.png'))], [1, 1], (player.x + 5, player.y + 5))
                        if self.ani == 11:
                            self.ani = 0'''
                if self.objs[b].type != 'none':
                    if self.rect.colliderect(self.objs[b].rect):
                        run = False
                        chekpoint = 0
                        self.alive = False
            if self.rect.colliderect(ground):
                self.m_up = True
                self.m_down = False
                temp = 0
                if animation == 0 or animation == 2:
                    self.pict = self.mario_r
                    animation = 0
                if animation == 1 or animation == 3:
                    self.pict = self.mario_l
                    animation = 1

            if self.rect.colliderect(ground) == False and self.objs == [] and temp == 0:
                self.m_down = True
                self.m_up = False
                if animation == 0 or animation == 4 or animation == 6 or animation == 8 or animation == 10:
                    self.pict = self.mario_jr
                    animation = 2
                elif animation == 1 or animation == 5 or animation == 7 or animation == 9 or animation == 11:
                    self.pict = self.mario_jl
                    animation = 3

            ''' for i in objects:
                if self.rect.colliderect(i.top) == False and temp == 0 and self.rect.colliderect(ground) == False:
                    self.m_down = True
                    self.m_up = False
                    if animation == 0 or animation == 2:
                        self.pict = self.mario_jr
                        animation = 2
                    elif animation == 1 or animation == 3:
                        self.pict = self.mario_jl
                        animation = 3'''
            if self.x - 5 < 0:
                while self.x - 5 < 0:
                    self.x += 5
            if self.x + 5 > 1240 - self.w:
                while self.x + 5 > 1240 - self.w:
                    self.x -= 5

                if animation == 0 or animation == 2:
                    self.pict = self.mario_r
                    animation = 0
                if animation == 1 or animation == 3:
                    self.pict = self.mario_l
                    animation = 1
                
            if temp == 16 and self.m_up == False:
                self.m_down = True

            if self.m_down:
                self.y += 5

            # Обробник подій

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and self.m_left:
                if self.x < start.x  + 620 and self.x < 620 or self.x > end.x - 610 and self.x > 615:
                    self.x -= 5
                else:
                    for i in all_obj:
                        i.x += 5
                    end.x += 5
                    start.x += 5
            if keys[pygame.K_RIGHT] and self.m_right:
                if self.x < start.x + 620 and self.x < 615 or self.x > end.x - 610 and self.x > 610:
                    self.x += 5
                else:
                    for i in all_obj:
                        i.x -= 5
                    end.x -= 5
                    start.x -= 5

            if keys[pygame.K_SPACE] and self.m_up:
                temp = 1
                self.m_up = False
                if animation == 0 or animation == 4 or animation == 6 or animation == 8 or animation == 10:
                    self.pict = self.mario_jr
                    animation = 2
                elif animation == 1 or animation == 5 or animation == 7 or animation == 9 or animation == 11:
                    self.pict = self.mario_jl
                    animation = 3

            if keys[pygame.K_a] and self.m_up == True and self.time > 0.6:
                self.balls.append(Sprite.Player.Ball(self.x, self.y + self.h/2, 2))

            if temp >= 1 and temp < 16 and self.m_up == False:
                temp += 1
                self.y -= 5

            # Визначення якій анімацій руху запуститись
            if keys[pygame.K_LEFT] and self.m_up:
                if temp3 >= 0 and temp3 < 8:
                    self.pict = self.mario_rl
                    animation = 7
                    temp3 += 1

                if temp3 >= 8 and temp3 < 16:
                    self.pict = self.mario_rl2
                    animation = 9
                    temp3 += 1

                if temp3 >= 15 and temp3 < 22:
                    self.pict = self.mario_rl3
                    animation = 11
                    temp3 += 1
                if temp3 >= 22 and temp3 < 30:
                    self.pict = self.mario_rl4
                    animation = 11
                    temp3 += 1

                if temp3 >= 30 and temp3 < 36:
                    self.pict = self.mario_rl5
                    animation = 11
                    temp3 += 1
                
                if temp3 == 36:
                    temp3 = 0

            if keys[pygame.K_RIGHT] and self.m_up:
                if temp3 >= 0 and temp3 < 8:
                    self.pict = self.mario_rr
                    animation = 6
                    temp3 += 1

                if temp3 >= 8 and temp3 < 16:
                    self.pict = self.mario_rr2
                    animation = 8
                    temp3 += 1

                if temp3 >= 15 and temp3 < 22:
                    self.pict = self.mario_rr3
                    animation = 10
                    temp3 += 1
                if temp3 >= 22 and temp3 < 30:
                    self.pict = self.mario_rr4
                    animation = 10
                    temp3 += 1

                if temp3 >= 30 and temp3 < 36:
                    self.pict = self.mario_rr5
                    animation = 10
                    temp3 += 1
                
                if temp3 == 36:
                    temp3 = 0


            if keys[pygame.K_LEFT] and self.m_up == False:
                self.pict = self.mario_jl
                animation = 3
            if keys[pygame.K_RIGHT] and self.m_up == False:
                self.pict = self.mario_jr
                animation = 2

            if keys[pygame.K_LEFT] == False and keys[pygame.K_RIGHT] == False and keys[pygame.K_SPACE] == False and self.m_up or keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
                temp3 = 0
                if temp2 >= 0 and temp2 < 15:
                    if animation == 0 or animation == 4 or animation == 6 or animation == 8 or animation == 10:
                        temp2 += 1
                        self.pict = self.mario_wr
                        animation = 4
                    if animation == 1 or animation == 5 or animation == 7 or animation == 9 or animation == 11:
                        temp2 += 1
                        self.pict = self.mario_wl
                        animation = 5

                if temp2 >= 15 and temp2 < 30:
                    if animation == 0 or animation == 4 or animation == 6 or animation == 8 or animation == 10:
                        temp2 += 1
                        self.pict = self.mario_r
                        animation = 0
                    if animation == 1 or animation == 5 or animation == 7 or animation == 9 or animation == 11:
                        temp2 += 1
                        self.pict = self.mario_l
                        animation = 1

                if temp2 == 30:
                    temp2 = 0

            t2 = time.time()
            self.time += (t2 - t1) * 5

            if self.time > 0.7:
                self.time = 0

    class Mob():
        def __init__(self, x, y, w, h):
            global all_obj, mobs
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.type = 'sprite.mob'

            self.left = pygame.Rect(self.x, self.y+6, 1, self.h - 12)
            self.top = pygame.Rect(self.x+6, self.y, self.w-12, 1)
            self.right = pygame.Rect(self.x + self.w -1, self.y+6, 1, self.h - 12)
            self.bottom = pygame.Rect(self.x + 6, self.y + self.h-1, self.w - 12, 1)
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

            self.pict = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'sprite.png')), (self.w, self.h))
            self.time = 0
            self.step = 1
            mobs.append(self)
            all_obj.append(self)

        def draw(self):
            self.left = pygame.Rect(self.x, self.y+6, 1, self.h - 12)
            self.top = pygame.Rect(self.x+6, self.y, self.w-12, 1)
            self.right = pygame.Rect(self.x + self.w -1, self.y+6, 1, self.h - 12)
            self.bottom = pygame.Rect(self.x + 6, self.y + self.h-1, self.w - 12, 1)
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
            win.blit(self.pict, self.rect)
        
        def move(self, coor, t):
            global t1, player
            t2 = time.time()
            if self.x <= coor[0] or self.x >= coor[1]:
                self.time += t2 - t1
                self.step *= -1
                self.x += self.step
            else:
                self.x += self.step
            if self.time != 0 and self.time != t:
                self.time += t2 - t1
            if self.time >= t:
                self.time = 0

player = Sprite.Player(0, 560, 50, 75, [
    pygame.image.load(os.path.join('Assets', 'player_w2.png')),  
    pygame.image.load(os.path.join('Assets', 'player_wl1.png')), 
    pygame.image.load(os.path.join('Assets', 'player_jr2.png')), 
    pygame.image.load(os.path.join('Assets', 'player_jl2.png')), 
    pygame.image.load(os.path.join('Assets', 'player_w4.png')), 
    pygame.image.load(os.path.join('Assets', 'player_wl2.png')), 
    pygame.image.load(os.path.join('Assets', 'player_run_r1.png')), 
    pygame.image.load(os.path.join('Assets/player_run_l', '1.png')), 
    pygame.image.load(os.path.join('Assets', 'player_run_r2.png')), 
    pygame.image.load(os.path.join('Assets/player_run_l', '2.png')), 
    pygame.image.load(os.path.join('Assets', 'player_run_r3.png')), 
    pygame.image.load(os.path.join('Assets/player_run_l', '3.png')),
    pygame.image.load(os.path.join('Assets', 'player_run_r4.png')), 
    pygame.image.load(os.path.join('Assets/player_run_l', '4.png')),
    pygame.image.load(os.path.join('Assets', 'player_run_r5.png')), 
    pygame.image.load(os.path.join('Assets/player_run_l', '5.png'))])
bar1 = B.Rect(100, 595, 50,50, 'Barrel_small.png')
bar2 = B.Rect(150, 595, 150, 50, 'Block_16.png')
bar3 = B.Rect(300, 545, 100, 100, 'Block_32.png', 100, 100)
bar4 = B.Rect(400, 545, 150, 50, 'flygrass')
bar7 = B.Rect(350, 495, 150, 50, 'Block_16.png')
bar8 = B.Rect(500, 475, 50, 70, 'Barrel_big.png', 50, 70)
bar9 = B.Rect(560, 420, 100, 50, 'flygrass')
bar10 = B.Rect(400, 245, 150, 50, 'flygrass')
bar11 = B.Rect(400, 195, 50, 50, 'Barrel_small.png')
bar12 = B.Rect(100, 95, 200, 50, 'flygrass')
bar16 = B.Rect(150, 545, 150, 50, 'flygrass')
bar15 = B.Rect(-1, 295, 150, 50, 'flygrass')
bar14 = B.Rect(50, 245, 50, 50, 'Block_16.png')
bar13 = B.Rect(0, 225, 50, 70, 'Barrel_big.png', 50, 70)
bar17 = B.Rect(670, 145, 100, 150, 'Stone.png')
bar19 = B.Rect(771, 495, 100, 50, 'flygrass')
bar21 = B.Rect(770, 595, 50, 50, 'Barrel_small.png')
bar18 = B.Rect(670, 445, 100, 200, 'Stone.png')
bar20 = B.Rect(771, 145, 100, 50, 'flygrass')
bar22 = B.Rect(875, 590, 100, 50, 'flygrass')
bar24 = B.Rect(1275, 595, 50, 50, 'Barrel_small.png')
bar23 = B.Rect(1175, 595, 50, 50, 'Barrel_small.png')
bar25 = B.Rect(1225, 575, 50, 70, 'Barrel_big.png', 50, 70)
bar26 = B.Rect(1025, 295, 200, 50, 'flygrass')
bar27 = B.Rect(1075, 245, 50, 50, 'Barrel_small.png')
bar28 = B.Rect(1125, 195, 100, 100, 'Block_32.png', 100, 100)
bar29 = B.Rect(1475, 345, 200, 50, 'flygrass')
bar30 = B.Rect(1525, 295, 50, 50, 'Block_16.png')
bar31 = B.Rect(1575, 275, 50, 70, 'Barrel_big.png', 50, 70)
bar32 = B.Rect(1750, 425, 100, 50, 'flygrass')
bar33 = B.Rect(1850, 425, 150, 50, 'Block_16.png')
bar34 = B.Rect(1950, 375, 50, 50, 'Barrel_small.png')
bar76 = B.Rect(2000, 425, 200, 400, 'Stone.png')
bar35 = B.Rect(2000, 0, 500, 100, 'Stone.png')
bar36 = B.Rect(2300, 100, 200, 150, 'Stone.png')
bar37 = B.Rect(2000, 250, 500, 250, 'Stone.png')
bar39 = B.Rect(1980, 625, 540, 60, 'Stone.png')
bar40 = B.Rect(420, 595, 250, 50, 'shripe.png', 60, 50, 'shripe')
bar45 = B.Rect(2570, 480, 50, 50, 'Shripe.png', 50, 50, 'shripe flip')
bar41 = B.Rect(2500, 450, 150, 50, 'flygrass')
bar42 = B.Rect(2500, 400, 50, 50, 'Barrel_small.png')
bar43 = B.Rect(2660, 450, 100, 50, 'flygrass')
bar44 = B.Rect(2850, 400, 150, 150, 'Stone.png')
bar46 = B.Rect(2750, 200, 100, 50, 'flygrass')
bar48 = B.Rect(2900, 240, 100, 50, 'Shripe.png', 50, 50, 'shripe flip')
bar47 = B.Rect(2900, 200, 100, 50, 'Stone.png')
bar48 = B.Rect(2700, 0, 200, 50, 'Shripe.png', 50, 50, 'shripe flip')
bar49 = B.Rect(2900, 0, 200, 50, 'Stone.png')
bar50 = B.Rect(2950, 150, 100, 50, 'Stone.png')
bar51 = B.Rect(3050, 450, 100, 50, 'flygrass')
bar53 = B.Rect(3200, 300, 100, 50, 'flygrass')
bar54 = B.Rect(3200, 225, 50, 75, 'Barrel_big.png', 50, 75)
bar55 = B.Rect(3250, 450, 150, 50, 'flygrass')
bar56 = B.Rect(3350, 400, 50, 50, 'Barrel_small.png')
bar57 = B.Rect(3300, 200, 100, 50, 'flygrass')
bar58 = B.Rect(3350, 150, 50, 50, 'Barrel_small.png')
bar59 = B.Rect(3400, 100, 100, 150, 'Stone.png')
bar61 = B.Rect(3525, 175, 250, 50, 'Shripe.png', 50, 50, 'shripe flip')
bar60 = B.Rect(3500, 150, 300, 50, 'flygrass')
bar62 = B.Rect(3600, 600, 700, 50, 'Stone.png')
bar63 = B.Rect(3700, 550, 550, 50, 'Stone.png')
bar64 = B.Rect(3850, 500, 350, 50, 'Stone.png')
bar65 = B.Rect(3900, 450, 300, 50, 'Stone.png')
bar66 = B.Rect(3900, 50, 150, 100, 'Stone.png')
bar67 = B.Rect(3600, 300, 50, 50, 'Barrel_small.png')
bar68 = B.Rect(3550, 350, 100, 50, 'flygrass')
bar69 = B.Rect(4200, 150, 100, 100, 'Stone.png')
bar70 = B.Rect(4325, 600, 150, 50,  'flygrass')
bar71 = B.Rect(4300, 0, 300, 50, 'Shripe.png', 50, 50, 'shripe flip')
bar72 = B.Rect(4500, 175, 200, 150, 'Stone.png')
bar73 = B.Rect(4850, 225, 150, 50, 'flygrass')
bar74 = B.Rect(4950, 150, 50, 75, 'Barrel_big.png', 50, 75)
bar75 = B.Rect(2250, 175, 50, 75, 'Barrel_big.png', 50, 75)
t = B.T(2100, 595)

end_open = False

t2 = time.time()
clock = pygame.time.Clock()
while main_menu == True:
    t1 = time.time()
    if player.alive == True:
        m_menu()
    if player.alive == False:
        died()
    pygame.display.update()
    clock.tick(FPS)
    t2 = time.time()
    
    while run == True and player.alive == True:
        t1 = time.time()

        if player.rect.colliderect(t.rect):
            if t.rect_ not in objects:
                start.x = bar35.x + 350
                chekpoint = 2
        win.blit(bg_img, (0, 0))
        win.blit(ground_texture, (ground.x, 635))
        player.collide()
        bar9.move([480, 245, 140])
        bar16.move([290, 550])
        bar22.move([600, 495, 140])
        bar32.move([600, 425, 220], )
        bar43.move([445, 595])
        bar70.move([605,  175, 45], 5, 0.1)
        for i in objects:
            if i.x + i.w > 0 and i.x < 1240:
                i.draw()
        for i in mobs:
            if i.x + i.w > 0 and i.x < 1240:
                i.draw()
        win.blit(menu_icon, (5, 5))
        if player.rect.colliderect(bar74.rect):
            end_open = True
        if player.rect.colliderect(bar27.rect):
            if bar76 in objects:
                objects.remove(bar76)
                all_obj.remove(bar76)
        if end_open:
            win.blit(end_p, (end.x-55, 545))
            if player.rect.colliderect(end):
                run = False
                main_menu  = False
        win.blit(pygame.transform.flip(end_p, True, False), (arka.x, 545))
        player.draw()
        player.move()
        t.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                main_menu = False
                end_open = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    p_menu = True
                    win.blit(p_menu_bg, (0,0))
                    while p_menu == True and run == True:
                        pause_m()
                        pygame.display.update()

                        clock.tick(FPS)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                x, y = event.pos
                if menu_icon.get_rect().collidepoint(x, y):
                    p_menu = True
                    win.blit(p_menu_bg, (0,0))
                    while p_menu == True and run == True:
                        pause_m()
                        pygame.display.update()
                        clock.tick(FPS)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            run = False
        
        pygame.display.update()

        clock.tick(FPS)
        t2 = time.time()

a = False

if end_open:
    a = True

q = 0
while a == True and q < 5:
    t1 = time.time()
    win.blit(pygame.transform.scale(pygame.image.load(os.path.join("Assets", 'menu.png.png')), (1240, 720)), (0, 0))
    win.blit(pygame.font.SysFont('Forte', 100).render('You get it!', True, 'white'), (200, 50))
    win.blit(pygame.font.SysFont('Forte', 50).render('Created by Sasha Goncharuk', True, 'white'), (400, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()

    clock.tick(FPS)
    t2 = time.time()
    q += t2 - t1