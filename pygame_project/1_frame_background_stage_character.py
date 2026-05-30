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

running = True
while running:
  dt = clock.tick(30)

  # 이벤트 처리 (키보드, 마우스 등)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
  # 화면에 렌더링
  screen.blit(background, (0, 0))
  screen.blit(stage, (0, screen_height - stage_height))
  screen.blit(character, (character_x_pos, character_y_pos))
  pygame.display.update() # 게임 화면 다시 그리기

pygame.time.delay(2000) # 2초 대기

# pygmae 종료
pygame.quit()

