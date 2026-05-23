import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height)) # 캔버스 설정 Surface 객체 변수 할당

# 화면 타이틀 설정
pygame.display.set_caption("YooHyeok Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load('C:\\Users\\~\\pygame_basic\\background.png')

# 스프라이트(캐릭터) 이미지 불러오기
character = pygame.image.load('C:\\Users\\~\\pygame_basic\\character.png')
character_size = character.get_rect().size # 이미지 크기 반환
character_width = character_size[0] # 가로
character_height = character_size[1] # 세로
character_x_pos = (screen_width / 2) - (character_height / 2) # 가로 위치(화면기준 중앙)
character_y_pos = screen_height - character_height # 세로 위치(화면 기준 최하단)

# 이벤트 루프: 실행되는 동안 발생하는 이벤트를 계속 감지하고 처리
running = True # 게임 진행중 여부 Flag
while running:
  for event in pygame.event.get(): # pygame에서 발생하는 모든 이벤트 추출
    if event.type == pygame.QUIT: # 게임창의 [X] 버튼을 통한 종료 이벤트
      running = False
  screen.blit(background, (0, 0)) # 배경 이미지 불러오기 - 튜플 (x좌표, y좌표)
  screen.blit(character, (character_x_pos, character_y_pos)) # 배경 이미지 불러오기 - 튜플 (x좌표, y좌표)
  pygame.display.update() # 게임 화면 다시 그리기

# pygmae 종료
pygame.quit()
