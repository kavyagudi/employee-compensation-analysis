import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
# data EDA
sns.set_theme(style="whitegrid")
os.makedirs("charts", exist_ok=True)
raw = pd.read_csv("EMPLOYEE.csv")
print(raw.shape)                 # (rows, columns)
raw.head()                       # first 5 rows
raw.info()                       # column names, types, non-null counts
print(raw.isnull().sum())        # missing values per column
print(raw.duplicated().sum())    # number of duplicate rows
raw.describe()   # min, max, mean, quartiles
# CLEAN THE DATA
df = raw.drop_duplicates().copy()
# Impossible ages -> missing
bad_age = (df.age < 18) | (df.age > 70)
df.loc[bad_age, "age"] = np.nan
# Salary outlier -> missing
df.loc[df.salary > 1_000_000, "salary"] = np.nan
# Text dates -> real dates (day-month-year)
df["join_date"] = pd.to_datetime(df["join_date"], format="%d-%m-%Y")
#CREATE NEW COLUMNS
df["join_year"] = df.join_date.dt.year
df["exp_band"] = pd.cut(df.experience, [-1, 2, 5, 10, 15], labels=["0-2", "3-5", "6-10", "11-15"])
df["rating"] = pd.Categorical(df.rating,["Poor", "Average", "Good", "Excellent"], ordered=True)
df["education"] = pd.Categorical(df.education,["Diploma", "Bachelors", "Masters"], ordered=True)
#CHARTS
fig, axes = plt.subplots(1, 3, figsize=(14, 4))
for ax, col in zip(axes, ["department", "city", "education"]):
    sns.countplot(data=df, x=col, ax=ax, color="#4C78A8")
    ax.set_title(f"Headcount by {col}")
    for c in ax.containers:
        ax.bar_label(c)
plt.tight_layout()
plt.savefig("charts/01_headcount.png", dpi=150, bbox_inches="tight")
plt.show()
# RELATION OF SALARY AND DEPARTMENT
order = df.groupby("department").salary.median().sort_values(ascending=False).index

summary = df.groupby("department").salary.agg(["count", "mean", "median", "min", "max"])
print(summary.loc[order].round(0))

sns.boxplot(data=df, x="department", y="salary", order=order)
plt.title("Salary distribution by department")
plt.show()
#EXPERIENCE B/W SALARY AND EXPERIENCE
corr = df.salary.corr(df.experience)
print(f"Correlation: {corr:.2f}")

sns.regplot(data=df, x="experience", y="salary",
            scatter_kws={"alpha": 0.5}, line_kws={"color": "red"})
plt.title(f"Experience vs salary (r = {corr:.2f})")
plt.show()

df.groupby("exp_band", observed=True).salary.median()
# RATING AFFECT PAY
print(df.groupby("rating", observed=True).salary.median())
print(df.groupby("education", observed=True).salary.median())

fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))
sns.boxplot(data=df, x="rating", y="salary", ax=axes[0])
sns.boxplot(data=df, x="education", y="salary", ax=axes[1])
plt.show()

# Share of each rating inside each department
ct = pd.crosstab(df.department, df.rating, normalize="index").round(2)
sns.heatmap(ct, annot=True, cmap="Blues", fmt=".2f")
plt.show()
# HARING TREND
hires = df.groupby("join_year").size()
hires.plot(marker="o")
plt.title("Employees hired per year")
plt.show()
#STATISTICAL TEST
sal = df.dropna(subset=["salary"])   # tests can't handle missing values

# Does salary differ across departments?
groups = [g.salary.values for _, g in sal.groupby("department")]
f, p = stats.f_oneway(*groups)
print(f"Department: F={f:.2f}, p={p:.2e}")

# Does salary go up with experience?
r, p = stats.pearsonr(sal.experience, sal.salary)
print(f"Experience: r={r:.2f}, p={p:.2e}")

# Does salary differ by rating?
groups = [g.salary.values for _, g in sal.groupby("rating", observed=True)]
f, p = stats.f_oneway(*groups)
print(f"Rating: F={f:.2f}, p={p:.3f}")

# Is rating related to department?
chi, p, dof, _ = stats.chi2_contingency(pd.crosstab(df.department, df.rating))
print(f"Rating vs department: p={p:.3f}")
# SAVE THE CLEANED DATA
df.to_csv("EMPLOYEE_cleaned.csv", index=False)
