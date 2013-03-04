from datetime import datetime

from django import template

register = template.Library()

@register.filter(name="beats")
def beats(value):
	"""
	Expects a UTC datetime, either naive or timezone-aware.  
	Outputs the date and the number of "beats" that have elapsed in the current day.
	"Mar 4: 725.beats"	
	"""
    date = datetime(value.year, value.month, value.day, tzinfo=value.tzinfo)
    beats = (value - date).total_seconds() / 86.4
    return "%s: %0.0f.beats" % (value.strftime('%b %d'), beats)
