import pygame
from pygame.locals import *
import random
pygame.init()
# Màu nền
gray=(100,100,100)
green=(76,208,56)
yellow=(255,232,0)
red=(200,0,0)
white=(255,255,255)

# tạo cửa sổ game
width =500
height=500
screen_size=(width,height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Game đua xe')

# khởi tạo biến
gameplay=False
speed=2
score=0
# đường xe chạy
road_width=300
street_width=10
street_height=50

# lane coordinates
left_lane=150
center_lane=250
right_lane=350
lanes=[left_lane,center_lane,right_lane]

# Road và edge
road=(100,0,road_width,height)
left_edge=(95,0,street_width,height)
right_edge=(395,0,street_width,height)


# cài đặt fps
clock=pygame.time.Clock()
fps =120
# Vòng lặp xử lý game
running = True
while running:
    # Chỉnh frame hình trên giây
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type==QUIT:
            running=False
    # Vẽ địa hình cỏ
    screen.fill(green)

    pygame.display.update()
pygame.quit()