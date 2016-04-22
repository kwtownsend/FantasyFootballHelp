from django.contrib import admin
from webapp.models import nflstats
# from clubMembers.models import ClubMember, MemberRating

class nflstatsAdmin(admin.ModelAdmin):
    # fields = ['shortDescription', 'owner', 'lendable']
    list_display = ('name', 'pos', 'fpts', 'fptsg', 'gp', 'pyds', 'ptd', 'ryd', 'rtd', 'recyds', 'rectd', 'fum', 'sack', 
    	'fr', 'intercept', 'td', 'sfty', 'fg', 'fgmiss', 'xpt')
    # list_filter = ['lendable', 'owner', 'thingy_type']
    # date_hierarchy = 'add_date'
    # fields = (('shortDescription', 'owner'), 'lendable')


admin.site.register(nflstats, nflstatsAdmin)


# Register your models here.
