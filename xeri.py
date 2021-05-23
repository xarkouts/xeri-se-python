import random 
katigories={"Σπαθι","Κουπα","Καρο","Μπαστουνι"}
fila={1,2,3,4,5,6,7,8,9,10,"Βαλες","Νταμα","Ριγας"}
trapoyla={(k,f) for k in katigories for f in fila}
del katigories
del fila
trapoyla=list(trapoyla)
xeri1=[]
xeri2=[]
trapezi=[]
paixtis=2
kerdismena_1=[]
kerdismena_2=[]

def mirasma(t=False):
    
    for _ in range(1,7):
        
          
        xarti=random.randrange(0,len(trapoyla))
        xeri1.append(trapoyla.pop(xarti))
        xarti=random.randrange(0,len(trapoyla))
        xeri2.append(trapoyla.pop(xarti))
    if t==True:
         for _ in range(1,5):
           xarti=random.randrange(len(trapoyla))
           trapezi.append(trapoyla.pop(xarti))
   
def paixtes(paixtis):
    if paixtis==2:
        return 1
    elif paixtis==1:
        return 2

def paixnidi (paixtis):
    print(f"Παιζει ο παιχτις {paixtis}")
    print(trapezi)
    print("-"*6)
    if paixtis==1:
        print(xeri1)
        epilogi=input("Διαέξε να ριξεις ενα χαρτι στο τραπεζι απο το 0 μεχρι το "+str(len(xeri1)-1)+"\n")
        
        while True:
            if epilogi.isdigit():
                epilogi=int(epilogi)
                if epilogi>=0 and epilogi<=(len(xeri1)-1):
                    break
            print("H επιλογη που επιλεξατε ητνα λαθασμενη")
            epilogi=input("Διαέξε να ριξεις ενα χαρτι στο τραπεζι απο το 0 μεχρι το "+str(len(xeri1)-1)+"\n")
        trapezi.insert(0,xeri1.pop(epilogi))
              
    elif paixtis==2:
          print(xeri2)
          epilogi=input("Διαέξε να ριξεις ενα χαρτι στο τραπεζι απο το 0 μεχρι το "+str(len(xeri2)-1)+"\n")
        
          while True:
              if epilogi.isdigit():
                epilogi=int(epilogi)
                if epilogi>=0 and epilogi<=(len(xeri2)-1):
                    break
              print("H επιλογη που επιλεξατε ηταν λαθασμενη")
              epilogi=input("Διαέξε να ριξεις ενα χαρτι στο τραπεζι απο το 0 μεχρι το "+str(len(xeri1)-1)+"\n")
          trapezi.insert(0,xeri2.pop(epilogi))

    if len(xeri1)==0 and len(xeri2)==0:
        return      

def ta_perni(paixtis):
    if len(trapezi)<2:
        return
    if paixtis==1:
        if trapezi[0][1]==trapezi[1][1]:
            
            for x1 in trapezi:
                kerdismena_1.append(x1)
            if len(trapezi)==2:
                kerdismena_1.append("Ξερη με "+str(trapezi[0][1]))
            trapezi.clear()
            if len(kerdismena_1)>0:
                 print("Τα κερδιμσενα χαρτια του παιχτη 1 ειναι ",kerdismena_1)
        elif trapezi[0][1]=="Βαλες":
            for x1 in trapezi:
                kerdismena_1.append(x1)
            trapezi.clear()
            if len(kerdismena_1)>0:
                 print("Τα κερδιμσενα χαρτια του παιχτη 1 ειναι ",kerdismena_1)

        

    elif paixtis==2:
        if trapezi[0][1]==trapezi[1][1]:
            for x2 in trapezi:
                kerdismena_2.append(x2)
            if len(trapezi)==2:
                kerdismena_2.append("Ξερι με "+str(trapezi[0][1]))
            trapezi.clear()
            if len(kerdismena_2)>0:
                 print("Τα κερδιμσενα χαρτια του παιχτη 2 ειναι ",kerdismena_2)    
        elif trapezi[0][1]=="Βαλες":
            for x2 in trapezi:
                kerdismena_2.append(x2)
            trapezi.clear()
            if len(kerdismena_2)>0:
                 print("Τα κερδιμσενα χαρτια του παιχτη 2 ειναι ",kerdismena_2)    

def metrima_ponton(l,s):
    xeres=[]
    p=0
    ponti_xeron=0
    fiogoyres=0
    kalo_10=0
    kalo_2=0
    dekargia=0
    asoi=0
    
    for g in l:
        if type(g)==str:
            xeres.append(g)     
    
    for d in xeres:
        l.remove(d)   

    for xeri in xeres:
        if xeri=="Ξερη με Βαλες":
            ponti_xeron+=20 
        else:
            ponti_xeron+=10

    for i in l:
        
        if i[1]=="Βαλες" or i[1]=="Νταμα" or i[1]=="Ριγας":
            fiogoyres+=1
            continue
        if i[0]=="Καρο" and i[1]==10:
            kalo_10=2
            continue    
        elif i[0]=="Σπαθι" and i[1]==10 or i[0]=="Κουπα" and i[1]==10 or i[0]=="Μπαστουνι" and i[1]==10:
            dekargia+=1
            continue
        elif i[0]=="Σπαθι" and i[1]==2:
            kalo_2=1
            continue
        if i[1]==1:
            asoi+=1
            continue
    xeres.clear()
    for k in s:
        if type(k)==str:
            xeres.append(k)

    for de in xeres:
        s.remove(de)        
    xeres.clear()
    p=ponti_xeron+fiogoyres+dekargia+asoi+kalo_2+kalo_10
    if len(l)<len(s):
        return p
    elif len(l)==len(s):
        return p
    else:
        return p+3        
     
    








        
 
 
mirasma(True)
while True:
    paixtis=paixtes(paixtis)
    paixnidi(paixtis)
    ta_perni(paixtis)
    if len(xeri1)==0 and len(xeri2)==0:
         mirasma()
         print("Απομενου τοσα χαρτια στη τραπουλα",len(trapoyla))
    if len(trapoyla)==0:
        if paixtis==1:
            if len(trapoyla)==0:
             for x1 in trapezi:
                kerdismena_1.append(x1)
             trapezi.clear()
        elif paixtis==2:
            if len(trapoyla)==0:
             for x1 in trapezi:
                kerdismena_1.append(x1)
             trapezi.clear()         
        print("το τραπεζει ειναι",trapezi)
        break    

pontoi_1=metrima_ponton(kerdismena_1,kerdismena_2)
pontoi_2=metrima_ponton(kerdismena_2,kerdismena_1)

if pontoi_1>pontoi_2:
    print(f"nikise o paixtis 1 me pontoys {pontoi_1} enanti toy paiti 2 me poyntoys {pontoi_2}")
else:
     print(f"nikise o paixtis 2 me pontoys {pontoi_2} enanti toy paiti 1 me poyntoys {pontoi_1}")    