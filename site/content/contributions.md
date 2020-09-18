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
from numpy_survey_results.utils import flatten, gluval
# Location of generated content
os.makedirs('_generated', exist_ok=True)
# For variable integration
from myst_nb import glue
```

# Community Contributions and Development

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
    'interested', 'limitations'
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
# Compute fraction of regular contributors.
num_oss_regular = np.sum(ossdata['regular'][oss_contributors_mask] == 'Yes')
num_np_regular = np.sum(npdata['regular'][np_contributors_mask] == 'Yes')
# Links for report
glue('num_respondents', npdata.shape[0], display=False);
glue(
    'oss_contributors',
    gluval(num_oss_contributors, num_respondents),
    display=False
)
glue(
    'np_contributors',
    gluval(num_np_contributors, num_respondents),
    display=False
)
glue(
    'numpy_and_oss_contributors',
    gluval(num_both_contributors, num_np_contributors),
    display=False
)
glue(
    'oss_regulars',
    gluval(num_oss_regular, num_oss_contributors),
    display=False
)
glue(
    'np_regulars',
    gluval(num_np_regular, num_np_contributors),
    display=False
)
```
% TODO: Intro sentences here about open-source development and community-led
% nature of NumPy.

# NumPy & OSS Contributors

Of the {glue:text}`num_respondents` survey participants, 
{glue:text}`oss_contributors` have contributed to at least one open source
software project, while {glue:text}`np_contributors` have contributed to
NumPy specifically.
{glue:text}`oss_regulars` of OSS contributors are *currently*[^currently]
regular contributors to at least one OSS project, while
{glue:text}`np_regulars` of the NumPy contributors contribute to NumPy
regularly.
Reflecting its central position in the scientific Python ecosystem, 
{glue:text}`numpy_and_oss_contributors` of NumPy contributors reported
contributing to other OSS projects as well.

## OSS Contributions

The following figure illustrates shows what fraction of contributors are 
working on various popular scientific Python projects.

[^currently]: i.e. regularly contributing at the time of the survey. This does
              not include contributors who have contributed regularly to
              projects in the past.

```{code-cell} ipython3
---
tags: [hide-input]
---
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
        100 * cnts / mask.sum(),
        align='edge',
        label=label,
    )
ax.set_yticks(np.arange(start_ind, 2 * len(labels), 2))
ax.set_yticklabels(labels)
ax.set_xlabel('Percentage of Contributors')
ax.legend()
fig.tight_layout()
```

## Types of Contributions

We also asked **in what ways** people are contributing to open-source software
projects.
The following figure shows what percentage of contributors reported participating
in some common tasks.

% TODO: Clean up data here so that NumPy/Other OSS contributions can be 
% directly compared (like above figure). WARNING: the current solution in
% code cell below is *very* hacky

```{code-cell} ipython3
---
tags: [hide-input]
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

## How Did Contributors Get Their Start?

We also asked how contributors got started working on the OSS packages that
they contribute to:

```{code-cell} ipython3
---
tags: [hide-input]
---
fig, ax = plt.subplots(figsize=(12, 8))
for start_ind, (data, mask, label) in enumerate(zip(
    (ossdata, npdata), 
    (oss_contributors_mask, np_contributors_mask),
    ('Non-NumPy Contributors', 'NumPy Contributors')
)):
    how_data = data['how_got_started'][mask]
    # Remove non-responses
    how_data = how_data[how_data != '']
    data = flatten(how_data)
    labels, cnts = np.unique(data, return_counts=True)
    # Plot
    ax.barh(
        np.arange(start_ind, 2 * len(labels), 2),
        100 * cnts / len(how_data),
        align='edge',
        label=label,
    )
ax.set_yticks(np.arange(start_ind, 2 * len(labels), 2))
ax.set_yticklabels(labels)
ax.set_xlabel('Percentage of Contributors')
ax.legend()
fig.tight_layout()
```

## Motivations

We asked NumPy contributors about what motivates them to contribute to NumPy.

```{code-cell} ipython3
---
tags: [hide-input]
---
# NumPy data only, no need to apply np/oss masks
motivations = npdata['motivations'][npdata['motivations'] != '']
labels, cnts = np.unique(flatten(motivations), return_counts=True)
I = np.argsort(cnts)
labels, cnts = labels[I], cnts[I]

fig, ax = plt.subplots(figsize=(12, 6))
ax.barh(np.arange(len(labels)), 100 * cnts / len(motivations))
ax.set_yticks(np.arange(len(labels)))
ax.set_yticklabels(labels)
ax.set_xlabel('Percentage of NumPy Contributors')
fig.tight_layout()
```

## Retention

Finally, we asked NumPy contributors whether they plan to continue to 
contribute to NumPy.
{glue:text}`regular_continue_pct` of survey participants who identified
themselves as regular NumPy contributors plan to continue contributing.
Of the {glue:text}`num_nonregular_np_contributors` NumPy contributors who did
not consider themselves *regular* contributors, {glue:text}`become_regular_pct`
plan to continue contributing.

```{code-cell} ipython3
---
tags: [hide-input]
---
np_regular_mask = npdata['regular'] == 'Yes'
regular_continue = npdata['continue'][np_regular_mask] == 'Yes'
glue(
    'regular_continue_pct',
    gluval(regular_continue.sum(), np_regular_mask.sum()),
    display=False
)
non_regular_contributor_mask = (np_contributors_mask) & (~np_regular_mask)
glue(
    'num_nonregular_np_contributors',
    non_regular_contributor_mask.sum(),
    display=False
)
num_nonregular_continue = np.sum(
    npdata['continue'][non_regular_contributor_mask] == 'Yes'
)
glue(
    'become_regular_pct',
    f'{100 * num_nonregular_continue / non_regular_contributor_mask.sum():1.0f}%',
    display=False
)
```

# Users Who Haven't (Yet) Contributed

We also wanted to get the perspective of NumPy (and other OSS) users who have
not directly contributed back to project --- is there generally interest in
doing so? What are the biggest stumbling blocks for users who want to
contribute back?
Of the {glue:text}`num_respondents` survey respondents, 
{glue:text}`oss_non_contributors` report never having contributed to an OSS
project and {glue:text}`np_non_contributors` report never having contributed to
NumPy specifically.

```{code-cell} ipython3
---
tags: [hide-input]
---
num_oss_non_contributors = np.sum(ossdata['contributed'] == 'No')
num_np_non_contributors = np.sum(npdata['contributed'] == 'No')
glue(
    'oss_non_contributors',
    gluval(num_oss_non_contributors, num_respondents),
    display=False
)
glue(
    'np_non_contributors',
    gluval(num_np_non_contributors, num_respondents),
    display=False
)
```

## Interest in Contributing

We asked these respondents whether they were interested in contributing to
the OSS packages that they use.
{glue:text}`oss_interested` said they were interested in contributing to OSS
generally, and {glue:text}`np_interested` to NumPy specifically.


```{code-cell} ipython3
---
tags: [hide-input]
---
oss_interested_mask = (ossdata['contributed'] == 'No') & (ossdata['interested'] == 'Yes')
np_interested_mask = (npdata['contributed'] == 'No') & (npdata['interested'] == 'Yes')
glue(
    'oss_interested',
    gluval(oss_interested_mask.sum(), num_oss_non_contributors),
    display=False
)
glue(
    'np_interested',
    gluval(np_interested_mask.sum(), num_np_non_contributors),
    display=False
)
```

## Contribution Blockers

We also asked respondents who expressed interest in contributing  about the
biggest blockers that prevent them from doing so.

% NOTE: Missing responses from NumPy-specific version of this question

```{code-cell} ipython3
---
tags: [hide-input]
---

fig, ax = plt.subplots(figsize=(12, 8))
limitations = ossdata['limitations'][oss_interested_mask]
# Remove non-responses
limitations = limitations[limitations != '']
data = flatten(limitations)
labels, cnts = np.unique(data, return_counts=True)
I = np.argsort(cnts)
labels, cnts = labels[I], cnts[I]
# Plot
ax.barh(np.arange(len(labels)), 100 * cnts / len(limitations))
ax.set_yticks(np.arange(len(labels)))
ax.set_yticklabels(labels)
ax.set_xlabel('Percentage of Contributors')
fig.tight_layout()
```

## Interests of Potential Contributors

We also asked potential NumPy contributors about there interests.

```{code-cell} ipython3
---
tags: [hide-input]
---
interests = npdata['interests'][np_interested_mask]
interests = interests[interests != '']
data = flatten(interests)
labels, cnts = np.unique(data, return_counts=True)
# TODO: Remove these hacks when categories have been synchronized
labels, cnts = labels[2:], cnts[2:]
labels[3] = 'Narrative documentation (e.g. tutorials)'
labels[-1] = 'Technical documentation (e.g. docstrings)'
I = np.argsort(cnts)
labels, cnts = labels[I], cnts[I]

fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(np.arange(len(labels)), 100 * cnts / len(interests))
ax.set_yticks(np.arange(len(labels)))
ax.set_yticklabels(labels)
ax.set_xlabel('Percentage of Contributors')
fig.tight_layout()
```
