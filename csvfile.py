import csv



# with 구문과 같이 사용하면 close() 처리를 자동으로 해줌
with open('member.csv', 'r', encoding='cp949') as csvfile :
  r = csv.reader(csvfile, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
  for line in r :
    print(line[:])
