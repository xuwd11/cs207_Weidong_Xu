---
title: Project
layout: default
---

## Due Date ##

The due date is Monday, December 11th 2017 at 9:00 AM.  We will have group 
presentations on that day.

## Course Project:  Overview

**The Goal**

You will develop a software library for a client (the teaching staff).  
The development of this library will leverage modern software development 
practices covered in the course.  Ultimately, at the end of the semester, 
the client should be able to easily install and run your package with 
little to no difficulty.

**The Topic**

You are asked to write a chemical kinetics library.  The ultimate goal is 
to return the right-hand-side of an ODE.  You do not need to solve the ODE! 
The idea is that the client will just call your package to provide the 
right-hand-side and use that right-hand-side in any way they wish.  They might 
want to use it as the righ-hand-side of the ODE, or they might want to use it 
in a neural net code to learn new reaction pathways.  Those details don't 
matter to you at the moment. 

<img src="https://rawgit.com/IACS-CS-207/cs207-F17/gh-pages/svgs/42c65df43828c7cba2df2682a5cf2282.svg?invert_in_darkmode" align=middle width=70.18555500000001pt height=28.926479999999973pt/>

Of course, there are details in the right-hand-side function and we will 
cover these as needed.  **Note:  You are not expected to become and expert 
in chemical kinetics!  You will not be assessed on your chemical kinetics 
knowledge.**

## Expectations 

The client should be able to easily install the library, run the tests, 
access the documentation, and use the library for their application.

You are required to add a non-trivial feature to your library of your choosing.  
If you are having difficulty coming up with a compelling new feature, please 
set up an appointment with me to discuss possible ideas.  The teaching staff 
will be able to give you a few suggestions if need be.

Documentation for every subsystem in the project should be provided. Link to the 
docs from the ``README.md`` in each folder. The top level ``README.md`` should 
contain an overview, links to other docs, and an installation guide which will help 
us install and test your system.

For those parts of the project which are modules, ``python setup.py test`` should 
suffice. For all other parts, include instructions on how to test your code. Where 
possible, provide links to Travis-CI test runs and Coveralls coverage.

## Deliverables

Coming soon...

## Milestones

You will present the progress of your libary in a midterm presentation on Wednesday, 
October 18th in class.  You should also propose the feature that you will be adding 
for your final project during the midterm presentation.

The final presentation will occur on Monday, December 11th.  This presentation will 
be a demo of your entire library.  The final deliverable will be in the form of 
documentation of your library including instructions on how to install, run the tests, 
and examples for new users.

## Assessment

The final project is worth 50% of your course grade.  Here is a breakdown of the 
components of the project:

* Midterm:  20%
  * Presentation:  5%
  * Document:  25%
  * Library:  70%
* Final deliverables:  30%
  * Presentation:  5%
  * Document:  25%
  * Library:  70%

Exact details on how each component will be graded are forthcoming.
