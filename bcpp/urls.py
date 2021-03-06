"""bcpp URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from edc_appointment.admin_site import edc_appointment_admin
from edc_base.views import LogoutView, LoginView

from plot.admin_site import plot_admin
from household.admin_site import household_admin
from member.admin_site import member_admin
# , bcpp_subject_ahs_t2_admin
from bcpp_subject.admin_site import bcpp_subject_admin
from edc_metadata.admin_site import edc_metadata_admin
from edc_registration.admin_site import edc_registration_admin

from .views import HomeView, AdministrationView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/', edc_appointment_admin.urls),
    url(r'^admin/', plot_admin.urls),
    url(r'^admin/', household_admin.urls),
    url(r'^admin/', member_admin.urls),
    url(r'^admin/', bcpp_subject_admin.urls),
    url(r'^admin/', edc_metadata_admin.urls),
    url(r'^admin/', edc_registration_admin.urls),
    # url(r'^admin/', bcpp_subject_ahs_t2_admin.urls),
    url(r'^admininistration/', AdministrationView.as_view(),
        name='administration_url'),
    url('plot/', include('plot.urls', namespace='plot')),
    url('household/', include('household.urls', namespace='household')),
    url('member/', include('member.urls', namespace='member')),
    url('enumeration/', include('enumeration.urls', namespace='enumeration')),
    url('subject/', include('bcpp_subject.urls', namespace='bcpp-subject')),
    url(r'^appointment/',
        include('edc_appointment.urls', namespace='edc-appointment')),
    url(r'^edc/', include('edc_base.urls', 'edc-base')),
    url(r'^edc_consent/', include('edc_consent.urls', 'edc-consent')),
    url(r'^edc_metadata/', include('edc_metadata.urls', 'edc-metadata')),
    url(r'^edc_registration/',
        include('edc_registration.urls', 'edc-registration')),
    url(r'^edc_visit_schedule/',
        include('edc_visit_schedule.urls', 'edc-visit-schedule')),
    url(r'^tz_detect/', include('tz_detect.urls')),
    url(r'login', LoginView.as_view(), name='login_url'),
    url(r'logout', LogoutView.as_view(
        pattern_name='login_url'), name='logout_url'),
    url(r'', HomeView.as_view(), name='home_url'),
]
