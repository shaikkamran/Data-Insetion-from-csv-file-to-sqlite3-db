from databasecon  import connection
import csv
#
k=[]
l=[]
conn,c=connection()
with open('bowlersipl2016.csv') as csv_file:
	csvreader=csv.reader(csv_file)
	#print(csvreader)
	next(csvreader)
	c=0;x=0
	for line in csvreader:
		#print(line)
		if line !=['Pos', 'Player', 'Mat', 'Inns', 'Overs', 'Runs', 'Wkts', 'BBI', 'Avg', 'Econ', 'SR', '4w', '5w'] :
			if line[0]!='':
				l.append(line)
				#print(line)
				c+=1
			else:
				k.append(line[1])
				x+=1
	print(c,x)		
m=[['' for i in range(len(l[0])+1)]for j in range (len(l))]
for i in range (len(l)):
	for j in range (len(l[0])):
		m[i][j]=l[i][j]
	m[i][13]=k[i]					
conn.commit()
for i in m:
	print(i)
conn.close()

x=set(k)
print(x)