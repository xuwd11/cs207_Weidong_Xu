# Milestone 2 Rubric

| Component                   | Percentage |
| :-------------------------: | :--------: |
| Packaging and Installation  | 30%      |
| Reversible Reactions        | 40%      | 
| Proposed Feature            | 30%      |

---

## Due Date:  Monday, November 20th 2017

## Packaging and Installation

### Packaging
Your code should have a clearly defined package structure. 
Directories should be organized into logical units.  Your tests 
should reside in their own directory called `tests/` (or some 
other analogous name).  Make sure `__init__.py` files are present 
in each subdirectory and contain proper namespace initializations 
(if necessary).

### Installation
You must offer your code as package.  Distribution can be handled 
in a number of ways.  Two acceptable and common methods are: 
* Distribution is on `PyPI` and the user installs with `pip3`.
* The user downloads the code from `GitHub`, and runs 
  `python setup.py install` to install.
As part of the installation process, the user must be able to 
run the test suite.  After installing, the user should be able 
to run `python setup.py test` to run the test suite and make sure 
everything installed correctly.

## Reversible Reactions and Database

### Reversible Reactions
The code should be able to handle reversible, elementary reactions. 
I will provide the methods to you, but it is your responsibility to 
organize them in your code base and refactor the methods as necessary 
for consistency with your current code.

### Database of NASA Polynomials
Your code should read NASA polynomial coefficients in from a SQL database.  
This should be done as part of the input parsing process.  The user provides 
a list of the species in the mixture as part of the standard `.xml` input file 
(from Milestone 1).  This time you should query the database to store the 
NASA polynomial coefficients (at both high and low temperature ranges) in a 
data structure.  This datastructure will be used to evaluate the NASA polynomials 
for reversible reactions.

## Proposed Feature
You must propose a nontrivial feature for your final deliverable.  You **should not** 
implement the feature for this milestone.  We will assess the feasibility of the feature 
and make suggestions during the code review.

Here are the basic requirements:
* You should motivate and describe the feature
* Explain how the feature will fit into your code base (and package)
* Discuss the modules that you will write to realize your feature 
* Map out the methods you plan on implementing 
* Overview how you envision the user to use your new feature
* Discuss any external dependencies that your feature will require

The preceeding requirements can be in a section of your code documentation called 
`Future Features` or some analogous section title.
