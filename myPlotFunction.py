
import statsmodels.api as sm
import matplotlib.pyplot as plt

def plotPanel(data, ax, axes,trialCondition):
    # Extract the subset of the data corresponding to vestibular-only stimulation
    # and recordings from V1
    dataSubset = data.loc[(data["Trial Condition"] == trialCondition) & (data["Region"] == "V1"), :]
    # Plot the spikes counts in Bin(i) as a function of the absolute value of
    # the stimulation speed
    axes[ax].scatter(x=abs(dataSubset["Speed"]), y=dataSubset["Bin(i)"], c="lightgray")
    axes[ax].set_title(trialCondition)
    # Estimate the regression line
    regressors = sm.add_constant(abs(dataSubset["Speed"]))
    fit = sm.OLS(endog=dataSubset["Bin(i)"], exog=regressors).fit()
    legend = "p={:.4f}".format(fit.pvalues[1])
    axes[ax].plot(abs(dataSubset["Speed"]), fit.params[0] + abs(dataSubset["Speed"]) * fit.params[1], color="red",
                 label=legend)
    axes[ax].legend(loc="upper left")
    axes[ax].set_title(trialCondition)
    axes[ax].set_xlabel("Abs(Speed)")
    axes[ax].set_ylabel("Spike Count")