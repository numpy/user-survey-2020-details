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
plt.style.use('../../site.mplstyle')
%matplotlib inline
from numpy_survey_results.utils import gluval
# Location of generated content
os.makedirs('_generated', exist_ok=True)
# For variable integration
from myst_nb import glue
```

```{code-cell} ipython3
---
tags: [remove-cell]
---
# Vectorized helper functions for string processing
capitalize = np.vectorize(str.capitalize, otypes='U')
strip = np.vectorize(lambda s: s.strip('" '), otypes='U')
title = np.vectorize(str.title, otypes='U')
```

# Community

A summary of the demographic information of the NumPy survey respondents.

```{code-cell} ipython3
---
tags: [hide-input]
---
fname = "data/2021/numpy_survey_results.tsv"
column_names = [
    'age', 'gender', 'lang', 'lang_other', 'country', 'degree', 'degree_other',
    'field_of_study', 'field_other', 'role', 'role_other', 'version', 'version_other',
    'primary_use', 'share_code', 'programming_exp', 'numpy_exp', 'use_freq', 'components',
    'use_c_ext', 'prog_lang', 'prog_lang_other', 'surv2020'
]
demographics_dtype = np.dtype({
    "names": column_names,
    "formats": ['<U600'] * len(column_names),
})

data = np.loadtxt(
    fname, delimiter='\t', skiprows=3, dtype=demographics_dtype, 
    usecols=list(range(11, 33)) + [90], comments=None, encoding='UTF-16'
)

glue('2021_num_respondents', data.shape[0], display=False)
```

## Demographics

### Age

Of the {glue:text}`2021_num_respondents` survey respondents, 
{glue:text}`2021_num_age_respondents` shared their age.

The majority of respondents are in the age groups 25-34 and 35-44. Very few respondents are older than 55, and even fewer are younger than 18.

```{code-cell} ipython3
---
tags: [hide-input]
---
# Ignore empty fields and "prefer not to answer"
drop = np.logical_and(data['age'] != '', data['age'] != 'Prefer not to answer')
age = data['age'][drop]
labels, cnts = np.unique(age, return_counts=True)
ind = np.array([5,0,1,2,3,4])
labels, cnts = labels[ind], cnts[ind]

fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(
  np.arange(len(labels)),
  100 * cnts / age.shape[0], 
  tick_label=labels,
)
ax.set_ylabel('Percentage of Respondents')
ax.set_xlabel('Age Group')
ax.set_title("Age Distribution of Survey Respondents");
fig.tight_layout()

glue('2021_num_age_respondents', gluval(age.shape[0], data.shape[0]), display=False)
```

### Gender

Of the {glue:text}`2021_num_respondents` survey respondents,
{glue:text}`2021_num_gender` shared their gender.

An overwhelming majority of respondents identify as male. Only about 11% of respondents identify as female.

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
ax.set_title("Gender Distribution");
fig.tight_layout()

glue('2021_num_gender', gluval(gender.shape[0], data.shape[0]), display=False)
```

### Language Preference

Of the {glue:text}`2021_num_respondents` respondents,
{glue:text}`2021_num_lang_pref` shared their preferred language.

Over 67% of respondents reported English as their preferred language.

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

glue('2021_num_lang_pref', gluval(lang.shape[0], data.shape[0]), display=False)
```

````{admonition} Click to show/hide table
:class: toggle

```{include} _generated/language_preference_table.md
```
````

### Country of Residence

Of the {glue:text}`2021_num_respondents` respondents,
{glue:text}`2021_num_country_respondents`shared their current country of residence.
The survey saw respondents from {glue:text}`2021_num_unique_countries` countries in
all. A quarter of respondents reside in the United States.

The following chart shows the relative number of respondents from ~10 
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

# Plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(pcnts, labels=plabels, autopct='%1.1f%%')
ax.set_title("Country of Residence");
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

glue('2021_num_unique_countries', len(labels), display=False)
glue(
    '2021_num_country_respondents',
    gluval(country.shape[0], data.shape[0]),
    display=False
)
```

```{include} _generated/countries_by_continent.md
```

### Education

{glue:text}`2021_num_education` respondents shared their education history,
spanning the range from pre-highschool graduation through Doctorate level with
many other specialist degrees. 

Generally, respondents are highly educated. Nine out of ten have at least a Bachelor’s degree and one in three holds a PhD.

The following figure summarizes the distribution for the highest degrees obtained by respondents.

```{code-cell} ipython3
---
tags: [hide-input]
---
degree = data['degree'][data['degree'] != '']
labels, cnts = np.unique(degree, return_counts=True)

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(cnts, labels=labels, autopct='%1.1f%%', labeldistance=None)
ax.legend()
ax.set_title("Highest Level of Education");
fig.tight_layout()

glue('2021_num_education', gluval(degree.shape[0], data.shape[0]), display=False)
```

### Job Roles

{glue:text}`2021_num_top_3_categories` of the {glue:text}`2021_num_occupation`
respondents who shared their occupation identify as an
{glue:text}`2021_top_3_categories`.

```{code-cell} ipython3
---
tags: [hide-input]
---
role = data['role'][data['role'] != '']
labels, cnts = np.unique(role, return_counts=True)

# Sort results by number of selections
inds = np.argsort(cnts)
labels, cnts = labels[inds], cnts[inds]

fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(np.arange(len(cnts)), cnts, align='center')
ax.set_yticks(np.arange(len(cnts)))
ax.set_yticklabels(labels)
ax.set_xlabel("Number of Respondents")
ax.set_title("Current Role");
fig.tight_layout()

glue('2021_num_occupation', role.shape[0], display=False)
glue(
    '2021_num_top_3_categories',
    gluval(cnts[-3:].sum(), role.shape[0]),
    display=False,
)
glue('2021_top_3_categories', f"{labels[-3]}, {labels[-2]}, or {labels[-1]}", display=False)
```

### 2020 Community Survey Respondents

{glue:text}`2021_num_surv2020_respondents` of respondents shared whether or not they responded to the 2020 Community Survey. Only {glue:text}`2021_yes_percent` percent of people reported having completed last year's survey.

```{code-cell} ipython3
---
tags: [hide-input]
---
# Ignore empty fields and "prefer not to answer"
drop = np.logical_and(data['surv2020'] != '', data['surv2020'] != 'Not sure')
surv2020 = data['surv2020'][drop]
labels, cnts = np.unique(surv2020, return_counts=True)

glue('2021_num_surv2020_respondents', gluval(surv2020.shape[0], data.shape[0]), display=False)
yes_percent = 100 * cnts[1].sum() / cnts.sum()
glue('2021_yes_percent', f"{yes_percent:1.1f}", display=False)
```

## Experience and Usage

### Programming Experience

{glue:text}`2021_programming_exp_5plus_years` of respondents have significant
experience in programming, with veterans (10+ years) taking the lead.
Interestingly, when it comes to using NumPy, noticeably more of our
respondents identify as beginners than experienced users.

```{code-cell} ipython3
---
tags: [hide-input]
---
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
# Ascending order for figure
ind = np.array([-1, 0, 2, 3, 1])
for exp_data, ax in zip(('programming_exp', 'numpy_exp'), axes):
    # Analysis
    prog_exp = data[exp_data][data[exp_data] != '']
    labels, cnts = np.unique(prog_exp, return_counts=True)
    cnts = 100 * cnts / cnts.sum()
    labels, cnts = labels[ind], cnts[ind]
    # Generate text on general programming experience
    glue(f'2021_{exp_data}_5plus_years', f"{cnts[-2:].sum():2.0f}%", display=False)
    # Plotting
    ax.bar(np.arange(len(cnts)), cnts)
    ax.set_xticks(np.arange(len(cnts)))
    ax.set_xticklabels(labels)
axes[0].set_title('General Programming Experience')
axes[0].set_ylabel('Percentage of Respondents')
axes[1].set_title('Experience with NumPy');
fig.autofmt_xdate();
fig.tight_layout();
```

### Programming Languages

{glue:text}`2021_num_proglang_respondents` of survey participants shared their
experience with other programming languages.
{glue:text}`2021_num_top_lang` of respondents are familiar with {glue:text}`2021_top_lang`,
and {glue:text}`2021_num_2nd_lang` with {glue:text}`2021_second_lang`.


```{code-cell} ipython3
---
tags: [hide-input]
---
pl = data['prog_lang'][data['prog_lang'] != '']
num_respondents = len(pl)
glue('2021_num_proglang_respondents', gluval(len(pl), data.shape[0]), display=False)

# Flatten & remove 'Other' write-in option
other = 'Other (please specify, using commas to separate individual entries)'
apl = []
for row in pl:
    if 'Other' in row:
        row = ','.join(row.split(',')[:-2])
        if len(row) < 1:
            continue
    apl.extend(row.split(','))
labels, cnts = np.unique(apl, return_counts=True)
cnts = 100 * cnts / num_respondents
I = np.argsort(cnts)
labels, cnts = labels[I], cnts[I]

fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(np.arange(len(cnts)), cnts, align='center')
ax.set_yticks(np.arange(len(cnts)))
ax.set_yticklabels(labels)
ax.set_xlabel("Percentage of Respondents")
ax.set_title("Programming Language Familiarity")
fig.tight_layout()

# Highlight two most popular
glue('2021_num_top_lang', f"{cnts[-1]:2.0f}%", display=False)
glue('2021_top_lang', labels[-1], display=False)
glue('2021_num_2nd_lang', f"{cnts[-2]:2.0f}%", display=False)
glue('2021_second_lang', labels[-2], display=False)
```

{glue:text}`2021_percent_other` percent of respondents reported familiarity with
computer languages other than those listed above.
Of these, {glue:text}`2021_most_popular` was the most popular with 
{glue:text}`2021_most_popular_pct` respondents using this language.
A listing of other reported languages can be found below (click to expand).

%TODO: Create mapping to consolidate write-in responses, e.g. 
%Lisp, lisp, common lisp, elisp, all -> 'Lisp'

```{code-cell} ipython3
---
tags: [remove-cell]
---
# Determine most popular 'other' language.
plo = data['prog_lang_other'][data['prog_lang_other'] != '']
# Process write-in field
aplo = []
for row in plo:
    # NOTE: ignoring cases in language name
    aplo.extend([l.strip().lower() for l in row.split(',')])
labels, cnts = np.unique(aplo, return_counts=True)

glue('2021_percent_other', gluval(len(plo), len(pl)), display=False)
#NOTE: capitalization doesn't generalize!
glue('2021_most_popular', labels[np.argmax(cnts)].capitalize(), display=False)
glue('2021_most_popular_pct', gluval(cnts.max(), len(pl)), display=False)
```

```{code-cell} ipython3
---
tags: [remove-input, hide-output]
---
print(labels)
```

### Code Sharing

{glue:text}`2021_num_share_code` of survey participants shared information on how many others they typically share code with. Most respondents share code with {glue:text}`2021_top_share` people.


```{code-cell} ipython3
---
tags: [hide-input]
---
from numpy_survey_results.utils import flatten

share_code = data['share_code'][data['share_code'] != '']
labels, cnts = np.unique(flatten(share_code), return_counts=True)

# Sort categories in ascending order (i.e. "0", "1-2", "3-5", "5-10", "10+")
ind = np.array([0, 1, 3, 4, 2])
labels, cnts = labels[ind], cnts[ind]

fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(
    np.arange(len(labels)),
    100 * cnts / share_code.shape[0], 
    tick_label=labels,
)
ax.set_ylabel('Percentage of Respondents')
ax.set_xlabel('Number of people you typically share code with')
fig.tight_layout()

# Highlights most popular
glue('2021_top_share', labels[np.argmax(cnts)], display=False)

# Number who answered question
glue(
    '2021_num_share_code',
    gluval(share_code.shape[0], data.shape[0]),
    display=False
)
```
