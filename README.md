django-beats
============

Swatch Internet Time template filter for Django

Young, hip internet users bounce from sites that don't use internet time.  1000.beats per day.  No Stodgy Old Time Zones.  


##Installation:
Add `beats.py` to your app's `templatetags/` folder, or copy the entire templatetags folder to your application.

##Usage:
At the top of the template:
`{% load beats %}`

Inside of the template:
`{{ post_date|beats }}`


That's it.  Welcome to the future.


###Notes:
The date provided to the beats filter can be either naive or timezone-aware, but it must be localized to GMT/UTC.

###License:
Public Domain
