import math
import scipy.stats as stats

# sample A
n1 = 30
x1 = 85
s1 = 6

# sample B
n2 = 30
x2 = 82
s2 = 5

# calculate pooled standard deviation
sp = math.sqrt(((n1 - 1)*(s1**2) + (n2 - 1)*(s2**2)) / (n1 + n2 - 2))

# calculate t-value
t = (x1 - x2) / (sp * math.sqrt((1/n1) + (1/n2)))

# calculate degrees of freedom
df = n1 + n2 - 2


alpha = 0.01
# t_critical/t tabulated for two tail test
t_crit = stats.t.ppf(1-alpha/2, df)
# # t_critical/t tabulated  for one tail test
# t_crit = stats.t.ppf(1-alpha, df)


# compare t-value and critical t-value
if abs(t) > t_crit:
    print("Reject null hypothesis. The mean score for teaching method A is significantly different from the mean score for teaching method B.")
else:
    print("Fail to reject null hypothesis. There is not enough evidence to conclude that the mean score for teaching method A is significantly different from the mean score for teaching method B.")

print("t-value:", t)
print("critical t-value:", t_crit)
