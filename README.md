# NumPy Community Survey Results

Analyses and publications of the results of the NumPy community surveys
[NumPy Community Survey][survey_repo].

[survey_repo]: https://github.com/numpy/numpy-surveys

## Running an analysis

The following steps are required to analyze and publish the survey results:

 1. Acquiring the survey data
 2. Configuring the environment
 3. Running the analysis & generating the website

Each of these steps is detailed below.

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

## Converting to Jupyter notebooks

For those who are more comfortable with Jupyter notebooks, the `myst-nb`
text-based notebook files can be converted to `.ipynb` files:

```bash
cd site
make notebooks
```

This converts all of the `.md` files in `content/` to `.ipynb` files of the
same name and moves them to `site/notebooks`.
The notebooks can then be opened for interactive use in the standard way, e.g.

```bash
cd site/notebooks
jupyter notebook
```

#### Note:

The text-based notebook format includes more features than are currently
supported by traditional Jupyter notebooks.
Therefore, some features (e.g. `glue` or other MyST roles & directives) will
not render when interacting with the `.ipynb` file.
