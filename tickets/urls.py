from django.conf.urls import url

# Remember to include your view below
# example: from tickets.views.view_category import *
from tickets.views import *
from tickets.views.views import *
from tickets.views.ticket_details_view import *
# from tickets.views.view_search_tickets import *

app_name = "tickets"
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login$', login_user, name='login'),
    url(r'^logout$', user_logout, name='logout'),
    url(r'^register$', register, name='register'),
    url(r'^ticket_details/(?P<ticket_id>.+?)/$', ticket_details, name='ticket_details')
    # url(r'^search_tickets/$', search_tickets, name='search_tickets')    
    # url(r'^tickets$', list_tickets, name='list_tickets'),
    # url(r'^Mytickets$', my_tickets, name='my_tickets')
    # url(r'^sell$', sell_ticket, name='sell'),
    # url(r'^category_tickets/(?P<category_id>.+?)/$', list_category_tickets, name='category_tickets'),
    # url(r'^categories$', category_tickets, name='categories'),
    # url(r'^order$', view_order, name='order'),
    # url(r'^payment$', view_payments, name='payment'),
    # url(r'^confirmation$', confirm_order, name='confirmation'),
    # url(r'^profile$', profile, name='profile'),
    # url(r'^add_payment$', add_payment, name='add_payment'),
    # url(r'^profile/view_payments$', view_payments, name='profile/view_payments'),
    # url(r'^profile/edit_account$', edit_account, name="profile/edit_account"),
    # url(r'^order_history$', view_order_history, name="order_history"),
    # url(r'^order_history/(?P<order_id>.+?)/$', view_order_details, name="order_details"),
    # url(r'^profile/edit_account$', edit_account, name="profile/edit_account"),    
    # url(r'^recommend_ticket/(?P<ticket_id>.+?)/$', recommend_ticket, name='recommend_ticket')
]