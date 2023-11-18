import sys
import random
import pygame
from pygame.locals import *
from random import random

match_value = [[1, 1], [1, 1]]

def main(): 
  # ゲーム画面を初期化
  pygame.init()
  screen_width, screen_height = 800, 600
  screen = pygame.display.set_mode((screen_width, screen_height))
  black = (0, 0, 0)
  
  # 表示テキストの初期化
  font = pygame.font.Font(None, 36)  # デフォルトのフォント、サイズ36
  text = "(" +  str(match_value[0][0]) + ", " +  str(match_value[0][1]) + ") : (" + str(match_value[1][0])  + ", " + str(match_value[1][1]) + ")"
  text_surface = font.render(text, True, (255, 255, 255))  # 白色の文字
  text_rect = text_surface.get_rect()
  text_rect.center = (screen_width // 2, screen_height // 2)
  clock = pygame.time.Clock()  # クロックオブジェクトの初期化
  fps = 1  # フレームレートの設定
  
  # 繰り返し画面を描画 
  while True:
      screen.fill(black)  
      screen.blit(text_surface, text_rect)
      attack_random(0, 1)
      attack_random(1, 0)
      
      clock.tick(fps)
      
      # 表示テキストの更新
      text = "(" +  str(match_value[0][0]) + ", " +  str(match_value[0][1]) + ") : (" + str(match_value[1][0])  + ", " + str(match_value[1][1]) + ")"
      text_surface = font.render(text, True, (255, 255, 255))  # 白色の文字
      text_rect = text_surface.get_rect()
      text_rect.center = (screen_width // 2, screen_height // 2)
      
      # 画面を更新 
      pygame.display.update()
      
      # 終了イベントを確認 
      for event in pygame.event.get():
          if event.type == QUIT:
              pygame.quit()
              sys.exit()
              
def attack_random(attack_player_num, receive_player_num):
    attack_hand_num = 0
    
    # 自分のどちらの手で攻撃するかの決定
    if  (match_value[attack_player_num][0] >= 5):
      attack_hand_number = 1
    elif(match_value[attack_player_num][1] >= 5):
      attack_hand_number = 0
    
    elif (random() < 0.5):
      attack_hand_number = 0
    else :
      attack_hand_num = 1

    # 相手のどちらかの手を攻撃するかの決定と攻撃
    if (match_value[receive_player_num][0] >= 5):
      match_value[receive_player_num][1] += match_value[attack_player_num][attack_hand_num]
    if (match_value[receive_player_num][1] >= 5):
      match_value[receive_player_num][0] += match_value[attack_player_num][attack_hand_num]
      
    if (random() < 0.5) :
      match_value[receive_player_num][0] += match_value[attack_player_num][attack_hand_num]
    else:
      match_value[receive_player_num][1] += match_value[attack_player_num][attack_hand_num]
    
    """
      // 自分のどちらの手で攻撃するかの決定
      // どちらかの自分の手が5以上の場合
      if (matchValue[attackSideNumber][0] >= 5) {
        attackHandNumber = 1;
      }
      else if (matchValue[attackSideNumber][1] >= 5) {
        attackHandNumber = 0;
      }
      // どちらの自分の手も5未満の場合
      // 0で攻撃する場合
      else if (p.random() < 0.5) {
        attackHandNumber = 0;
      }
      // 1で攻撃する場合
      else {
        attackHandNumber = 1;
      }

      // 相手のどちらかの手を攻撃するかの決定と攻撃
      // どちらかの相手の手が5以上の場合
      if (matchValue[receiveSideNumber][0] >= 5) {
        matchValue[receiveSideNumber][1] += matchValue[attackSideNumber][attackHandNumber];
      }
      else if (matchValue[receiveSideNumber][1] >= 5) {
        matchValue[receiveSideNumber][0] += matchValue[attackSideNumber][attackHandNumber];
      }
      // どちらの自分の手も5未満の場合
      // 0を攻撃する場合
      else if (p.random() < 0.5) {
        matchValue[receiveSideNumber][0] += matchValue[attackSideNumber][attackHandNumber];
      }
      // 1を攻撃する場合
      else {
        matchValue[receiveSideNumber][1] += matchValue[attackSideNumber][attackHandNumber];
      }
    """
              
if __name__ == "__main__":
    main()
