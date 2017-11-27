# Final Rubric

| Component                   | Percentage |
| :-------------------------: | :--------: |
| Presentation                | 10%      |
| Documentation               | 40%      | 
| Final Library               | 50%      |

---

## Due Date:  Monday, December 11th 2017

## Presentation

The presentation should be a total of 15 minutes with questions. 
The main portion of the presentation should be a demo of the new 
code feature.  However, you must also demonstrate to the class 
how to install your library and how to access its basic 
functionality.  Each member of the group should give a portion of 
the presentation.

## Documentation

The code documentation and model doc should be complete.  The 
following sections are required:
1. **Introduction:**  Describe what problem the code is solving.  You may borrow the Latex 
   expressions from my lecture notes.  Discuss in broad strokes what the purpose of the 
   code is along with any features.  Do not describe the details of the code yet.
2. **Installation:**  Tell the user how to install the library.  Be thorough here.  If there is 
   more than one way to find and use the code, then please clearly discuss each method.  
   Suggest a preferred installation method.  Tell the user how they can contribute to the 
   development version if they so desire.  Tell the user how to run the test suite.  Be 
   explicit on any dependencies.
3. **Basic Usage and Examples:**  Provide a few examples on using your software in some 
   common situations.  You may want to show how the code works with a small set of 
   reactions.  This is where you would introduce a toy demo problem and show off basic 
   use cases.  You would also highlight how to use your new feature here as well.  If 
   your code produces output or figures, you may want to include an `examples/` 
   directory in your repo so the user can try to reproduce the results in this section.
4. **New Feature:**  This is where you discuss the final feature.  This section should 
   contain the following information:
   * Motivation of the new feature.
   * Implementation details including any new modules, classes, or methods.  I can 
     find the exact implementation in your code base, so your job here is to make sure 
     I can understand why you made certain design decisions and how everything works 
     together.

I recommend that you write your model doc in Markdown.  Please don't use Word.  Using 
Latex is also acceptable.

## Final Library
Your library must be on `GitHub`.  It should be easily installable either via `pip` 
(`pip3`) or download from `GitHub`.  The teaching staff should be able to reproduce 
your demos and use the library for their own purposes.  Your project repo must have 
badges for Travis CI and Coveralls.  All tests must be passing and coverage should 
remain above 75%.  The code should have an approriate level of commenting, should 
include doctests and docstrings, and should be written in a Pythonic way.  For 
example, do not use 
```python
for i in range(N):
```
where and `enumerate` would work.  The code should be able to handle reversible and 
irreversible elementary reactions and combinations thereof at a minimum.  The user 
should specify the reaction set and participating species through an `.xml` input 
file.  The NASA polynomial coefficients should be queried from a `sqlite` database.

### Update NASA polynomial coefficients
**Note:**  You must extend your thermodynamic coefficients database to include 
several new species.  A `.txt` version of the new database can be found under the 
`projects/final` directory or at the following website: 
[](http://combustion.berkeley.edu/gri_mech/version30/files30/thermo30.dat).  You 
do not need to convert the `.txt` file to `.xml` first.  You can go directory 
from `.txt` to `sqlite`.
