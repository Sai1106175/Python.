#How to creat a new file.


f = open('myfile2.txt','w')
line =['Pradee \n', 'Sai \n' , 'Varun \n', 'Karthik \n']
f.writelines(line)
f.close()

