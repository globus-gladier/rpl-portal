from django.urls import path, include


urlpatterns = [
    # Include any custom URLs for this portal.
    path("", include("rpl_portal.urls")),
    # Provides the basic search portal
    path("", include("globus_portal_framework.urls")),
    # Provides Login urls for Globus Auth
    path("", include("social_django.urls", namespace="social")),
]
