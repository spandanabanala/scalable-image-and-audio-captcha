def calculate_accuracy():
  
 file= open('stuff.txt','r')
 lines=file.readlines()
 accurate_guess=0
 for i in lines:
   lhs=i[0:5]
   rhs=i[11:16]
   if(lhs==rhs):
     accurate_guess+=1
 accuracy=(accurate_guess/len(lines))*100
 print('accuracy:{}%'.format(accuracy))

calculate_accuracy()