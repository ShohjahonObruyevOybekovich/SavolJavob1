from .models import Question, Result, Answer, Category
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

    def questuon_count(self,obj):
        return obj.questuon_count.count()
    questuon_count.short_description = ''

class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = ['name', 'is_correct']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['name', 'category']
    list_display = ['name', 'category', ]
    search_fields = ['name','category__name']
    list_filter = ['category__name', 'name']
    inlines = [AnswerInlineModel]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_correct', 'question']

@admin.action(description='return to null')
def return_null(modeladmin, request, queryset):
    queryset.update(score=0)

class ResultAdmin(ImportExportModelAdmin):
    search_fields = ['user__phone', 'score']
    list_display = ['user','category', 'total_question', 'total_correct', 'score','is_passed']
    actions = [return_null]
admin.site.register(Result, ResultAdmin)
