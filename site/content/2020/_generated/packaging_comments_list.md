|Comments|
|--------|
|work on a packaged distribution like anaconda, but independent.|
|I think it's more of a general python packaging thing. Everything feels so fractured between conda and pip and apt-get (for example) that so many people I know run everything in a container and I feel like that's just kicking the can down the road, wrt dependencies. |
|1. conda is horrible for windows. Need something better for packaging. 2. More explicitly detailed error messages when install fails.|
|provide individual feature specific installation instead all at one. Provide wrapper for all programming languages with standardized output such as JSON, xml, BJSON or other format. |
|It has gotten much better than it was in the past, occasionally still see compile-time issues.|
|I would love to have a distribution for numpy as independent of the OS as possible. So numpy can be executed anywhere.|
|wheels for more platforms, like aarch |
|Propose new packages with which simulations and models can be carried out in different areas of science, seek collaborations with people who can contribute to each of the packages. (Original in Spanish: Proponer nuevos paquetes con los cuáles se pueda realizar simulaciones y modelos en distintas áreas de ciencia, buscando colaboraciones con distintas personas que puedan contribuir a cada uno de los paquetes.)|
|Ability to distribute only selected submodules of numpy (with pyinstaller)|
|Better integration with setuptools|
|Supply conda packages for new Numpy releases.|
|plotly|
|Ensure it is easy to install on all major OSes with pip and conda.|
|arm64 wheels|
|It's pretty good right now. I put it up high on my priority list to indicate that none of the lower priority items should be allowed to endanger simplicity of installation. NumPy is too fundamental for computational science.|
|Building from source could be made easier. The documentation is a bit scarce on that, making it difficult to find all the nobs that can and/or should be set. Also some sort of dependency on what Cython version should be used for which Numpy version would be helpful.|
|Splitting numpy up into smaller packages, making applications using numpy smaller if they don't require everything  Help make something like conda-forge for regular Pypi packages be a thing. This will help smaller projects leverage the same best practices when it comes to creating packages with compiled code|
|Some portions of NumPy's build system could be broken out to small, reusable packages (like the multithreading builder). I'd like to see a few more ManyLinux2014 special arch's supported (like PowerPC), though the one I'm most interested in, AARCH64, is now included which is great.|
|pandas|
|fftpack scipy.signal|
|Easy to install high performance on any platform|
|I'm not quite up to date with the new developments but remember it being a quite haphazard in the past (~2018/2019) with how it picks up dependencies via environment variables. The documentation was thin and it would be good to offer some advice regarding the fact that the pip/conda versions are only targeted to the base x86_64 instructions and should be avoided if performance is important. Intel-numpy is a workaround but it's not mentioned in the numpy docs and a more general statement in the numpy docs would be more helpful imo (for any x86/arm/etc vendor)|
|Distribution in terms of blas vs mkl, this issue is nontrivial for those unfamiliar|
|Packaging looks ok to me|
