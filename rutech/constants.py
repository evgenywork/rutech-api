from django.utils.translation import gettext_lazy as _


BACKGROUND_CHOICES = (
    (1, _('Photo')),
    (2, _('Music')),
)

ROOM_TYPE_CHOICES = (
    (1, _('Common chat')),
    (2, _('Room chat')),
    (3, _('Individual chat')),
)

AVATAR_CHOICES = (
    (1, _('Аватар 1')),
    (2, _('Аватар 2')),
    (3, _('Аватар 3')),
)

NETWORKING_CHOICES = (
    (0, _('Ожидание второго пользователя')),
    (1, _('Общение')),
    (2, _('Коннект')),
    (3, _('Отказ')),
)