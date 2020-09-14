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
import os
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
# Location of generated content
os.makedirs('_generated', exist_ok=True)
```

```{code-cell} ipython3
---
tags: [remove-cell]
---
# Vectorized helper functions for string processing
capitalize = np.vectorize(str.capitalize, otypes='U')
strip = np.vectorize(str.strip, otypes='U')
title = np.vectorize(str.title, otypes='U')
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

## Language Preference

Of the 1236 respondents, 1173 shared their preferred language.

```{code-cell} ipython3
---
tags: [hide-input]
---
# Ignore empty fields
lang = data['lang'][data['lang'] != '']
# Self-reported language
lang_other = data['lang_other'][data['lang_other'] != '']
lang_other = capitalize(lang_other)
lang = np.concatenate((lang, lang_other))
labels, cnts = np.unique(lang, return_counts=True)
cnts = 100 * cnts / cnts.sum()
I = np.argsort(cnts)[::-1]
labels, cnts = labels[I], cnts[I]

# Create a summary table
with open('_generated/language_preference_table.md', 'w') as of:
    of.write('| **Language** | **Preferred by % of Respondents** |\n')
    of.write('|--------------|-----------------------------------|\n')
    for lbl, percent in zip(labels, cnts):
        of.write(f'| {lbl} | {percent:1.1f} |\n')
```

````{admonition} Click to show/hide table
:class: toggle

```{include} _generated/language_preference_table.md
```
````

## Country of Residence

Of the 1236 respondents, 1095 shared their current country of residence. The
survey saw respondents from 75 countries in all.

The following chart shows the relative number of respondents from ~20 
countries with the largest number of participants. 
For privacy reasons, countries with fewer than a certain number of 
respondents are not included in the figure, and are instead listed in
the subsequent table.

```{code-cell} ipython3
---
tags: [hide-input]
---
# Preprocess data
country = data['country'][data['country'] != '']
country = strip(country)
# Distribution
labels, cnts = np.unique(country, return_counts=True)
# Privacy filter
num_resp = 10
cutoff = (cnts > num_resp)
plabels = np.concatenate((labels[cutoff], ['Other']))
pcnts = np.concatenate((cnts[cutoff], [cnts[~cutoff].sum()]))

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(pcnts, labels=plabels, autopct='%1.1f%%')
ax.set_title('Global Distribution of Respondents')
fig.tight_layout()

# Map countries to continents
import pycountry_convert as pc
cont_code_to_cont_name = {
    'NA': 'North America',
    'SA': 'South America',
    'AS': 'Asia',
    'EU': 'Europe',
    'AF': 'Africa',
    'OC': 'Oceania',
}
def country_to_continent(country_name):
    cc = pc.country_name_to_country_alpha2(country_name)
    cont_code = pc.country_alpha2_to_continent_code(cc)
    return cont_code_to_cont_name[cont_code]
c2c = np.vectorize(country_to_continent, otypes='U')

# Organize countries below the privacy cutoff by their continent
remaining_countries = labels[~cutoff]
continents = c2c(remaining_countries)
with open('_generated/countries_by_continent.md', 'w') as of:
    of.write('|  |  |\n')
    of.write('|---------------|-------------|\n')
    for continent in np.unique(continents):
        clist = remaining_countries[continents == continent]
        of.write(f"| **{continent}:** | {', '.join(clist)} |\n")
```

```{include} _generated/countries_by_continent.md
```

## Education

1118 respondents shared their education history, spanning the range from 
pre-highschool graduation through Doctorate level with many other specialist
degrees. 
The following figure summarizes the distribution for the most common types of
degrees reported.

```{code-cell} ipython3
---
tags: [hide-input]
---
degree = data['degree'][data['degree'] != '']
labels, cnts = np.unique(degree, return_counts=True)

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(cnts, labels=labels, autopct='%1.1f%%')
ax.set_title("Distribution of Highest Degree Obtained by Respondents")
fig.tight_layout()
```

## Occupation

1106 respondents shared their current occupation.

```{code-cell} ipython3
---
tags: [hide-input]
---
role = data['role'][data['role'] != '']
labels, cnts = np.unique(role, return_counts=True)

fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(np.arange(len(cnts)), cnts, align='center')
ax.set_yticks(np.arange(len(cnts)))
ax.set_yticklabels(labels)
ax.set_xlabel("Number of Respondents")
```

# Experience and Usage

## Programming Experience

```{code-cell} ipython3
---
tags: [hide-input]
---
prog_exp = data['programming_exp'][data['programming_exp'] != '']
labels, cnts = np.unique(prog_exp, return_counts=True)
cnts = 100 * cnts / cnts.sum()
# Ascending order for figure
ind = np.array([-1, 0, 2, 3, 1])
labels, cnts = labels[ind], cnts[ind]

fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(np.arange(len(cnts)), cnts)
ax.set_xticks(np.arange(len(cnts)))
ax.set_xticklabels(labels)
fig.autofmt_xdate();
ax.set_title("Programming Experience of Respondents");
ax.set_ylabel("Percentage of Respondents");
