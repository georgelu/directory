# directory
A SacHacks food resources project

_Demo:_ open [the index file](templates/angularindex.html) in a browser.

The contents of the Feedback/Corrections form are on this [google doc](https://docs.google.com/spreadsheets/d/184QEwk06fxhsCmkmgL8FnLInUsw1FOtwJQSzWK_Z1Fg/edit?usp=sharing). Note that the timestamp is recorded in UNIX time and that there is no validation of fields.

The project consists of several directories.

**templates**
Contains front end angular/html files

**static**
Contains resources such as JS, CSS, etc.

**eventapi.py**
is a small python script that accepts JSON (exported from this [google doc](https://docs.google.com/spreadsheets/d/1JwAlUxOp9ixiEl-AwyPmRLRFgGUR7I1qWzLog2rCydo/edit?usp=sharing)) and returns json to directory.json with the next event time provisioned in a JSON readable format.

**TODO:** [![Card Ready to Work On](https://badge.waffle.io/georgelu/directory.svg?label=ready&title=Cards%20Ready%20To%20Work%20On)](https://waffle.io/georgelu/directory) (links to Waffle.io board.

Frontend:
* Pagination of events
* More sort/filtering
* Adjust language to be more understandable
* Add google maps directions/API integration

Backend:
* Document dependencies and environment needed to run `eventapi.py`
* Host API (preferably on Flask)
* Add other data fields (is event part of a series? are there any requirements/restrictions for the event?)
* Add Twilio API


