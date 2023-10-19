
# 게임 월드를 관리하는 모듈

# 게임 월드의 표현 [ 객체들의 리스트 ]
# 두개의 layer를 갖는 게임월드로 구현
objects = [ [], [], [] ]


# 월드에 객체를 넣는 함수
def add_object(_obj, depth = 0):
    # objects.append(_obj)
    objects[depth].append(_obj)

# 월드를 업데이트 하는, 객체들을 모두 업데이트 하는 함수
def update():
    # for _obj in objects:
    #     _obj.update()
    for Layer in objects:
        for _obj in Layer:
            _obj.update()

# 월드 객체들을 모두 그리기
def render():
    for Layer in objects:
        for _obj in Layer:
            _obj.draw()

# 객체 삭제
def remove_object(_obj):
    # objects.remove(_obj)
    for Layer in objects: # 레이어에 안들어있는데 삭제하려면 오류남 [존재하지 않는 놈 삭제하려면 오류남]
        if _obj in Layer: # --> 만약 레이어 안에 있다면 지우기
            Layer.remove(_obj) # 오브젝트 안에 있는 모든 레이어에 대해 지워라
            return # 한번 지웠으면 굳이 for루프 돌 필요없다. -> 최적화

    raise ValueError('[오류] 없는데 왜 지우려고 하니')  # 존재하지 않는 걸 지우려고 할 때 알려주는 역할 -> safe 코딩
