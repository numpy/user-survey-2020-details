|Comments|
|--------|
|Not quite sure, but they're the life blood that really draws in new users AND re-engages the existing base.|
|I'd love to see support for automatic differentiation (via AutoDiff as in Jax for example) land in NumPy.|
|If programmers in stackoverflow can't find a way to solve his task with numpy and it appears often, this task must send to NumPy to make new functions and possibilities|
|Automatic differentiation|
|I do not know Numpy well, but I know that a great competitor of numpy is Matlab, because it has many functions for engineers in an easy way, that's why many remain in Matlab and do not migrate to python. Ease of rolling number models, differential equations, optimization and visualizing the results with just a few lines of code is what keeps some engineers from experiencing the potential of NumPy. (Original in Spanish: conosco Numpy profundamente, pero sé que un grande competidor de numpy es Matlab, porque tiene muchas funciones para ingenieros de forma facil, por eso muchos siguén en Matlab y no migran para python.. facilidades de rodar modelos números, de ecuaciones diferenciales, optimización  e visualizar los resultados con pocas lineas de código es lo que hace que algunos ingenieros no experimenten del potencial de numpy.)|
|easier operator overloading of numpy arrays, e.g. to change '+' to direct sum and '*' to tensor product|
|Not really sure actually, just certain there is more for you to add|
|Distributed computation Cuda support|
|GPU support Different upscaling/donwscaling for ndim arrays |
|Standard Error|
|Take over Biopython to make it better A lot of analysis pipelines for biological big data is restricted to R. Would be nice if it can be done in Numpy. |
|Support for physical units|
|Adequate frequency filtering|
|Wavelet support.|
|GPU support|
|Better support for handling large scale data, lazy loading, reading multiple files|
|More control over low level functioning and documentation of what the function does in an unobtrusive but encouraging way|
|Add suport for Homogeneous transformations. These are 4x4 matrices that contain information about position and orientation of objects. They are very popular in robotics and it would be very nice to have support for that in numpy. I need to build this matrices from Euler angles, or get the euler angles from them, and also y need to be able to do differentiaton an integration operations with 6D velocity vector.|
|Nothing specific. I think numpy is fantastic, but if I was to pick anything to make it better, it would be more stuff.|
|Lifting the array dimension limit would be nice.|
|NumPy on CUDA|
|* an interface to access copy or the original array easily. can't be sure from time to time. this needs to simplified.|
|I often use numpy to run simple physics models in a vectorised manner, i.e. operating on a numpy array to compute many solutions at once. I find it difficult to write code that can accept a single float as well as a numpy array, often getting type errors. I also have cases where the code may bifurcate in behaviour into two cases. In these cases I have to compute difference things and store them in different parts of the array, which is a quite manual process. Possibly I don't know all the features that are already there! |
|Develop/Promote utilities around `np.memmap` to work with large arrays on disk seamlessly.|
|Laplace transforms and modules for control. (Original in Spanish: Transformadas de Laplace y módulos para control.)|
|Optimisation|
|Support for type annotations|
|GPU support|
|Named arrays (like pytorch named tensors)|
|Supporting modern fortran (particularly derived type and coarray) in f2py; Specifying dtype using type annotation (PEP 484)|
|Nan value for int arrays (sorry I know that is not numpy's fault)... new dtypes|
|more utilities for machine learning, for example interfaces for pytorch and tensorflow.|
|- Better support for generators, and other streaming-like techniques for minimizing memory usage - Better support for user-space parallelism (something like multiprocessing.Pool.map and variants would be nice)|
|Expanded tensor algebra would be cool.|
|Algebraic topology algorithms would be very useful. Geometric objects as well|
|Native GPU support (like CuPy, but better coverage of Numpy-related operations), better serving for robotics project (like e.g export to ONNX feature)|
|More functions for Signal processing. New functions.|
|rational number support for exact linear algebra calculations|
|An easier way to define new ufuncs, and finalization of the __array_function__ interface.|
|I would like a better way of addressing specific axis in a multidimensional array. Right now I'm tampering with numpy.s_ and direct calls to __getitem__, but I'm not satisfied with that. It is also not usable in numba compiled code and this limits me.|
|Some way to deal with auto detecting upper and lower limits of data (e.g calculating a mean of an array containing a '10&lt;' value). An object with upper and lower error bounds included and functions to deal with them (e.g getting errors on log values, propagation of errors etc).|
|Named axes, named axis based broadcasting, performance diagnostic and inspection tools|
|Automatic differentiation|
|Function for findingen nearst indcies|
|Marking missing data without using NaN, i.e. a NA value.|
|Sparse matrices Ragged arrays|
|Type system improvements A high-level API name-space like numpy.api |
|Extend the functional programming subpackage.|
|Easy data plotting|
|more linalg functions.|
|NEP-37 or successor improvement|
|I'd like to see more linear algebra, either wrappers around existing C or Fortran or entirely new development|
|Better support for classes that inherit from NumPy|
|Being a core element in designing API for external projects extending arrays|
|One feature that came up on twitter is the ability to estimate trends in time series that have serially-correlated noise. There are nice C++ packages available (for example Hector http://segal.ubi.pt/hector/) , but such a function in numpy or scipy would be very useful.|
|I am very new to numpy so perhaps this question isn't appropriate.  Why can't there by strings in a numpy array?|
|The ability to index multi-dimensional arrays with a scalar index such as that returned by argmin and argmax without resorting to unravel_index function.  This would clean up a lot of code and allow direct indexing with argmax/argmin results.|
|Automatic differentiation outside of JAX, which might still be too tied to the Google ecosystem/way of doing things.|
|Pursuing development related to NEP18|
|Features I would use if available (have written own code to implement): - Constrained spline fits that preserve concavity. - Translating FORTRAN-formatted text files with floating point values with exponents that are written without the 'E' separator.|
|A function to keep only the unique numbers of an array and eliminate the repeated ones, but without preserving the order. (Original in Spanish: Una función para conservar solo los números únicos de un array y eliminar los repetidos, pero sin conservar el orden.)|
|Named arrays|
|Functions that work weights such as the average, extend these functions with percentiles, std, kurt, skew, etc. (Original in Spanish: Funciones que trabajen pesos como el average, extender estas funciones con percentiles, std, kurt, skew, etc.)|
|Integration with other numeric GPU librareis - e.g pytorch/mxnet|
|High-order spectrum analysis Bispectrum/Trispectrum. (Original in Japanese: 高次スペクトル解析 バイスペクトル/トライスペクトル.)|
|A function to perform calculations in multiple loops with the same memory and performance as C language. (Original in Japanese: 多重ループでの計算をC言語と同程度のメモリ、パフォーマンスで行う機能.)|
|GPU support with simple commands|
|Lightweight JIT python-markup lang similar to halide-lang but only genreate stack call, caching, localisation and loops. Still count on normal compiled C functions that serve sclalers, SIMD vectors, also it should support GPU, and threads.  The idea behind it is to reduce the memory and CPU caching journey, just one memory load & store|
|- Easier ways to create fast implementations of recurrence relations, which typically are implemented using loops.  - Custom stride implementations. I’m regularly dealing with data structures for spherical harmonics, which naturally would be indexed with two indices, where one is always positive and the other is positive or negative, smaller in magnitude than the first. Similar to how a “normal” array is mapped to a linear index using stride[0]*idx[0] + stride[1]*idx[1], my data can be mapped to linear index using idx[0]**2 + idx[1].  Currently I have to choose between easy implementations using “normal” arrays which give me ease of indexing and broadcasting at the cost of storing a lot of zeros, and custom implementations using algorithms working directly on the linear stricture or wrapping them in classes. None of these two custom solutions give me access to the really nice broadcasting in numpy.  I realize that this is a massive change to how numpy works, but I think it could simplify quite a lot of scientific calculations in data structures which are not “rectangular”.|
|Add static types to NumPy|
|Better sparse / large matrix management. Though I suppose this is part of scipy, it’s such important area that therehould be serious thoughts about how the overall sparse infrastructure can be improved / extended / made faster. |
|More variety of mathematical functions, can be implemented in numpy.|
|Features concerning better integration/interoperability within PyData ecosystem.|
|continued progress on various protocols proposed in recent NEPs for supporting compatibility with third party libraries implementing the NumPy API.|
|Incorporation of various routines/functions from Math 77 Library, e.q. DIVA|
