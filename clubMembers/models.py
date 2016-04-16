from django.db import models
from django.contrib.auth.models import User
from clubs.models import Club, MemberRequest
from django.core.validators import RegexValidator

"""
This model will provide additional custom fields to the built-in
User class that django provided.

We need to store at least a phone number.
"""


class ClubMember(models.Model):
    member = models.OneToOneField(User, primary_key=True)
    # phone = models.CharField(max_length=12)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_regex_us_easy = RegexValidator(regex=r'^\(\d{3}\)[ -]\d{3}[ -]\d{4}', message="Phone must be (###) 555 1212 or ### 555 1212; you can use dashes instead of spaces")
    phone_number = models.CharField(max_length=20, validators=[phone_regex_us_easy], blank=False) # validators should be a list
    zip_regex = RegexValidator(regex=r'^\d{5}$', message="5-digit Zip Code only")
    member_zip = models.CharField(max_length=5, validators=[zip_regex], blank=False)
    # we can add a photo or avatar image later
    # TODO: what additional info about members do we want?

    def create_member(self, phone_number, member, **extra_fields):
        return self._create_member(phone_number, member, **extra_fields)

    def requester_relationship(self, asking_member):
        """
        The asking_member will be the person him/herself,
        or will be in the same club,
        or will be in a club the person wants to join
        or will be world+dog member.
        Return a string of the relationship
        :param asking_member:
        :return:
        """
        if asking_member == self:
            # the person himself
            return "self_request"

        ask_user = asking_member.member
        self_user = self.member
        asker_clubs = Club.objects.filter(members=ask_user)
        self_clubs = Club.objects.filter(members=self_user)
        common_clubs = asker_clubs & self_clubs
        print("common clubs:")
        for c in common_clubs:
            print(c.name)
        if len(common_clubs) > 0:
            return "club_buddy"
        # TODO: look up all club requests, get a queryset of those clubs
        # compare to requester's clubs
        # c_reqs = Club.objects.filter(members__requester=self_user)
        # # club_requests = MemberRequest.objects.filter(requester=self_user)
        #
        # # requested_clubs = club_requests.all(self_clubs)
        # common_clubs = asker_clubs & c_reqs
        # print("request common clubs")
        # for c in common_clubs:
        #     print(c.name)
        # if len(common_clubs) > 0:
        #     return "prospective_club_buddy"
        return "world_dog"

    def get_prospective_buddy_info(self):
        info = {"username":self.member.username}
        return info







class MemberRating(models.Model):
    target_member = models.OneToOneField(User)
    rated_by = models.ForeignKey(User, related_name="member_related", null=False, blank=False)
    rating = models.PositiveSmallIntegerField()
    rating_date = models.DateField()

