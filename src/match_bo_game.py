import sys
import random
import pygame
from pygame.locals import *

# ゲーム画面を初期化 --- (*1)
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
black = (0, 0, 0)
# フォントの初期化
font = pygame.font.Font(None, 36)  # デフォルトのフォント、サイズ36
# 配列を文字列に変換
match_value = [[1, 2], [3, 4]]
text = "(" +  str(match_value[0][0]) + ", " +  str(match_value[0][1]) + ") : (" + str(match_value[1][0])  + ", " + str(match_value[1][1]) + ")"

# 文字列を描画
text_surface = font.render(text, True, (255, 255, 255))  # 白色の文字

# 文字列の位置
text_rect = text_surface.get_rect()
text_rect.center = (screen_width // 2, screen_height // 2)


# 繰り返し画面を描画 --- (*2)
while True:
    # 背景と円を描画 --- (*3)
    screen.fill(black)  # 背景を黒で塗りつぶす
    # pygame.draw.circle(screen, white, (300, 200), 150)  # 円を描画
    screen.blit(text_surface, text_rect)
    
    # 画面を更新 --- (*4)
    pygame.display.update()
    # 終了イベントを確認 --- (*5)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def add(a, b):
  return a + b