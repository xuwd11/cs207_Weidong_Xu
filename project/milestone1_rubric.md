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
requirements are met.  The teaching staff may run additional tests to check the 
different aspects of the code.

You are not required to make a formal presentation.  Your group should simply 
be prepared to demo your code.

The output of your code should be the reaction rates of a set of species given 
a set of elementary reactions.

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
Your code must be written in an object oriented manner.  Here is an outline of the required 
structural components:
* You should include all classes in a single file called `chemkin.py`.  
* All classes must include at least two special methods.
* Make a class for reaction rate coefficients.  So far we have only talked about three types 
  of reaction rate coefficients:  constant, Arrhenius, and modified Arrhenius.  There are 
  other types and your code should be easily extensible to handle new types of reaction 
  rate coefficients in future verions.
  - At a minimum, your reaction rate coefficients class should consist of:
    1. A reaction rate base class with a constructor and other special methods as necessary 
       (e.g. `__repr__`).
    2. A subclass that implements the Arrhenius reaction rate coefficients.
    3. The constant reaction rate coefficient can go in it's own subclass, the base class, 
       or the Arrhenius subclass.
    4. If you think that there is a better way to design the reaction rate coefficients 
       class, then feel free to do so.  Just remember that you must include the 
       three typs of reaction rate coefficients discussed in class and permit the 
       code to be extended to other types of reaction rate coefficients.
* Make a class for reactions.  So far we have only talked about irreversible elementary reactions.  
  There are other types of irreversible reactions.  For example, *three-body reactions* and *duplicate* 
  reactions are common.  There could be other types as well.  Your code should be 
  written in such a way that it can be easily extended to these other types of reactions 
  in future versions.
  - At a minimum, your reactions class should consist of:
    1. A base class with a constructor and other special methods as necessary
       (e.g. `__repr__).
    2. A subclass for irreversible reactions.
    3. Methods for computing progress rates and reaction rates.
* Note that we have only worked with **irreversible** reactions.  Most reactions are 
  actually reversible.  Your code should be aware of this fact and have hooks for 
  future modifications that can handle fully reversible reactions.

## Test suite
Be sure to include a comprehensive test suite.  You must use Travis CI to run your tests 
and use Coveralls to test code coverage.  All tests **must** pass!  Your code coverage 
should be greater than 70%.  Put build and coverage status badges in your project repo 
README.md.
