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

# Features, Problems, and Deprecations

```{code-cell} ipython3
---
tags: [hide-input]
---
fname = "data/numpy_survey_results.tsv"
column_names = [
    'using_random', 'bug', 'bug_resolution', 'bug_resolution_other',
    'unsolvable', 'unsolvable_resolution', 'unsolvable_resolution_other',
    'deprecation', 'deprecation_other'
]
featdep_dtype = np.dtype({
    "names": column_names,
    "formats": ['U1024'] * len(column_names),
})

data = np.loadtxt(
    fname, delimiter='\t', skiprows=3, dtype=featdep_dtype,
    usecols=range(87, 96), comments=None
)
```

This section comprises various questions to try to gain insight on things
like new feature adoption, issue resolution, and the length of deprecation
cycles.

## New `numpy.random` Adoption

A [new API for random number generation][nprandom] was added to `numpy.random`
in version 1.17.
We asked survey paricipants whether they were using the new random API.
Of the {glue:text}`num_respondents` survey participants, 
{glue:text}`num_random_users` shared whether they were using the new `random`
API.

[nprandom]: https://numpy.org/doc/stable/reference/random/index.html

```{code-cell} ipython3
---
tags: [hide-input]
---
rand = data['using_random'][data['using_random'] != '']
labels, cnts = np.unique(rand, return_counts=True)

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(cnts, labels=labels, autopct='%1.1f%%')
fig.tight_layout()

glue(
    'num_random_users',
    f'{rand.shape[0]} ({100 * rand.shape[0] / data.shape[0]:1.0f}%)',
    display=False
)
```
