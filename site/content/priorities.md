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
for category in column_names[:-1]:
    print(f" - {category.replace('_', ' ').capitalize()}")
```
