|Comments|
|--------|
|The reference manual is too much programmation-oriented. For me there is a lack of a presentation which is more mathematically-oriented.|
|Better cross-linking and more links to Python and C-level source code|
|Most functions have excellent documentation and I can tell that there's a lot of attention given to docstrings. Some functions however lack a single application example. Sometimes I get a much quicker grasp on a function by just looking at the examples as opposed to reading through verbose descriptions of the numerous arguments. Especially in cases I don't even end up using the function, it is much less frustrating when there are examples so that I immediately see that it is not what I'm looking for.|
|Tbh the documentation is already probably some of the best of any library I use but specifically it would be great if it was a little easier to get into the Numpy source code.  As it's quite a large and mature project, it can be tricky to know where to start with it and how much of say the Python C-API it's necessary to know about to feel comfortable.  It's maybe too much work for someone to do but what I've found amazingly useful in the past are guides where someone builds up a 'minimal version' of a project so you can see the core of the library (like this fort SQLite https://cstack.github.io/db_tutorial/) - it's something I thought about trying to do with Numpy at some point (just the core array structure, no linear algebra etc) |
|Providing more stand alone examples of common tasks. Often I read docs and find an example of what I am trying to do, but then need to read several other layers of docs to understand the example.|
|yes, i think documentation plays a key role in sowing a seed inside learner and it would be really great if a user can find a better way in understanding the analogies and codes comprehensively used in this library|
|Better examples|
|I always find difficulty doing things in numpy way and has to do it in python way. Not sure what can be done.|
|More simple and intermediate usage examples, and clearer documentation and usage of new confusing random number generator changes. |
|More concrete examples. Though to be honest. StackExchange probably serves that purpose pretty well.|
|More basics for beginners|
|I guess more "beginner" stuff.|
|More tutorials and examples!|
|More examples|
|Add longer, narrative tutorials or case studies|
|More examples. Often the examples are very minimalistic (e.g. numpy.fft.fft). Having more examples helps using functions.|
|More examples in the documentation|
|"Simple English" explanations of how functions work.|
|Try to make it easier to constructively find information, now it is sometimes "hidden" in extra tutorials |
|I don't think there's anything to improve, But I think it should continue to be focused to be as consistent as possible :)|
|Tutorials for example.|
|Jupyter notebook examples|
|how to use obscure features like striding, C-API etc|
|Have a complete and organized index of functions. Optionally give more examples of using options that drastically change behavior (eg axis =). (Original in French: Avoir un index complet et organisé des fonctions. Éventuellement donner plus d'exemples d'utilisation des options qui modifient radicalement le comportement (par exemple axis=).)|
|More examples for each non-trivial feature|
|Better search facility|
|More examples of usage of reach tool in different contexts|
|More examples or how-to guides.|
|Extend code examples at the function level. They are very helpful.|
|Documentation of less major functions and more examples, more on performance optimization.|
|I regularly work with structured arrays to read binary data dumps, and a 1:1 C-structure to structured array dtype would be very helpful.  I'm specifically thinking of how to translate a C union into a structured array.  Otherwise, python is gaining traction at my company, so documentation is the most important thing for us.|
|Examples for intermediate uses|
|See above. Documentation always helps, but numpys is pretty good anyway. |
|It is good, but sometimes it can be hard to find functions that I suspect that NumPy has. The doctrees have been greatly improved but drilling down to the functions can be confusing.   Additionally, lots of functions have good details if you are an expert in the topic but are not so good if you are not. A good example is the filter design functions. scipy.signal.butter has an argument called "analog" it's description is unhelpfully "When True, return an analog filter, otherwise a digital filter is returned." What is the difference? why might I care?  The code samples for scipy.signal.butter are another good example, they use the library very differently than I might when I use it. (this is more typical: https://stackoverflow.com/a/12233959/4492611)  This is not to say that the docs are not excellent, they are just the main way that I interact with NumPy and the topic I care the most about.|
|* giving more examples for different situations instead of making one for multiple methods. * also, plus one weird example might widen people's horizon|
|improve the structured overview so that idiots like me don't try to program stuff that is just a small subset of np.einsum|
|The NumPy library is very large, and because of fairly strict backward-compatibility guarantees, there are many different ways to achieve a particular task.  I think that the documentation could be improved with an informal style guide that helps new and old users sort out what the 'modern' NumPy way is.  An alternative (if a style guide would be too contentious) is to provide a collection of examples of 'modern' NumPy being used to accomplish common tasks and avoid gotchas.  For example, a linear algebra collection might include examples of the use of 1d/2d ndarrays as opposed to the outdated matrix type, the use of @ as opposed to np.dot, etc.|
|Taking scikit-learn as an example, maybe more tutorials on how to do things and documentation explaining the theory and concepts behind the functions and implementations.|
|More examples in the documentation would be awesome, sometimes I found myself using functions that solved my problems but the utility of it did not came from documentation, but from a colleague showing it to me|
|The NumPy documentation is already excellent. The only problem I have is that it sometimes feels hard to figure out all the features that exist. I am not sure how to overcome this exactly. Maybe some more use-cases where a user is guided through a complete problem set is helpful (I know that this also already exist, maybe more of that for different use cases). |
|I will first say that in my view numpy is a gold standard in self-generated documentation and everyone involved in the project should be very proud of the state of the documentation. I have found some cases where more examples would be useful. I have a background in numerical physics and I find some of the documentation of complex numerical algorithms to be lacking, although the only examples I can think of now are in scipy. Where a complex numerical algorithm is concerned I don't think it is enough to document the API. There are always limitations and edge cases where the algorithm will not perform well, or could even return incorrect results. The documentation could do more on this front.|
|More examples and recommendations, I would copy pandas. (Original in Spanish: Más ejemplos y recomendaciones, copiaria a pandas.)|
|Organising documentation will surely help a lot. Good examples are Docker or Tensorflow documentation.   Another improvement is to add more guides for developers that are interested in contributing to NumPy.|
|Certain scientific doc's are ok, but not always referencing good papers/sites.|
|NumPy, to me, had and sometimes has a steep cliff: I can easily understand the basic use of a function, but actually wrapping my head around how to use the function on a dataset in a useful way in a complex function can be difficult. I don't think there's necessarily an easy solution for this, but more varied examples in documentation could help.|
|inclusion of in depth examples|
|- documentation between numpy and scipy (and different versions) is a bit confusing sometimes - documentation in some cases is just not enough to understand what a function does - sometimes I'm not sure if I just cannot find the correct method I am looking for or if it does not exist entirely|
|I think adding some high-level tutorials, especially for the more obscure parts of NumPy: - Stride tricks - Structured Arrays and complicated dtypes - Buffer protocol integration (especially w/ 3rd party libraries or custom C/C++ codebases) - Docs on how to get better performance (w/ pointers to 3rd party libraries like Cython or Numba)|
|more documentation in Spanish. (Original in Spanish: mas documentacion en español.)|
|Expand the connection between current documentation and basic mathematical models. Currently in many sections of the documentation there is an extract of the concepts used (as in fft) but it would be nice to have the reverse process: A documentation that from the mathematical models can reach the related numpy functions. (Original in Spanish: Ampliar la conexión entre la documentación actual y los modelos matemáticos de base.Actualmente en muchas secciones de la documentación hay un extracto de los conceptos usados (como en fft) pero estaría bien tener el proceso inverso: Una documentación que desde los modelos matemáticos pueda llegar a las funciones de numpy relacionadas.)|
|I am sometimes confused over the exact working of the more seldomly used arguments of a function even after reading the docs. More examples and longer explanations would help. Also, numpy has many functionalities and I often find it hard to identify what I need for a certain problem.|
|Add more examples on the use of numpy in specific areas (differential equations in physics, mathematical models of biological systems, etc). (Original in Spanish: Agregar más ejemplos sobre el uso de numpy en áreas específicas (ecuaciones diferenciales en física, modelos matemáticos de sistemas biológicos, etc).)|
|Documentation of all the algorithms/methods should have appropriate citations and a variety of examples (many of them do already, but this can still be improved)|
|Videotutorials|
|All functions should be typed so tools like pyright can give better live documentation to the user.|
|Please add more step-by-step tutorials (and direct links to them from official documentation). Examples are the great way to understand some new concepts|
|Sometimes it is difficult to find the documentation and sometimes you will find documentation of functions from previous versions that are not known to be older, so it would be good to specify which functions are current and which are not. Also sometimes it is difficult to know how to search certain functions. (Original in Spanish: A veces es difícil encontar la documentación y a veces se encuentra documentación de funciones de versiones anteriores que no se sabe que son anteriores, por lo que sería bueno especificar cuáles funciones son actuales y cuáles no. También a veces es difícil saber como buscar ciertas funciones.)|
|Tutorials and for some people, translations. (Original in Spanish: Tutoriales y para algunas personas, traducciones.)|
|Putting more examples of how to use the functions|
|It is important to have information in a native language, especially when learning. (Original in Spanish: Es importante tener información en una lengua nativa sobre todo cuando se está aprendiendo.)|
|It tends to be criptic. I usually need to go to other sources to learn|
|Translation to multiple languages|
|More tutorials beginners, with very simple ideas, very simple terms, with lots of explanations|
|Some features such as __array_function__ or __array_ufuncs__ are poorly documented for more complicated use cases. While the documentation is fine to provide a simple understanding, to get a more complete understanding I read full implementations from dask or cupy.  Also some less ``mainstream'' interfaces sometimes lack examples that would greatly facilitate the meaning of options. A recent example that comes to mind is lgmres (can't think of a numpy right in this instance).|
|More examples and tutorials.|
|The docs are dense for new users. Provide more examples and applications, including video when possible, and worksets, possibly in notebooks?|
|Better and clear documentation for many methods missing.|
|Documentation isn't always clear on what to do and some terms are very full of jargon.|
|I would like to see more extensive examples|
|I actually think your documentation is very good, especially when combined with stack overflow answers. But I was required to pick something!|
|can be useful to have multiple (consistent and integrated) documentation systems that target specific users. e.g. language level specification vs gentle introduction including concepts.|
|Docstrings of numpy functions do not all match in style.|
|Although not really anyone's fault, old deprecated commands (especially on the SciPy documentation) are everywhere. Streamlining the numpy.random documentation to clarify trade-offs would be helpful. I also think that many beginner's are unaware of a lot of the many useful commands, so having some easy way to find new commands (like numpy.roll) would be great. There have been many times that I have written code one way, then learned of a superior (cleaner / more performant) way a year later. I think the numpy.where command is a good example.|
|Examples - Lots|
|Many of the high level documentation pages in the numpy documentation are incomplete. For example, the documentation on dtypes does not list every possible dtype and doesn't give a full description of things like the string dtype specification. |
|Easy to understand how to use Numpy in Japanese. (Original in Japanese:  Numpyの使い方を日本語でわかりやすく整備.)|
|Types, better navigation|
|more How Tos|
|One simple thing is update the formatting - I think some simple stylesheet tweaking may make the docs themselves a bit more aesthetic ;)  More cross-references between components (e.g. "See also" linking np.random.uniform to np.random). Some examples on reference pages are great, but some pages are missing them. Also, it would be excellent if the existing NumPy tutorials could be linked (as permalinks / versions) from the documentation when possible.  I'm thinking MATLAB-level documentation quality (which TBH is a high bar!).|
|documentation is the most important thing about anything. It allows everyone to read the data and useful information about the project ang get to know more technically.|
|I think including links to more sophisticated uses of numpy, using common idioms, might be helpful |
|As someone who has been introducing peers to using Python as a scientific tool, questions about NumPy are often raised (e.g. how to do particular things, "gotchas" when implementing specific functions, or more general interest in a "cookbook" of various minimal working examples of it being used). While the NumPy documentation (specifically, that available through the manual) goes some way to addressing this (especially as a quick reference for function arguments/outputs/references!), there is always room for improvement:  One particular aspect of this could be in the examples provided for "less trivial" examples where users may trip up on certain details in the implementation.  Another possibility could be adding additional sections to the "Explanations" and "How Tos" pages to cover common Q&As from e.g. Stack Overflow etc (although I see that this is only a fairly recent addition as per NEP 44, and look forward to seeing how it progresses!)|
|Documentation on using on embedded devices (like for example how to call from C++, etc.)|
|Make documentation easier to understand, and written in plain language.|
|Make it more like scikit-learn docs|
|I want more execution examples. (Original in Japanese: 実行例を増やして欲しい.)|
|Perhaps the current docs with format Overview-&gt;Functions-&gt;examples could be more explicit. When you find yourself looking for np.fft.rfft, it is not always clear what you want, and moving between the three is not always intuitive (I use the top banner to move up, moving down is a little awkward. Overall though, numpy documentation is light years ahead of a lot of projects that I have used.|
|more case based tutorials|
|More "vignette" style examples. Just generally more examples, both straightforward, and within the context of a real use case.|
|I would like to see more examples given, perhaps with some reference regarding performance.|
|Possiblity add more useage examples to less commonly used functions?|
|- Documentation can be hard to find. For instance, say I go to learn about vectorization. This page (https://numpy.org/doc/stable/) has at least six different links that one might follow to find relevant documentation. Picking one, Tutorials (https://numpy.org/doc/stable/user/tutorials_index.html), gives another set of links with no hint as to their contents. Finally, I have to guess that my topic would be considered "NumPy Basics". I think this navigation system should reworked.  - Also, lots of documentation pages require a non-trivial understanding of NumPy to parse.|
|giving more elaborate examples|
|It might be nice to have more real world examples/use cases regarding what you can do with some of the algorithms within numpy.|
|It would be great to have some: 1. More beginners tutorials 2. Performance optimizations guidelines 3. More usage examples. 4. Make some online sandbox to test examples with different versions 5. Right now most of questions can be answered using google. Probably, most popular must be kept in documentation. 6. We need some Slack/Discuss platform to discuss|
|Reference documentation is already good, but more tutorials and longer examples would be useful. |
|More extensive examples.|
|More elaborate examples and better error messages.|
|A gallery of examples for the different use cases, much like you'd see for a vis library.|
|I actually think the numpy documentation is generally good, but making sure documentation is current, well-explained and in as many languages as possible should always be a high priority for an open source projetct as important as numpy.|
|It always amazes me *how much numpy can do*. I only recently found out that there are financial functions included in the library.  I find it really hard to find most of these things out until I'm specifically looking for something, and then eventually find my way back into numpy through 3rd party platforms (e.g. StackOverflow telling me I should have been using numpy for this all along).  Tutorials and worked examples make great reference material, the scikit-learn community is one of the places that I continue to draw a lot of inspiration from.|
|More examples.|
|The old "EricsBroadcastingDocument" should in my opinion be part of the core documentation for how broadcasting works, it's extremely good and the figures help A LOT.|
|more example code|
|nice clear examples and guides|
|Additional examples Better "discontinued in future" error messages: these tend not to offer any help in how to replace them, though I migth misremember and this was Pandas fault.|
|More examples. There already are numerous examples and the documentation is generally excellent, but in terms of examples it is not yet at Mathematica levels.|
|If you do provide the option to inherently parallelize certain functions, the documentation to use those features needs to be written. Otherwise, I think the documentation is fine.|
|The documentation is very good and reliable imo. I would like more detailed narrative docs for the technical parts and the descriptions of algorithms)|
|More concrete examples from different areas where numpy is being used. Also rating them as starter to experienced|
|Fixing/updating inconsistencies|
|Maybe more worked examples|
|Related, a problem often arises when users of other packages (like pandas) fall back on really slow design patterns that could easy be optimized with numpy. More documentation for best practices integrating numpy into a pandas-centric workflow could users who don't think about optimization regularly. |
|IT can be hard to fully grasp the details about what a function does and how it interacts with other parts of python.|
|I think more/clearer examples could be effective some don’t fully explain the functions|
|More examples.|
|Tutorials|
|I want detailed documentation on minor functions. (Original in Japanese: マイナーな機能にも詳しいドキュメントが欲しい.)|
|The Numpy documentation could add detailed examples for each function, details in the sense more explanation about input and output.|
|Documentation is often unclear or incomplete. I think also some older versions of numpy have functionalities renamed which can be confusing.|
|I would like you to include some graphical examples, sometimes it is difficult to extrapolate the math. (Original in Spanish: Me gustaría que incluyera algunos ejemplos gráficos, aveces es difícil extrapolar la matemática.)|
|Insert more usage examples and raise some points that, although they are clear to those who have been using them for the longest time, still confuse new users like the cases of the views of the arrays when there is slicing. (Original in Portuguese:  Inserir mais exemplos de uso e levantar alguns pontos que embora sejam claros pra quem é usuário há mais tempo, ainda confunde novos usuários como os casos das views dos arrays quando há o fatiamento.)|
|Try to provide different examples of use for each function.|
|I'm a brand new numpy user. I want to be able to find answers to my questions.|
|I feel that np has pretty good documentation out there, but it's often hard to *find* the right documentation for what you're looking for. For instance, there are often several functions that are closely related and it's hard to know which is the right one to use (it's even harder to remember without needing to look it up each time!). Perhaps additional ways to group together pieces of documentation with a high-level commentary that says "here's the one you should generally use unless you're in this case..." would help.|
|I like the plans in NEP 44. The current (1.20.dev0) "absolute basics" and "quickstart" tutorials repeat a lot of the same content, and could probably be consolidated. The "absolute basics" material has 26 section headings, which makes it hard to follow. I really like the way new front page of the website highlights the main concepts of "vectorization, indexing, and broadcasting" and then lists some of the subpackages than NumPy offers. Perhaps that's an outline that our intro docs could follow? I also wonder if multidimensional arrays should be introduced part-way through the new user tutorial so they can see some basic array operations sooner?|
|More (and more thorough) code examples. A HOWTO (like Python's -- https://docs.python.org/3/howto/index.html) that details recommended solutions to common problems.|
|searching for numpy functions in duck duck go/google often returns docs for older versions of numpy first. fix SEO/remove older pages so that newest pages show up at the top.|
|Use case notebooks|
|Easier to navigate index|
|It would be nice to have a small visual refresh for NumPy's docs (the new website is great!). The pandas project has a really nice new theme. Also, as a developer, I really like NumPy's docstyle and would like to learn more about tooling for enforcing NumPy docstyle in my own packages. pandas has really nice docstyle enforcers in their CI, maybe I should try those in my own project.|
|I still think completeness and specificity in the documentation is the weakest link in numpy. I think users should not have to consult source to verify specifics of the underlying maths of some functionality but currently that is sometimes required|
|add best practice and/or performance comparison of optimal/sub-optimal ways to use each functions|
|Keep up the good work. Numpy/Scipy documentation is first rate.|
|Streamlining (directing users more clearly to different parts of the documentation: tutorial, user guide, API reference) and modernizing the design. Obviously, improve the writing on many sections.|
|More tutorials. Lots of examples in almost all docstrings.|
|The documentation is already very good. For beginners more example code and/or visual explanations for cocepts that are hard to understand may be useful.|
|The high level documentation like tutorials and narrative docs on advanced topics are not in good shape, and there isn't enough of it.|
|The API document design feels old. I want you to design the same as the project top page. (Original in Japanese: APIドキュメントのデザインが古臭く感じる。プロジェクトトップページと同じようなデザインにしてほしい.)|
|Expansion of Japanese documents. (Original in Japanese: 日本語ドキュメントの拡充.)|
|Like statsmodels, please enrich the examples with a mathematical background and a notebook. (Original in Japanese:  statsmodelsのように、数学的な背景とnotebookによる例を充実させてほしい.)|
|More Examples that explain what things do and how they work Visual Explanations, especially in everything that manipulates ndarrays|
|The documentation could be more comprehensive, with case studies, for example. Simpler tutorials on "basics", or "what to do" with Numpy could also be covered. There are many basic users who don't understand where Numpy ends and where Scipy starts. (Original in Portuguese: A documentação poderia ser mais abrangente, contando com estudos de caso, por exemplo. Tutoriais mais simples sobre o "básico", ou "o que fazer" com o Numpy também poderiam ser abordados. Há muitos usuários básicos que não entendem onde acaba o Numpy e onde começa o Scipy. )|
|I want annotations on newly introduced functions and methods. (Original in Japanese: 新規導入された関数やメソッドに注釈が欲しい.) Add 'introduced-version' notes to new functions or methods.|
|I think it is good to set up a project to translate documents into each language. (Original in Japanese: 文書の各言語への翻訳プロジェクトを立ち上げるのが良いと思います.)|
|Creation of various kinds of educational material, contemplating different levels of expertise and experience.|
|The new website is a nice improvement.  The documentation presented by it should have a high priority as it is the basic way users learn how to incorporate NumPy's functionality into their projects.|
|1) If I google for some numpy function, all the top hits are referring to version 1.17 instead of the latest version, and there is no easy way to directly go to the latest version.  2) It is fairly common that I feel that the documentation only covers very simple examples, so the complicated usage is not obvious.|
|Stronger documentation standards and automated docstring checking and validation, c.f., pandas. For example, how are parameters referenced in doc strings, ``param``, `param`, param, or *param*|
|NumPy feels like it is in a relatively good place. What gaps remain should be filled as soon as possible especially examples should be used extensively.|
|Documentation is the core of any project. Any new comer would look towards the documentation for better understanding of the software/open-source project. Hence documentation should be given an equal amount of priority as well.|
|Overall I find the documentation very good and comprehensive. Two areas where the documentation may improve is in: 1. Containing more "typical usage" guides for some of the functionality in NumPy. 2. Better explaining subtle details that may cause a lot of frustration if unknown, possibly via references to other sources.|
|Making great strides, but more examples for various disciplines would help attract users.  Some documentation is devoid of practical examples.|
|Documenting the (limited) portion of NumPy that users should actually use|
|Documentation is improving well already, stay on track :-)|
|In general the docs are good, but the small examples illustrating a function are sometimes a bit cryptic. A short sentence describing what's happening could help /  / As a dev it's also helpful when a parameter is tagged with eg "new on 1.14" so I know whether I can use it depending on our dependency constraints|
|Numpy docs are completely functional and do the job. However, between the time the numpy project began and now better documentation solutions have come online. Numpy docs have a strange previous/next topic interface that don't make sense without context. A full featured scrollable table of contents on the left (a la readthedocs) and even better fonts (I'm always bothered by the main function font and spacing with the black/yellow contrast).  /  / My personal favorites for how documentation could look like would be Julia and Bokeh.|
|Including more use/edge cases in the docs as examples, possibly drawing from common uses in stack overflow, for instance.|
|Just anecdotal: I found that a combination of tensordot, moveaxes and diagonal solved a specific problem for me. But finding out what to assign to the parameters axes, axis1 and axis2 was literally an exhaustive search. I wrote loops trying every possible combination and compared the result to the correct one. A bit of prosa and examples would have helped to understand what is happening.|
|Latex|
|The documentation is not lacking, but comments on what the examples are doing in some packages, especially pointing out where a function call is made for speed or memory optimization would make finding the sample code I'm looking for a more smooth experience. |
|While I do like the documentation and I'll be honest, I should probably look at it more than just messing about or defaulting to stackoverflow (so take my words with a grain of salt!), I think as I stated to the previous question, really focusing on how people can work optimally with NumPy and not just what the features are would be amazing. |
|Ensure every parameter is documented at sufficient level. Many params are left by the wayside|
|More examples.|
|I think the documentation is really good. But it could be better, especially in providing context for why I should use one function vs another with similar functionality|
|Alot more easy-to-understand & use tutorials for what can be done using NumPy & some of the newer tools that use it, like ML, .....|
|Ability to change version (e.g., from v1.19 to v1.18) without leaving the webpage.|
|Research and design ways to make learning and applying numpy more effective. Seek funding to research and implement these learning processes. (Original in Spanish: Investigar y diseñar formas de hacer mas efectivo el aprendizaje y aplicación de numpy. Buscar fondos para investigar sibre estos procesos de aprendizaje e implementarlos.)|
|The documentation could be improved to perform operations with images of more than three bands. (Original in Spanish: Se podría mejorar la documentación para hacer operaciones con imagines de mas de tres bandas.)|
|Several functions lack good documentation. The only way to know their behavior is to test it manually which can be time consuming.|
