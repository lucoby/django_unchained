from django.contrib import admin

from madeit.models import Thread, Comment

# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('thread_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None,               {'fields': ['thread_title', 'thread_text', 'votes']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [CommentInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Thread, ThreadAdmin)