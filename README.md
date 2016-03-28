# directory
A SacHacks food resources project

_Demo:_ open [the index file](templates/angularindex.html) in a browser.

The contents of the Feedback/Corrections form are on this [google doc](https://docs.google.com/spreadsheets/d/184QEwk06fxhsCmkmgL8FnLInUsw1FOtwJQSzWK_Z1Fg/edit?usp=sharing). Note that the timestamp is recorded in UNIX time and that there is no validation of fields.

The project consists of several directories.

*templates*
Contains front end angular/html files

*static*
Contains resources such as JS, CSS, etc.

*eventapi.py*
is a small python script that accepts JSON (exported from this [google doc](https://docs.google.com/spreadsheets/d/1JwAlUxOp9ixiEl-AwyPmRLRFgGUR7I1qWzLog2rCydo/edit?usp=sharing)) and returns json to directory.json with the next event time provisioned in a JSON readable format.

**directory.json**
cleaned and refactored (currently: the first 21 rows on the Google Doc).

**TODO:** 

See issues:
* [frontend](https://github.com/georgelu/directory/issues?q=is%3Aissue+is%3Aopen+label%3Afrontend)
* [backend](https://github.com/georgelu/directory/issues?q=is%3Aissue+is%3Aopen+label%3Abackend)
* [data processing](https://github.com/georgelu/directory/issues?q=is%3Aissue+is%3Aopen+label%3A%22data+processing%22)

Or, check out the Waffle.io board (note there is always a '?' in the badge if the repo is private):
* [![Stories Ready to Work On](https://badge.waffle.io/georgelu/directory.svg?label=ready&title=Cards%20Ready%20To%20Work%20On)](https://waffle.io/georgelu/directory)



## Data cleaning process


- Creating separate rows for sites with multiple days (EX: A site with operations
on Tuesday and Thursday will have two rows: one for Tuesday and one for
Thursday)
- Adding a coded day (0-6 for python days)
- Adding a coded 'interval' (representing the week of the month the event occurs, with 5 representing every week)
- Adding a starting hour

_Caveat_ This cleaning is imperfect and the JSON schema is very tentative. There
are a number of data issues which might favor alternative or
similar data schemas.

