from django.urls import (path,
                         include,
                         )
from .views import (Homepage,
                    Policy,
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
]