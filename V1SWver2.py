import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import myPlotFunction
#import myUtils

#dataFilename = "C:\Users\Simon Weiler\Desktop\pystarters2019\data\All_three_exp_conditions_3.csv"
figFilename = "figures/absSpeedVsSpikesV1.png"

data = pd.read_csv(r"C:\Users\Simon Weiler\Desktop\pystarters2019\data\All_three_exp_conditions_3.csv", index_col=0)

regions = data.loc[:, "Region"].unique()
print(regions)
# ['SUB' nan 'V1' 'SC' 'RSPg' 'RSPd' 'Hip']
trialConditions = data.loc[:, "Trial Condition"].unique()
print(trialConditions)

# We will make a figure with len(trialConditions)==3 panels
f, axes = plt.subplots(1, len(trialConditions), sharey=True)

myPlotFunction.plotPanel(data,0, axes,"Vestibular")
myPlotFunction.plotPanel(data,1, axes,"Visual")
myPlotFunction.plotPanel(data,2,axes,"VisVes")

plt.show()

#myUtils.savefig(figFilename)




