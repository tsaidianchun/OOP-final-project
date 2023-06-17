import pygame
import math

class Images():# 圖檔
    def __init__(self,image,centerx,centery):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery
    def draw(self):
        screen.blit(self.image, self.rect)
    def change_scale(self,scale_x,scale_y):
        self.image = pygame.transform.scale(self.image , (scale_x,scale_y))    

class Text():# 文字
    def __init__(self,font,centerx,centery):
        self.text = font
        self.rect = self.text.get_rect()
        self.rect.center = (centerx,centery)
    def draw(self):
        screen.blit(self.text, self.rect)
        
class Ball():# 音符
    def __init__(self, x, y, image, speed_x, color):
        self.image = image
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.color = color
        self.alive = True
    def draw(self):
        if self.alive:
            self.image.rect = self.image.image.get_rect(center=(self.x, self.y))
            self.image.change_scale(200, 130)
            self.image.draw()
    def update(self):
        self.x -= self.speed_x
        if self.x < 0:
            self.alive = False
    def detect(self, score, score_text):
        if self.x >= 170 and self.x <= 210 and self.alive:
            if self.alive:
                score[0] += 5
                score_text[0] = font.render("score:" + str(score[0]), True, (255, 255, 255))
                screen.blit(text, (350, 200))
                self.alive = False
        
def check_quit_event():
    # Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def DrawDrum(screen,color,keys):# 遊戲畫面的鼓
    pygame.draw.circle(screen, color["white"], (400, 350), 75, 0)
    pygame.draw.circle(screen, color["black"], (400, 350), 53, 3)
    pygame.draw.line(screen, color["black"], (400,275), (400,425),3)
    if keys[pygame.K_f]:
        pygame.draw.arc(screen, color["Red"], pygame.Rect(350, 300, 100, 100), math.pi/2, math.pi*3/2, 55)

    if keys[pygame.K_j]:
        pygame.draw.arc(screen, color["Red"], pygame.Rect(350, 300, 100, 100), -math.pi/2, math.pi/2, 55)

    if keys[pygame.K_d]:
        pygame.draw.arc(screen, color["Blue"], pygame.Rect(325, 275, 150, 150), math.pi/2, math.pi*3/2, 25)

    if keys[pygame.K_k]:
        pygame.draw.arc(screen, color["Blue"], pygame.Rect(325, 275, 150, 150), -math.pi/2, math.pi/2, 25)

def change_music_choose(keys,music_choose,triangle):#移動選擇箭頭
    if keys[pygame.K_UP] and music_choose[0] == 2:
        music_choose[0] -= 1

    if keys[pygame.K_DOWN] and music_choose[0] == 1:
        music_choose[0] += 1

    if music_choose[0] == 1:
        for i in range(3):
            triangle[i] = triangle_points1[i]
    
    if music_choose[0] == 2:
        for i in range(3):
            triangle[i] = triangle_points2[i]

def music_play(musicfile):# 播放音樂
    pygame.mixer.music.pause()
    pygame.mixer.music.load(musicfile)
    pygame.time.delay(10)
    pygame.mixer.music.play()

pygame.init()
pygame.mixer.init()
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("太鼓達人")

color = {"white":(255,255,255), "black":(0,0,0), "Red":(255,0,0), "Blue":(0,0,255)}

# 設置字型和字體大小
font = pygame.font.Font("Fonts/msjh.ttc", 36)

# 音樂選擇畫面的文字
song_name1 = Text(font.render('基礎教學', True, color["white"]),400,150)
song_name2 = Text(font.render('千本櫻', True, color["white"]),400,250)
difficulty = Text(font.render('★★★★★★★★★★', True, color["white"]),400,300)
sentence1 = Text(font.render('按 f 或 j 擊打紅色音符', True, color["white"]),200,200)
sentence2 = Text(font.render('按 d 或 k 擊打藍色音符', True, color["white"]),600,200)
sentence3 = Text(font.render('打中各加5分', True, color["white"]),150,300)
# 初始化分數
score = [0]
# 創建分數的文本
score_text = [font.render("score:" + str(score[0]), True, color["white"])]

Game_Time = 0

music_choose = [1]
triangle_points1 = [(320, 150), (300, 160), (300, 140)]
triangle_points2 = [(320, 250), (300, 260), (300, 240)]
triangle = [(0,0),(0,0),(0,0)]

#音樂
musicfile1 = "music.wav"
musicfile2 = "John Cena.mp3"
music_play(musicfile2)
# musicfile4 = pygame.mixer.Sound("don.mp3")
# musicfile5 = pygame.mixer.Sound("ka.mp3")
# musicfile4.set_volume(0.5)
# musicfile5.set_volume(0.5)

#匯入圖片
start_button = Images(pygame.image.load("start_button.png"),795,300)
start_button.change_scale(350,50)
red_button = Images(pygame.image.load("red_button.png"),0,0)
blue_button = Images(pygame.image.load("blue_button.png"),0,0)

title = Images(pygame.image.load("title.png"),400,100)
background1 = Images(pygame.image.load("background1.png"),950,540)
background1.change_scale(810,500)
background2 = Images(pygame.image.load("background2.png"),600,360)
background2.change_scale(810,500)

flash_interval = 500  # 閃爍間隔時間
last_flash_time = pygame.time.get_ticks()  # 上次閃爍的時間
is_flashing = False  # 是否正在閃爍

ListTime =  [1,4,7,9,12,15,17,20,23,25,29,33,36,39,41,44,47,49,53,57,61,65,67,69,70,71,73,75,77,78,79,81,83,85,86,87,89,91,92,93,95,97,99,101,102,103,105,107,109,110,111,113,115,117,119,121,122,123,125,127,129,131,133,134,135,137,139,141,142,143,145,147,149,150,151,153,155,156,157,159,161,163,164,165,167,168,169,171,173,174,175,176,177,179,180,181,183,185,189,191,193,195,197,198,199,201,203,205,206,207,209,211,213,214,215,217,219,220,221,223,225,227,229,230,231,233,235,237,238,239,241,243,245,247,249,250,251,253,255,257,259,261,262,263,265,267,269,270,271,273,275,277,278,279,281,283,284,285,287,289,290,291,293,294,295,297,299,301,303,305,308,311,321,325,328,329,330,331,333,335,337,341,345,347,349,353,357,360,361,362,363,365,367,369,373,377,378,379,381,385,389,392,393,394,395,397,399,401,405,409,411,413,417,421,424,425,426,427,429,433,437,441,445,449,453,457,461,465,467,468,469,471,473,481,485,489,493,497,499,500,501,503,505,507,508,509,513,517,521,525,529,531,532,533,535,537,541,543,545,547,551,553,557,561,565,567,577,579,580,581,583,585,587,588,589,591,593,594,595,597,599,601,605,607,609,611,612,613,615,617,619,620,621,623,625,627,628,629,631,633,637,639,641,643,644,645,647,649,651,652,653,655,657,658,659,661,663,665,669,671,673,677,681,685,689,691,693,695,697,701,703,705,707,708,709,711,713,715,716,717,719,721,723,724,725,727,729,733,735,737,739,740,741,743,745,747,748,749,751,753,755,756,757,759,761,765,767,769,771,772,773,775,777,779,780,781,783,785,787,788,789,791,793,797,799,801,805,809,813,817,819,821,823]
blue = [25,29,49,53,61,65,67,73,75,81,83,97,99,105,107,115,117,119,121,122,123,125,127,129,131,137,139,145,147,163,164,165,171,173,174,175,176,177,179,180,181,183,185,193,195,201,203,209,211,225,227,233,235,243,245,247,249,250,251,253,255,257,259,265,267,273,275,293,294,295,301,303,325,328,330,333,335,341,349,357,360,362,365,367,373,381,389,392,394,397,399,405,413,421,424,426,429,441,445,449,453,469,489,493,497,499,500,509,513,517,533,577,581,585,589,593,594,595,601,611,612,615,619,620,623,629,633,641,645,649,653,657,658,659,665,673,677,681,685,707,708,711,715,716,719,725,729,739,740,743,747,748,751,757,761,771,772,775,779,780,783,789,793,801,805,809,813,821,823]

# 定義文字内容
text = font.render("Perfect", True, color["white"])

# 關鍵參數
note_speed = 10
note_speed2 = 5
music_start_time = 56
bpm_setting = 3.747
# 這個數字越大 球球跑得越慢
# 這個數字越小 球球跑得越快

# Game loop
is_running = True
is_running2 = True
is_running3 = True
while is_running:

    is_running = check_quit_event()

    # 偵測鍵盤輸入    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        pygame.mixer.music.pause()
        while is_running:
            
            is_running = check_quit_event()

            keys = pygame.key.get_pressed()
            
            change_music_choose(keys,music_choose,triangle)
        
            if keys[pygame.K_UP] and music_choose[0] == 1:
                music_play(musicfile1)
                pygame.mixer.music.pause()

            if keys[pygame.K_DOWN] and music_choose[0] == 2:
                music_play(musicfile1)
            
            if keys[pygame.K_SPACE]:
                
                pygame.mixer.music.pause()
                if music_choose[0] == 1:
                    #重置各種參數
                    balls = []
                    now = 0
                    blue_now = 0
                    red_balls = []
                    blue_balls = []
                    end_time = 0
                    Game_Time = 0
                    score = [0]
                    score_text[0] = font.render("score:" + str(score[0]), True, (255, 255, 255))
                    is_running3 = True
                    # 產生一個紅色音符
                    ball2 = Ball(850, 120, red_button, note_speed2, "red")
                    red_balls.append(ball2)
                    balls.append(ball2)
                    while is_running3:

                        is_running3 = check_quit_event()
                        is_running = is_running3
                        #更新遊戲時間
                        Game_Time += 1
                        # 產生一個藍色音符
                        if Game_Time == 20:
                            ball1 = Ball(850, 120, blue_button, note_speed2, "blue")
                            blue_balls.append(ball1)
                            balls.append(ball1)

                        screen.fill(color["black"])
                        keys = pygame.key.get_pressed()
                        # 音符在特定位置時偵測按鍵
                        if keys[pygame.K_f] or keys[pygame.K_j]:
                            for item in red_balls:
                                item.detect(score, score_text)

                        if keys[pygame.K_d] or keys[pygame.K_k]:
                            for item in blue_balls:
                                item.detect(score, score_text)

                        screen.blit(score_text[0], (10, 10))
                        # 畫出判定位置的圓
                        pygame.draw.circle(screen, color["white"], (200, 120), 33, 2)
                        # 畫出下面的鼓
                        DrawDrum(screen,color,keys)
                        for item in balls:
                            item.draw()
                            item.update()

                        if keys[pygame.K_ESCAPE]:
                            music_choose = [1]
                            pygame.mixer.music.pause()
                            is_running3 = False

                        sentence1.draw()
                        sentence2.draw()
                        sentence3.draw()
                        pygame.display.update()
                        pygame.time.Clock().tick(60)

                if music_choose[0] == 2:
                    #重置各種參數
                    balls = []
                    now = 0
                    blue_now = 0
                    red_balls = []
                    blue_balls = []
                    end_time = 0
                    Game_Time = 0
                    score = [0]
                    score_text[0] = font.render("score:" + str(score[0]), True, (255, 255, 255))
                    is_running2 = True
                    while is_running2:
                            
                        is_running2 = check_quit_event()
                        is_running = is_running2
                        
                        if music_choose[0] == 2 and Game_Time == music_start_time:
                            music_play(musicfile1)

                        if Game_Time > 823*bpm_setting:
                            end_time += 1
                        
                        elif Game_Time == int(ListTime[now]*bpm_setting):
                            now += 1
                            
                            if Game_Time == int(blue[blue_now]*bpm_setting):
                                ball = Ball(850, 120, blue_button, note_speed, "blue")
                                blue_balls.append(ball)
                                blue_now += 1
                            else:
                                ball = Ball(850, 120, red_button, note_speed, "red")
                                red_balls.append(ball)
                            balls.append(ball)
                        
                        screen.fill(color["black"])
                            
                        keys = pygame.key.get_pressed()
                                                
                        # 音符在特定位置時偵測按鍵
                        for item in red_balls:
                            if keys[pygame.K_f] or keys[pygame.K_j] or (item.x >= 170 and item.x <= 210):
                            #for item in red_balls:
                                item.detect(score, score_text)

                        for item in blue_balls:
                            if keys[pygame.K_d] or keys[pygame.K_k] or (item.x >= 170 and item.x <= 210):
                                #for item in blue_balls:
                                    item.detect(score, score_text)
                        
                        # 在屏幕上繪製分數
                        screen.blit(score_text[0], (10, 10))
                        # 畫出判定位置的圓
                        pygame.draw.circle(screen, color["white"], (200, 120), 33, 2)
                        # 畫出下面的鼓
                        DrawDrum(screen,color,keys)
                        # 移動音符
                        for item in balls:

                            item.draw()
                            item.update()

                        #更新遊戲時間    
                        Game_Time += 1
                        
                        #遊戲結束回到選單
                        if end_time >= 105 or keys[pygame.K_ESCAPE]:
                            music_choose = [1]
                            pygame.mixer.music.pause()
                            is_running2 = False
            
                        pygame.display.update()
                        pygame.time.Clock().tick(60)
                
            screen.fill(color["black"])
            background2.draw()

            current_time = pygame.time.get_ticks()
            # 閃爍
            if current_time - last_flash_time >= flash_interval:
                is_flashing = not is_flashing
                last_flash_time = current_time

            if is_flashing:
                pygame.draw.polygon(screen, color["white"], triangle)

            song_name1.draw()
            song_name2.draw()
            difficulty.draw()
            pygame.display.update()
    
    screen.fill(color["white"])
    background1.draw()
    title.draw()

    current_time = pygame.time.get_ticks()
    # 閃爍
    if current_time - last_flash_time >= flash_interval:
        is_flashing = not is_flashing
        last_flash_time = current_time

    if is_flashing:
        start_button.draw()  

    pygame.display.update()
    
pygame.quit()