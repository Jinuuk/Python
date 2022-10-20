# 딕셔너리 객체 생성1
print('딕셔너리 객체 생성1\n')
dictionary = {}
print(type(dictionary))

# 딕셔너리 객체 생성2
# dictionary2 = dict()
# print(type(dictionary2))

# 요소추가
print('요소추가\n')
dictionary['student'] = '학생'
dictionary['teacher'] = '선생'
dictionary['classroom'] = '교실'
print(dictionary)

# 요소 삭제
print('요소 삭제\n')
del dictionary['classroom']
print(dictionary)

deletedItem = dictionary.pop('teacher')
print(deletedItem)
print(dictionary)

# 요소 수정
print('요소 수정\n')
dictionary['student'] = '학생2'
print(dictionary)

# 요소 조회
print('요소 조회\n')
dictionary['teacher'] = '선생'
dictionary['classroom'] = '교실'

# 요소조회 1) items()
# 요소(키,값)들을 튜플로, 전체는 리스트로 반환
print('요소조회 1) items()\n')
items = dictionary.items()
print(items)

# 요소조회 2) keys() 
# 키를 요소로 갖는 리스트 반환
print('요소조회 2) keys() \n')
keys = dictionary.keys()
print(keys)

# 요소조회 3) values()
# 값을 요소로 갖는 리스트를 반환
print('요소조회 3) values()\n')
values = dictionary.values()
print(values)

# 요소조회 4-1) 키로 값 조회하기
print('요소조회 4-1) 키로 값 조회하기\n')
value = dictionary['student']
print(value)

# 요소조회 4-2) get() 키로 값 조회하기
# 만약 없으면 2번째 매개값을 반환
print('요소조회 4-2) get() 키로 값 조회하기\n')
value2 = dictionary.get('student','none')
print(value2)
value3 = dictionary.get('student22',-1)
print(value3)

# 요소 전체 출력하기
print('요소 전체 출력하기\n')

def printList(dic) :
  for ele in dic.keys() : 
    print('{:10}:{}'.format(ele,dictionary.get(ele)))
print(dictionary)

# dict객체 복사
print('dict객체 복사\n')
dictionary3 = dictionary.copy()
print(dictionary,'\n',dictionary3)

# 2개의 dict 객체 병합하기 update()
# 키가 동일하면 업데이트 다르면 추가되는 방식
print('2개의 dict 객체 병합하기 update()\n')
dictionary3['blackboard'] = '칠판'
dictionary.update(dictionary3)
print(dictionary)

# 키가 있으면 값을 반환하고 없으면 추가
# 1.키가 있으면 값을 반환
print('1.키가 있으면 값을 반환\n')
print(dictionary.setdefault('student','학생3'))

# 2.키가 없으면 요소 추가
print('2.키가 없으면 요소 추가\n')
print(dictionary.setdefault('student3','학생3'))
print(dictionary)


# key 존재여부 판단
print('key 존재여부 판단\n')
print('student' in dictionary)
print('student' not in dictionary)

# 요소의 개수
print('요소의 개수\n')
print(len(dictionary))
#print(list(dictionary.items()).count())

# 요소 정렬
from copyreg import pickle
import operator
print('===정렬 시작===')
sortedDictionary = sorted(dictionary.items(), key=operator.itemgetter(0))
reversedDictionary = reversed(sortedDictionary)
print(sortedDictionary)

print('==오름차순==')
for item in sortedDictionary :
  print('{:15} : {}'.format(item[0],item[1]))

print('==내림차순==')
for item in reversedDictionary :
  print('{:15} : {}'.format(item[0],item[1]))

print('==정렬 끝==')

# 문자열의 공백 제거
# replace() : 모든 공백 제거
# strip(),lstrip(),rstrip() : 양쪽, 왼쪽, 오른쪽 공백 제거

# 파일에 저장
f = open('d:\javaedu9\python\dictionary.txt','w', encoding='UTF8')
if f.writable :
  for line in sortedDictionary :
    f.write('{}:{}\n'.format(line[0].strip(),line[1].strip()))
  f.close()

# 파일에서 읽어오기
f = open('d:\javaedu9\python\dictionary.txt','r', encoding='UTF8')
if f.readable() :
  dic={}
  for line in f.readlines() :
    list = line.strip().split(':')
    print(list)
    dic[list[0].strip()] = list[1].strip()
  f.close()
  print(dic)

# 요소 전체 삭제
print('요소 전체 삭제\n')
dictionary.clear()
print(len(dictionary)) #{}

# 사전 객체 제거 : 메모리에서 제거되어 접근 불가
# del dictionary
# print(len(dictionary))

# 문자열 길이 구하기 len()
# 문자열 비교 ==
# 소문자, 대문자 변환 : lower(), upper()
print('abc'.upper())

word = input('단어를 입력하세요 >> ')
print(word.upper())
print(word.lower())
