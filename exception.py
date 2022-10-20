# 함수
# 매개변수 (튜플, 찾고자하는 요소)
# 반환값 : 찾은 요소의 인덱스

def findIndex(tuple,element) :
  idx = -1
  try :
    idx = tuple.index(element)
  except ValueError as e:
    print('오류 유형 : {}'.format(type(e)))
    print('오류1 : {}'.format(e))
    print('오류2 : {}'.format(e.args))
    pass
  else :
    print('오류가 발생하지 않는 경우 1회 수행')
  finally :
    print('오류 발생 여부와 상관없이 1회 수행')
  return idx

fruits = ['apple','mango','grapes']

stop = False
while not stop :
  fruit = input('찾는 과일은?(종료:x) >>')

  if fruit == 'x' or fruit == 'X':
    print('프로그램을 종료합니다.')
    stop = True
    continue
  foundIndex = findIndex(fruits,fruit)
  if foundIndex != -1 :
    print('위치 : {}'.format(foundIndex+1))
  else :
    print('찾고자하는 요소가 없습니다.')
