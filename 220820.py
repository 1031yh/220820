a1 = '안녕하세요'
a2 = '저는'
a3 = '윤건희 입니다'

print (a1)
print (a2)
print (a3)

a_list = ['안녕하세요', '저는', '윤건희 입니다' ]
         # 0번째 인덱스  1번쨰     2번째 인덱스
print(a_list[0:2])
a_list.append ('추가')
print(a_list)
a_list = ['앞에 추가']+a_list
print(a_list)
a_list.insert(1, '첫번')
print(a_list)