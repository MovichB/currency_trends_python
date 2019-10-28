#Author @MovichB
#Support and Resistance using Seaborn
nb = 30 #number of days 
datee,date,datee_1,date_1,up,down = [],[],[],[],[],[]

upper = BD_tend.loc[range(0,nb),'Ouv. + Variation %'].sort_values(ascending = False)[:3].values #3 max values
lower = BD_tend.loc[range(0,nb),'Ouv. + Variation %'].sort_values(ascending = True)[:3].values #3 min values

for u in upper:
    up.append(u)    
    datee.append(BD_tend.loc[BD_tend['Ouv. + Variation %']==u,'Date'].values)
for i in datee:
    date.append(i[0])
    
for d in lower:
    down.append(d)    
    datee_1.append(BD_tend.loc[BD_tend['Ouv. + Variation %']==d,'Date'].values)
for j in datee_1:
    date_1.append(j[0])
    
try:
    grid = sns.JointGrid(BD_tend.loc[range(0,nb),'Date'],BD_tend.loc[range(0,nb),'Ouv. + Variation %'], data = BD_tend, space=0, ratio=50)
    grid.plot_joint(sns.lineplot, color="g")
    grid.plot_joint(sns.regplot(d_up['Date'].map(dt.datetime.toordinal),upper,ci=0),sns.regplot(d_down['Date'].map(dt.datetime.toordinal),lower,ci=0),sns.regplot(d_down['Date'].map(dt.datetime.toordinal),rolling_mean_dern(40)))
except:
    TypeError
