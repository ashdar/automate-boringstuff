# automate-boringstuff
I plan to use this to hold work from a Udemy intro-to-python course called "Automate The Boring Stuff". This class seems well-liked on Reddit, so I might as well start here. Another popular choice seems to be "Think Python". 

I have been programming for decades, mostly in Transact-SQL and PowerShell, but I haven't learned a language from scratch in some time. Many of the languages I worked with and new sort-of-well, at one time, are dead. A few different BASIC dialects, a few Pascal dialects and a thing called "C". 

While I was aware of python 20 years ago, I never really pursued Python learning it. 

With COVID-19 and some 'free time', it's time to try to skill up a bit. Python, R, PowerBI, Tableau and Snowflake all seem to be worth learning. I came across a "free course" offer on Udemy, so I signed up.

I am starting this repository becuase I like revision control systems and I want somewhere to keep my work. I do not expect anyone to use this code.

I'm walking into this a little bit blind: I have no idea how the course is organized or how I will organize the source in this repository.


[https:\\automatetheboringstuff.com](https:\\automatetheboringstuff.com)


What am I doing differently than the class?
* I have been reading the textbook after I watch the videos on Udemy. That's probably backwards, but going back and reviewing the material is ++ useful for knowledge retention, I'm told.
* I have set up Visual Studio Code to edit python files. It is easy to do, just install the extension. I like to type in the (short) programs becuase I feel that helps build muscle memory for how things are supposed "to look". VS Code's syntax highlighter quickly points out my typos.
* I have set up Windows Terminal (which is still in preview) so that I can use it for my python shell.
* I am tracking my progress in a small Jira project. Trello and MS-Planner seem to "small" for this. Jira might be overkill.
* Must of the introductory stuff is, well, introductory. I know how a boolean data type works, I have a grasp of string, integer and float data types, I understand conditional branching, I understand immutability, passing by reference vs. passing by value and so forth. I am watching the videos at 2x normal speed and slowing down when something more 'pythony' needs reviewing.


What Big Questions do I have?
* I am going to want to see how database connectivity works. I presume that I need to install a package via pip.
* I am curious to see how python performs when compared to PowerShell. I expect that PowerShell is more memory- and cpu-hungry than python.
* I like using Pester with my PowerShell programs (as well as using Pester for infrastructure validation, checking for known issues in databases and so forth).

I can't help but compare Python to PowerShell. What (initial) observations do I have about Python? 
* This class is an introductory class, so it is side-stepping object-oriented concepts. Which is OK becuase I have only toyed with classes in PowerShell. I do have "do more stuff with classes in PowerShell" on my list of want-to-do items.
* Python seems extremely barebones and stripped-down. I presume that most of the magic is in third-party packages/libraries/modules.
* I know that PowerShell has lifted numerous things from Python (and other languages). 
* While PowerShell relies on .Net for data types, classes and member functions, must of this is built into Python. (I'm thinking of things like .ToUpper(), .ToLower() and so forth.). When comparing to the .Net string class, Python's string class has a similar, but different set of functions. 
* PowerShell has a lot of support for documentation and parameter validation.
* Lists and hashes seem to be the crux of the whole thing. 
* Hash 'output' looks suspiciously like a chunk of JSON.
* The "indentation determines code blocks/program flow" seems ++ wierd to me. As long as my code editor has a good formatter, I do not think this matters very much anymore. Does anyone manually format code these days?


