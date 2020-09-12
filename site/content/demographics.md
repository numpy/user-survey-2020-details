---
jupytext:
  formats: md:myst
  text_representation:
    format_name: myst
kernelspec:
  display_name: Python 3
  name: python3
---

```{code-cell} ipython3
---
tags: [remove-cell]
---
# Notebook setup
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
```

# Demographics

A summary of the demographic information of the NumPy survey respondents.

```{code-cell} ipython3
---
tags: [hide-input]
---
fname = "data/numpy_survey_results.tsv"
column_names = [
    'age', 'gender', 'lang', 'lang_other', 'country', 'degree', 'degree_other',
    'field_of_study', 'field_other', 'role', 'role_other', 'version', 
    'primary_use', 'programming_exp', 'numpy_exp', 'use_freq', 'components',
    'use_c_ext', 'prog_lang', 'prog_lang_other',
]
demographics_dtype = np.dtype({
    "names": column_names,
    "formats": ['<U512'] * len(column_names),
})

data = np.loadtxt(
    fname, delimiter='\t', skiprows=3, dtype=demographics_dtype, 
    usecols=range(11, 31), comments=None
)
```


## Age

Of the 1236 survey respondents, 1089 shared their age.

```{code-cell} ipython3
---
tags: [hide-input]
---
age = data['age']
# Preprocessing
ignore_chars = ('', '> 40')
for value in ignore_chars:
    age = age[age != value]
age = age.astype(int)
# Distribution
bwidth = 10
bedges = np.arange(0, age.max() + bwidth, bwidth)
h, _ = np.histogram(age, bins=bedges)
h = 100 * h / h.sum()

fig, ax = plt.subplots(figsize=(12, 8))
x = np.arange(len(h))
ax.bar(x, h)
labels = [f"{low}-{high - 1}" for low, high in zip(bedges[:-1], bedges[1:])]
ax.set_xticks(x)
ax.set_xticklabels(labels)
fig.autofmt_xdate();
ax.set_title("Age Distribution of Survey Respondents");
ax.set_xlabel("Age (yrs)");
ax.set_ylabel("Percentage of Respondents");
```

## Gender

Of the 1236 survey respondents, 1100 shared their gender

```{code-cell} ipython3
---
tags: [hide-input]
---
# Ignore empty fields and "prefer not to answer"
drop = np.logical_and(data['gender'] != '', data['gender'] != 'Prefer not to answer')
gender = data['gender'][drop]
labels, cnts = np.unique(gender, return_counts=True)

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(cnts, labels=labels, autopct='%1.1f%%')
ax.set_title("Gender Distribution of Survey Respondents");
fig.tight_layout()
```
