portein = int(input())

peanut_protein = 0  # 땅콩
chicken_protein = 0  # 닭
pure_protein = 0  # 순수

pure_protein = portein // 250 #//연산자는 나누고 몫만 반환함..
remain_portein = portein - (pure_protein * 250)

chicken_protein = remain_portein // 40
remain_portein = remain_portein - (chicken_protein * 40)

peanut_protein = remain_portein // 10
remain_portein = remain_portein - (peanut_protein * 10)


if remain_portein != 0:
    print("-1")
else:
    print(peanut_protein, chicken_protein, pure_protein)
