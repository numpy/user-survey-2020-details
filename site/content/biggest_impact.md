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

# The Big Picture

```{code-cell} ipython3
---
tags: [hide-input]
---
fname = "data/numpy_survey_results.tsv"

# Load
data = np.loadtxt(
    fname, delimiter='\t', skiprows=3, dtype='U', usecols=range(96, 98),
    comments=None
)
# Parse
biggest_impact = data[:, 0][data[:, 0] != '']
other_changes = data[:, 1][data[:, 1] != '']
# Re-order
rng = np.random.default_rng(0xDEADC0DE)
rng.shuffle(biggest_impact)
rng.shuffle(other_changes)
# Reporting values
glue(
    'num_biggest_impact',
    f'{biggest_impact.shape[0]} ({100 * biggest_impact.shape[0] / data.shape[0]:1.0f}%)',
    display=False
)
glue(
    'num_other',
    f'{other_changes.shape[0]} ({100 * other_changes.shape[0] / data.shape[0]:1.0f}%)',
    display=False
)
```

To conclude the survey, we asked participants to share their thoughts on what
changes to NumPy would have the most significant impact for them as users.

## Biggest Impact

We asked survey participants the following question:

  > What single immediate change to NumPy would bring the most value to
  > you as a NumPy user?

The responses of the {glue:text}`num_biggest_impact` survey participants who
answered this question are listed below.

% TODO: Switch to fully-translated dataset

```{code-cell} ipython3
---
tags: [hide-input]
---
# Generate a nicely-formatted md list
with open('_generated/biggest_impacts_list.md', 'w') as outf:
    for response in biggest_impact:
        outf.write(f" - {response}\n")
```

````{admonition} Expand to see responses!
:class: toggle
```{include} _generated/biggest_impacts_list.md
```
````
