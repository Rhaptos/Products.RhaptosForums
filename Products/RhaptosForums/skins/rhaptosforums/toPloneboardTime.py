## Script (Python) "toPloneboardTime"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=time=None
##title=
##
#given a time string convert it into a DateTime and then format it appropariately
from DateTime import DateTime
ploneboard_time=None
ts = context.translation_service
utranslate = context.utranslate

format = '%Y;%m;%d;%w;%H;%M;%S'

# fallback formats, english
# young_format_en = '%A %H:%M' 
# old_format_en = '%B %d. %Y'
rhaptos_format = '%Y-%m-%d %I:%M%p'


if not time:
    return 'Unknown date'

try:
    if not isinstance(time, DateTime):
        time = DateTime(str(time))
 
    ploneboard_time = time.strftime(rhaptos_format).lower()

except IndexError:
    pass 

return ploneboard_time
