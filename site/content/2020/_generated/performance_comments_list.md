|Comments|
|--------|
|I dont know enough what goes under the hood in NumPy, but still at least for me it is the top priority |
|As NumPy is a library that is widely used both professionally and academically, it is certain to guarantee high performance and reliability. (Original in Portuguese: Como NumPy é uma biblioteca de vasto uso tanto em âmbito profissional como acadêmico, é certo garantir alta performance e confiabilidade.)|
|Since NumPy operations are at the core of so many programs, any performance improvement will have a significant impact on many applications. NumPy is by no means slow, but optimizing its performance would be nice.|
|Give `numpy.random.Generator.choice` an output parameter|
|- slow on small arrays - better integration with pypy - why not a jit / or integration of numba - more transparent access to GPU (even though it's quite good already)|
|GPU support|
|Parallel support with numba, vectorization of functions and speed improvements, possible implementation with something like arrow|
|many functionalities can be sped up using numba, it would be good if this gap could be closed|
|by improving user-base interaction by continuous updates of features by emphasizing on key learning objectives  by working on tutorials |
|Proper and dynamic support for vector extensions across the entire library, i.e. current versions of AVX etc. numpy should auto-detect the capabilities of CPUs and choose the fastest option for every operation.|
|Many projects are addressing performance issues around data manipulation. As a core component, maintaining performance is important.|
|More parallelization and GPU support|
|Mostly I think Numpy is very performant - the changes to the fft backends are greatly appreciated. I just think that maintaining this performance would be good - making use of multi-threaded operations would be good, but I know this is outside of scope for NumPy generally and I use other libraries with a NumPy-like API when I need this.|
|Some operations take too long time.|
|No particular place - I just think that as the existing np code is already quite well documented, etc. Performance is the most important aspect of a scientific/numerical library.|
|Open to this improving however possible.|
|Facilitate the use of multiple threads or processes for operations that require high computing power. (Original in Spanish: Facilitar el uso de múltiples hilos o procesos para las operaciones que requieran alto poder de computo.)|
|It should always be a priority. It is for me what makes numpy great. It is fast!|
|I want the ability to use the GPU.|
|As manually added, I think GPU-processing mit help. I‘m in the field of image algorithm development so mostly work on image data (image sequences as I‘m working on digital cinema technology) Performance isn‘t that bad btw. just the thing that can‘t be improved to much.|
|I actually select Others & Performance. As I'm using NumPy extensively for image processing, being able to directly address the GPU without requiring CuPy, for example, is extremely important if not critical.|
|I believe that the numba project is very promising, and I would really love to see better cooperation between numba and numpy.  |
|Make it easier to use numba, dask, cython|
|You guys are doing a great job, more connection to c++ And other high performance languages by promoting and explaining functionality in the documentation and media outlets, understanding and learning deeper abstractions by using numpy|
|NumPy to be competitive performance with compiler-based tools that encourage less elegant programming styles|
|parallel processing, utilizing specialized hardware (optionally)|
|I get complaints about numpy vs matlab perfomance, mostly from people who've never used numpy.  I know numpy is about as fast as Matlab, but haters gonna hate and taters gonna tate.|
|Improve computational efficiency, especially for large arrays. (Original in Japanese: 提高计算效率，尤其针对大数组.)|
|I code optimization solvers that have to do many small matrix-vector multiplications as part of the function, as in they can not be folded into some higher matrix operation, etc.  I realize that this is a rather niche use case but is there anyway to bring down the calling overhead? For example a Ax with being a 5x5 is effectively no different in cost to A being a 30x30 on my machine. I think a small matrix optimization would do wonders.  Also default linking to something other then MKL|
|Perhaps an integrated integration with numba, so when you call a function on an array you could specify a how=numba type parameter |
|Potentially include the use of GPUs.|
|Specify arrays of fixed size so that certain functions run faster. I work a lot with small matrices, mostly for linear algebra stuff, so it would be nice to have functions optimized for certain sizes of arrays. |
|Nothing in particular. I think as one of the go-to libraries for scientific computing Numpy should strive to maintain and improve the performance of its underlying functions, for current and future features.|
|Could NumPy run on GPUs?|
|Numpy is key for the Machine Learning.. Need Performance is the key factor|
|more use of parallel computing|
|Ability to automatically hand off certain operations to Intel MKL, Blitz, ... libraries when available on the system and faster.|
|I don’t have any ideas on how to improve it but it seems to me that it is always the most important thing and why it is used. I would love to collaborate on whatever development priority is taken. (Original in Spanish: No tengo ideas de como mejorar pero me parece que siempre es lo más importante y por lo que se lo usa. Me encantaría colaborar en cualquier prioridad que se tome de desarrollo.)|
|I know NumPy already has a lot of vectorization and paralelization, but maybe including automatic paralelization using GPUs or coprocessors. Probably similar to what JAX does but built in in some core components of NumPy.|
|By testing, indexing with numpy took much longer than the same function but with numba's njit decorator. Perhaps you could adopt certain improvements that are invisible to the user. (Original in Spanish: Haciendo pruebas, el realizar un indexing con numpy se demoró mucho más que la misma función pero con el decorador njit de numba. Tal vez se podría adoptar ciertas mejoras que sean invisibles al usuario.)|
|I just wanted to express that the most important thing for me would be the improved performance whenever possible. Probably incorporating parallelism in linear algebra libraries would be a good idea not that complicated to execute. (Original in Spanish: Lamentablemente no se me ocurre como solo quise expresar que lo más importante para mi sería que mejoren cada vez que pueden el rendimiento. Probablemente incorporar paralelismo en las librerías de álgebra lineal sería una buena idea no tan complicada de ejecutar. )|
|Use a lighter implementation closest to the function calls on cython. But without changes on the code, something easy to enable and disable. Using decorators maybe? |
|Default inter-core parallelization options. (Original in Spanish: Opciones de paralelizacion entre núcleos por defecto.)|
|I don't have any suggestions, I just think that performance should be prioritized.|
|More explanation on how to write more performant code|
|I think numpy performance is spectacular, but I believe it should continue to be a focus.|
|I have few good thoughts about this, I just believe that performance is most important.|
|if ndarray was displayed how a matrix is displayed in matlab or R, it would be much more convenient|
|I came from IDL and when I write the same algorithm in IDL it is almost always faster. Part of that is that I understand how to write to take advantage of the parts of IDL that are fast more than I do with NumPy, but even when I use the community-accepted best option, it is usually slower.|
|Ways to perform array selection based off criterion for the indices and data value at the index simultaneously.|
|Develop a portable binary file storage format for use from different languages (C, C++ and Fortran) Borrow ideas from pandas and incorporate in numpy. Pandas is slow compared to numpy but more robust that numpy.|
|Use  of GPU for some calculations|
|Performance on the overall library is really good. It's just that as my priorities go, it is the most important.|
|There are certain tasks that require multiple passes of arrays that simply don't need to do so, due to numpy's heavy leaning into masks for certain queries.  Numba of course helps mitigate a lot of these, but that's a crutch for an obvious design flaw in numpy at it's core.|
|There is not much to improve, I put it there as it should always be the highest priority when changing/adding code and features|
|Make everything even faster :)|
|Make it easier to new users to access high performance code by means of jit or something similar.|
|The performance of numpy is very important, as important as documentation and reliability. (Original in Spanish: El rendimiento de numpy es muy potente y esa potencia debería de ser igual como en documentación y fiabilidad.)|
|It is important to measure the execution time looking for opportunities for improvement. (Original in Spanish: Es importante medir el tiempo de ejecución buscando oportunidades de mejora.)|
|Improving performance through parallelism. (Original in Spanish: Mejorando el rendimiento por medio de paralelismo.)|
|More support for parallel programming, CUDA or vectorization of custom functions.|
|Parallel computing, improved algorithms|
|GPU support|
|Use code acceleration (GPU, TPU) similar to PyTorch and JAX. (Original in Russian: Использовать различные ускорения кода (GPU, TPU). Например как в PyTorch, JAX.)|
|Performance is great. It should just stay a priority.|
|I have used numpy as the basic library in many large research projects, performance is usually more than adequate. A challenge has been to profile large programs using numpy. |
|Make it “Faster"!|
|Fix Memory usage, restrictions and support on various platforms.|
|JIT compilation, easy parallel / GPU support|
|improve memory-access critical operations|
|Native distributed, multi-threaded numpy.|
|I guess I'm really looking at Numba and Dask for this...|
|Improved speed, intuitive function design. (Original in Japanese: 速度の向上、直感的に操作できるような関数の設計.)|
|The performance is quite good for my uses - I just think it should be maintained|
|It's already good but it can be made even better.|
|To process and handle large distributed data.|
|gpu support|
|Logic that processes large numbers of calculations as constraints. (Original in Japanese: 大量計算を拘束に処理するロジック.)|
|the race for better technology is always won by performance and reliability. That's why I kept them in higher priority.|
|Add Numba like JIT support. A specific set of IR can be purposed.|
|Support to Gpus|
|Adding GPU support for accelerated matrix operations|
|Further improvements in multicore and multithreading. Packages to support hpc usage|
|I use NumPy because it is very fast at most tasks.|
|General speed improvements.|
|e.g. Put np.min and np.max in one func|
|Complex expressions may create temporary arrays behind the scenes. Would be nice if clever coding in the interior of numpy eliminated this.|
|It is perfect.|
|NumPy is outdated in terms of leveraging new hardware instructions and there is a lot of room for improvement.|
|Goes together with 'New Feature' below: I would like a better way of addressing specific axis in a multidimensional array. Right now I'm tampering with numpy.s_ and direct calls to __getitem__, but I'm not satisfied with that. It is also not usable in numba compiled code and this limits me.|
|I don't have many ideas on the topic. I know that there have been already a lot of work on performance, and that more SSE/AVX vectorized implementations are on the way. I imagine things can always be improved somewhat given enough effort of benchmarking, profiling etc. |
|Plus easy to optimize the programs. (Original in French: Plus facile optimiser les programmes.)|
|GPU|
|Explicit standardization of core API so other tools can be swapped in as backends for parallel or GPU computing|
|making use of GPU|
|Integrate new features from Intel MKL & BLAS libraries. Optimize performance on new processors with high core counts like AMD's Threadripper CPUs.|
|Maybe via Numba.|
|Automatically take advantage of multi cores where feasible|
|Better Sync with DL based frameworks.|
|NumPy differential equation solving is slow.|
|Automatic detection of GPU, support for multithreading|
|Heterogenous ops|
|More documentation on best practices for performance, tips and tricks etc, would make it easier to get the performance that may already be there but currently requires a lot of extra knowledge to obtain.|
|Would be great if Numpy had native GPU support, although CuPy essentially makes most applications possible. Would be great to have more options for distributed array computing.|
|Make use of GPU acceleration  (e.g. allow use of alternative underlying Fortran code with added OpenACC directives, even if only for some common operations)|
|Continue to find most computationally efficient methods of executing code.|
|Community organizing around nep-18|
|You might be able to provide a separate option to inherently parallelize certain functions, and/or provide examples on using numpy with other packages that might boost performance.|
|I don't think, performance is an issue as of now. It is just, that I think (in general) numpy is in a state where I don't have much to complain about and performance gains are always nice...|
|Reduce memory consumption. (Original in Spanish: Reducir el consumo de memoria.)|
|Faster code is always helpful|
|Parallelization, GPU|
|Add GPU Support|
|NumPy should use numba.|
|Numpy is really fast, and I don't have a ton of experience in making it faster. However, I always fall back on numpy for code optimization and I think it is an important place to focus resources.|
|expanded randomized linear algebra routines|
|Automatic execution on GPUs|
|I primarily use NumPy to analyze large data sets. Loading those data sets (up to 2GB of csv files) with NumPy is not the most time efficient and eats up a lot of memory.|
|I have no knowledge on this subject, but believe NumPy's main usefulness to the scientific community is high performance. This should continue to be a priority.|
|Enable gpu support wherever it can be used|
|One specific problem (which is not purely numpy related) I have is the difficulty to parallelize my Python codes, given the ease in other languages like Julia and C++|
|Provide benchmark suite that we can run on platforms at our disposal. Python, owing to its nature (e.g. OpenCV interfaces), is slower compared to same set of operations on other platforms. This handicap makes it a tougher "sell" in mainstream IT departments.|
|Performance should always be top priority.|
|I'm not sure. Just make sure it performs well.|
|Make sure it works as efficiently as possible.|
|Performance is the key value prop for numpy versus pure Python implementations of algorithms.|
|The performance concerns are mainly around masked arrays, which can be extraordinarily slow.|
|Identify areas where current algorithms are highly sub-optimal or where there are advanced algorithms that perform much better.  I think of numpy and scipy together here. For example, numpy median filters are much slower than implementations in other languages such as IDL, and are far slower than optimal algorithms.  The last time I tested, the numpy histogram algorithm was very slow.|
|The work on vectorization sounds great. There are also some parts of NumPy that could be optimized (like 2D regular binned histograms). As far as I know, the Windows NumPy does not yet include the expression fusing that Unix does, which would be nice. (Most these are just light-weight suggestions, I work further down from NumPy usually, but since so much relies on NumPy, performance gains can affect a huge community)|
|1. The core of Numpy written in C should use the new hpy API so that it would be possible for PyPy (and other Python implementations) to accelerate Numpy code.  2. It should be clearly mentioned in the website / documentation that to get high performance, numerical kernels have to be accelerated with tools like Transonic, Numba, Pythran, Cython, ... See http://www.legi.grenoble-inp.fr/people/Pierre.Augier/transonic-vision.html|
|I work in HPC so I am always thinking about performance. Many functions are already fast but more speed is always better. :)|
|I don't have any specific thoughts, but faster is better :)|
|I'd love to see NumPy as _the_ de facto array computing API, with other packages voluntarily choosing to allow interoperability.|
|In general, I'm pretty happy with the current state of NumPy, so general performance gains of numeric routines and aggregations still be a great way to continue to improve NumPy.|
|It would be really nice if the FFT in NumPy were "best in class." Typically FFTW performs better than KissFFT (which I think is the basis for NumPy) but there are licensing issues so FFTW itself can't be used.|
|I'm very impressed with the direction of performance - keep on rocking!|
|Improve interoperability with numba & cupy.|
|Very large data set performance|
|Improve support for intrinsics / SIMD instructions.|
|Integration of acceleration by GPU natively. (Original in Spanish: Integración de la aceleración por gpu de forma nativa.)|
|I found the performance of NumPy fantastic.|
|Guides and recommendations or use cases on how to perform the functions in a parallelized way. (Original in Spanish: Guías y recomendaciones o implementaciones para realizar las funciones de forma paralelizada.)|
|parallelization, SIMD|
|There are increasing opportunities for processing large amounts of data. I hope it will be a little faster. (Original in Japanese: 大量データの処理の機会が増えてきています。) 少しでも早くなることを期待します|
|Create standard benchmarks so they can be evaluated. (Original in Japanese: 標準ベンチマークを作成して、評価できるようにする.)|
|Increase processing speed. (Original in Japanese: 処理速度を早くする.)|
|Speed ​​up of vectorized functions. (Original in Japanese: ベクトル化した関数の速度向上.)|
|Jit compiler (numba/torchscript like maybe) to allow "kernel fusion" e.g. make for i in x:   for j in y:     for k in z:        some complex operation per matrix entry fast.|
|Numpy has great performance; however, the project is "old". Perhaps a reformulation in the basic code would bring an even better performance. (Original in Portuguese: Numpy tem ótima performance; contudo, o projeto é "antigo". Talvez uma reformulação no código básico traria uma performance ainda melhor.)|
|Parallel computing support, memory saving, or organizing documents to do them. (Original in Japanese: 並列計算の支援、省メモリ、あるいはそれらを行うためのドキュメントの整理.)|
|Improve the use of partner libraries or reformulate the code, aiming at high performance and preparation for use in quantum computing. (Original in Portuguese: Melhorar o uso de bibliotecas parceiras ou códigos reformulados, visando performance elevada e preparação para uso em computação quântica.)|
|Make it faster and more efficient|
|Doing performance benchmarks with other libs that does the same (maybe even in other languages).|
|Improve algorithms implementations with latest research|
|After getting done from SIMD optimizations, I was thinking about to add direct support for OpenCL & Cuda |
|Speed especially with very large arrays|
|No specific thoughts on how to improve - just that I believe performance is a cornerstone of what makes NumPy so valuable and widely used (in conjunction with the expressive array syntax). IMO it is important for NumPy to maintain high performance to prevent ecosystem fragmentation with the introduction of many new array computation libraries (e.g. PyTorch).|
|More widespread usage of multithreading.|
|It is not really necessary to improve performance and reliability in any specific way. But it is important that you maintain them and keep good performance as it was before.|
|Benchmark against Julia.|
|I think there are ideas about using more vectorisation (with SIMD instructions), which seems interesting. More generally better performance with respect to use of multiple CPUs and memory allocation is always good to take.|
|Numpy in already extremely fast. But as more and more data is coming, Numpy has to be faster in many operations |
|Include ARM compliance and performance testing as a priority (with a view to macOS but also recent super computer usage).|
|Increase use of vector instruction (AVX, Neon ...) Make numpy more friendly to JIT compiler like numba|
|faster small arrays|
|Allow SIMD access from all platforms, move to more modern glibc beyond manylinux2014|
|continued work on SIMD acceleration of ufuncs, etc.|
|Make it go faster and better. Benchmarked optimizations.|
|Integrate simd and task-based multithreading (e.g. tbb) throughout|
|Keep doing what you are. I don't think performance is broken as it stands.|
|I dont have specific targets, just anything that makes it generally faster is helpful in nearly all scenarios|
|NumPy is becoming the de facto way of handling data, it should strive to be the best possible tool.|
|Exposing C APIs for more modules, to be used via Cython|
|Multiple low-level backends (eg MKL) with dynamical switching. OpenMP low-level parallelism|
|Compare the python library random to numpy.random. there are certain scenarios where one is better than the other. For instance, if you want to generate multiple random numbers random.uniform is better; but numpy.random.sample is superior for sampling from a list. It'd be nice to have numpy superior at all times|
|Scaling out, compatibility with other libraries or data types|
|Build a stronger, highly active community. I would like to see seminars and conferences like tensorflow|
|Do multi threaded or multi processing calculations wherever possible without or with very few user interaction.|
|There isn't a performance shortfall, but continuing to optimize the library and say optimized is always important.|
|I am just a user of NumPy (and a big fan!), but what I see with performance is: / 1. People not efficiently using NumPy so that they think NumPy is too slow, just because their code is not optimized. This is why documentation and presenting the most optimized solutions is so important.  / 2. I tried messing around with CuPy and I had some graphic card issues, so my experience is limited, but is it crazy or out of scope to want GPU support in NumPy for some things?|
|I'm always interested in improved performance. It doesn't require any work from me but I still benefit from it|
|The linear algebra module could see some improvement, (not my area of expertise, so I'm not sure how it could be improved).|
|I'd love to see support for accelerators and massive parallelism (via XLA as in Jax for example) land in NumPy.|
|Speed up computation process. Currently, we need other packages like Numba, NumExpr, or Cupy. It will be interesting to have speed without any additional packages.|
