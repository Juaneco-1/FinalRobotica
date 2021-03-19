import numpy as np
import math
class directo():
    teta1=0
    teta3=0
    teta4=0
    teta5=0
    teta2=0
    teta6=0
    lo=5
    l6=5
    d2=0
    l4=0
    d3=0
    d5=0
    a1=0
    a2=0
    a3=0
    a4=0
    a5=0
    a6=0
    alfa1=0
    alfa2=0
    alfa3=0
    alfa4=0
    alfa5=0
    alfa6=0
    sol=[]
    def __init__(self,t1,t2,t3,t4,t5,t6,dis1,dis2,dis3,dis4,dis5,dis6,a1,a2,a3,a4,a5,a6
    ,alfa1,alfa2,alfa3,alfa4,alfa5,alfa6):
        self.teta1=float(t1)
        self.teta2=float(t2)
        self.teta3=float(t3)
        self.teta4=float(t4)+180
        self.teta5=float(t5)+180
        self.teta6=float(t6)
        self.d1=float(dis1)
        self.d2=float(dis2)
        self.d3=float(dis3)
        self.l4=float(dis4)
        self.d5=float(dis5)
        self.d6=float(dis6)
        self.a1=float(a1)
        self.a2=float(a2)
        self.a3=float(a3)
        self.a4=float(a4)
        self.a5=float(a5)
        self.a6=float(a6)
        self.alfa1=float(alfa1)
        self.alfa2=float(alfa2)
        self.alfa3=float(alfa3)
        self.alfa4=float(alfa4)
        self.alfa5=float(alfa5)
        self.alfa6=float(alfa6)
        #self.d6=float(dis6)
        self.matrices()
        
    def matrices(self):
        A01=np.array([[ math.cos(math.radians(self.teta1)), -math.sin(math.radians(self.teta1)),0,0],
        [ math.sin(math.radians(self.teta1)),math.cos(math.radians(self.teta1)),0,0],
        [ 0, 0, 1,self.lo],
        [ 0, 0,0,1]])
        print(A01)
        
        A12=np.array([[ 0, 0, 1,0],
        [ 1,0,0,0],
        [0,1,0,self.d2],
        [0,0,0,1]])

        A23=np.array([[ 0, -1, 0,0],
        [ 1,0,0,0],
        [0,0,1,self.d3],
        [0,0,0,1]])

        A34=np.array([[math.cos(math.radians(self.teta4)),0,math.sin(math.radians(self.teta4)),0],
        [ math.sin(math.radians(self.teta4)),0,-math.cos(math.radians(self.teta4)),0],
        [ 0,1,0,self.l4],
        [ 0, 0,0,1]])

        A45=np.array([[ math.cos(math.radians(self.teta5)),0,math.sin(math.radians(self.teta5)),0],
        [ math.sin(math.radians(self.teta5)),0,-math.cos(math.radians(self.teta5)),0],
        [ 0, 1, 0,0],
        [ 0, 0,0,1]])

        A56=np.array([[ math.cos(math.radians(self.teta6)), -math.sin(math.radians(self.teta6)),0,0],
        [ math.sin(math.radians(self.teta6)),math.cos(math.radians(self.teta6)),0,0],
        [ 0, 0, 1,self.l6],
        [ 0, 0,0,1]])
        self.multiplicacion(A01,A12,A23,A34,A45,A56)
    def multiplicacion(self,A01,A12,A23,A34,A45,A56):
        p1=np.dot(A01,A12)
        p2=np.dot(p1,A23)
        p3=np.dot(p2,A34)
        p4=(np.dot(p3,A45))
        T=np.round(np.dot(p4,A56),1)

        print(T)
        
        if (T[1,3] == -0.0):
            T[1,3]=0
        self.sol.clear()
        
        self.sol.append(T[0,3])
        self.sol.append(T[1,3])
        self.sol.append(T[2,3])

        print(T[0,3])
        print(T[1,3])
        print(T[2,3])
    def __iter__(self):
        return iter(self.sol)
