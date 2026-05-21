# 나도 코딩 Python 활용 1
## 추억의 오락실 게임만들기

### pygame 라이브러리 활용
pygame이란?  
파이썬에서 2D 게임 및 멀티미디어 애플리케이션을 개발할 수 있도록 해주는 오픈소스 라이브러리

- pygame 라이브러리 설치 명령
  ```bash
  pip install pygame
  ```

- pygame 실행 코드: 프레임 설정, 이벤트루프 설정
  ```py
  import pygame

  pygame.init() # 초기화 (반드시 필요)

  # 화면 크기 설정
  screen_width = 480 # 가로 크기
  screen_height = 640 # 세로 크기
  screen = pygame.display.set_mode((screen_width, screen_height))

  # 화면 타이틀 설정
  pygame.display.set_caption("YooHyeok Game") # 게임 이름

  # 이벤트 루프: 실행되는 동안 발생하는 이벤트를 계속 감지하고 처리
  running = True # 게임 진행중 여부 Flag
  while running:
    for event in pygame.event.get(): # pygame에서 발생하는 모든 이벤트 추출
      if event.type == pygame.QUIT: # 게임창의 [X] 버튼을 통한 종료 이벤트
        running = False

  # pygmae 종료
  pygame.quit()
  ```