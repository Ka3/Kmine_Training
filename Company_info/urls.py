from django.conf.urls import patterns, include, url

app_name = 'Company_info'

import views


urlpatterns = [
               #url(r'add_company', views.Add_Company_View.as_view(), name='add_company'),
               url(r'add_company/$', views.add_Company, name='add_company'),
               #url(r'list_companies', views.List_Companies.as_view(), name='List_company'),
               #url(r'view_company/(?P<pk>[-\w]+)/$', views.View_Company.as_view(), name='view_company')

               ]
                              
#url(r'add_company/$', views.add_Company, name='add_company'),
#
#url(r'view_company/(?P<pk>[-\w]+)/$', views.view_Company, name='view_company'),
               
               
#url(r'^$', login_required(views.Landing), name='landing'),
#url(r'^$', login_required(views.Landing), name='landing'),
#url(r'^$', login_required(views.Landing), name='landing'),
'''
,
'''
'''

url(r'list_companies/$', views.list_Companies, name='List_company'),
url(r'view_company/(?P<pk>[-\w]+)/$', views.view_Company, name='view_company'),
''
#test
'''
'''
dfasdfljwe
kwellwre
'''
