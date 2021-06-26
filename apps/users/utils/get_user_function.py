from django.contrib.auth.models import User


def get_user(user_id=None, user=None):
    """
    :param user_id: (int)
    :param user: (instance)
    :return: (instance)
    """
    if user_id:
        user = User.objects.get(id=user_id)

    try:
        user = user.freelance
        return user
    except Exception as ex:
        pass

    return user
