import math
rows=int(input("Enter Rows:")) # here we are creating a matrix and taking inputs
columns=int(input("Enter Columns:"))
list2=[]
for i in range(rows):
  list1=[]
  for j in range(columns):
    values=int(input("Enter Values:"))
    list1.append(values)
  list2.append(list1)  
print("Matrix is ",list2)   

determinant=0 #now we will be taking determinant
determinant=(list2[0][0]*list2[1][1])-(list2[0][1]*list2[1][0])
print("Determinant is ",determinant)


side=list2[0][0] #taking adjoint
list2[0][0]=list2[1][1]
list2[1][1]=side

list2[0][1]=(list2[0][1]*-1)
list2[1][0]=(list2[1][0]*-1)
print("Adjoint of matrix is ",list2)

#taking inverse
inverse=[[list2[0][0]/determinant, list2[0][1]/determinant],
                [list2[1][0]/determinant, list2[1][1]/determinant]]
print("The inverse of the matrix is ",inverse )
for a in range(len(inverse)):
    for b in inverse:
        print(b[a], end ='  ')
    print()

#finding identity matrix
matrix1=[(inverse[0][0]*list2[0][0])+(inverse[0][1]*list2[1][0])] #for matrix 1
#matrix1=[(inverse[0][0]*list2[0][0])+(inverse[0][1]*list2[1][0])]
matrix2=[(inverse[0][0]*list2[0][1])+(inverse[0][1]*list2[1][1])] #for matrix 2
matrix3=[(inverse[1][0]*list2[0][0])+(inverse[1][1]*list2[1][0])] #for matrix 3
matrix4=[(inverse[1][0]*list2[0][1])+(inverse[1][1]*list2[1][1])] #for matrix 4
identity=matrix1+matrix2+matrix3+matrix4
print("If we multiply the matrix with its inverse, it results in ",identity,"which is an identity matrix")