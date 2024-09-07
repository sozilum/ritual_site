from django.urls import (path,
                         )
from .views import (Homepage,
                    Policy,
                    About,
                    Discounts,
                    Contacts,
                    Personal_data,
                    )


urlpatterns = [
    path('',
         Homepage.as_view(),
         name ='homepage'
         ),
    path('policy',
         Policy.as_view(),
         name = 'policy',
         ),
    path('about',
         About.as_view(),
         name = 'about',
         ),
    path('discounts',
         Discounts.as_view(),
         name='discount',
         ),
    path('contacts',
         Contacts.as_view(),
         name = 'contacts',
         ),
]