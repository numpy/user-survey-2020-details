# NumPy Survey Results

Analysis and publication of the results of the 2020
[NumPy Community Survey][survey_repo].

[survey_repo]: https://github.com/numpy/numpy-surveys

## Running the analysis

Several steps are required to analyze and publish the survey results:

 1. Acquiring the survey data
 2. Configuring the environment
 3. Running the analysis & generating the website.

Each of these steps is covered below.

### Survey data

**Coming soon...**

### Environment setup

The necessary packages for analyzing and publishing the results are listed in
`requirements.txt` and `site/requirements.txt`, respectively.
The following procedure can be used to set up an environment for data
analysis:

```bash
python -m venv survey_analysis
source survey_analysis/bin/activate
python -m pip install .[publish]
```

### Running the analysis

[Sphinx](https://www.sphinx-doc.org/en/master/) is used to automatically run
the analysis via the [myst-nb](https://myst-nb.readthedocs.io/en/latest/)
plugin and generate a static website presenting the results:

```bash
cd site
make html
```

The generated site can then be viewed by opening `site/_build/html/index.html`
in your preferred browser.
