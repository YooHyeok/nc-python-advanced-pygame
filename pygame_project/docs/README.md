# [루트/README.md](../../README.md)
# [기본기](../../pygame_basic/docs/README.md)
# 오락실 Pang 게임 만들기

## [게임 조건]
1. 캐릭터는 화면 아래에 위치, 좌우로만 이동 가능
2. 스페이스를 누르면 무기를 쏘아 올림
3. 큰 공 1개가 나타나서 바운스
4. 무기에 닿으면 공은 작은 크기 2개로 분할, 가장 작은 크기의 공은 사라짐
5. 모든 공을 없애면 게임 종료 (성공)
6. 캐릭터는 공에 닿으면 게임 종료 (실패)
7. 시간 제한 99초 초과 시 게임 종료 (실패)
8. FPS 는 30 으로 고정 (필요시 speed 값을 조정)

## [게임 이미지]
1. 배경 : 640 * 480(가로 세로) - background.png
2. 무대 : 640 * 50 - stage.png
3. 캐릭터 : 33 * 60 - character.png
4. 무기 : 20 * 430 - weapon.png
5. 공 : 160 * 160, 80 * 80, 40 * 40, 20 * 20  
- balloon1.png ~ balloon4.png

# 예제1) 배경, 캐릭터
## 목차
A) 프레임 기본 설정  
  - 가로 : 640 / 세로: 480  
  
B) 이미지 출력   
  - 배경 출력  
  - 스테이지 출력
  - 캐릭터 출력

<br>
<details>
<summary>접기/펼치기</summary>
<br>

![alt text](image.png)  

### A) 프레임 기본 설정
가로 : 640 / 세로: 480
- [1_frame_background_stage_character.py](../1_frame_background_stage_character.py)
  ```py
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

  running = True
  while running:
    dt = clock.tick(30)

    # 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    pygame.display.update() # 게임 화면 다시 그리기
  pygame.time.delay(2000) # 2초 대기

  # pygmae 종료
  pygame.quit()
  ```
### B) 이미지 출력
a) 배경 출력
  1. background 변수에 이미지 파일 경로 할당
  2. Surface 객체를 할당한 변수 screen에 blit(file, axis) 함수에 매개변수로 전달
      - 첫번째 매개변수에 이미지파일 경로 할당
      - 두번째 매개변수에 이미지를 출력할 초기 시작 좌표 할당.  
  3. 게임 실행 루프내에서 blit() 함수 호출

b) 스테이지 출력
  1. stage 변수에 이미지 파일 경로 할당
  2. Surface 객체를 할당한 변수 screen에 blit(file, axis) 함수에 매개변수로 전달
      - 첫번째 매개변수에 이미지파일 경로 할당
      - 두번째 매개변수에 이미지를 출력할 초기 시작 좌표 할당.  
        세로: 화면 기준 최하단 (스크린 높이 - 스테이지 높이)
  3. 게임 실행 루프내에서 blit() 함수 호출

c) 캐릭터 출력
  1. character 변수에 이미지 파일 경로 할당
  2. Surface 객체를 할당한 변수 screen에 blit(file, axis) 함수에 매개변수로 전달
      - 첫번째 매개변수에 이미지파일 경로 할당
      - 두번째 매개변수에 이미지를 출력할 초기 시작 좌표 할당.  
        가로: 화면 기준 중앙 / 세로: stage 기준 상단
  3. 게임 실행 루프내에서 blit() 함수 호출

- [1_frame_background_stage_character.py](../1_frame_background_stage_character.py)
  ```py
  # 생략
    
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
    # 생략
      
    # 화면에 렌더링
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update() # 게임 화면 다시 그리기

  # 생략
  ```
### 전체 코드
- [1_frame_background_stage_character.py](../1_frame_background_stage_character.py)
  ```py
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

  ```
</details>
<br>
<hr>
<br>