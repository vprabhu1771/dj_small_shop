from django.shortcuts import render
from io import BytesIO

from django.http import HttpResponse

from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

from backend.models import Order, OrderItem


# Create your views here.

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

class ViewPDF(View):
    def get(self, request, *args, **kwargs):

        order_id = self.kwargs.get('order_id')
        # print(roll_id)

        order = Order.objects.filter(id=order_id).first()
        # Fetch all order items for the given order
        order_items = OrderItem.objects.filter(order_id=order_id)

        if order:
            data = {
                'order': order,
                'order_items': order_items
            }
        pdf = render_to_pdf('backend/pdf/invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')