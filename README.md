# directory
A Sachacks food resources project

The project consists of several directories.

<b>Template</b>
Contains front end angular/html files

<b>Static</b>
Contains resources such as JS, CSS, etc.

<b>Eventapi.py</b>
is a small python script that accepts JSON (exported from this [google doc](https://docs.google.com/spreadsheets/d/1JwAlUxOp9ixiEl-AwyPmRLRFgGUR7I1qWzLog2rCydo/edit?usp=sharing)) and returns json to directory.json with the next event time provisioned in a JSON readable format.

<b>TODO:</b>
Frontend:
* Pagination of events
* More sort/filtering
* Adjust language to be more understandable
* Add google maps directions/API integration

Backend:
* Host API (preferably on Flask)
* Add other data fields (is event part of a series? are there any requirements/restrictions for the event?)
* Add Twilio API
