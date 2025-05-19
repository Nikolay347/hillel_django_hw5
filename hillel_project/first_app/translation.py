from modeltranslation.translator import TranslationOptions, register

from first_app.models import Position


@register(Position)
class PositionTranslationOption(TranslationOptions):
    fields = ("title", "description")


