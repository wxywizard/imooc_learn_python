import os

# 项目的根目录
import pygame

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 静态文件的目录
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

# 背景图片
BG_IMAGE = os.path.join(ASSETS_DIR, 'images/background.png')
BG_IMAGE_OVER = os.path.join(ASSETS_DIR, 'images/game_over.png')
# 标题图片
IMG_GAME_TITLE = os.path.join(ASSETS_DIR, 'images/game_title.png')
IMG_GAME_START_BTN = os.path.join(ASSETS_DIR, 'images/game_start.png')
# ryna头像
IMG_RYNA = os.path.join(ASSETS_DIR, 'images/ryna.png')
# 背景音乐
BG_MUSIC = os.path.join(ASSETS_DIR, 'sounds/game_bg_music.mp3')
# 游戏分数颜色
TEXT_SOCRE_COLOR = pygame.Color(255, 255, 0)
# 击中小型飞机添加10分
SCORE_SHOOT_SMALL = 10
# 游戏结果存储的文件地址
PLAY_RESULT_STORE_FILE = os.path.join(BASE_DIR, 'store/rest.txt')

# 我方飞机的静态资源
OUR_PLANE_IMG_LIST = [os.path.join(ASSETS_DIR, 'images/hero1.png'),
                      os.path.join(ASSETS_DIR, 'images/hero2.png')
                      ]
# 坠毁图片
OUR_DESTROY_IMG_LIST = [
    os.path.join(ASSETS_DIR, 'images/hero_broken_n1.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n2.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n3.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n4.png')
]

# 子弹图片
BULLET_IMG = os.path.join(ASSETS_DIR, 'images/bullet1.png')
# 子弹发射声音
BULLET_SHOOT_SOUND = os.path.join(ASSETS_DIR, 'sounds/bullet.wav')

# 敌方小型飞机图片及音效
SMALL_ENEMY_PLANE_IMG_LIST = [os.path.join(ASSETS_DIR, 'images/enemy1.png')]
SMALL_ENEMY_DESTROY_IMG_LIST = [
    os.path.join(ASSETS_DIR, 'images/enemy1_down1.png'),
    os.path.join(ASSETS_DIR, 'images/enemy1_down2.png'),
    os.path.join(ASSETS_DIR, 'images/enemy1_down3.png'),
    os.path.join(ASSETS_DIR, 'images/enemy1_down4.png')
]
SMALL_ENEMY_PLANE_DOWN_SOUND = os.path.join(ASSETS_DIR, 'sounds/enemy1_down.wav')

# 字体
PLAY_FONT = os.path.join(ASSETS_DIR, 'images/STXINWEI.TTF')