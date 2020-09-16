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

# Mentorship

```{code-cell} ipython3
---
tags: [hide-input]
---
fname = "data/numpy_survey_results.tsv"
column_names = [
    'participated', 'role', 'mentor_paid', 'mentor_motivation',
    'mentor_motivation_other', 'mentor_connect', 'mentor_connect_other',
    'mentor_activities', 'mentor_activities_other', 'mentee_charged',
    'mentee_connect', 'mentee_connect_other', 'mentee_activities',
    'mentee_activities_other', 'satisfaction', 'interested'
]
mentorship_dtype = np.dtype({
    "names": column_names,
    "formats": ['<U1024'] * len(column_names),
})

data = np.loadtxt(
    fname, delimiter='\t', skiprows=3, dtype=mentorship_dtype, 
    usecols=range(56, 74), comments=None
)
```
