import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height)) # 캔버스 설정 Surface 객체 변수 할당

# 화면 타이틀 설정
pygame.display.set_caption("YooHyeok Game") # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load('C:\\Users\\dq\\diquest\\study\\inflearn\\nado-python-advanced-game\\pygame_basic\\background.png')

# 스프라이트(캐릭터) 이미지 불러오기
character = pygame.image.load('C:\\Users\\dq\\diquest\\study\\inflearn\\nado-python-advanced-game\\pygame_basic\\character.png')
character_size = character.get_rect().size # 이미지 크기 반환
character_width = character_size[0] # 가로
character_height = character_size[1] # 세로
character_x_pos = (screen_width / 2) - (character_height / 2) # 가로 위치(화면기준 중앙)
character_y_pos = screen_height - character_height # 세로 위치(화면 기준 최하단)


# 이동할 좌표
to_x = 0
to_y = 0

# 이동속도
character_spped = 0.6

# 이벤트 루프: 실행되는 동안 발생하는 이벤트를 계속 감지하고 처리
running = True # 게임 진행중 여부 Flag
while running:
  '''
  가정) 케릭터가 1초동안 100만큼 이동  
  A) 10 fps일 경우 - 1번에 10만큼 이동 = 10 * 10
  B) 20 fps일 경우 - 1번에 5만큼 이동 = 5 * 20
  '''
  dt = clock.tick(10) # 초당 프레임수: 높을수록 부드럽고 빠르며, 낮을수록 부자연스럽고 느림.
  for event in pygame.event.get(): # pygame에서 발생하는 모든 이벤트 추출
    if event.type == pygame.QUIT: # 게임창의 [X] 버튼을 통한 종료 이벤트
      running = False
    if event.type == pygame.KEYDOWN: # 키보드 입력 여부 확인
      if event.key == pygame.K_LEFT: # 캐릭터 왼쪽 이동
        to_x -= character_spped
      elif event.key == pygame.K_RIGHT: # 캐릭터 오른쪽 이동
        to_x += character_spped
      elif event.key == pygame.K_UP: # 캐릭터 위로 이동
        to_y -= character_spped
      elif event.key == pygame.K_DOWN: # 캐릭터 아래로 이동
        to_y += character_spped
    # 방향키 해제시 stop
    if event.type == pygame.KEYUP: 
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        to_x = 0
      elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        to_y = 0
    
  character_x_pos += to_x * dt # 프레임별 이동 속도 보정
  character_y_pos += to_y * dt

  # 임계값 처리
  ## 가로
  if character_x_pos < 0:
    character_x_pos = 0
  elif character_x_pos > screen_width - character_width: # 우측 최대 위치 입계값 : 스크린 가로너비 - 캐릭터 가로너비
    character_x_pos = screen_width - character_width
  ## 세로
  if character_y_pos < 0:
    character_y_pos = 0
  elif character_y_pos > screen_height - character_height: # 하단 최대 위치 입계값 : 스크린 세로높이 - 캐릭터 세로높이
    character_y_pos = screen_height - character_height

  screen.blit(background, (0, 0)) # 배경 이미지 불러오기 - 튜플 (x좌표, y좌표)

  screen.blit(character, (character_x_pos, character_y_pos)) # 배경 이미지 불러오기 - 튜플 (x좌표, y좌표)

  pygame.display.update() # 게임 화면 다시 그리기

# pygmae 종료
pygame.quit()

