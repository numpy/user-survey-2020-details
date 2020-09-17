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

Of the {glue:text}`num_respondents` survey participants,
{glue:text}`num_prioritizers` shared their priorities for NumPy moving forward.

```{code-cell} ipython3
---
tags: [hide-input]
---
# GitHub-style horizontal bargraph showing the % composition of each topic
# for each priority level
colors = ['r', 'g', 'b', 'y', 'm', 'c', 'k']

# Unstructured, numerical data
raw = data.view(np.dtype('U1')).reshape(-1, len(column_names)).astype(int)
for priority_num in np.arange(len(column_names)) + 1:
    # Right and left bounds for horizontal rectangle
    right = np.sum(raw == priority_num, axis=0)
    left = np.concatenate(([0], np.cumsum(right)[:-1]))
    for l, r, c, lbl in zip(left, right, colors, column_names):
        plt.barh(priority_num, r, left=l, color=c, label=lbl)
```
