import os.path

file = r'd:\javaedu9\python\단어장.txt'

vocabulary = {}
vocaFile = None

if not os.path.exists(file) :
  vocaFile = open(file,'w',encoding='UTF8')
else :
  vocaFile = open(file,'a',encoding='UTF8')
  vocaFile = open(file,'r', encoding='UTF8')
  if vocaFile.readable() :
    for line in vocaFile.readlines() :
      list = line.strip().split(':')
      vocabulary[list[0].strip()] = list[1].strip()

stop = False
while not stop :
  selectedMenu = input('[메뉴] 1.저장 2.검색 3.수정 4.삭제 5.목록 6.통계 7.종료(x) >> ')
  if selectedMenu == '1' : #1.저장
    if len(vocabulary) == 5 :
      print('단어는 최대 5개까지 저장할 수 있습니다.')
    else :
      inputWord = input('저장할 단어를 입력하세요 : ')
      if inputWord.lower() in vocabulary  :
        print('이미 존재하는 단어입니다.')
      else : 
        inputMeaning = input('저장할 뜻 입력하세요 : ')
        vocabulary[inputWord.lower()] = inputMeaning
        print('저장이 완료되었습니다.')

  elif selectedMenu == '2' : #2.검색
    inputWord = input('검색할 단어를 입력하세요 : ')
    import operator
    ascVocabulary = sorted(vocabulary.items(), key=operator.itemgetter(0))
    for voca in ascVocabulary :
      if inputWord.lower() in voca[0] :
        print('단어 검색 완료')
        print('{}:{}'.format(voca[0],vocabulary[voca[0]]))
    if inputWord.lower() not in vocabulary :
      print('단어를 검색할 수 없습니다.')

  elif selectedMenu == '3' : #3.수정
    inputWord = input('수정할 단어를 입력하세요 : ')
    if inputWord.lower() in vocabulary :
      inputMeaning = input('수정할 뜻 입력하세요 : ')
      vocabulary[inputWord.lower()] = inputMeaning
      print('단어의 뜻을 수정하였습니다.')
    else :
      print('단어를 검색할 수 없습니다.')

  elif selectedMenu == '4' : #4.삭제
    inputWord = input('삭제할 단어를 입력하세요 : ')
    if inputWord.lower() in vocabulary :
      del vocabulary[inputWord.lower()]
      print('단어를 삭제하였습니다.')
    else :
      print('단어를 검색할 수 없습니다.')

  elif selectedMenu == '5' : #5.정렬
    selectedSubMenu = input('[정렬 방식] 1.오름차순 2.내림차순 >> ')
    if len(vocabulary) == 0 :
      print('단어장이 비어있습니다.')
    else :
      import operator
      ascVocabulary = sorted(vocabulary.items(), key=operator.itemgetter(0))
      descVocabulary = reversed(ascVocabulary)
      if selectedSubMenu == '1' :
        for voca in ascVocabulary :
          print('{:15} : {}'.format(voca[0],voca[1]))
      else :
        for voca in descVocabulary :
          print('{:15} : {}'.format(voca[0],voca[1]))

  elif selectedMenu == '6' : #6.통계
    vocabularySortedByKeyLength = {}
    for k in sorted(vocabulary, key=len, reverse=True) :
      vocabularySortedByKeyLength[k] = vocabulary[k]
    print('저장된 단어 수 >> {}'.format(len(vocabulary)))
    try : 
      print('가장 긴 단어 >> {}:{}'.format(next(iter(vocabularySortedByKeyLength)),vocabulary[next(iter(vocabularySortedByKeyLength))])) 
    except :
      print('가장 긴 단어 >> 없음')
    print('글자수 기준 내림차순 정렬')
    for voca in vocabularySortedByKeyLength :
      print('{} : {}'.format(voca,vocabulary[voca]))
    
  elif selectedMenu == '7' or selectedMenu == 'x' or selectedMenu == 'X'  : #8.종료
    print('단어장 프로그램을 종료합니다.')
    vocaFile = open(file,'w',encoding='UTF8')
    if vocaFile.writable :
      for voca in vocabulary :
        vocaFile.write('{}:{}\n'.format(voca,vocabulary[voca]))
      vocaFile.close()
    stop = True
    continue
