portein = int(input()) 

peanut = 0 #땅콩
chicken = 0 #닭
pure = 0 #순수

pure =  portein // 250 
remain = portein - (pure * 250)

chicken = remain // 40
remain = remain - (chicken * 40)

peanut = remain // 10
remain = remain - (peanut * 10)

if remain != 0:
    print("-1")
else:
    print(peanut, chicken, pure)
