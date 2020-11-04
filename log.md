

# Day -1: Anaconda vs conda.
-- NO CODE --
Added folium via conda
Started new repo for earthquakes
set up postman account

**Completion Date:** Wed 28 Oct 2020

**Learned:**
I know very little about API calls
USGS does not provide tsunami warnings. Those are provided by NOAA.
USGS does provided an intersting product, PAGER.

<br>
---
# Day 0: Anaconda vs conda.
Printing exercises. Not a whole lot new but there were a few distinctions.

**Completion Date:** Thurs 29 Oct 2020

**Learned:**
You can positionally index the contents inside the brackets. Index is zero based 
as show in the example

```
print("The number of the {1} shall be {0}. No more; no less.".format(3, 'counting'))
```

Some more vim commands I've learned tonight:

 - Replace a character ==> r{new char}
 - Copy a whole line ==> yy
 - Copy more than one line (e.g., 3 lines) ==> 3yy
 - Paste a copied section ==> p
 - Append text at the end of a line ==> A
 - Change the case of single letter ==> ~
 - Change the case of several letters (e.g., 3 letters) ==> 3~
 - Undo a change ==> Crtl-r

<br>
---
# Day 1:
Switched to TPTM 100 days as the CaptCorpMURICA seems good but is more basic -- and also not complete.

This was on datetime. The lessons were good but the project still isn't complete, the difficulty being in parsing.

**Completion Date:** Fri, 30 Oct 2020 

**Learned:**
So far, not a ton other than parsing datetime objects wasn't as easy as I thought they would be.

<br>

# Day 2: Mostly getting a csv of earthquakes to display in folium

**Completion Date:** Sat, 31 Oct 2020

**Learned:**
This is why I should write stuff down earlier. There was some trick like a loop I did. I really expected there to be some sort answer via broadcasting but nothing I could find. Happy Halloween!

<br>

# Day 3: More work on datetime module
Completed the two pybites challenges, plus a MVP of an egg timer. For next steps I think doing this a command line tool seems good. The only thing left is parsing dates from logs. Apparently, this was too hard as:
>Edit: We decided to simplify Bite 7 slightly after some feedback we received from students. We've now removed the requirement to read in the file which should keep the Bite focused on the theme.

Which I had gotten done but not the parsing. I'll spend a little more on it now.

**Completion Date:** Sun, 01 Nov 2020

**Learned:**
From RealPython's article on datetime:
>[Python Module] time is less powerful and more complicated to use than datetime. Many functions in time return a special struct_time instance. This object has a named tuple interface for accessing stored data, making it similar to an instance of datetime. However, it doesn’t support all of the features of datetime, especially the ability to perform arithmetic with time values.

<br>

# Day 4: namedtuple, defaultdict, Counter, and Deque
The videos for these were short and sweet.
 * namedtuple
 * defaultdict
 * Counter
 * Deque

Since there wasn't much in the way of work, I looked up the [collections documention](https://docs.python.org/3.3/library/collections.html?highlight=namedtuple#module-collections)

ChainMap is beyond any use case I can think of right now.

**Completion Date:** Mon, 02 Nov 2020

**Learned:**
Not sure that I'd say I learned it. More like learned about it. Also, there
wasn't any coding for this even with the Jupyter Notebook. So it's hard to say
how that goes with the whole code an hour a day part.

# Day 5: Analysis project using ~~Day04's stuff~~ pandas

This was disappointing. The TPTM/Pybites 100 days lesson really wasn't for primetime. The requirements for the #100daysofcode is to code for an hour a day. Day04 lesson was "watch these video and you can follow along with the complete notebook" Then a lesson you aren't prepared for. So, I'll do it pandas

**Completion Date:** Tues, 02 Nov 2020

**Learned:**
Other than pybites not being service I'm interested in and some more practice in pandas, not all that much.