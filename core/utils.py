# coding: utf-8

from django.core.mail import EmailMessage


def send_email(csv_data):
    """
    :param csv_data: csv to be sent
    """
    message = EmailMessage('Nuevo pedido', 'Se adjunta pedido en csv.', 'destinatario@mail.com', ['emisor@mail.com'])
    message.attach('order.csv', csv_data.getvalue(), 'text/csv')
    message.send(fail_silently=False)
