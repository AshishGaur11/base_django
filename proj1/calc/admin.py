from django.contrib import admin

from .models import Question, Choice

#user name is admin
#user password 123456789

# admin.site.register(Question)
admin.site.register(Choice)

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question, QuestionAdmin)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3