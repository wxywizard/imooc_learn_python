import sys,pygame

# 初始化pygame
pygame.init()

# 屏幕对象
screen = pygame.display.set_mode((500,500))

#加载图片
ball = pygame.image.load('intro_ball.gif')

red = pygame.Color(255,0,0)

# 游戏主循环
while True:
    #处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #更新状态

    # 画线
    pygame.draw.line(screen,red,(10,10),(200,200),10)

    # 画矩形
    pygame.draw.rect(screen,red,(10,20,200,300),10)

    # 画圆
    pygame.draw.circle(screen,red,(100,100),50,5)

    #绘制
    screen.blit(ball,(100,100))
    pygame.display.flip()