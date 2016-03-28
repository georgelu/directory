# directory
A Sachacks food resources project

_Demo:_ open [the index file](templates/angularindex.html) in a browser.

The project consists of several directories.

*templates*
Contains front end angular/html files

*static*
Contains resources such as JS, CSS, etc.

*eventapi.py*
is a small python script that accepts JSON (exported from this [google doc](https://docs.google.com/spreadsheets/d/1JwAlUxOp9ixiEl-AwyPmRLRFgGUR7I1qWzLog2rCydo/edit?usp=sharing)) and returns json to directory.json with the next event time provisioned in a JSON readable format.

*TODO:*

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
