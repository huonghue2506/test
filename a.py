import pygame
from pygame.locals import *
import random
from pygame.sprite import Group
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
lane_move_y=0

# Road và edge
road=(100,0,road_width,height)
left_edge=(95,0,street_width,height)
right_edge=(395,0,street_width,height)
# Vị trí ban đầu của xe người chơi
player_x=250
player_y=400
# Đối tượng xe lưu thông
class Vehicle(pygame.sprite.Sprite):
    def __init__(self,image,x,y ):
        pygame.sprite.Sprite.__init__(self)
        # Scale images
        image_scale = 45 / image.get_rect().width
        new_width = image.get_rect().width*image_scale
        new_height = image.get_rect().height*image_scale
        self.image = pygame.transform.scale(image,(new_width,new_height))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
# Đối tượng xe player
class PlayerVehicle(Vehicle):
    def __init__(self,x,y):
        image = pygame.image.load('images/car.png')
        super().__init__(image,x,y)
# sprite group 
player_group = pygame.sprite.Group()
Vehicle_group= pygame.sprite.Group()
# Tạo xe người chơi
player = PlayerVehicle(player_x,player_y)
player_group.add(player)

# Load xe lưu thông
image_name = ['pickup_truck.png','semi_trailer.png','taxi.png','van.png']
Vehicle_image = []
for name in image_name:
    try:
     image = pygame.image.load('images/' + name)
     Vehicle_image.append(image)
    except Exception as e:
        print(f"Lỗi tải hình ảnh {name}:{e}")
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
    # vẽ road-đường chạy
    pygame.draw.rect(screen,gray,road)
    # vẽ edge- hành lang đường
    pygame.draw.rect(screen,yellow,left_edge)
    pygame.draw.rect(screen,yellow,right_edge)
    # vẽ lane đường
    lane_move_y+=speed * 2
    if lane_move_y >=street_height*2:
        lane_move_y=0
    for y in range(street_height* -2,height,street_height*2):
        pygame.draw.rect(screen,white,(left_lane+45,y + lane_move_y,street_width,street_height))
        pygame.draw.rect(screen,white,(center_lane+45,y + lane_move_y,street_width,street_height))
    # Vẽ xe player
    player_group.draw(screen)
    
    # Vẽ phương tiện giao thông
    if len(Vehicle_group) < 2:
        add_verhicle = True
        for verhicle in Vehicle_group:
            if verhicle.rect.top < verhicle.rect.height * 1.5:
                add_verhicle = False
        if add_verhicle:
                lane = random.choice(lanes)
                image= random.choice(Vehicle_image)
                verhicle=Vehicle(image,lane,height/-2)
                Vehicle_group.add(verhicle)
    # Cho xe công cộng chạy 
    for vehicle in Vehicle_group:
        vehicle.rect.y += speed
        # # Remove vehicle
        if vehicle.rect.top >= height:
            vehicle.kill()
            score += 1
            # Tăng tốc độ khó - chạy
            if score >0 and score % 5 ==0:
                speed+=1
    # Vẽ nhóm lưu thông xe 
    Vehicle_group.draw(screen)

pygame.display.update()
pygame.quit()