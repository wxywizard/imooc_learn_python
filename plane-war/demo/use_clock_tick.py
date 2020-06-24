import pygame,sys

pygame.init()

screen = pygame.display.set_mode((500,500))

# 加载图片
image = pygame.image.load('./static/hero1.png')
image2 = pygame.image.load('./static/hero2.png')

# 获取帧速率对象
clock = pygame.time.Clock()

count = 0

while True:
    count += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    # 绘制背景
    screen.fill(pygame.Color(255,255,255))
    # 如果count被5整除切换
    if count % 5 == 0:
        # 绘制图片
        screen.blit(image,(20,20))
    else:
        screen.blit(image2,(20,20))
    pygame.display.flip()