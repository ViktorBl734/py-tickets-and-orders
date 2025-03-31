from datetime import datetime

from django.db import transaction
from django.db.models import QuerySet

from db.models import User, Ticket, Order
from tests.test_main import users_data


def create_order(tickets: list, username: str, date: str = None) -> None:
    with transaction.atomic():
        user_ = User.objects.get(username=username)
        order = Order(user=user_)
        if date:
            order.created_at = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        order.save()
        for ticket in tickets:
            Ticket.objects.create(order=order, movie_session = ticket['movie_session'],
                                  row=ticket['row'], seat = ticket['seat'])


def get_orders(username: str = None) -> QuerySet:
    orders = Order.objects.all()
    orders.filter(user__username=username)
    return orders
