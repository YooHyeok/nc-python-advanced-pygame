import pygame
####################################################################################################################################
# 0. 기본 초기화(필수 설정)

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height)) # 캔버스 설정 Surface 객체 변수 할당

# 화면 타이틀 설정
pygame.display.set_caption("YooHyeok Game") # 게임 이름

# FPS
clock = pygame.time.Clock()

####################################################################################################################################
# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

running = True
while running:
  dt = clock.tick(30)

  # 2. 이벤트 처리 (키보드, 마우스 등)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
    
  # 3. 게임 캐릭터 위치 정의

  # 4. 충돌 처리

  # 5. 화면에 렌더링

  pygame.display.update() # 게임 화면 다시 그리기

pygame.time.delay(2000) # 2초 대기

# pygmae 종료
pygame.quit()

