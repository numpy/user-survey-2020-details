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
# For variable integration
from myst_nb import glue
```

# Development and Community Contributions

% NOTE: The structure of the NumPy and non-NumPy contributions questions are
% slightly different.

```{code-cell} ipython3
---
tags: [hide-input]
---
# Load data related to open-source contributions *other* than NumPy

fname = "data/numpy_survey_results.tsv"
column_names = [
    'contributed', 'projects', 'projects_other', 'contr_type', 
    'contr_type_other', 'regular', 'how_got_started', 'how_got_started_other',
    'interest', 'limitations'
]
nonnumpy_contributions_dtype = np.dtype({
    "names": column_names,
    "formats": ['<U1024'] * len(column_names),
})

ossdata = np.loadtxt(
    fname, delimiter='\t', skiprows=3, dtype=nonnumpy_contributions_dtype, 
    usecols=range(31, 42), comments=None
)
```

```{code-cell} ipython3
---
tags: [hide-input]
---
# Load data related to NumPy contributions
column_names = [
    'contributed', 'contr_type', 'contr_type_other', 'regular',
    'how_got_started', 'how_got_started_other', 'motivations',
    'motivations_other', 'continue', 'limitations', 'limitations_other',
    'interested', 'interests', 'interests_other'
]

numpy_contributions_dtype = np.dtype({
    "names": column_names,
    "formats": ['<U1024'] * len(column_names),
})

npdata = np.loadtxt(
    fname, delimiter='\t', skiprows=3, dtype=numpy_contributions_dtype, 
    usecols=range(42, 57), comments=None
)
```

```{code-cell} ipython3
---
tags: [hide-input]
---
assert npdata.shape[0] == ossdata.shape[0]  # Sanity check on data
# Selection criteria for subsequent analysis
oss_contributors_mask = ossdata['contributed'] == 'Yes'
np_contributors_mask = npdata['contributed'] == 'Yes'
# Compute some basic parameters on OSS/np-specific contributions
num_respondents = npdata.shape[0]
num_oss_contributors = oss_contributors_mask.sum()
num_np_contributors = np_contributors_mask.sum()
num_both_contributors = np.sum(oss_contributors_mask & np_contributors_mask)
# Links for report
glue('num_respondents', npdata.shape[0], display=False);
glue(
    'oss_contributors',
    f'{num_oss_contributors} ({100 * num_oss_contributors / num_respondents:1.0f}%)',
    display=False
)
glue(
    'np_contributors',
    f'{num_np_contributors} ({100 * num_np_contributors / num_respondents:1.0f}%)',
    display=False
)
glue(
    'numpy_and_oss_contributors',
    f'{num_both_contributors} ({100 * num_both_contributors / num_np_contributors:1.0f}%)',
    display=False
)
```
% TODO: Intro sentences here about open-source development and community-led
% nature of NumPy.

Of the {glue:text}`num_respondents` survey participants, 
{glue:text}`oss_contributors` have contributed to at least one open source
software project, while {glue:text}`np_contributors` have contributed to
NumPy specifically.
Reflecting its central position in the scientific Python ecosystem, 
{glue:text}`numpy_and_oss_contributors` of NumPy contributors reported
contributing to other OSS projects as well.
The following figure illustrates shows what fraction of contributors are 
working on various popular scientific Python projects.

```{code-cell} ipython3
---
tags: [hide-input]
---
# Helper function for collating data
def flatten(data, delimiter=','):
    out = []
    for row in data:
        out.extend(row.split(delimiter))
    return out
# Remove less-popular projects
projects_to_drop = (
    'Gensim', 'spaCy', '',
    'Other (please specify - use commas to separate multiple entries)'
)

fig, ax = plt.subplots(figsize=(12, 8))
for (start_ind, mask, label) in zip(
    (0, 1), 
    (oss_contributors_mask, np_contributors_mask),
    ('Non-NumPy Contributors', 'NumPy Contributors')
):
    project_data = flatten(ossdata['projects'][mask])
    labels, cnts = np.unique(project_data, return_counts=True)
    # Projects to drop from all datasets
    for proj in projects_to_drop:
        drop = (labels != proj)
        labels, cnts = labels[drop], cnts[drop]
    # Plot
    ax.barh(
        np.arange(start_ind, 2 * len(labels), 2),
        100 * cnts / cnts.sum(),
        align='edge',
        label=label,
    )
ax.set_yticks(np.arange(start_ind, 2 * len(labels), 2))
ax.set_yticklabels(labels)
ax.set_xlabel('Percentage of Contributors')
ax.legend()
fig.tight_layout()
```

We also asked **in what ways** people are contributing to open-source software
projects.
The following figure shows what percentage of contributors reported participating
in some common tasks.

% TODO: Clean up data here so that NumPy/Other OSS contributions can be 
% directly compared (like above figure). WARNING: the current solution in
% code cell below is *very* hacky

```{code-cell} ipython3
---
tags: [hidden-input]
---
oss_contr_type = flatten(ossdata['contr_type'][oss_contributors_mask])
np_contr_type = flatten(npdata['contr_type'][np_contributors_mask])

fig, ax = plt.subplots(2, 1, figsize=(8, 12))
# NOTE: Unfortunately, the categories for the OSS & np contributions aren't 
# the same, so direct comparison is more difficult.
# Handle each dataset separately.
labels, cnts = np.unique(np_contr_type, return_counts=True)
# Ignore duplicate categories from bad split
labels, cnts = labels[1:], cnts[1:]
I = np.argsort(cnts)
labels, cnts = labels[I], cnts[I]
ax[0].set_title('NumPy Contributions')
ax[0].barh(np.arange(len(labels)), 100 * cnts / np_contributors_mask.sum(), align='center')
ax[0].set_yticks(np.arange(len(labels)))
ax[0].set_yticklabels(labels)
ax[0].set_xlabel('Percentage of NumPy Contributors')
labels, cnts = np.unique(oss_contr_type, return_counts=True)
labels, cnts = labels[3:], cnts[3:]
# TODO: Remove these hacks when categories have been synchronized
labels[3] = 'Developing tutorials'
labels[-1] = 'Writing documentation'
I = np.argsort(cnts)
labels, cnts = labels[I], cnts[I]
ax[1].set_title('Other (non-NumPy) OSS Contributions')
ax[1].barh(np.arange(len(labels)), 100 * cnts / oss_contributors_mask.sum(), align='center')
ax[1].set_yticks(np.arange(len(labels)))
ax[1].set_yticklabels(labels)
ax[1].set_xlabel('Percentage of OSS Contributors')
fig.tight_layout()
```
