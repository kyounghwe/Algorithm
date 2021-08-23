portein = int(input()) 

peanut_protein = 0 #땅콩
chicken_protein = 0 #닭
pure_protein = 0 #순수

pure_protein =  portein // 250 
remain_protein = portein - (pure_protein * 250)

chicken_protein = remain_protein // 40
remain_protein = remain_protein - (chicken_protein * 40)

peanut_protein = remain_protein // 10
remain_protein = remain_protein - (peanut_protein * 10)

if remain_protein != 0:
    print("-1")
else:
    print(peanut_protein, chicken_protein, pure_protein)
