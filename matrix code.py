import math
number_rows=int(input("Please enter 2 rows:")) # here we are creating a matrix and taking inputs
number_columns=int(input("Please enter 2 columns:"))
list2=[]
for i in range(number_rows):
  list1=[]
  for j in range(number_columns):
    values=int(input("Please enter your matrix entries 1,2,3,4 in order."))
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
#we do this by dividing every entry of the matrix by the determinant

inverse_of_matrix=[[list2[0][0]/determinant, list2[0][1]/determinant],
                [list2[1][0]/determinant, list2[1][1]/determinant]]


print("The inverse of the matrix is ",inverse_of_matrix )



#finding identity matrix
matrix_1=[(inverse_of_matrix[0][0]*list2[0][0])+(inverse_of_matrix[0][1]*list2[1][0])]
#here we are multiplying each entry of the matrix by inverse of the matrix
matrix_2=[(inverse_of_matrix[0][0]*list2[0][1])+(inverse_of_matrix[0][1]*list2[1][1])] 

matrix_3=[(inverse_of_matrix[1][0]*list2[0][0])+(inverse_of_matrix[1][1]*list2[1][0])] 

matrix_4=[(inverse_of_matrix[1][0]*list2[0][1])+(inverse_of_matrix[1][1]*list2[1][1])] 
resultant_identity=matrix_1+matrix_2+matrix_3+matrix_4
print("If we multiply the matrix with its inverse, it results in ",resultant_identity,"which is an identity matrix")