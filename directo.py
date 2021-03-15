import numpy as np
import math
class directo():
    teta1=0
    d1=0
    a2=0
    teta3=0
    teta4=0
    teta5=0
    teta2=0
    teta6=0
    a5=0
    d4=0
    d3=0
    d6=0
    sol=[]
    def __init__(self,t1,t4,t5,t6,dis1,dis3,dis6):
    
        self.teta1=float(t1)
        self.teta4=float(t4)
        self.teta5=float(t5)
        self.teta6=float(t6)
        self.d1=float(dis1)
        self.d3=float(dis3)
        self.d6=float(dis6)
        self.matrices()
        
    def matrices(self):
        A01=np.array([[ math.cos(math.radians(self.teta1)), -math.sin(math.radians(self.teta1)),0,0],
        [ math.sin(math.radians(self.teta1)),math.cos(math.radians(self.teta1)),0,0],
        [ 0, 0, 1,self.d1],
        [ 0, 0,0,1]])
        print(A01)
        
        A12=np.array([[ 0, 0, 1,0],
        [ 1,0,0,0],
        [0,1,0,0],
        [0,0,0,1]])

        A23=np.array([[ 0, -1, 0,0],
        [ 1,0,0,0],
        [0,0,1,self.d3],
        [0,0,0,1]])

        A34=np.array([[math.cos(math.radians(self.teta4)),0,math.sin(math.radians(self.teta4)),0],
        [ math.sin(math.radians(self.teta4)),0,-math.cos(math.radians(self.teta4)),0],
        [ 0,1,0,0],
        [ 0, 0,0,1]])

        A45=np.array([[ math.cos(math.radians(self.teta5)),0,math.sin(math.radians(self.teta5)),0],
        [ math.sin(math.radians(self.teta5)),0,-math.cos(math.radians(self.teta5)),0],
        [ 0, 1, 0,0],
        [ 0, 0,0,1]])

        A56=np.array([[ math.cos(math.radians(self.teta6)), -math.sin(math.radians(self.teta6)),0,0],
        [ math.sin(math.radians(self.teta6)),math.cos(math.radians(self.teta6)),0,0],
        [ 0, 0, 1,self.d6],
        [ 0, 0,0,1]])
        self.multiplicacion(A01,A12,A23,A34,A45,A56)
    def multiplicacion(self,A01,A12,A23,A34,A45,A56):
        p1=np.dot(A01,A12)
        p2=np.dot(p1,A23)
        p3=np.dot(p2,A34)
        p4=(np.dot(p3,A45))
        T=np.round(np.dot(p4,A56),1)

        print(T)
        print(T[0,3])
        print(T[1,3])
        print(T[2,3])

        self.sol.append(T[0,3])
        self.sol.append(T[1,3])
        self.sol.append(T[2,3])
    def __iter__(self):
        return iter(self.sol)
