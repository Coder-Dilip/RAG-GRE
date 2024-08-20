from django.contrib import admin
from .models import UserVocabulary

class UserVocabularyAdmin(admin.ModelAdmin):
    list_display = ('user', 'vocab_preview')
    search_fields = ('user__username', 'vocab')
    
    def vocab_preview(self, obj):
        return f"{obj.vocab[:50]}..."
    vocab_preview.short_description = 'Vocabulary Preview'

admin.site.register(UserVocabulary, UserVocabularyAdmin)
