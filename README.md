django-beats
============

Swatch Internet Time template filter for Django

Young, hip internet users bounce from sites that don't use internet time.  1000.beats per day.  No Stodgy Old Time Zones.  

Turn your legacy times into times that will give your site a legacy:

**Jan 4, 1:33 p.m.**   *Lame!!*

**Jan 4: 856.beats**   *Awesome!!*


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
