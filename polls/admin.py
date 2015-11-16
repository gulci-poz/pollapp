from django.contrib import admin
from .models import Question, Choice

#admin.StackedInline
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']

    #podział na zbiory pól
    #pierwszy element krotki to nagłówek
    #django udostępnia klasy HTML
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    inlines = [ChoiceInLine]

    list_display = ('question_text', 'pub_date', 'was_published_recently')

    list_filter = ['pub_date']

    search_fields = ['question_text']

    #inne opcje:
    #list_per_page
    #date_hierarchy

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)
#admin.site.register(Question)
