import sys, pygame
pygame.init()

size = width, height = 320, 240

screen = pygame.display.set_mode(size)

class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height, init_pos):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos

# 实例化精灵对象
sprite_1 = Block(pygame.Color(255,0,0),50,50,(50,50))
sprite_2 = Block(pygame.Color(0,225,0),50,50,(150,150))


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.blit(sprite_1.image,sprite_1.rect)
    screen.blit(sprite_2.image,sprite_2.rect)

    # 矩形检测碰撞
    rest = pygame.sprite.collide_rect(sprite_1,sprite_2)
    print('rest',rest)
    # 链式调用 定义碰撞面积
    rest2 = pygame.sprite.collide_circle_ratio(0.5)(sprite_1,sprite_2)
    print('rest2', rest2)
    pygame.display.flip()