from django.contrib import admin
from Players.models import Player
# from clubMembers.models import ClubMember, MemberRating

class PlayersAdmin(admin.ModelAdmin):
    # fields = ['shortDescription', 'owner', 'lendable']
    list_display = ('name', 'pos', 'fpts', 'fptsg', 'gp', 'pyds', 'ptd', 'ryd', 'rtd', 'recyds', 'rectd', 'fum', 'sack', 
    	'fr', 'intercept', 'td', 'sfty', 'fg', 'fgmiss', 'xpt')
    # list_filter = ['lendable', 'owner', 'thingy_type']
    # date_hierarchy = 'add_date'
    # fields = (('shortDescription', 'owner'), 'lendable')


admin.site.register(Player, PlayersAdmin)




# class ClubMemberAdmin(admin.ModelAdmin):
#     list_display = ('member', 'phone_number', 'pk')
#     # list_filter = ['User']


# class MemberRatingAdmin(admin.ModelAdmin):
#     list_display = ('target_member', 'rated_by', 'rating', 'rating_date', 'pk')


# admin.site.register(ClubMember, ClubMemberAdmin)

# admin.site.register(MemberRating, MemberRatingAdmin)
