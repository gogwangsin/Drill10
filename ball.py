from pico2d import load_image

import game_world


class Ball: # 객체를 생성하기 위해 class 만들기
    image = None

    # 생성위치 디폴트
    def __init__(self, x = 400, y = 300, velocity = 1):
        if Ball.image == None: # 처음 생성에서 이미지 관리 self 안붙임
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity # x축 방향으로 이동

        if self.x < 50 or self.x > 800 - 50: # 끝이 800이라는 걸 알려주는 것 / 처음 끝이 50거리가 됐을 때
            game_world.remove_object(self) # 자기자신 지우기
