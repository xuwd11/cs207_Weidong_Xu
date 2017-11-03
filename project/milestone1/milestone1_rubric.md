# Milestone 1 Rubric

| Component                   | Percentage |
| :-------------------------: | :--------: |
| Model Document              | 12.5%      |
| Code documentation          | 12.5%      | 
| Input file + parsing        | 12.5%      |
| Code                        | 50%        |
| Test suite                  | 12.5%      |

---

## Due Date:  Wednesday, October 18th 2017
Groups will present their project to the teaching staff in a code-review session.  
The presentations should include a demo of the code to show that all of the 
requirements are met.

You are not required to make a formal presentation.  Your group should simply 
be prepared to demo your code.

The output of your code should be the reaction rates of a set of species given 
a set of elementary reactions.

The teaching staff will try a variety of input files on your code to test 
different situations (e.g. different reactions, erroneous inputs, different 
species, different reaction rate coefficients, etc).

---

## Model Document
Write a document that describes the API and how to run the code.  The sections of the 
document should be:
1. Introduction:  Describe what problem the code is solving.  You may borrow the Latex 
   expressions from my lecture notes.  Discuss in broad strokes what the purpose of the 
   code is along with any features.  Do not describe the details of the code yet.
2. Installation:  Describe where the code can be found and downloaded.  Tell the user 
   how to run the test suite.  We are not releasing this code as a package yet, but 
   when we do that this section will include instructions how how to install the package.
3. Basic Usage and Examples:  Provide a few examples on using your software in some 
   common situations.  You may want to show how the code works with a small set of 
   reactions.

I recommend that you write your model doc in Markdown.  Please don't use Word.  Using 
Latex is also acceptable.

Please consult [!https://github.com/libqueso/queso](https://github.com/libqueso/queso) 
for an example of a model doc.  In particular, take a look at `QUESO_users_manual.pdf` 
for an example of a nice model doc in the form of a users manual.  Note that the `QUESO` 
users manual is much more comprehensive than what I am asking for you to do here.  
However, you should feel free to use the `QUESO` users manual as an example.

## Code Documentation
All modules, classes, and methods must be documented.  Make sure you include doctests.

## Input file
Your code must be able to read in and parse an `XML` input file (as discussed in class).  I will 
provide you with the form of the input file.

## Code design
Your code must be written in an object oriented manner.  We want to give you broad freedoms 
in how you design your code.  To that end, we shall refrain from imposing stringent 
structural or design requirements on your code.  However, a few basic requirements must 
be met.  These are:

* You should include all classes in a single file called `chemkin.py`.  
* There must be at least one class that contains the relevant kinetics methods.
* You must have *at least* two special methods (such as `__repr__` or `__len__`.
* Your code must be able to handle the following situations:
  - Elementary reactions
  - Irreversible reactions
  - Constant reaction rate coefficients
  - Arrhenius reaction rate coefficients
  - Modified Arrhenius (a.k.a Kooij) reaction rate coefficients
* The code must be sufficiently general to handle an arbitrary number of 
  species.
* The code must be sufficiently general to handle an arbibrary number of 
  elementary reactions.
* The code must be easily extensible with hooks for the following:
  - Reversible reactions
  - Non-elementary reactions (for example "duplicate reactions" or "three-body reactions")
  - Reaction rate coefficients not discussed in class.
  Your code should handle each of the situations above gracefully.  You choose 
  how to handle the situation.
  


## Test suite
Be sure to include a comprehensive test suite.  You must use Travis CI to run your tests 
and use Coveralls to test code coverage.  All tests **must** pass!  Your code coverage 
should be greater than 70%.  Put build and coverage status badges in your project repo 
README.md.
