from didyouknow.posts.models import User
from didyouknow.posts.models import Post
from didyouknow.posts.models import Comment
from django.contrib import admin


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class UserAdmin(admin.ModelAdmin):
    fieldsets = [ ( 'Username', {'fields' : ['username']} ),
                  ( 'Password', {'fields' : ['password']}),
                  ( 'Registered in', {'fields' : ['registered_date']}),
                  ( 'Email', {'fields' : ['email']}),
                  ( 'Bio', {'fields' : ['biography']})
     ]
    #display list
    list_display = ['username','email', 'biography', 'registered_date']

class PostAdmin(admin.ModelAdmin):
    fieldsets = [ ('Did You Know?', {'fields' : ['post']}),
                  ('Published', {'fields' : ['pub_date']}),
                  ('User Publish', {'fields' : ['user']}),
    ]
    #Tabular Inline For Comment
    inlines = [CommentInline]

    #display list
    list_display = ['post', 'pub_date', 'user']





#put user model in admin page
admin.site.register(User, UserAdmin)
#put post model in admin page
admin.site.register(Post, PostAdmin)
#put comment model in admin page
admin.site.register(Comment)
