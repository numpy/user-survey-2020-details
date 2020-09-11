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
%matplotlib inline
import numpy as np
```

# Demographics

A summary of the demographic information of the NumPy survey respondents.

```{code-cell} ipython3
---
tags: [hide-input]
---

fname = "data/numpy_survey_results.tsv"
column_names = [
    'age', 'gender', 'lang', 'lang_other', 'country', 'degree', 'degree_other',
    'field_of_study', 'field_other', 'role', 'role_other', 'version', 
    'primary_use', 'programming_exp', 'numpy_exp', 'use_freq', 'components',
    'use_c_ext', 'prog_lang', 'prog_lang_other',
]
demographics_dtype = np.dtype({
    "names": column_names,
    "formats": ['<U512'] * len(column_names),
})

data = np.loadtxt(
    fname, delimiter='\t', skiprows=3, dtype=demographics_dtype, 
    usecols=range(11, 31), comments=None
)
```


## Age


