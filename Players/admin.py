from django.contrib import admin
from clubMembers.models import ClubMember, MemberRating



class ClubMemberAdmin(admin.ModelAdmin):
    list_display = ('member', 'phone_number', 'pk')
    # list_filter = ['User']


class MemberRatingAdmin(admin.ModelAdmin):
    list_display = ('target_member', 'rated_by', 'rating', 'rating_date', 'pk')


admin.site.register(ClubMember, ClubMemberAdmin)

admin.site.register(MemberRating, MemberRatingAdmin)
