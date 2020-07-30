# automate-boringstuff

## Why am I interested in Python?

I have been programming for decades, mostly in Transact-SQL and PowerShell, but I haven't learned a language from scratch in around ten years. 

I have wanted to spend some time with Python for quite a while. I had some exposure to it through a co-worker 20 years ago, but I never picked it up. 

I don't intend to become a Python expert, but I do want to understand how Python programmers think about "stuff". I've been a PowerShell programmer (among my other skills) since PowerShell 1.0. I do want to write some Python programs and I thought that I would follow along with a class in a more formalized manner than my usual thing, which is read a bunch of blogs and look at "real" code on GitHub.

With COVID-19 and a 'pause' of work at some clients, I have some free time to spend on skilling up. I am interested in Python, R, C#, Rust, PowerBI, Tableau and Snowflake (in no particular order). All of those languages seem to be worth learning. I'm also interested in Azure Data Factory, but it seems too easy to rack up significant charges and I'm leaving that for 'later'. 

## What is this repo for?

I am using this repository to hold work from the Udemy intro-to-python course called "Automate The Boring Stuff" (ATBS). This class seems well-liked on Reddit, so I started with it. There is a [book](https:\\automatetheboringstuff.com), which the Udemy class follows closely but not precisely.

I am starting this repository becuase I like revision control systems and I want somewhere to keep my work. I do not expect anyone to use this code. Or read this page.

# What other tools am I using?

* I have a private Jira project to keep track of what tasks I am working on and what tasks I have remaining. Trello, MS-Planner and MS-Tasks seem too "small" for this project. I don't have access to MS-Project. Jira might be overkill, but I am also working on improving my modest Jira skills.

* I have a Python 3.8 shell running in Windows Terminal for "the simple stuff". 

* I am using Visual Studio Code to write things that are too complicated for a shell. 

* Late in this effort, I found that many of the examples aimed at data science people are written for Jupyter Notebooks. Azure Data Studio supports those. I happen to keep that installed on my workstation, so I tinkered with that for a while. 

## What am I doing differently than the class?

* I am going a bit beyond the course information by using the unittest package to test some of the functions that I write. I found that I was constructing my own, tiny, low-feature, low-quality testing framework for the Chapter project programs. It's just a habit. If I am going to do that, I might as well exert a little more effort learn the 'Python way' to do unit testing. From some quick Googling, it seems that the unittest package is the accepted way (I am, of course, used to PowerShell's Pester module). One small issue is that unittest seems to require implementing your unit tests with classes. Classes are not touched on by the book or Udemy class, but it's a very light use of classes, there are plenty of simple examples and I am not doing anything complicated. So, it's not too much of a stretch to start "early" with classes. 


* I have been reading the textbook after I watch the videos on Udemy. That's probably backwards, but going back and reviewing the material is ++ useful for knowledge retention, I'm told. The chapters don't line up 100% with the video segments from Udemy, particularly later in the class.

* Must of the introductory stuff is, well, introductory. I know how a boolean data type works, I have a grasp of string, integer and float data types, I understand conditional branching, I understand immutability, passing by reference vs. passing by value and so forth. I do not necessarily know the "Python Way" to do those things. I am watching the videos at 2x normal speed and slowing down when something more 'pythony' needs reviewing.

* It is almost as if there are two paths through the course. You can read the book. You can watch the videos. There isn't quite a 1:1 correspondance between the book's chapters and the seperate video sections. This is why my project has folders for Chapters (from the book) and Sections (from the videos on Udemy's site). When I fiddle with code while watching the video, I tend to put the resulting Python files (if they seem worth saving) in the 'Section' folders. Similarly, I use the 'Chapter' folders while working on examples or practice programs from the book.

* I ran through the last few chapters. They seem to have little bearing on my work. Most of the effort in sending email is security configuration. If I work working somewhere, an adminitration team would already have mail working. Sending mail is usually pretty trivial, from the programmer's perspective.


## What Big Questions do I have?

Now that I have finished the course...

### How does database connectivity work?
This isn't covered in the class, but I work with databases (Microsoft SQL Server) constantly. I jumped ahead in my studies and had a quick look. The basic answer seems to be "install the pyodbc module". I do miss PowerShell's easy-to-use columnar formatting. Python provides support for printing in a columnar format, but this doesn't have the power of PowerShell's pipeline or formatters. I have a tiny demo file in the .\Extras folder.

### How does Python perform when compared to PowerShell for simple things like parsing CSV or JSON? 

I have not actually run speed tests. 

Qualitatively, I expect that PowerShell is more memory- and cpu-hungry than python. Of course, PowerShell tries to do more for you.

### How does one write unit tests for Python programs? 

I like using Pester with my PowerShell programs (as well as using Pester for infrastructure validation, checking for known issues in databases and so forth). 

I experimented with using the unittest package to test the programs I wrote as I worked through the chapters.

### I can't help but compare Python to PowerShell. What observations do I have about Python? 

1. The "indentation determines code blocks/program flow" seems ++ wierd to me. As long as my code editor has a good formatter, I do not think this matters very much. Does anyone manually format code these days? 

1. I know that PowerShell has lifted numerous things from Python (and other languages). I presume that Python's exensive module system had some influence. Or maybe perl.

1. Lists and hashes seem to be the crux of the whole thing. Hash 'output' looks suspiciously like a chunk of JSON.

1. Python seems extremely barebones and stripped-down. It seems that most of the magic is in third-party packages/libraries/modules. There seems to be a package to help with anything that you might want to do.

1. I'm kind of bummed that PowerShell doesn't seem to have a charting module as easy to use as matplotlib, or Plotly.

1. Modules like scikit or numpy could be super handy.

1. Much of pandas seems built into the default PowerShell cmdlets.

1. While PowerShell relies on .Net for data types, classes and member functions, much of this is built into Python. (I'm thinking of member functions like .ToUpper(), .ToLower() and so forth). When comparing to the .Net string class, Python's string class has a similar, but different set of functions. 

1. PowerShell has a lot of support for documentation and parameter validation. Python seems weaker here.


###  What about objects?
This class is an introductory class, so it is side-stepping object-oriented concepts. Which is OK becuase I have only toyed with classes in PowerShell. I do have "do more stuff with classes in PowerShell" on my list of want-to-do items.

