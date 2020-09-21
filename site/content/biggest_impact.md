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
from numpy_survey_results.utils import gluval
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
loading_params = dict(
    delimiter="\t", skiprows=1, dtype='U', usecols=0, comments=None
)

biggest_impact = np.loadtxt(
    "data/biggestimpact_comments_master.tsv", **loading_params
)
other_changes = np.loadtxt(
    "data/significantchanges_comments_master.tsv", **loading_params
)

# Filter
biggest_impact = biggest_impact[biggest_impact != '']
other_changes = other_changes[other_changes != '']
# Re-order
rng = np.random.default_rng(0xDEADC0DE)
rng.shuffle(biggest_impact)
rng.shuffle(other_changes)
# Reporting values
glue(
    'num_biggest_impact',
    biggest_impact.shape[0],
    display=False
)
glue(
    'num_other',
    other_changes.shape[0],
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

## Other Significant Changes

Finally, we asked participants to share any other changes that would 
significantly improve NumPy.
The responses of the {glue:text}`num_other` participants who answered this
question are listed below.

% TODO: Switch to fully-translated dataset

```{code-cell} ipython3
---
tags: [hide-input]
---
# Generate a nicely-formatted md list
with open('_generated/other_changes_list.md', 'w') as outf:
    for response in other_changes:
        outf.write(f" - {response}\n")
```

````{admonition} Expand to see responses!
:class: toggle
```{include} _generated/other_changes_list.md
```
````
