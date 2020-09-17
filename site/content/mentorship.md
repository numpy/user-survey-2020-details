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

We asked survey participants about their experiences with
**mentorship programs** related to OSS scientific software.
Of the {glue:text}`num_respondents` survey respondents,
{glue:text}`num_mentorship_participants` reported participating in some form
of mentorship program dealing with scientific software:
{glue:text}`num_mentors` as mentors, {glue:text}`num_mentees` as mentees, and
{glue:text}`num_both` in both capacities[^both].

[^both]: No distinction is made for those who have participated in multiple
         different mentorship programs.

```{code-cell} ipython3
---
tags: [hide-input]
---
participant_mask = data['participated'] == 'Yes'
glue('num_mentorship_participants', participant_mask.sum(), display=False)
mentor_mask, mentee_mask, both_mask = (
    data['role'] == key for key in ('Mentor', 'Mentee', 'Both')
)
num_mentors = mentor_mask.sum()
num_mentees = mentee_mask.sum()
num_both = both_mask.sum()
glue('num_mentors', num_mentors, display=False)
glue('num_mentees', num_mentees, display=False)
glue('num_both', num_both, display=False)
```

## Paid vs. Unpaid Programs

{glue:text}`mentors_paid` of respondents who served as mentors reported being
paid by the program, and {glue:text}`mentees_charged` mentees reported being
charged fees.

```{code-cell} ipython3
---
tags: [hide-input]
---
num_paid_mentors = np.sum(data['mentor_paid'] == 'Yes')
num_charged_mentees = np.sum(data['mentee_charged'] == 'Yes')
glue(
    'mentors_paid',
    f'{num_paid_mentors} ({100 * num_paid_mentors / (num_mentors + num_both):1.0f}%)',
    display=False,
)
glue(
    'mentees_charged',
    f'{num_charged_mentees} ({100 * num_charged_mentees / (num_mentees + num_both):1.0f}%)',
    display=False,
)
```

## Mentor Motivations

We asked mentors to share their motivations for serving as OSS mentors.

```{code-cell} ipython3
---
tags: [hide-input]
---
all_mentors_mask = mentor_mask | both_mask
# TODO: move flatten to analysis module so it can be imported
def flatten(data, delimiter=','):
    out = []
    for row in data:
        out.extend(row.split(delimiter))
    return out
motivations = data['mentor_motivation'][all_mentors_mask]
motivations = motivations[motivations != '']
num_resp = motivations.shape[0]
motivations = flatten(motivations)
labels, cnts = np.unique(motivations, return_counts=True)
I = np.argsort(cnts)
labels, cnts = labels[I], cnts[I]
cnts = 100 * cnts / num_resp

fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(np.arange(len(labels)), cnts)
ax.set_yticks(np.arange(len(labels)))
ax.set_yticklabels(labels)
ax.set_xlabel('Percentage of Mentors')
fig.tight_layout()
```

## Mentor Connections

We asked both mentors and mentees how they were matched with their
counterparts.

```{code-cell} ipython3
---
tags: [hide-input]
---
fig, ax = plt.subplots(figsize=(12, 8))
for start_ind, (key, label) in enumerate(zip(
    ('mentor_connect', 'mentee_connect'),
    ('Mentors', 'Mentees')
)):
    cnxn_data = data[key][data[key] != '']
    num_resp = cnxn_data.shape[0]
    labels, cnts = np.unique(flatten(cnxn_data), return_counts=True)
    # Plot
    ax.barh(
        np.arange(start_ind, 2 * len(labels), 2),
        100 * cnts / num_resp,
        align='edge',
        label=label,
    )
ax.set_yticks(np.arange(start_ind, 2 * len(labels), 2))
ax.set_yticklabels(labels)
ax.set_xlabel('Percentage of Participants')
ax.legend()
fig.tight_layout()
```

## Mentorship Activities

We asked participants what sorts of activities they engaged in as part of the
mentorship program.

```{code-cell} ipython3
---
tags: [hide-input]
---
# NOTE: not every activity was reported by both mentors/mentees
labels = np.unique(flatten(data['mentor_activities']))[3:]
fig, ax = plt.subplots(figsize=(12, 8))
for start_ind, (key, label) in enumerate(zip(
    ('mentor_activities', 'mentee_activities'),
    ('Mentors', 'Mentees')
)):
    activities_data = data[key][data[key] != '']
    num_resp = activities_data.shape[0]
    activities_data = np.array(flatten(activities_data))
    cnts = np.array([np.sum(activities_data == act) for act in labels])
    # Plot
    ax.barh(
        np.arange(start_ind, 2 * len(labels), 2),
        100 * cnts / num_resp,
        align='edge',
        label=label,
    )
# Manual modification to one category name
labels[labels == 'Attend a lecture'] = 'Attend an Event'
ax.set_yticks(np.arange(start_ind, 2 * len(labels), 2))
ax.set_yticklabels(labels)
ax.set_xlabel('Percentage of Participants')
ax.legend()
fig.tight_layout()
```

## Program Satisfaction

We asked mentees how satisfied they were with their experience in the 
mentorship program(s).

```{code-cell} ipython3
---
tags: [hide-input]
---
satisfaction = data['satisfaction'][data['satisfaction'] != '']
labels, cnts = np.unique(satisfaction, return_counts=True)

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(cnts, labels=labels, autopct='%1.1f%%')
fig.tight_layout()
```

## Interest in a NumPy Mentorship Program

Finally, we asked survey participants whether they would be interested in a
formal NumPy mentorship program.
Of the {glue:text}`num_responded_mentorship_interest` participants who 
responded to this inquiry, {glue:text}`interested_in_mentorship` said that
they would be interested.

```{code-cell}
---
tags: [hide-input]
---
num_resp = np.sum(data['interested'] != '')
num_yes = np.sum(data['interested'] == 'Yes')
glue('num_responded_mentorship_interest', num_resp, display=False)
glue(
    'interested_in_mentorship',
    f'{num_yes} ({100 * num_yes / num_resp:1.0f}%)',
    display=False
)
