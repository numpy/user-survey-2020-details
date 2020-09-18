from setuptools import find_packages, setup
import os

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        contents = f.read()
    return contents

setup(
    name="numpy-survey-results",
    version=0.1,
    description=(
        "Analysis and Publication of results from the NumPy Community Survey"
    ),
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Ross Barnowski",
    author_email="rossbar@berkeley.edu",
    license="BSD-3",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        req for req in read("requirements.txt").split('\n')
        if not req.startswith("#")
    ],
    extras_require={
        "publish": [
            req for req in read("site/requirements.txt").split('\n')
            if not req.startswith("#")
        ],
    },
)
