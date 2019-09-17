from django.contrib import admin
from .models import Question , Choice

# Register your models here.

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3




class QustionAdmin(admin.ModelAdmin):
    fields = [(None, {'fields': ['question_text']}),
                  ('Date information', {'fields': ['pub_date'], 'classes': ['collaps']}),
             ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']

admin.site.register(Question, QustionAdmin)
# admin.site.register(Choice)