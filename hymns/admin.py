from django.contrib import admin
from .models import Hymn, Verse, Line


class LineInline(admin.StackedInline): #O StackedInline si prefieres una representación vertical
  model = Line
  extra = 1 # Número de líneas adicionales a mostrar por defecto


class VerseInline(admin.StackedInline):
  model = Verse
  inlines = [LineInline]
  extra = 1

@admin.register(Hymn)
class HymnAdmin(admin.ModelAdmin):
  inlines = [VerseInline]
  list_display = ('name', 'author', 'year', 'favorite')
  search_fields = ('name', 'author')
  list_filter = ('favorite',) # Filtro por el campo 'favorite'


@admin.register(Verse)
class VerseInline(admin.ModelAdmin):
  inlines = [LineInline]
  extra = 1

admin.site.register(Line) #Para este caso no se hace necesario personalizarlo