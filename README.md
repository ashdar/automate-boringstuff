# automate-boringstuff

## What is this repo for?
I am using this repository to hold work from a Udemy intro-to-python course called "Automate The Boring Stuff" (ATBS). This class seems well-liked on Reddit, so I might as well start there. There is a book: [https:\\automatetheboringstuff.com](https:\\automatetheboringstuff.com)

I am using Jira to keep track of what tasks I am working on and what tasks I have remaining. That is not publically available. Trello, MS-Planner and MS-Tasks seem too "small" for this project. Jira might be overkill, but I am also working on 
improving my modest Jira skills.

I have been programming for decades, mostly in Transact-SQL and PowerShell, but I haven't learned a language from scratch in around ten years. 

While I was aware of Python 20 years ago, I never pursued learning it with any vigor. 

With COVID-19 and a 'pause' of work at some clients, I have some free time to spend on skilling up. I am interested in Python, R, Rust, PowerBI, Tableau and Snowflake (in no particular order). All of those languages seem to be worth learning. I'm also interested in Azure Data Factory, but it seems too easy to rack up significant charges and I'm leaving that for 'later'. 

I am starting this repository becuase I like revision control systems and I want somewhere to keep my work. I do not expect anyone to use this code. 

I am going a bit beyond the course information by using the unittest package to test some of the functions that I write. I found that I was constructing my own, tiny, low-feature, low-quality testing framework for the Chapter project programs. If I am going to do that, I might as well learn the 'Python way' to do unit testing. From some quick Googling, it seems that the unittest package is the accepted way (I am, of course, used to PowerShell's Pester module). One small issue is that unittest seems to require implementing your unit tests with classes. Classes are not touched on by the book or Udemy class, but it's a very light use of classes so it's not too much of a stretch. I'm not an object wizard, but I think I can get by with what I know.

## What am I doing differently than the class?
* I have been reading the textbook after I watch the videos on Udemy. That's probably backwards, but going back and reviewing the material is ++ useful for knowledge retention, I'm told. The chapters don't line up 100% with the video segments from Udemy. 
* I have set up Visual Studio Code to edit python files. This is very easy to do-just install the extension. I like to type in the (short) programs becuase I feel that helps build muscle memory for how things are supposed "to look". VS Code's syntax highlighter quickly points out my typos. IDLE, the in-the-box Python editor feels clunky to me.
* I have set up Windows Terminal so that I can use it for a Python shell. This is useful for short experiments and to try snippets from the book or videos.
* Must of the introductory stuff is, well, introductory. I know how a boolean data type works, I have a grasp of string, integer and float data types, I understand conditional branching, I understand immutability, passing by reference vs. passing by value and so forth. I am watching the videos at 2x normal speed and slowing down when something more 'pythony' needs reviewing.
* It is almost as if there are two paths through the course. You can read the book. You can watch the videos. There isn't quite a 1:1 correspondance between the book's chapters and the seperate video sections. This is why my project has folders for Chapters (from the book) and Sections (from the videos on Udemy's site). When I fiddle with code while watching the video, I tend to put the resulting Python files (if they seem worth saving) in the 'Section' folders. Similarly, I use the 'Chapter' folders while working on examples or practice programs from the book.


## What Big Questions do I have?

These things might need to wait until I have finished the course.

* How does database connectivity work?
* How does Python perform when compared to PowerShell for simple things like parsing CSV or JSON? I expect that PowerShell is more memory- and cpu-hungry than python.
* How does one write unit tests for Python programs? I like using Pester with my PowerShell programs (as well as using Pester for infrastructure validation, checking for known issues in databases and so forth). I have already started answering this question by using the unittest package to test the programs I write as I work through the chapters.

* I can't help but compare Python to PowerShell. What (initial) observations do I have about Python? 
* This class is an introductory class, so it is side-stepping object-oriented concepts. Which is OK becuase I have only toyed with classes in PowerShell. I do have "do more stuff with classes in PowerShell" on my list of want-to-do items.
* So far, Python seems extremely barebones and stripped-down. I presume that most of the magic is in third-party packages/libraries/modules.
* I know that PowerShell has lifted numerous things from Python (and other languages). 
* While PowerShell relies on .Net for data types, classes and member functions, much of this is built into Python. (I'm thinking of things like .ToUpper(), .ToLower() and so forth.). When comparing to the .Net string class, Python's string class has a similar, but different set of functions. 
* PowerShell has a lot of support for documentation and parameter validation. Python seems weaker here.
* Lists and hashes seem to be the crux of the whole thing. 
* Hash 'output' looks suspiciously like a chunk of JSON.
* The "indentation determines code blocks/program flow" seems ++ wierd to me. As long as my code editor has a good formatter, I do not think this matters very much anymore. Does anyone manually format code these days?


