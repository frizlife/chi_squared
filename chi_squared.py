from scipy import stats
import pandas as pd
import collections
import matplotlib.pyplot as plt

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
# Drop null rows
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])
#plt.figure()
#plt.bar(freq.keys(), freq.values(), width=1)
#plt.show()
chi, p = stats.chisquare(freq.values())
print("The Chi-squared value is " + str(chi))
print("The p-value is " + str(p))
