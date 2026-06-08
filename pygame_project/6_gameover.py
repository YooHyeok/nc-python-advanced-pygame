from pathlib import Path
import os
import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height)) # 캔버스 설정 Surface 객체 변수 할당

# 화면 타이틀 설정
pygame.display.set_caption("YooHyeok Pang") # 게임 이름

# FPS
clock = pygame.time.Clock()

# 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

# background = pygame.image.load(str(Path(__file__).resolve().parent / "img" / "background.png"))
background = pygame.image.load(os.path.join(os.path.join(os.path.dirname(__file__), "img"), "background.png"))
stage = pygame.image.load(os.path.join(os.path.join(os.path.dirname(__file__), "img"), "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용
character = pygame.image.load(os.path.join(os.path.join(os.path.dirname(__file__), "img"), "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

# 캐릭터 이동 방향(좌표)
character_to_x = 0 # 좌우로만 이동하므로 y는 불필요

# 캐릭터 이동 속도
character_speed = 5

# 무기
weapon = pygame.image.load(os.path.join(os.path.join(os.path.dirname(__file__), "img"), "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기목록 (1회 N발 발사)
weapons = []
weapon_speed = 10 # 무기 이동 속도

# 공 만들기 (4개 크기에 대해 따로 처리)
ball_images = [
  pygame.image.load(os.path.join(os.path.join(os.path.dirname(__file__), "img"), "ballon1.png")),
  pygame.image.load(os.path.join(os.path.join(os.path.dirname(__file__), "img"), "ballon2.png")),
  pygame.image.load(os.path.join(os.path.join(os.path.dirname(__file__), "img"), "ballon3.png")),
  pygame.image.load(os.path.join(os.path.join(os.path.dirname(__file__), "img"), "ballon4.png")),
]

# 공 크기에 따른 최초 속도 정의
ball_speed_y = [-18, -15, -12, -9]

# 공 목록
balls = []
balls.append({
  "pos_x" : 50, # 공의 x좌표
  "pos_y" : 50, # 공의 y좌표
  "img_idx" : 0, # 공의 이미지 인덱스
  "to_x" : 3, # x축 이동 방향(-3: 좌측, 3: 우측)
  "to_y" : 3, # y축 이동 방향
  "init_spd_y" : ball_speed_y[0] # y축 최초 속도
})

# 사라질 무기, 공 정보 저장 변수
weapon_to_remove = -1
ball_to_remove = -1

# Font 정의
game_font = pygame.font.Font(None, 40)
total_time = 100
start_ticks = pygame.time.get_ticks() # 시작 시간 정의

# 게임 종료 메시지 - 상태에 따라 변경: Time Over(시간 초과 실패), Mission Complete(성공), Game Over(캐릭터 ↔ 공 충돌 실패)
game_result = "Game Over" 

running = True
while running:
  dt = clock.tick(30)

  # 이벤트 처리 (키보드, 마우스 등)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT: # 캐릭터를 좌측으로 이동
        character_to_x -= character_speed
      elif event.key == pygame.K_RIGHT: # 캐릭터를 우측으로 이동
        character_to_x += character_speed
      elif event.key == pygame.K_SPACE: # 무기 발사
        weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2) # 무기 위치 : 케릭터 중간위치
        weapon_y_pos = character_y_pos # 무기 위치 : 케릭터 상단위치
        weapons.append([weapon_x_pos, weapon_y_pos])

    # 방향키 해제시 stop
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        character_to_x = 0

  # 3. 게임 캐릭터 위치 정의
  character_x_pos += character_to_x

  # 임계값
  if character_x_pos < 0:
    character_x_pos = 0
  elif character_x_pos > screen_width - character_width:
    character_x_pos = screen_width - character_width
  
  # 무기 위치 조정: 100(x), 200(y) → 180, 160, 140, ... / 500(x), 200(y) → 180, 160, 140, ...
  weapons = [ # 무기 위치 위로 발사 (출력할 무기 목록 할당)
    [w[0], w[1] - weapon_speed] for w in weapons 
      if w[1] > 0 # 무기 최상단 접근시 삭제: y좌표가 0보다 클 경우에만 무기 출력(출력할 무기 목록 할당)
  ]

  # 4. 충돌 처리
  # 캐릭터 rect 정보 업데이트
  character_rect = character.get_rect()
  character_rect.left = character_x_pos
  character_rect.top = character_y_pos

  # 공 위치 정의
  for ball_idx, ball_val in enumerate(balls): # balls 리스트의 요소가 index, value - 각 공의 정보 처리로 인덱스 정보가 필요하다.
    ball_pos_x = ball_val["pos_x"]
    ball_pos_y = ball_val["pos_y"]
    ball_img_idx = ball_val["img_idx"]

    ball_rect = ball_images[ball_img_idx].get_rect()
    ball_size = ball_rect.size
    ball_width = ball_size[0]
    ball_height = ball_size[1]

    # 공 임계값 처리 - 반대로 튕기기
    if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width: # 가로 벽
      ball_val["to_x"] = ball_val["to_x"] * (-1) # 반대로 튕기기(부호 반전)
    if ball_pos_y >= screen_height - stage_height - ball_height: # 세로 벽 : 스테이지 상단
      ball_val["to_y"] = ball_val["init_spd_y"] # 반대로 튕기기: 스테이지에 닿았기 때문에 최초 속도
    else: # 그 외 모든 경우 속도 증가
      ball_val["to_y"] += 0.5
    
    # x 좌표, y 좌표에 반영 공 위치 반영
    ball_val["pos_x"] += ball_val["to_x"]
    ball_val["pos_y"] += ball_val["to_y"]

    # 4. 충돌 처리
    # 공 rect 정보 업데이트
    ball_rect.left = ball_val["pos_x"]
    ball_rect.top = ball_val["pos_y"]

    # 실제 충돌 처리
    if character_rect.colliderect(ball_rect): # 공 ↔ 캐릭터
      game_result = "Game Over"
      running = False
      break

    # 공 ↔ 무기
    for weapon_idx, weapon_val in enumerate(weapons):
      weapon_pos_x = weapon_val[0]
      weapon_pos_y = weapon_val[1]

      weapon_rect = weapon.get_rect()
      weapon_rect.left = weapon_pos_x
      weapon_rect.top = weapon_pos_y

      if ball_rect.colliderect(weapon_rect): # 공 ↔ 무기
        weapon_to_remove = weapon_idx # 무기 제거를 위한 값 할당
        ball_to_remove = ball_idx # 현재 공 제거를 위한 값 할당

        # 공 쪼개기
        if ball_img_idx < 3: # 가장 작은공이 아니라면 쪼개지기

          # 현재 공 크기 정보 조회
          ball_width = ball_rect.size[0]
          ball_height = ball_rect.size[1]

          # 나눠진 공 정보
          small_ball_rect = ball_images[ball_img_idx + 1].get_rect() # 지금 크기의 공보다 한단계 작은(idx +1) 공
          small_ball_width = small_ball_rect.size[0]
          small_ball_height = small_ball_rect.size[1]

          # 좌측으로 튕겨나가는 작은 공
          balls.append({ 
            "pos_x" : ball_pos_x + (ball_width/2) - (small_ball_width/2), # 공의 x좌표
            "pos_y" : ball_pos_y + (ball_height/2) - (small_ball_height/2), # 공의 y좌표
            "img_idx" : ball_img_idx + 1, # 공의 이미지 인덱스
            "to_x" : -3, # x축 이동 방향(-3: 좌측, 3: 우측)
            "to_y" : -6, # y축 이동 방향
            "init_spd_y" : ball_speed_y[0] # y축 최초 속도
          })
          # 우측으로 튕겨나가는 작은 공
          balls.append({
            "pos_x" : ball_pos_x + (ball_width/2) - (small_ball_width/2), # 공의 x좌표
            "pos_y" : ball_pos_y + (ball_height/2) - (small_ball_height/2), # 공의 y좌표
            "img_idx" : ball_img_idx + 1, # 공의 이미지 인덱스
            "to_x" : 3, # x축 이동 방향(-3: 좌측, 3: 우측)
            "to_y" : -6, # y축 이동 방향
            "init_spd_y" : ball_speed_y[0] # y축 최초 속도
          })
        break

  # 충돌된 공 혹은 무기 제거
  if ball_to_remove > -1:
    del balls[ball_to_remove]
    ball_to_remove = -1 
  if weapon_to_remove > -1:
    del weapons[weapon_to_remove]
    weapon_to_remove = -1

  # 모든 공을 없앤 경우 게임 종료 (성공)
  if len(balls) == 0:
    game_result = "Mission Complete !"
    running = False

  # 화면에 렌더링
  screen.blit(background, (0, 0))
  
  for weapon_x_pos, weapon_y_pos in weapons: # 무기 출력
    screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

  for idx, val in enumerate(balls):
    ball_pos_x = val["pos_x"]
    ball_pos_y = val["pos_y"]
    ball_img_idx = val["img_idx"]
    screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

  screen.blit(stage, (0, screen_height - stage_height))
  screen.blit(character, (character_x_pos, character_y_pos))

  # 경과 시간 계산
  elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # / 1000 연산 : ms → s 변환
  timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255, 255, 255)) # 출력될 timer font 등록
  screen.blit(timer, (10, 10)) # timer font 로드

  # 제한시간 99초 초과시 게임 종료
  if total_time - elapsed_time <= 0:
    game_result = "Time Over"
    running = False
  
  pygame.display.update() # 게임 화면 다시 그리기


msg = game_font.render(game_result, True, (255, 255, 0)) # 노란색 출력
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2))) # 화면 중앙
screen.blit(msg, msg_rect) # timer font 로드

pygame.display.update() # 게임 화면 다시 그리기

pygame.time.delay(2000) # 2초 대기

# pygmae 종료
pygame.quit()

