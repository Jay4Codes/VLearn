from django.urls import path,include
from .views import *

urlpatterns = [
	path('csvinput/',csvfileinfo.as_view(),name='csvfileimport'),
	path('columns/',columndata.as_view(),name='columns'),
	path('codetoenglish',codetoenglish.as_view(),name='codetoenglish'),
	path('Top25Fundedcompanybargraphapi/',Top25Fundedcompanybargraphapi.as_view()),
    path('statefundedcompanycountPIE/',statefundedcompanycountPIE.as_view()),
    path('companycountpermonthBARAPI/',companycountpermonthBARAPI.as_view()),
    path('monthwisefundingPIE/',monthwisefundingPIE.as_view()),
    path('stagesectormixPIE/',stagesectormixPIE.as_view()),
    path('Fundingperregionbargraphapi/',Fundingperregionbargraphapi.as_view())


]