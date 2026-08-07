from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import Group

@receiver(post_save,sender=User)
def activation_mail(sender,instance,created,**kwargs):
    if created:
        token=default_token_generator.make_token(instance)
        url=f"{settings.FRONTEND_URL}/users/activate/{instance.id}/{token}"
        subject='Activate Your Account'
        message = (
    f"Hi {instance.first_name},\n\n"
    f"Please activate your account by clicking the link below:\n\n"
    f"{url}\n\n"
    f"Thank you."
)
        mail=[instance.email]
        try:
            send_mail(subject,message,settings.EMAIL_HOST_USER, mail)
        except Exception as e:
            print('Faild to send email')



@receiver(post_save,sender=User)
def assign_role(sender,instance,created,**kwargs):
    if created:
        group,created=Group.objects.get_or_create(name='User')
        instance.groups.add(group)
        instance.save()