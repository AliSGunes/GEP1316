# 1 den 999 a kadar olan sayılar arasında döngü yaptırıyor
print(sum([i for i in range(1,1000) if 0 in [i%3,i%5]]))
#input()