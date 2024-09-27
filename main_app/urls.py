from django.urls import (path,
                         )
from django.views.generic import TemplateView

from .views import ApiView


urlpatterns = [
     path('',
          TemplateView.as_view(template_name = 'main_app/homepage.html'),
          name ='homepage'
          ),
     path('policy',
          TemplateView.as_view(template_name = 'main_app/policy.html'),
          name = 'policy',
          ),
     path('about',
          TemplateView.as_view(template_name = 'main_app/about.html',),
          name = 'about',
          ),
     path('discounts',
          TemplateView.as_view(template_name = 'main_app/discount.html'),
          name='discount',
          ),
     path('contacts',
          TemplateView.as_view(template_name = 'main_app/discount.html'),
          name = 'contacts',
          ),
     path('api',
          ApiView.as_view(),
          name = 'api',
          ),
]