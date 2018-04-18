from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DetailsView

urlpatterns = {
    url(r'^(?P<base_currency>[a-zA-Z]{3})/(?P<target_currency>[a-zA-Z]{3})/$',
        DetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)