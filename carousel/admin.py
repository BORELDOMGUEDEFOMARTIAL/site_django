from django.contrib import admin


from .models import Carousel,Article_eglise,Article_paroissiale

admin.site.register(Carousel)
admin.site.register(Article_eglise)
admin.site.register(Article_paroissiale)