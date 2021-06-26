from django.utils.html import format_html


def get_url_of_related_fields(relationship_instance, field_name):
    """
    Returns links separated by commas, from many-to-many relationships.

    For use in Django Admins.
    Example:
        list_display = ['all_types']

        def all_types(self, obj):
            text = get_url_of_related_fields(
                relationship_instance=obj.types,
                field_name='name')
            return text

    :param relationship_instance: (class ManyRelatedManager) Many-to-many relationship
    :param field_name: (str) Field to display of the related model
    :return: (html) HTML text of the links
    """
    # get instance
    instance = relationship_instance.first()

    if instance:
        # get the names to create the url
        app_label = instance.__class__._meta.app_label
        model_name = instance.__class__._meta.model_name

        # create url
        url_admin = '{app_label}/{model_name}'.format(
            app_label=app_label,
            model_name=model_name)
        url_generic = '/admin/' + url_admin + '/{id}/change/'

        text = ''
        for counter, item in enumerate(relationship_instance.all()):
            url = url_generic.format(id=item.id)
            a_html = '<a href="{url}">{name}</a>'.format(
                url=url,
                name=getattr(item, field_name))
            if counter != 0:
                text = '{}, {}'.format(text, a_html)
            else:
                text = a_html

        return format_html(text)

    return None
