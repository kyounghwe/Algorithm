prot = int(input())

prot_prot = 0;
prot_chi = 0;
prot_pea = 0;

prot_stub = 0;
prot_stub1 = prot
prot_300 = int(prot/300)
if prot_300 > 0 and int(prot/250) == 0:
    prot_stub = prot - prot_300*300
    prot_prot += prot_300
    prot_chi += prot_300
    prot_pea += prot_300
    if int(prot_stub/250) > 0:
        prot_prot +=int(prot_stub/250)
        prot_stub -= 250*int(prot_stub/250)
        if int(prot_stub/40) > 0:
            prot_chi += int(prot_stub/40)
            prot_stub -= 40*int(prot_stub/40)
            if int(prot_stub/10) > 0:
                prot_pea += int(prot_stub/10)
        else:
            if int(prot_stub/10) > 0 :
                prot_pea += int(prot_stub/10)
    else:
        if int(prot_stub/40) > 0:
            prot_chi += int(prot_stub/40)
            prot_stub -= 40*int(prot_stub/40)
            if int(prot_stub/10) > 0:
                prot_pea += int(prot_stub/10)
        else:
            if int(prot_stub/10) > 0:
                prot_pea += int(prot_stub/10)
elif int(prot/250) != 0:
    prot_prot +=int(prot_stub1/250)
    prot_stub1 -= 250*int(prot_stub1/250)
    if int(prot_stub1/40) > 0:
        prot_chi += int(prot_stub1/40)
        prot_stub1 -= 40*int(prot_stub1/40)
        if int(prot_stub1/10) > 0:
                prot_pea += int(prot_stub1/10)
    else:
        if int(prot_stub1/10) > 0 :
            prot_pea += int(prot_stub1/10)
    
else:
    if int(prot_stub1/250) > 0:
        prot_prot +=int(prot_stub1/250)
        prot_stub1 -= 250*int(prot_stub1/250)
        if int(prot_stub1/40) > 0:
            prot_chi += int(prot_stub1/40)
            prot_stub1 -= 40*int(prot_stub1/40)
            if int(prot_stub1/10) > 0:
                prot_pea += int(prot_stub1/10)
        else:
            if int(prot_stub1/10) > 0:
                prot_pea += int(prot_stub1/10)
    else:
        if int(prot_stub1/40) > 0:
            prot_chi += int(prot_stub1/40)
            prot_stub1 -= 40*int(prot_stub1/40)
            if int(prot_stub1/10) > 0:
                prot_pea += int(prot_stub1/10)
        else:
            if int(prot_stub1/10) > 0:
                prot_pea += int(prot_stub1/10)
                

if prot != 250*prot_prot + 40*prot_chi + 10*prot_pea or prot <= 0 or prot>10000 :
    print(-1)
else:
    print(prot_pea,prot_chi,prot_prot)
