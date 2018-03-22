from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.db.models import Q


from billing.models import BillingProfile
from .models import Order

class OrderListView(LoginRequiredMixin, ListView):

    def get_queryset(self):
        return Order.objects.by_request(self.request).not_created()

class ReferredOrderListView(LoginRequiredMixin, ListView):

    template_name = 'orders/referred-order-list.html'

    def get_queryset(self):

        user = self.request.user

        buyers_billing_profiles = []

        for buyer in user.buyers.all():
            buyer_billing_profile = BillingProfile.objects.all().filter(email=buyer.email).first()
            buyers_billing_profiles.append(buyer_billing_profile)

        return Order.objects.filter(billing_profile__in=buyers_billing_profiles)

    # model = Order

    # def get_queryset(self):
    #     user = self.request.user

    #     orders_list = []
    #     for buyer in user.buyers.all():
    #         print(buyer.email)
    #         buyer_billing_profile = BillingProfile.objects.all().filter(email=buyer.email)
    #         buyer_orders = Order.objects.all().filter(billing_profile=buyer_billing_profile)
    #         #print(buyer_orders)

    #         for order in buyer_orders:
    #             orders_list.append(order)


    #         print("end of user")

    #     print(orders_list)
    #     return orders_list

    # def get_context_data(self, **kwargs):
    #     context = super(ReferredOrderListView, self).get_context_data(**kwargs)

    #     user = self.request.user

    #     orders = []

    #     for buyer in user.buyers.all():
    #         print(buyer.email)
    #         buyer_billing_profile = BillingProfile.objects.all().filter(email=buyer.email).first()

    #         buyer_orders = Order.objects.all().filter(billing_profile=buyer_billing_profile)
    #         #print(buyer_orders)

    #         for order in buyer_orders:
    #             orders.append(order)


    #         print("end of user")

    #     context['orders'] = orders

    #     return context




class OrderDetailView(LoginRequiredMixin, DetailView):

    def get_object(self):
        #defaults:
        #return Order.objects.get(id=self.kwargs.get('id'))
        #return Order.objects.get(slug=self.kwargs.get('slug'))
        qs = Order.objects.by_request(
                self.request
            ).filter(
                order_id = self.kwargs.get('order_id')
            )

        if qs.count() == 1:
            return qs.first()
        raise Http404


