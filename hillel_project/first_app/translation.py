from modeltranslation.translator import TranslationOptions, register

from first_app.models import Position
from first_app.models import Department

@register(Position)
class PositionTranslationOption(TranslationOptions):
    fields = ("title", "description",)

@register(Department)
class DepartmentTranslationOption(TranslationOptions):
    fields = ("name",)
