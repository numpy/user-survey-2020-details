|Comments|
|--------|
|simple possibility to use different CPU cores for parallel different arrays calculating without complex sintax|
|Greater reach to users in general. (Original in Spanish: Mayor alcance a las usuarias en general.)|
|Automatic differentiation|
|Better error messages and error handling. Sometimes numpy has incorrect statements and includes text not intended for the error message.|
|User-defined scalar types (e.g. high precision floats)|
|consistency with xarray api, migration path to using numpy.random with Jax|
|More speed! I use numpy because it’s fast - I want more of that. Also articles and tips on how to use performance features (out kwarg comes to mind)|
|Better bug tracking (current number of open but duplicated bugs in GitHub is excessive)|
|Unite Numpy and Scipy in a single project / library. (Original in Spanish: Unir Numpy y Scipy en un único proyecto / librería.)|
|A clearly defined and smaller API that is 100% compatible with Dask, CuPy and other array libraries.|
|signal processing and filter design tools (lighter weight versions of the tools in scipy)|
|Not sure. I generally love Numpy! Maybe including the Minuit optimization package more formally into the numpy ecosystem.|
|a ruthless standardization on snake_case methods instead of "sometimes it's .foobar() and sometimes it's .foo_bar()"|
|documentation should be more interactive|
|Most of the documentation examples are extremely concise, and only illustrate one to a few uses of an API.|
|Easier/native reading of Fortran binary files|
|Full fledged typing (mypy) support, with dimensions, shape and dtype.|
|newcomers tutorials|
|Best practices|
|Better type annotations|
|Proper methods for 1:1 image display in matplotlib|
|Examples and documentation|
|small matrix optimizations|
|a homogeneous use of size and shape parameters :p|
|Versatile boundary conditions for time integration|
|Type hints|
|Parallelization|
|more How Tos|
|even better docs|
|COMMENTS|
|Improvements in performance|
|More examples of use with visualisation tools|
|I would love to see some kind of series of videos or webinars teaching numpy|
|Interoperability with other low level array libraries.|
|GPU|
|Documentation accessibility|
|Documentation improvement to add clearer examples (maybe with some visualizations)|
|A more intuitive dtype system.|
|less pickiness about what kind of sequence of things a function (array, list, tuple ...) can accept (this may be a general Python issue, though.)|
|Clearer documentation|
|Add homogeneous transformations|
|Stop unwrapping zero-dimensional arrays into scalars.|
|GPU support|
|Easier docs for multidimensional operations (from stack/roll to whatever)|
|Matrix operations|
|Parallelism in summations. (Original in Spanish: Paralelismo en sumatorias.)|
|Multi-threading by default|
|Maybe easier way to move data between library especially deep learning.|
|Integration with units libraries|
|Plotting data easily|
|Better string array support and performance|
|More examples of its use (particularly for my specific domain).|
|Documentation|
|Clearer opportunities to give back to the community|
|np.nan for int arrays|
|Column vectors as default as opposed to 1d vectors.|
|Multithreaded einsum|
|closer coordination with pandas|
|Improvements in Documentation|
|CUDA backend like jax|
|As optimization libraries|
|More tutorials and use cases for linear algebra|
|Better array reps in jupyter ?|
|Greater integration with Python. (Original in Spanish: Mayor integración con Python.)|
|became a framework|
|Nullable integers|
|numpy.dot should work on arrays of shape (...,n) x (n,...).|
|Speed|
|Increased adoption by other frameworks of __array_function__ protocol|
|Smaller steering committee|
|Type annotations. (But that's coming, from what I hear!)|
|More docs|
|randomized linear algebra|
|Documentation and Examples|
|An API/set of hooks to allow functions like `concatenate` to create duck arrays/subclasses.|
|Faster FFTs.|
|Comprehensive documentation|
|I run into floating point rounding errors often, sometimes that cause large bugs. This seems to stem from np.loadtxt.|
|F2py handle Fortran 2008 and be thread safe|
|NEP 21|
|Integrate quaternions as a basic type. (Original in Spanish: Integrar los cuaterniones como un tipo básico.)|
|beginner-friendly numpy is too comp.|
|Easy but efficient parallelism (like Mathematica's ParallelMap).|
|Stochastic linear algebra; specifically the ability to find the determinant of a LinearOperator. This might fit better in SciPy than NumPy|
|why zeros() uses shape, while randint() uses size? I always forget which is which|
|Tools for simulations (Monte Carlo method, generation of random numbers). (Original in Spanish: Herramientas para simulaciones (método Monte Carlo, generación de números aleatorios). )|
|Creation of a reliable binary format storage option.|
|Faster masked arrays|
|As a user, probably improved clarity/consistency of the documentation|
|Increase the types of special functions. (Original in Japanese: 特殊関数の種類を増やします.)|
|Static typing|
|Better native GPU integration|
|faster small arrays|
|changing numpy's name to np!!!|
|Better documentation of packages.|
|cleaner separation with scipy of FT - 2 equivalent modules with differences !|
|autodiff [but I am not sure I'd want it in numpy!]|
|copy vs original array specifications|
|GPU backend :)|
|Fixing masked array and making them "first-class citizens".|
|Something Community-wise, I'm sure.|
|new nditer C API support in Cython|
|Support for hardware accelerators|
|Performance comparable to rust ndarray (in my experience when used correctly Rust ndarray is ~2x faster)|
|Add an HOWTO example to documentation on how to extend Numpy with a gufunc written in Cython|
|this is a big ask, but it would be nice if numpy could run on gpus|
|processing speed. (Original in Japanese: 処理速度.)|
|A document describing best practices for using NumPy for scientific computing, targeted to a researcher using the package with limited computer science knowledge.|
|Efficiency|
|integer calculations like prime factorization|
|how ndarray is displayed as a 2D list not matrix|
|Adding the option to use more functions as methods. For many operations (sum, max, argmax, real/imag...) we have the option to access them as functions or methods. Many others (abs, angle, diff, sin, cos...) can only be used as functions. Sometimes it would be cleaner to write code with these as methods.|
|Some statistical or linear algebra functions are both in scipy and numpy, this is confusing for me.|
|Defining a numpy array with a string index|
|optional parallel computing|
|even better integration with other toolkits|
|It's hard to say. Numpy is probably my favorite library ever. If I was forced, maybe a course developed for both new and intermediate users.|
|more robust documentation|
|Improved performance. (Original in Japanese: パフォーマンスの向上.)|
|GPU usage|
|more examples in the wild. This is largely out of numpy's control though.|
|ability to run on GPU.|
|More tutorials|
|Make numpy.unique() handle objects arrays containing None again - this was working in Py2.|
|anything to help bring people update with confidence - the BDFL for my project still uses py27, and it's been pulling teeth to get him to 1.14. Even though I use 1.16 and 1.18 depending on the project, he is nervous because he remembers 'that one time numpy changed how views are handled'|
|Providing the features that would stop PyTorch, TensorFlow, JAX, etc. from reimplementing NumPy and fragmenting the ecosystem. I think this is only CPU/GPU transparency (i.e. absorb CuPy). We don't want to go back to the days of Numeric vs NumArray!|
|Tutorials and more examples in documentation|
|Improved seo that puts the latest docs at the top of searches. I frequently will end up with links to 1.15 docs|
|portability|
|Custom dtypes|
|linear interpolation along an axis|
|Be able to transform a 1D horizontal array to a 2D vertical array with the '.T' transform.|
|Better documentation. Examples. And explanation of underlying logic. It's already good. But always could be better|
|Speed ​​and ease of use. (Original in Spanish: Velocidad y facilidad de uso.)|
|More readable documentation would be welcome but otherwise NumPy is awesome!|
|np.unique should accept a tolerance keyword that treats floats as the same if they differ by less than the tolerance.|
|best practice and performance comparison of optimal/sub-optimal usages, and tutorial/documentation in this direction|
|Documentation (tutorials)|
|This might not be possible but having a fast way to iterate through arrays in a python for loop would make some operations easier.|
|I can proudly say all the improvements I want to see (in things like docs) would be large, no low hanging fruit.|
|Manipulation of ndarrays (indexing into, reshaping, etc.) could stand to be a little more transparent.|
|more error messages for debugging|
|I usually switch away from Numpy when my arrays contain strings. Perhaps there is a better way?|
|Mentorship (stronger involvement in NumPy). Some less used features are completely unknown to me and it is hard to find tutorials/materials on them besides the documentation.|
|Multithreaded functions|
|Better documentation|
|It would be really nice to have an api from numpy that evaluated the performance costs/benifits between different function calls with some input data, (like np.mat vs np.array, or np.dot vs np.einsum). It would make it easier to compare and see what I should be using in a specific case|
|More functionalities for images 2d and 3d|
|Names dimensions|
|Low level explainations|
|more documentation for advanced users for maximum performance|
|I would like an explicit pointer syntax|
|Static type hints|
|Performance|
|Ragged arrays/dtypes|
|Working with JAX to add the numpy protocols. Then I can really use either library however I want!|
|N-D linear interp|
|Adding a "a.b" notation for dot products|
|low-level parallel computing|
|FASTER|
|Clear and concise concatenation of 1D arrays to form a shape (N, 2) array. Currently using `np.vstack((...)).T'.|
|Some finances module, but other than that is awesome as it is now|
|Better tutorials and or easier way to create ufuncs|
|rational number support with arbitrary capacity (int8, int16, etc). Need this for chemical stoichiometry calculations, specifically for calculating nullspace of stoichiometry matrix.|
|Make the API reference less ad-hoc. See the Java docs for the ideal model.|
|Faster multi-threaded operations (but this is out of scope and I'm happy using other libraries)|
|[honestly it's perfect]|
|labelled arrays|
|CUDA integration...|
|A place for writing and submitting tutorials on how to implement things in numpy, and ways to link numpy functions to these tutorials.|
|Support to visualize data (matplotlib often too complicated)|
|GPU usage|
|optimization|
|Parallelization features|
|Better documentation of linear algebra wrappers|
|JIT|
|separate the C code from the python code: less extensive use of the CPython C-API|
|More visualization tools|
|Support for type annotations|
|NEP-35 and NEP-37 widespread adoption|
|.index() ... I've been seriously considering dropping numpy entirely in favour of pytorch over this, and frankly given how long it's been I think it might be prudent to do so even if numpy added .index() today.|
|More and better examples of using Numpy with more realistic data. (Original in Spanish: Más y mejores ejemplos de uso de Numpy con datos más realistas.)|
|Alternatives to very large arrays (memory error). (Original in Spanish: Alternativas a arrays muuuy grandes (memory error).)|
|Contract Simplification (mainly the sugar side of things)|
|Weighted quantiles. I'm working on it|
|Packaging of mkl libraries other than conda (wheel). (Original in Japanese: conda以外のmklライブラリのパッケージ化(wheel).)|
|CUDA|
|GPU support|
|Better modern Fortran support in f2py|
|A more user friendly vector class for linear algebra|
|Synchronization between numpy.linalg and scipy.linalg.|
|Consistent null value handling bumpy array|
|Easier to understand documentation|
|Better performance (paralelization)|
|(py)FFTW backend|
|Updated documentation for f2py|
|A more consistent API, perhaps? (Original in Portuguese: Uma API mais consistente, talvez?)|
|Add a way to keep track of units and to display answers with units|
|documentation|
|Documentation|
|Usability. Make it simpler to use|
|More speed ;)|
|Performance boosts using inherent parallelism.|
|Have a better documentation and tutorials.|
|Better examples on doc pages. Almost always I have to check stackoverflow to understand the function better.|
|Better control of array memory.|
|Language-independent API|
|Performant vectorisation|
|A clarification in the function documentation to quickly know if it works in view or in copy. (Original in French: Une clarification dans la documentation des fonctions pour savoir rapidement si elle travaille en vue ou en copie.)|
|Easy Documentation.. New learning is difficult with the current documentation model|
|An easier way to handle arrays larger than memory|
|better documentation, with more examples and use cases.|
|Give more examples along with the documentation, give use cases, redesign docs page|
|More integration with numba jit & cuda|
|Better tutorial/documentation on how to efficiently use numpy features (ufunc etc.)|
|More extensive and tutorial like documentation like stack overflow is with a continuous example|
|support NA/missing values|
|Increased random support. (Original in Spanish: Mayor soporte de random.)|
|Why do you speak in feminine? (Original in Spanish: Por que habláis en femenino?)|
|Codifying a “minimal NumPy”|
|Would love a feature to extract both the min and max of an array (with an optional axis parameter) in one stride|
|GPU|
|Multithreaded 2 and 3 dimensional FFTs|
|Adding the feature I requested|
|Making faster. Python is inefficient and Numpy does not help by default.|
|Better alternative for SWIG to wrap a proprietary I/O library written in C++|
|I think your masked array implementation is kind of clunky. The relationship between the mask and the underlying data array can get confusing. In particular, the behavior of the fill value is confusing. Setting something to the fill value in the data array doesn't change the mask. Changing the mask doesn't seem to update the data array. It's been a while since I've had to deal with this issue, but it can get confusing.|
|Allowing users to perform operations with one dimension removed. Eg adding a matrix of (3,4) to a vector of shape (3,)|
|I would like documentation in Spanish in the most complex areas. (Original in Spanish: Me gustaria documentacion en español en las areas mas complejas.)|
|Clearer separation between numpy and scipy in overlapping domains (linalg comes to mind)|
|In-built visualization support for NumPy arrays. Would make it easier to visualise high dimensional arrays.|
|allowing to slice an array with another array|
|numpy &lt;---&gt; netCDF examples. I know how to do it, but "exchange" between formats would be better documented|
|more hand-on with simple level 100 to 500|
|Way to access specific parts of the library since putting numpy in production is heavy. (Original in Spanish: Manera de acceder a partes específicas de la librería ya que poner numpy en produccion es pesado.)|
|Improve performance|
|ONNX support|
|Became more Developer friendly|
|GPU acceleration|
