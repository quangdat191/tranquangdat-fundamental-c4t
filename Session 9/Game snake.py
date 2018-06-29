import pygame
import sys
from pygame.locals import *
from random import*
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
window_height = 300
window_width = 400
display_surf = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Snake")
fps = 10
fps_clock = pygame.time.Clock()
class Pixel:
    def __init__(self,x,y,w,h,COLOR):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(x,y,w,h)
        self.COLOR = COLOR
    def draw(self):
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)

        pygame.draw.rect(display_surf,self.COLOR,self.rect)

class Apple:
    def __init__(self,w,h,x,y,COLOR):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.COLOR = COLOR
        self.rect = pygame.Rect(x, y, w, h)
    def draw(self):
        pygame.draw.rect(display_surf,self.COLOR,self.rect)
    def pos(self):
             self.COLOR = BLACK
             pygame.draw.rect(display_surf,self.COLOR,self.rect)

             while True:
                 x = randint(20, window_width - 21)
                 y = randint(20, window_height - 21)
                 if x % 10 == 0 and y % 10 == 0:
                    if display_surf.get_at((x,y)) == WHITE:
                        continue
                    elif display_surf.get_at((x,y)) == BLACK:
                        self.x = x
                        self.y = y
                        self.COLOR = GREEN
                        self.rect = pygame.Rect(x,y,self.w,self.h)
                        pygame.draw.rect(display_surf, self.COLOR, self.rect)
                        break

class Snake:
    speed = 10
    body = []
    direction = "..."
    def __init__(self,length,speed,x,y,w,h):
       self.head = Pixel(x, y, w, h, WHITE)
       self.length = length
       self.speed = speed
       for i in range(length):
           self.body.append(Pixel(self.head.x-(i*10),self.head.y,self.head.w,self.head.h,WHITE))
       self.head = self.body[0]
    def move_right(self):
        for i in range(len(self.body)):
            if i >0:
                self.body[len(self.body)-i].x = self.body[len(self.body)-i-1].x
                self.body[len(self.body) - i].y = self.body[len(self.body) - i - 1].y
        self.body[0].x += self.speed
        self.head = self.body[0]
    def move_left(self):
       for i in range(len(self.body)):
           if i > 0:
               self.body[len(self.body) - i].x = self.body[len(self.body) - i - 1].x
               self.body[len(self.body) - i].y = self.body[len(self.body) - i - 1].y
       self.body[0].x -= self.speed
       self.head = self.body[0]
    def move_up(self):
       for i in range(len(self.body)):
           if i > 0:
               self.body[len(self.body) - i].x = self.body[len(self.body) - i - 1].x
               self.body[len(self.body) - i].y = self.body[len(self.body) - i - 1].y
       self.body[0].y -= self.speed
       self.head = self.body[0]
    def move_down(self):
       for i in range(len(self.body)):
           if i > 0:
               self.body[len(self.body) - i].x = self.body[len(self.body) - i - 1].x
               self.body[len(self.body) - i].y = self.body[len(self.body) - i - 1].y
       self.body[0].y += self.speed
       self.head = self.body[0]
    def draw_snake(self):
       for i in self.body:
           i.draw()
    def move(self):
       self.head.COLOR = BLACK
       self.head.draw()
    def hit(self):
        if self.head.rect.bottom >= window_height - 10 or self.head.rect.top <= 5 or self.head.rect.right >= window_width - 10 or self.head.rect.left <= 5:
            return True
        else:
            return False

class Scoreboard:
   def __init__(self,fontsize = 20,score = 0):
       self.x = window_width - 150
       self.y = 20
       self.score = score
       self.font = pygame.font.Font('freesansbold.ttf',fontsize)
   def display(self,score):
       result_srf = self.font.render('Score: %s' %score, True, WHITE)
       result_rect = result_srf.get_rect()
       result_rect.topleft = (window_width - 150, 20)
       display_surf.blit(result_srf,result_rect)

class Box:
   def draw_box(self):
       display_surf.fill ((255, 255, 255))
       pygame.draw.rect (display_surf, BLACK, (5, 5, window_width - 10, window_height - 10))

class Game:
    def __init__(self):
       self.snake = Snake(3,10,100,100,10,10)
       self.apple = Apple(10,10,20,20,GREEN)
       self.box = Box()
       self.score = Scoreboard()
    def update(self):
       self.box.draw_box()
       self.snake.draw_snake()
       self.apple.draw()
       if self.apple.x == self.snake.head.x and self.apple.y == self.snake.head.y:
            self.apple.pos()
            self.score.score += 1
            self.snake.body.append(Pixel(self.snake.body[len(self.snake.body)-1].x,self.snake.body[len(self.snake.body)-1].y,self.snake.body[len(self.snake.body)-1].w,self.snake.body[len(self.snake.body)-1].h,self.snake.body[len(self.snake.body)-1].COLOR))
            global fps
            fps += 1
       self.score.display(self.score.score)

def main():
   pygame.init()
   box = Box()
   game = Game()
   # apple = Apple(10,10,20,20,GREEN)
   # snake = Snake(3,10,100,100,10,10)
   while True:
        for event in pygame.event.get():
            if event.type == QUIT:
               pygame.quit()
               sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    game.snake.direction = "RIGHT"
                elif event.key == K_LEFT:
                    game.snake.direction = "LEFT"
                elif event.key == K_UP:
                    game.snake.direction = "UP"
                elif event.key == K_DOWN:
                    game.snake.direction = "DOWN"
        if game.snake.direction == "RIGHT": game.snake.move_right()
        elif game.snake.direction == "LEFT": game.snake.move_left()
        elif game.snake.direction == "UP": game.snake.move_up()
        elif game.snake.direction == "DOWN": game.snake.move_down()
        if game.snake.hit():
            break
        game.update()
        pygame.display.update()

        fps_clock.tick(fps)

if __name__ == '__main__':
   main()


