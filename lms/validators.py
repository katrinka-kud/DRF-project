from rest_framework.serializers import ValidationError


class LinkValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, link):
        link_youtube = "https://www.youtube.com/"

        if link.get("link_video"):
            if link_youtube in link.get("link_video"):
                raise ValidationError(
                    "Ссылка на сторонние ресурсы запрещена, кроме youtube.com"
                )
        else:
            return None
