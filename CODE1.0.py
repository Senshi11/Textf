archivo=open('moby_abs.txt')
for linea in archivo:
        counts=[]
        dic_pal={}
        dic_pal2={}
        counts2=0
        text_clean=linea.split()
        for palabra in text_clean:
                counts.append(float(text_clean.count(palabra)))
                counts2+=1
                dic_pal2[counts2]=palabra
                for num in counts:
                        dic_pal[palabra]=round((num/float(len(text_clean))),4)

archivo.close()
grupo=[]
grupo2=[]
dicc={}
for x in dic_pal2:
    a=dic_pal2[x]
    if a not in grupo:
        numero=0
        grupo.append(str(a))
        grupo2.append(str(a)+':'+str(x+1))
        dicc[a]=numero+1
    else:
        numero=1
        grupo2.append(str(a)+':'+str(x+1))
        dicc[a]=numero+1
print dicc

print dic_pal2[dicc['as']]
archivo1=open('diccionario.txt','w')
archivo1.write(str(dic_pal2))
archivo1.close()

