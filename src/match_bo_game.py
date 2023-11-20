import json
import sys
import random
import pygame
from pygame.locals import *
from random import random
import math

match_value = [[1, 1], [1, 1]]
winner_number = -1

player0_win_count = 0
player1_win_count = 0
turn_count = 1
heuristic_player_number = 0
new_log = {
  "heuristic_player_number": heuristic_player_number
}



def main(): 
  # ゲーム画面を初期化
  pygame.init()
  screen_width, screen_height = 800, 600
  screen = pygame.display.set_mode((screen_width, screen_height))
  black = (0, 0, 0)
  
  # 表示テキストの初期化
  # font_path = pygame.font.match_font('arial')
  font_path = pygame.font.match_font('arialunicodems')
  font = pygame.font.Font(font_path, 36)  # デフォルトのフォント、サイズ36
  text = "(" +  str(match_value[0][0]) + ", " +  str(match_value[0][1]) + ") : (" + str(match_value[1][0])  + ", " + str(match_value[1][1]) + ")"
  text_surface = font.render(text, True, (255, 255, 255))  # 白色の文字
  text_rect = text_surface.get_rect()
  text_rect.center = (screen_width // 2, screen_height // 2 )
  clock = pygame.time.Clock()  # クロックオブジェクトの初期化
  fps = 60  # フレームレートの設定
  global turn_count
  global heuristic_player_number
  
  # 繰り返し画面を描画 
  while True:
      screen.fill(black)  
      screen.blit(text_surface, text_rect)
      
      # ゲームが続いている場合
      if(is_game_looped()):
        # 先攻プレイヤーの行動
        if (turn_count % 2 == 1):
          if((heuristic_player_number == 0) | (heuristic_player_number == 2)):
            # attack_heuristic(0, 1)
            # attack_heuristic_save_life(0, 1)
            attack_heuristic_save_life_re(0, 1)
          else:
            attack_random(0, 1)

          print (str(match_value[0]) +"->" + str(match_value[1]))
          new_log[turn_count] = str(match_value[0]) +"->" + str(match_value[1])
        # 後攻プレイヤーの行動
        else:
          if((heuristic_player_number == 1) | (heuristic_player_number == 2)):
            # attack_heuristic(1, 0)
            # attack_heuristic_save_life(1, 0)
            attack_heuristic_save_life_re(1, 0)
          else:
            attack_random(1, 0)

          print (str(match_value[0]) +"<-" + str(match_value[1]))
          new_log[turn_count] = (str(match_value[0]) +"<-" + str(match_value[1]))


        # 変数の更新
        turn_count += 1
        
      # ゲームが終わっている場合
      else:
        text_score = "player0 win rate = " + str(player0_win_count / (player0_win_count + player1_win_count) * 100) + ", player1 win rate = " + str(player1_win_count / (player0_win_count + player1_win_count) * 100)
        print("winner is player: " + str(winner_number) + " (heuristic is player: " + str(heuristic_player_number) + ")")
        # save_score()
        if (winner_number != heuristic_player_number):
          save_log()
        initialize_variables()
      
      clock.tick(fps)
      
      
      # 表示テキストの更新
      text = "(" +  str(match_value[0][0]) + ", " +  str(match_value[0][1]) + ") : (" + str(match_value[1][0])  + ", " + str(match_value[1][1]) + ")"
      if((player1_win_count != 0) & (player0_win_count != 0)):
        text_score = "\nplayer0 win(" +str(player0_win_count) + "): " + str(math.floor(player0_win_count / (player0_win_count + player1_win_count) * 100)) + "%, player1 win("+ str(player1_win_count) +"): " + str(math.floor(player1_win_count / (player0_win_count + player1_win_count) * 100)) + "%"
        text = text + text_score
      text_surface = font.render(text, True, (255, 255, 255))  # 白色の文字
      text_rect = text_surface.get_rect()
      text_rect.center = (screen_width // 2, screen_height // 2)
      
      # 画面を更新 
      pygame.display.update()
      
      # 終了イベントを確認 
      for event in pygame.event.get():
          if event.type == QUIT:
              text_score = "player0 win rate = " + str(player0_win_count / (player0_win_count + player1_win_count) * 100) + ", player1 win rate = " + str(player1_win_count / (player0_win_count + player1_win_count) * 100)
              print(text_score)
              pygame.quit()
              sys.exit()


def initialize_variables():
  global turn_count
  global new_log
  turn_count = 1
  match_value[0][0] = 1
  match_value[0][1] = 1
  match_value[1][0] = 1
  match_value[1][1] = 1
  new_log = {
    "heuristic_player_number": heuristic_player_number
  }

def is_game_looped():
  global player0_win_count
  global player1_win_count
  global winner_number
  
  
  if((match_value[0][0] >= 5) & (match_value[0][1] >= 5)):
    winner_number = 1
    player1_win_count += 1
    return False
  
  elif ((match_value[1][0] >= 5) & (match_value[1][1] >= 5)):
    winner_number = 0
    player0_win_count += 1
    return False
  
  else:
    return True
  
def attack_random(attack_player_num, receive_player_num):
    attack_hand_num = 0
    
    # 自分のどちらの手で攻撃するかの決定
    if(match_value[attack_player_num][0] >= 5):
      attack_hand_num = 1
    elif(match_value[attack_player_num][1] >= 5):
      attack_hand_num = 0
    
    elif(random() < 0.5):
      attack_hand_num= 0
    else :
      attack_hand_num = 1

    # 相手のどちらかの手を攻撃するかの決定と攻撃
    if (match_value[receive_player_num][0] >= 5):
      match_value[receive_player_num][1] += match_value[attack_player_num][attack_hand_num]
    elif (match_value[receive_player_num][1] >= 5):
      match_value[receive_player_num][0] += match_value[attack_player_num][attack_hand_num]
      
    elif (random() < 0.5) :
      match_value[receive_player_num][0] += match_value[attack_player_num][attack_hand_num]
    else:
      match_value[receive_player_num][1] += match_value[attack_player_num][attack_hand_num]
      
def attack_heuristic(attack_player_num, receive_player_num):
    attack_hand_num = 0
    
    # 自分のどちらの手で攻撃するかの決定
    if(match_value[attack_player_num][0] >= 5):
      attack_hand_num = 1
    elif(match_value[attack_player_num][1] >= 5):
      attack_hand_num = 0
      
    elif(match_value[attack_player_num][0] > match_value[attack_player_num][1]):
      attack_hand_num = 0
    else:
      attack_hand_num = 1

    # 相手のどちらかの手を攻撃するかの決定と攻撃
    if (match_value[receive_player_num][0] >= 5):
      match_value[receive_player_num][1] += match_value[attack_player_num][attack_hand_num]
    elif (match_value[receive_player_num][1] >= 5):
      match_value[receive_player_num][0] += match_value[attack_player_num][attack_hand_num]
      
    elif (match_value[receive_player_num][0] > match_value[receive_player_num][1]):
      match_value[receive_player_num][0] += match_value[attack_player_num][attack_hand_num]
    else: 
      match_value[receive_player_num][1] += match_value[attack_player_num][attack_hand_num]
      
def attack_heuristic_save_life(attack_player_num, receive_player_num):
    attack_hand_num = 0
    receive_hand_num = 0
    
    # 自分のどちらの手で攻撃するかの決定
    if(match_value[attack_player_num][0] >= 5):
      attack_hand_num = 1
    elif(match_value[attack_player_num][1] >= 5):
      attack_hand_num = 0
      
    # 自分のいずれかの手で攻撃した際に相手を倒せる場合
    elif(((match_value[attack_player_num][0] + match_value[receive_player_num][0] >= 5)&(match_value[receive_player_num][0] < 5)) | ((match_value[attack_player_num][0] + match_value[receive_player_num][1] >= 5)&(match_value[receive_player_num][1] < 5)) ):
      attack_hand_num = 0
    elif(((match_value[attack_player_num][1] + match_value[receive_player_num][0] >= 5)&(match_value[receive_player_num][0] < 5)) | ((match_value[attack_player_num][1] + match_value[receive_player_num][1] >= 5)&(match_value[receive_player_num][1] < 5)) ):
      attack_hand_num = 1
    # 自分のいずれの手で攻撃した際に相手を倒せない場合
    elif(match_value[attack_player_num][0] < match_value[attack_player_num][1]):
      attack_hand_num = 0
    else:
      attack_hand_num = 1


    # 相手のどちらかの手を攻撃するかの決定
    if (match_value[receive_player_num][0] >= 5):
      receive_hand_num = 1
    elif (match_value[receive_player_num][1] >= 5):
      receive_hand_num = 0
      
    # 自分のいずれかの手で攻撃した際に相手を倒せる場合
    elif(match_value[attack_player_num][attack_hand_num] + match_value[receive_player_num][0] >= 5):
      receive_hand_num = 0
    elif(match_value[attack_player_num][attack_hand_num] + match_value[receive_player_num][1] >= 5):
      receive_hand_num = 1
    # 自分のいずれの手で攻撃した際に相手を倒せない場合
    elif(match_value[receive_player_num][0] < match_value[receive_player_num][1]):
      receive_hand_num = 0
    else:
      receive_hand_num = 1
      
    # 攻撃
    match_value[receive_player_num][receive_hand_num] += match_value[attack_player_num][attack_hand_num]
    
    
def attack_heuristic_save_life_re(attack_player_num, receive_player_num):
    attack_hand_num = 0
    receive_hand_num = 0
    
    # 自分のどちらの手で攻撃するかの決定
    if(match_value[attack_player_num][0] >= 5):
      attack_hand_num = 1
    elif(match_value[attack_player_num][1] >= 5):
      attack_hand_num = 0
      
    # 自分のいずれかの手で攻撃した際に相手を倒せる場合
    elif(((match_value[attack_player_num][0] + match_value[receive_player_num][0] >= 5)&(match_value[receive_player_num][0] < 5)) | ((match_value[attack_player_num][0] + match_value[receive_player_num][1] >= 5)&(match_value[receive_player_num][1] < 5)) ):
      attack_hand_num = 0
    elif(((match_value[attack_player_num][1] + match_value[receive_player_num][0] >= 5)&(match_value[receive_player_num][0] < 5)) | ((match_value[attack_player_num][1] + match_value[receive_player_num][1] >= 5)&(match_value[receive_player_num][1] < 5)) ):
      attack_hand_num = 1
    # 自分のいずれの手で攻撃した際に相手を倒せない場合
    elif(match_value[attack_player_num][0] < match_value[attack_player_num][1]):
      attack_hand_num = 0
    else:
      attack_hand_num = 1


    # 相手のどちらかの手を攻撃するかの決定
    if (match_value[receive_player_num][0] >= 5):
      receive_hand_num = 1
    elif (match_value[receive_player_num][1] >= 5):
      receive_hand_num = 0
      
    # 自分のいずれかの手で攻撃した際に相手を倒せる場合
    elif(match_value[attack_player_num][attack_hand_num] + match_value[receive_player_num][0] >= 5):
      receive_hand_num = 0
    elif(match_value[attack_player_num][attack_hand_num] + match_value[receive_player_num][1] >= 5):
      receive_hand_num = 1
    # 自分のいずれの手で攻撃した際に相手を倒せない場合
    elif(match_value[receive_player_num][0] < match_value[receive_player_num][1]):
      receive_hand_num = 0
    else:
      receive_hand_num = 1
      
    # 攻めが[2,2], 受けが[1,2]の場合
    if((match_value[attack_player_num][0] == match_value[attack_player_num][1] == 2)):
      if((match_value[receive_player_num][0] == 1)&(match_value[receive_player_num][1] == 2)):
        receive_hand_num = 1
      elif((match_value[receive_player_num][0] == 2)&(match_value[receive_player_num][1] == 1)):
        receive_hand_num = 0
      
    # 攻撃
    match_value[receive_player_num][receive_hand_num] += match_value[attack_player_num][attack_hand_num]
      
def save_log():

  # ログの記録
  global new_log
  with open('data/log.json', 'r') as json_file:
    log_data = json.load(json_file)
    if new_log not in log_data:
      log_data.append(new_log)
      
      with open('data/log.json', 'w') as json_file:
        json.dump(log_data, json_file, indent=2)
        

def save_score():
  #json形式への書き出しと保存
  new_data = {
      #"match_value": match_value,
      "match_sum": player0_win_count + player1_win_count, 
      "player0_win": player1_win_count,
      "player1_win": player1_win_count
  }

  with open('data/result.json', 'r') as json_file:
      data = json.load(json_file)
      data.append(new_data)

  with open('data/result.json', 'w') as json_file:
      json.dump(data, json_file, indent=2)

if __name__ == "__main__":
    main()

