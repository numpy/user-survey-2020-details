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

# Development and Community Contributions

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
    'interest', 'limitations'
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
# Compute some basic parameters on OSS/np-specific contributions
assert npdata.shape[0] == ossdata.shape[0]  # Sanity check on data
num_respondents = npdata.shape[0]
num_oss_contributors = np.sum(ossdata['contributed'] == 'Yes')
num_np_contributors = np.sum(npdata['contributed'] == 'Yes')
# Links for report
glue('num_respondents', npdata.shape[0], display=False);
glue(
    'oss_contributors',
    f'{num_oss_contributors} ({100 * num_oss_contributors / num_respondents:1.0f}%)',
    display=False
)
glue(
    'np_contributors',
    f'{num_np_contributors} ({100 * num_np_contributors / num_respondents:1.0f}%)',
    display=False
)

```
% TODO: Intro sentences here about open-source development and community-led
% nature of NumPy.

Of the {glue:text}`num_respondents` survey participants, 
{glue:text}`oss_contributors` have contributed to at least one open source
software project, while {glue:text}`np_contributors` have contributed to
NumPy specifically.

