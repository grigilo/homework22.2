class TitleMixin(object):
    """
    Миксин для получения заголовка страницы.
    """

    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_title()

        return context
