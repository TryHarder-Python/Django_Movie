from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Вы подписались на рассылку',
        'Мы будем присылать вам фильмы',
        'django2322@gmail.com',
        [user_email],
        fail_silently=False,
    )