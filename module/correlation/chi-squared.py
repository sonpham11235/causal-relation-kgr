import numpy as np
from scipy.stats import chi2_contingency

obs = np.array([[10, 10, 20], [20, 20, 20]])

chi2_res = chi2_contingency(obs)
g2_res = chi2_contingency(obs, lambda_='log-likelihood')

print("Chi-squared test result: " + str(chi2_res.statistic))
print("G2 test result: " + str(g2_res.statistic))