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
    "formats": ['U1'] * len(column_names),
})

data = np.loadtxt(
    fname, delimiter='\t', skiprows=3, dtype=featdep_dtype,
    usecols=range(87, 96), comments=None
)
```

This section comprises various questions to try to gain insight on things
like new feature adoption, issue resolution, and the length of deprecation
cycles.
