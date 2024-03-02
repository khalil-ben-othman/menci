from django.core.mail import send_mail, mail_admins
from django.template.loader import render_to_string
from backend.models import Order
from django.conf import settings


def send_email_with_order(order_id):
    order = Order.objects.get(id=order_id)
    client = order.client
    items = order.items.all()

    client_subject = 'Your Bag Validation'
    admin_subject = 'New Order'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [client.email]
    admins = ['khalilbenothman4444@gmail.com', 'maherlamraoui00@gmail.com', 'malekbenslama00@gmail.com']

    # Create the context for the email template
    context = {
        'client': client,
        'items': items,
        'total': order.total, 
    }

    # Render the email template
    client_email_content = render_to_string('email_templates/bag_validation_email.html', context)
    admins_email_content = render_to_string('email_templates/new_order_email.html', context)
    # Send the email
    send_mail(client_subject, client_email_content, from_email, recipient_list, html_message=client_email_content, fail_silently=False)
    send_mail(admin_subject, admins_email_content, from_email, admins, html_message=admins_email_content, fail_silently=False)
 
