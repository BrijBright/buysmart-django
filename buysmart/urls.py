
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('store/', include('store.urls')),
    path('cart/', include('carts.urls')),
    path('accounts/', include('accounts.urls')),

    # ORDERS
    path('orders/', include('orders.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




# Customize Django admin interface
# admin.site.site_url = None
from django.utils.safestring import mark_safe

admin.site.site_header = mark_safe('<span style="color: #9B6BF2; font-size: 30px;">Buy</span><span style="font-size: 30px; line-height: 120%; font-family: \'Elephant\', serif; color: black;">Smart</span>')



