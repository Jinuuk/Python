# 쓰기모드
f = open('d:\javaedu9\python\sample.txt','w')
print(f.writable())
f.write('hello world1\n')
f.close()

# 추가모드
f = open('d:\javaedu9\python\sample.txt','a')
f.write('hello world2\n')
f.write('hello world3\n')
f.close()

# 읽기모드
f = open('d:\javaedu9\python\sample.txt','r')
for line in f.readlines() :
  print(line.strip())
f.close()

# 읽기모드
f = open('d:\javaedu9\python\member.csv','r')
for line in f.readlines() :
  print(line.strip())
f.close()