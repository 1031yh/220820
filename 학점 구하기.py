
점수 =int(input('점수를 입력하시오 ='))


if 점수>=90:
    print('학점= A')
elif 점수>=80:
    print('학점= B')
elif 점수>=80:
    print('학점= C')
elif 점수>=60:
    print('학점= D')
else:
    print('학점= F')
print(정답텍스트.format(점수, 학점))