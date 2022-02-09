import re

def solution(new_id):
    # 1 & 2단계 - 소문자 치환 & 소문자, 숫자, -, _, . 빼고 전부 삭제
    id = re.sub('[^a-z\d\-\_\.]', '', new_id.lower())
    # 3단계 - . 2개 이상 1개로 치환
    id = re.sub('\.\.+', '.', id)
    # 4단계 - 앞뒤 . 제거
    id = re.sub('^\.|\.$', '', id)
    # 5단계 - 빈 문자열이면 a 대입
    id = 'a' if id == '' else id
    # 6단계 - 15자 만들기 & 마지막이 . 이면 제거
    id = re.sub('\.$', '', id[:15])
    # 7단계 - 2자 이하면 마지막 문자 반복해서 3자 만들기
    if len(id) < 3:
        while True:
            id += id[-1]
            if len(id) == 3: break

    return id