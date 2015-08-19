__author__ = 'ye'
lrc=''
fin=open('lrc.txt','rt')
chunk=100
while True:
    fragment=fin.read(chunk)
    if not fragment:
        break
    lrc+=fragment
fin.close()
print(len(lrc))
print(lrc)


