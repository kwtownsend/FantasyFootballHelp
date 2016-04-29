from django.core.mail import EmailMessage
from clubMembers.models import ClubMember
from django.core.urlresolvers import reverse


def send_email_notice(subject, message, recipient_user):
    """
    Email notifications done through this method will ALWAYS
    check if the user has chosen to get them.
    :param subject:
    :param message:
    :param recipient_user:
    :return:
    """
    member_info = ClubMember.objects.get(member=recipient_user)
    if  member_info.accepts_email and recipient_user.email != None:
        email = EmailMessage(subject, message, to=[recipient_user.email])
        email.send()
    else:
        print("user doesn't accept emails")


def compose_ask_message(asker_user, asked_thingy, owner_user, askobject):
        message_body = asker_user.username + " has asked to borrow your thingy '" + asked_thingy.shortDescription + "'.\n"
        message_body += "Click this link " + "http://magentabackpack.com/ask/forlend/" + str(askobject.pk) + " to view the request.\n\n"
        message_body += "You can accept the request by clicking here: http://magentabackpack.com/ask/forlend/accept/" + str(askobject.pk) + "\n"
        message_body += "or decline it here: http://magentabackpack.com/ask/forlend/decline/" + str(askobject.pk) + "\n"
        message_body += '\nYou can turn off future email notifications on the "My info" page '
        message_body += "at http://magentabackpack.com/members/" + str(owner_user.pk) + ".\n\n"
        # there is probably a better way to do this.
        return message_body



