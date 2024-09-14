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
from numpy_survey_results.utils import gluval, gen_mdlist
# Location of generated content
os.makedirs('_generated', exist_ok=True)
# For variable integration
from myst_nb import glue
```

# Priorities

```{code-cell} ipython3
---
tags: [hide-input]
---
fname = "data/2021/numpy_survey_results.tsv"
column_names = [
    'website', 'performance', 'reliability', 'packaging', 'new_features',
    'documentation', 'other'
]
priorities_dtype = np.dtype({
    "names": column_names,
    "formats": ['U1'] * len(column_names),
})

data = np.loadtxt(
    fname, delimiter='\t', skiprows=3, dtype=priorities_dtype,
    usecols=range(58, 65), comments=None, encoding='UTF-16'
)

# Discard empty data
num_respondents = data.shape[0]
unstructured = data.view(np.dtype('(7,)U1'))
data = data[~np.any(unstructured == '', axis=1)]

glue('2021_num_prioritizers', gluval(data.shape[0], num_respondents), display=False)
```

We asked survey respondents to share their priorities for NumPy to get a sense
of the needs/desires of the NumPy community.
Users were asked to rank the following categories in order of priority:

```{code-cell} ipython3
---
tags: [hide-input]
---
for category in sorted(column_names[:-1]):
    print(f" - {category.replace('_', ' ').capitalize()}")
```

A write-in category (`Other`) was also included so that participants could
share priorities beyond those listed above.

## Overview

Of the {glue}`demographics.md::2021_num_respondents` survey participants,
{glue:text}`2021_num_prioritizers` shared their priorities for NumPy moving forward.

To get a sense of the overall relative "importance" of each of the categories,
the following figure summarizes the score for each category as determined by
the [Borda counting procedure for ranked-choice voting][borda-wiki].

[borda-wiki]: https://en.wikipedia.org/wiki/Borda_count

```{code-cell} ipython3
---
tags: [hide-input]
---
# Unstructured, numerical data
raw = data.view(np.dtype('U1')).reshape(-1, len(column_names)).astype(int)
borda = len(column_names) + 1 - raw
relative_score = np.sum(borda, axis=0)
relative_score = 100 * relative_score / relative_score.sum()
# Prettify labels for plotting
labels = np.array([l.replace('_', ' ').capitalize() for l in column_names])
I = np.argsort(relative_score)
labels, relative_score = labels[I], relative_score[I]

fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(np.arange(len(relative_score)), relative_score, tick_label=labels)
ax.set_xlabel('Relative Borda score (%)')
ax.set_title("Overall Importance Score");
fig.tight_layout()
```

In {ref}`sec:2021_priorities` we will take a closer look at how things are
prioritized.

(sec:2021_priorities)=

## Top Priorities

The following figure shows the breakdown of the top priority items.

```{code-cell} ipython3
---
tags: [hide-input]
---
# Prettify labels for plotting
labels = np.array([l.replace('_', ' ').capitalize() for l in column_names])
# Collate top-priority data
cnts = np.sum(raw == 1, axis=0)
I = np.argsort(cnts)
labels, cnts = labels[I], cnts[I]

fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(np.arange(cnts.shape[0]), 100 * cnts / cnts.sum(), tick_label=labels)
ax.set_title('Distribution of Top Priority')
ax.set_xlabel('Percent of Responses')
fig.tight_layout()
```

### Details

We asked respondents who shared their priorities to provide specifics on their
top two priorities.
For example, if a user ranked "Performance" as a top priority, they were asked
to share any specific thoughts on how performance could be improved.
The responses for each of the categories are provided below.

```{code-cell} ipython3
---
tags: [hide-input]
---
categories = {
    "docs", "newfeatures", "other", "packaging", "performance", "reliability",
    "website",
}

# Load the text responses for each category
response_dict = {}
for category in categories:
    responses = np.loadtxt(
        f"data/2021/{category}_comments_master.tsv", delimiter='\t', skiprows=1,
        usecols=0, dtype='U', comments=None
    )
    responses = responses[responses != '']
    response_dict[category] = responses

# Generate nicely-formatted lists
for category, responses in response_dict.items():
    gen_mdlist(responses, f"{category}_comments_list.md")

# Register number of responses in each category
for k, v in response_dict.items():
    glue(f"2021_num_{k}_comments", v.shape[0], display=False)
```

% TODO: This would be much more convenient if the MD tables could be included
% programmatically. For example, if myst-nb adds support for the 
% IPython.display Markdown() function

#### Documentation

{glue:text}`2021_num_docs_comments` participants shared their thoughts on how
documentation could be improved.

````{admonition} Click to expand!
:class: toggle
```{include} _generated/docs_comments_list.md
```
````

#### New Features

{glue:text}`2021_num_newfeatures_comments` participants shared their thoughts on
new features to improve NumPy.

````{admonition} Click to expand!
:class: toggle
```{include} _generated/newfeatures_comments_list.md
```
````

#### Other

{glue:text}`2021_num_other_comments` participants selected "Other" as a top
priority:

````{admonition} Click to expand!
:class: toggle
```{include} _generated/other_comments_list.md
```
````

#### Packaging

{glue:text}`2021_num_packaging_comments` participants shared their thoughts on how
the packaging utilities in NumPy could be improved.

````{admonition} Click to expand!
:class: toggle
```{include} _generated/packaging_comments_list.md
```
````

#### Performance

{glue:text}`2021_num_performance_comments` participants shared thoughts on why
performance is a top priority and ideas on how it can be improved.

````{admonition} Click to expand!
:class: toggle
```{include} _generated/performance_comments_list.md
```
````

#### Reliability

{glue:text}`2021_num_reliability_comments` participants shared their thoughts on
reliability and how it can be improved.

````{admonition} Click to expand!
:class: toggle
```{include} _generated/reliability_comments_list.md
```
````

#### Website

Finally, {glue:text}`2021_num_website_comments` participants selected the
NumPy website as a top priority and shared their thoughts on how it could
be improved.

````{admonition} Click to expand!
:class: toggle
```{include} _generated/website_comments_list.md
```
````

## Summary

The following figure shows the relative frequency of selection for each of
the listed categories[^other2021] at each priority level.

```{code-cell} ipython3
---
tags: [hide-input]
---
fig, axes = plt.subplots(3, 2, figsize=(12, 8))

for i, ax in enumerate(axes.ravel()):
    priority_level = i + 1
    cnts = np.sum(raw == priority_level, axis=0)[I]
    ax.barh(np.arange(cnts.shape[0]), 100 * cnts / cnts.sum(), tick_label=labels)
    ax.set_title(f"Priority: {priority_level}")
fig.tight_layout()
```

[^other2021]: Excluding `Other`, which was an optional category and therefore
          constitutes the majority of the "lowest-priority".
