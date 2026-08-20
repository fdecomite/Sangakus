TAILLE=500
from math import *

def rectangle(c=TAILLE):
    s="<rect x=\""+str(0.05*c)+"\" y=\""+str(c*0.05)+"\" width=\""+str(c)+"\" height=\""+str(c)+"\" fill=\"none\" stroke=\"red\"  />\n"
    return s+"<rect x=\"0\" width=\""+str(c*1.1)+"\" height=\""+str(c*1.1)+"\" rx=\"25\" fill=\"none\" stroke=\"red\"/>\n"

def equilateral(c=TAILLE):
    hauteur=c*sqrt(3)/2
    return "<polygon x=\""+str(c/2)+"\" points=\""+str(hauteur)+" 0,"+str(hauteur)+" "+str(c)+" , 0 "+str(c/2)+"\" fill=\"none\" stroke=\"red\"/>\n"

def cercle(center,rayon):
    cx=center[0]
    cy=center[1]
    return  "<circle  cx=\""+str(TAILLE/2+cx)+"\" cy=\""+str(TAILLE/2+cy)+"\" r=\""+str(rayon)+"\" fill=\"none\" stroke=\"red\"/>\n"

def ligne(depart,arrivee):
    x0=depart[0]+TAILLE/2
    y0=depart[1]+TAILLE/2
    x1=arrivee[0]+TAILLE/2
    y1=arrivee[1]+TAILLE/2
    return "<line x1=\""+str(x0)+"\" y1=\""+str(y0)+"\" x2=\""+str(x1)+"\" y2=\"" +str(y1)+"\" fill=\"none\" stroke=\"red\"/>\n"

    

def arc(rayon,depart,arrivee):
    return "<path d=\" M "+str(depart[0]+TAILLE/2)+" "+str(depart[1]+TAILLE/2)+"  A "+str(rayon)+" "+str(rayon)+"  0 0 1 "+str(arrivee[0]+TAILLE/2)+" "+str(arrivee[1]+TAILLE/2)+" \" fill=\"none\" stroke=\"red\" />"

def sangaku(c=TAILLE):
    entete="<svg viewBox=\"0 0 "+str(2*c)+" "+str(2*c)+"\" xmlns=\"http://www.w3.org/2000/svg\">\n"
    pied="</svg>\n"
    image=open("sortie.svg","w")
    image.write(entete)
    image.write(rectangle(c))
    image.write(equilateral(c))
    image.write(equilateral(c/cos(pi/12)))
    for i in range(10,50):
     image.write(cercle((300,300),5*i))
    image.write(pied)
    image.close()
    
def eventail(c=TAILLE):
    entete="<svg viewBox=\"0 0 "+str(2*c)+" "+str(2*c)+"\" xmlns=\"http://www.w3.org/2000/svg\">\n <g>"
    pied="</g></svg>\n"
    image=open("eventail.svg","w")
    image.write(entete)
    # calculs
    r=TAILLE/2
    
    r2=r/4 # variable
    #r3=r/8
   
    r3=(-2*r2*r2+r*r2)/r
    t=r-2*r3-2*r2
    r1=(r-t)/2
    #r3=0.5*(r-t-2*r2)
    u2mv2=(r1+r3)*(r1+r3)-(t+r3)*(t+r3) # u^2-v^2
    umoinsv=u2mv2/(t+r1) # u-v
    u=(umoinsv+(t+r1))/2
    v=(t+r1)-u
    l=sqrt((t+r3)*(t+r3)-v*v)
    coef=(t+2*r3+r2)/(t+r3)
    coef2=r/(t+r3)
    coef3=t/r
    print(str(r2)+" "+str(2*r3))
    print(str((t+r3)/(t+2*r3+r2))+" "+str(r3/r2))
    
    #image.write(cercle((0,0),r))
    #image.write(cercle((0,0),t))
    image.write(cercle((l,v),r3))
    image.write(cercle((coef*l,coef*v),r2))
    image.write(cercle((-l,v),r3))
    image.write(cercle((-coef*l,coef*v),r2))
    image.write(cercle((0,t+r1),r1))
    #image.write(ligne((0,0),(coef2*l,coef2*v)))
   
    # calcul de la rotation
    sinalpha=r3/(t+r3)
    cosalpha=sqrt(1-sinalpha*sinalpha)
    p1=(coef2*l,coef2*v)
    rotatp1=(p1[0]*cosalpha+p1[1]*sinalpha,-p1[0]*sinalpha+p1[1]*cosalpha)
    rotatp2=(-rotatp1[0],rotatp1[1])
    smallrp1=(rotatp1[0]*coef3,rotatp1[1]*coef3)
    smallrp2=(rotatp2[0]*coef3,rotatp2[1]*coef3)
    image.write(ligne((0,0),rotatp1))
    image.write(ligne((0,0),rotatp2))
    image.write(arc(r,rotatp1,rotatp2))
    image.write("<g>\n")
    image.write(arc(t,smallrp1,smallrp2))
    image.write(ligne((0,0),smallrp1))
    image.write(ligne((0,0),smallrp2))
    image.write("</g>")
    
    
    image.write(pied)
    image.close()
    
