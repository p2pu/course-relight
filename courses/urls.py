from django.conf.urls import url

from courses import views

urlpatterns = [
    url(r'^create/$', views.create_course,
        name='courses_create'),

    url(r'^import_project/(?P<project_slug>[\w-]+)/$',
        views.import_project,
        name='courses_import_project'),

    url(r'^(?P<course_id>[\d]+)/clone/$',
        views.clone_course,
        name='courses_clone'),

    url(r'^(?P<course_id>[\d]+)/$',
        views.course_slug_redirect,
        name='courses_slug_redirect'),

    url(r'^(?P<course_id>[\d]+)/learn_api_data/$',
        views.course_learn_api_data,
        name='courses_learn_api_data'),

    url(r'^(?P<course_id>[\d]+)/admin_content/$',
        views.course_admin_content,
        name='courses_admin_content'),

    url(r'^(?P<course_id>[\d]+)/discussion/$',
        views.course_discussion,
        name='courses_discussion'),

    url(r'^(?P<course_id>[\d]+)/people/$',
        views.course_people,
        name='courses_people'),

    url(r'^(?P<course_id>[\d]+)/settings/$',
        views.course_settings,
        name='courses_settings'),

    url(r'^(?P<course_id>[\d]+)/announcement/$',
        views.course_announcement,
        name='courses_announcement'),

    url(r'^(?P<course_id>[\d]+)/export_emails/$',
        views.course_export_emails,
        name='courses_export_emails'),

    url(r'^(?P<course_id>[\d]+)/badges/$',
        views.course_add_badge,
        name='course_add_badge'),

    url(r'^(?P<course_id>[\d]+)/signup/$',
        views.course_signup,
        name='courses_signup'),

    url(r'^(?P<course_id>[\d]+)/delete_spam/$',
        views.delete_spam,
        name='courses_delete_spam'),

    url(r'^(?P<course_id>[\d]+)/upload_image/$',
        views.course_image,
        name='courses_image'),

    url(r'^(?P<course_id>[\d]+)/add_user/$',
        views.course_add_user,
        name='courses_add_user'),

    url(r'^(?P<course_id>[\d]+)/change_status/$',
        views.course_change_status,
        name='courses_change_status'),

    url(r'^(?P<course_id>[\d]+)/change_signup/$',
        views.course_change_signup,
        name='courses_change_signup'),

    url(r'^(?P<course_id>[\d]+)/change_term/(?P<term>fixed|rolling)/$',
        views.course_change_term,
        name='courses_change_term'),

    url(r'^(?P<course_id>[\d]+)/update/(?P<attribute>[\w_]+)/$',
        views.course_update_attribute,
        name='courses_update_attribute'),

    url(r'^(?P<course_id>[\d]+)/update_tags/$',
        views.course_update_tags,
        name='courses_update_tags'),

    url(r'^(?P<course_id>[\d]+)/update_metadata/$',
        views.course_update_metadata,
        name='courses_update_metadata'),

    url(r'^(?P<course_id>[\d]+)/(?P<slug>[\w-]+)/$',
        views.show_course,
        name='courses_show'),

    url(r'^(?P<course_id>[\d]+)/remove_user/(?P<username>[\w\-\. ]+)/$',
        views.course_leave,
        name='courses_leave'),

    url(r'^(?P<course_id>[\d]+)/add_organizer/(?P<username>[\w\-\. ]+)/$',
        views.course_add_organizer,
        name='courses_add_organizer'),

    url(r'^(?P<course_id>[\d]+)/content/create/$',
        views.create_content,
        name='courses_create_content'),

    url(r'content/preview/$',
        views.preview_content,
        name='courses_preview_content'),

    url(r'^(?P<course_id>[\d]+)/content/(?P<content_id>[\d]+)/$',
        views.show_content,
        name='courses_content_show'),
    
    url(r'^(?P<course_id>[\d]+)/content/(?P<content_id>[\d]+)/edit/$',
        views.edit_content,
        name='courses_content_edit'),

    url(r'^(?P<course_id>[\d]+)/content/(?P<content_id>[\d]+)/remove/$',
        views.remove_content,
        name='courses_content_remove'),

    url(r'^(?P<course_id>[\d]+)/content/(?P<content_id>[\d]+)/up/$',
        views.move_content_up,
        name='courses_content_up'),

    url(r'^(?P<course_id>[\d]+)/content/(?P<content_id>[\d]+)/down/$',
        views.move_content_down,
        name='courses_content_down'),
]
