###  Collatz conjecture  ###  3x+1 - Problem  ###


import matplotlib.pyplot as plt
import pandas as pd
import os 


wd = os.getcwd()


## X-& Y-Werte erzeugen #####################

collatz_list = [19]							# StartWert

for i in collatz_list: 
	if i % 2 == 0:							# bei geraden Zahlen 
		y = i / 2
		collatz_list.append(y)
	else: 									# bei ungeraden Zahlen (i%2!=0) 
		y = 3*i + 1 
		collatz_list.append(y)
	
	if len(collatz_list) == 100: 
		break 


## Liste der natürlichen Zahlen erstellen  

def natZ(): 

	natZ_list = [] 
	x = 1 
	
	while x <= 100: 
		natZ_list.append(x) 
		x = x + 1 

	return natZ_list 


natZ_list = natZ()


## Plotten_1 ############################
plt.plot(collatz_list)
plt.title("Collatz Conjecture / 3x+1")
plt.xlabel("X-Werte")
plt.ylabel("Y-Werte")
plt.savefig(f'{wd}\collatz_testSave_Plot.png')
plt.show()

	
## Plotten_2 #######################
plt.bar(natZ_list, collatz_list)
#plt.show()
plt.scatter(natZ_list, collatz_list)
plt.title("Collatz Conjecture / 3x+1")
plt.xlabel("X-Werte")
plt.ylabel("Y-Werte")
plt.savefig(f'{wd}\collatz_testSave_ScatterBar.png')	
#plt.show()


## Pandas_Tabellen #################

## Series
# srs = pd.Series(collatz_list, index = natZ_list)
# srs.name = 'Collatz Conjecture'
# srs.index.name = 'x' 
# print(srs)


## DataFrame 

comment_list = []									# Test-Comments erzeugen
for i in collatz_list: 
	if i not in (1,4,2): 
		comment_list.append('Ok...')
	else: 
		comment_list.append('What...?')

df = pd.DataFrame({
	'x'		 : natZ_list, 
	'y'		 : collatz_list, 
	'Comment': comment_list
})
pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.width', None)
print(df)


## SAVE tables to file

df.to_csv(f'{wd}\CollatzConjecture_pandas.csv')

with open(os.path.join(wd, 'CollatzConjecture_pandas.txt'),'w') as outfile:
    df.to_string(outfile)
