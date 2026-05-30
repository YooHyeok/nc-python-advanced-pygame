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


  # 화면에 렌더링
  screen.blit(background, (0, 0))
  
  for weapon_x_pos, weapon_y_pos in weapons: # 무기 출력
    screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

  screen.blit(stage, (0, screen_height - stage_height))
  screen.blit(character, (character_x_pos, character_y_pos))
  pygame.display.update() # 게임 화면 다시 그리기

pygame.time.delay(2000) # 2초 대기

# pygmae 종료
pygame.quit()

