from math import ceil

def traffic_signal(cycles):
	current_time = 0		

	for i in range(1,cycles+1):
		print("For cycle +++++++++++++++++++ ", i)
		if i%2 == 0:
			NS = 'Red'
			EW = 'Green'			
			for j in range(1,14):
				print("j ", j)				
				if(j>8 and j<11):
					EW = 'Yellow'
				elif(j==12 or j==13):
					EW = 'Red'
				print("NS ", NS)
				print("EW ", EW)
		else:
			NS = 'Green'
			EW = 'Red'
			for j in range(1,14):
				print("j ", j)				
				if(j>8 and j<11):
					NS = 'Yellow'
				elif(j==12 or j==13):
					NS = 'Red'
				print("NS ", NS)
				print("EW ", EW)



traffic_signal(5)	