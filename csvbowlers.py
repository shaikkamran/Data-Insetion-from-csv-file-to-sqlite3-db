from databasecon  import connection
import numpy as np
import csv

def typecast(col_list,arr,st):
	for i in col_list:
	
		for j in range (len(arr)):
			if st=='i':
				if arr[j][i]!='-' and arr[j][i]!='':

					arr[j][i]=int(arr[j][i])
				else:
					arr[j][i]=None
			elif st=='f':
				if arr[j][i]!='-' and arr[j][i]!='':

					arr[j][i]=float(arr[j][i])
				else:
					arr[j][i]=None	
				
			#print(arr[0][j])
	return arr		


k=[]
#l=[]
conn,c=connection()
with open('Bowler_ipl.csv') as csv_file:
	csvreader=csv.reader(csv_file)
	#print(csvreader)
	next(csvreader)
	cm=0;x=0
	for line in csvreader:
	    #print(line)
	    k.append(line)
k=typecast([0,2,3,5,6,11,12],k,'i')
k=typecast([4,8,9,10],k,'f')
#c.executemany('')
c.executemany('insert into Bowlersipl values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)',k)


conn.commit()

conn.close()


print(k[1])


