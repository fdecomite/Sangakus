TAILLE=500
pourcentage=0.05
from math import *

def decalage(c,percent=pourcentage):
    return "\"translate("+str(c*percent)+","+str(c*percent)+")\""

#grouper deux rectangles pour définir le cadre
def rectangle(c=TAILLE,percent=pourcentage,transform="\"\""):
    s="<g> <rect x=\""+str(percent*c)+"\" y=\""+str(c*percent)+"\" width=\""+str(c)+"\" height=\""+str(c)+"\" fill=\"none\" stroke=\"red\" transform="+transform+ "/>\n"
    print(s)
    sprime="<rect x=\"0\" width=\""+str(c*(1+2*percent))+"\" height=\""+str(c*(1+2*percent))+"\" rx=\"25\" fill=\"none\" stroke=\"red\" transform="+transform+ "/></g>\n"
    print(sprime)
    return s+"<rect x=\"0\" width=\""+str(c*(1+2*percent))+"\" height=\""+str(c*(1+2*percent))+"\" rx=\"25\" fill=\"none\" stroke=\"red\" transform="+transform+ "/></g>\n"

def simplerectangle(c=TAILLE,percent=pourcentage,transform="\"\""):
    s="<rect x=\""+str(0)+"\" y=\""+str(0)+"\" width=\""+str(c)+"\" height=\""+str(c)+"\" fill=\"none\" stroke=\"red\" transform="+transform+ "/>\n"
    return s

def ligne(debut,fin,transform="\"\""):
     s="<line x1=\""+str(debut[0])+"\" y1=\""+str(debut[1])+"\" x2=\""+str(fin[0])+"\" y2=\""+str(fin[1])+"\" stroke=\"black\"   transform="+transform+" />\n"
     return s
    

def equilateral(c=TAILLE,transform="\"\""):
    hauteur=c*sqrt(3)/2
    return "<polygon points=\"0 "+str(c)+" ,"+str(c/2)+" "+str(c-hauteur)+" , "+str(c)+" "+str(c)+"\" fill=\"none\" stroke=\"red\" transform="+transform+"/>\n"

def cercle(cx,cy,rayon,transform="\"\""):
    return "<circle cx=\""+str(cx)+"\" cy=\""+str(cy)+"\"  r=\""+str(rayon)+"\" transform="+transform+" fill=\"none\" stroke=\"red\"/>\n"


def distance(p1,p2):
    difx=(p1[0]-p2[0])*(p1[0]-p2[0])
    dify=(p1[1]-p2[1])*(p1[1]-p2[1])
    return sqrt(difx+dify)


def distance3d(p1,p2):
     difx=(p1[0]-p2[0])*(p1[0]-p2[0])
     dify=(p1[1]-p2[1])*(p1[1]-p2[1])
     difz=(p1[2]-p2[2])*(p1[2]-p2[2])
     return sqrt(difx+dify+difz)
    

def intersection2cercles(c1,c2):
    # Retourne les deux points d'intersection de deux cercles
    xa=c1[0][0]
    ya=c1[0][1]
    print(ya)
    xb=c2[0][0]
    yb=c2[0][1]
    print(yb)
    pR=c1[1]
    gR=c2[1]
    a=2*(xb-xa)
    b=2*(yb-ya)
    c=(xb-xa)*(xb-xa)+(yb-ya)*(yb-ya)-gR*gR+pR*pR
   
    
    
    if (b!=0):
        delta=(2*a*c)*(2*a*c)-4*(a*a+b*b)*(c*c-b*b*pR*pR)
        xp=xa+(2*a*c-sqrt(delta))/(2*(a*a+b*b))
        xq=xa+(2*a*c+sqrt(delta))/(2*(a*a+b*b))
        xp=xa+(2*a*c-sqrt(delta))/(2*(a*a+b*b))
        xq=xa+(2*a*c+sqrt(delta))/(2*(a*a+b*b))
        yp=ya+(c-a*(xp-xa))/b
        yq=ya+(c-a*(xq-xa))/b
    else:
        xp=c/a
        xq=c/a
        d=abs(xa-xb)
        r=pR
        R=gR
        calcul=(-d+r-R)*(-d-r+R)*(-d+r+R)*(d+r+R)
        y=sqrt(calcul)/(2*d)
        yp=y
        yq=-y
        #yp=ya+sqrt(gR*gR-((2*c-a*a)*(2*c-a*a))/(4*a*a))
        #yq=ya-sqrt(gR*gR+((2*c-a*a)*(2*c-a*a))/(4*a*a))
        
    return ((xp,yp),(xq,yq))
        
    
    

def resoutCercle(p1,p2,p3):
    #retourne centre et rayon du cercle inscrit dans un triangle de sommets p1,p2,p3
    #longueur du cote oppose au point point1
    dist1=distance(p2,p3)
    dist2=distance(p1,p3)
    dist3=distance(p1,p2)
    denom=dist1+dist2+dist3
    #coordonnees du centre
    cx=(dist1*p1[0]+dist2*p2[0]+dist3*p3[0])/denom
    cy=(dist1*p1[1]+dist2*p2[1]+dist3*p3[1])/denom
    #rayon du cercle
    s=(dist1+dist2+dist3)/2
    radius=sqrt(s*(s-dist1)*(s-dist2)*(s-dist3))/s
    return (cx,cy),radius
    


def equilateralPenche(c=TAILLE,transform="\"\""):
    a=(2-sqrt(3))*c
    b=c-a
    return "<polygon  points=\""+str(c)+" 0 ,"+str(b)+" "+str(c)+" ,  0 "+str(a)+" \" fill=\"none\" stroke=\"red\" transform="+transform+"/>\n"


    
entete="<svg viewBox=\"0 0 "+str(1000)+" "+str(1000)+"\" xmlns=\"http://www.w3.org/2000/svg\">\n"
pied="</svg>\n"
image=open("polyedre.svg","w")
image.write(entete)
transfo="\"translate(400,200)\""



a3d=(-359,0,0)
a2d=(-359,0)
b3d=(0,0,0)
b2d=(0,0)
c3d=(-116.59,70.39,0)
c2d=(-116.59,70.39)
d3d=(113.54,-28.64,158.38)
c1=(b2d,distance3d(b3d,d3d)) #  cercle de centre B de rayon distance de B à D
c2=(c2d,distance(c3d,d3d)) # cercle de centre C et de rayon distance de C à D
inter=intersection2cercles(c1,c2)
image.write(ligne(a2d,b2d,transfo))
image.write(ligne(a2d,c2d,transfo))
image.write(ligne(c2d,b2d,transfo))
#image.write(cercle(c1[0][0],c1[0][1],c1[1],transfo))
#image.write(cercle(c2[0][0],c2[0][1],c2[1],transfo))
image.write(ligne(b2d,inter[1],transfo))
image.write(ligne(c2d,inter[1],transfo))
c3=(a2d,distance(a3d,d3d)) #  cercle de centre A de rayon distance de 1 à D
inter=intersection2cercles(c2,c3)# intersection des cercles de centre A et C
#image.write(cercle(c2[0][0],c2[0][1],c2[1],transfo))
#image.write(cercle(c3[0][0],c3[0][1],c3[1],transfo))
image.write(ligne(a2d,inter[0],transfo))
image.write(ligne(c2d,inter[0],transfo))
#image.write(cercle(c1[0][0],c1[0][1],c1[1],transfo))
#image.write(cercle(c3[0][0],c3[0][1],c3[1],transfo))
inter=intersection2cercles(c1,c3)# intersection des cercles de centre A et B
image.write(ligne(a2d,inter[1],transfo))
image.write(ligne(b2d,inter[1],transfo))
image.write(pied)
image.close()
     	
