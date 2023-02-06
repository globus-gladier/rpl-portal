from django.urls import path
from globus_portal_framework.urls import register_custom_index
from rpl_portal.views import RPLSearchView, example_view

app_name = "rpl-index"

register_custom_index("rpl_index", ["rpl"])

urlpatterns = [
    path("<rpl_index:index>/", RPLSearchView.as_view(), name="search"),
    # path('<rpl_index:index>/example/', example_view, name='my-cool-example-named-view'),
]
