from scipy import stats
Estimates=[100,300,450,350,700,650,450,600,900,890,700,450,120,130,1490,300,130,350,340,346,450,300,450,700,2000,1000,1515,1786,560,450,490,460,780,400,200,250,280,260,310,780,500,550,330,450,450,300,500,600,700,800,900,800,900,700,400,330,220,110,120,350,300,480,670,780,780,900,2000,1500,2000]
Estimates.sort()
m= stats.trim_mean(Estimates,0.1)
print(m)