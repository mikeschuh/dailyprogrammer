# dailyprogrammer

Solutions to reddit programming challenges at r/dailyprogrammer. Sorted by challenge numbers and difficulty, with all solutions (various languages) contained in the same challenge folder. Currently all solutions are single file python, but future solutions may require additional folder for each separate solution.


**https://www.reddit.com/r/dailyprogrammer/**

The full list of challenges in order is at:

* https://www.reddit.com/r/dailyprogrammer/wiki/challenges

--

Folder structure:

* [CNC] = challenge naming code
** {0-9}{0-9}{0-9}{e,m,h}
** e.g., 093e is \#93 easy
* Setup files provide language-specific config info to get started

Challenges /

* [CNC] / 
** [CNC].md
** [CNC].{py, c, ...}
 
Setup

* {py,c,...}.md
* quickadd.sh


## Useage

Use the quickadd.sh script to setup the folder/files for a new challenge
by name (saves a few commands). It creates the folder name and empty
.md and .py files that can be opened any way.

dailyprogrammer$ sh setup/quickadd.sh {CNC} 




