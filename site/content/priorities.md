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

# Project Priorities

```{code-cell} ipython3
---
tags: [hide-input]
---
fname = "data/numpy_survey_results.tsv"
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
    usecols=range(72, 79), comments=None
)

# Discard empty data
num_respondents = data.shape[0]
unstructured = data.view(np.dtype('(7,)U1'))
data = data[~np.any(unstructured == '', axis=1)]

glue(
    'num_prioritizers',
    f'{data.shape[0]} ({100 * data.shape[0] / num_respondents:1.0f}%)',
    display=False
)
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

Of the {glue:text}`num_respondents` survey participants,
{glue:text}`num_prioritizers` shared their priorities for NumPy moving forward.

To get a sense of the overall relative "importance" of each of the categories,
the following figure summarizes the score for each category as determined by
the [Borda counting procedure for ranked-choice voting][borda-wiki].

[borda-wiki]: https://en.wikipedia.org/wiki/Borda_count

% TODO: Expand on this if we keep it: Borda counting scheme for ranked-choice voting

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
fig.tight_layout()
```

In {ref}`sec:priorities` we will take a closer look at how things are
prioritized.

(sec:priorities)=

## Priorities

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

Figure {ref}`fig:all_priorities` shows the same distribution for each 
priority level.

```{code-cell} ipython3
---
tags: [hide-input,remove-output]
---
fig, axes = plt.subplots(3, 2, figsize=(12, 8))

for i, ax in enumerate(axes.ravel()):
    priority_level = i + 1
    cnts = np.sum(raw == priority_level, axis=0)[I]
    ax.barh(np.arange(cnts.shape[0]), 100 * cnts / cnts.sum(), tick_label=labels)
    ax.set_title(f"Priority: {priority_level}")
fig.tight_layout()
# Save for linking
plt.savefig('_generated/priority_distributions.png')
```

(fig:all_priorities)=

````{admonition} Click to show/hide
:class: toggle
```{figure} _generated/priority_distributions.png
```
````
