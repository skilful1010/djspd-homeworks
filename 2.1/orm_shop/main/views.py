from django.http import Http404
from django.shortcuts import render

from main.models import Car, Sale, Client


def cars_list_view(request):
    # получите список авто
    template_name = 'main/list.html'
    cars = {'car': {'image': Car.image,
                    'model': Car.model,
                    'price': Car.price,
                    'volume': Car.volume,
                    'fuel_type': Car.fuel_type,
                    'year': Car.year,
                    'gearbox': Car.gearbox}
            }

    return render(request, template_name, {'list': cars})  # передайте необходимый контекст


def car_details_view(request, car_id):
    # try:
    #     template_name = 'main/details.html'
    #     details = {
    #         }
    #     return render(request, template_name, {'details': details})  # передайте необходимый контекст
    # except Car.DoesNotExist:
    #     raise Http404('Car not found')
    pass

def sales_by_car(request, car_id):
    try:
        # получите авто и его продажи
        template_name = 'main/sales.html'
        number = int(car_id) - 1
        id_client = Sale.objects.all()[number].client_id
        buyer = Client.objects.get(id=id_client)
        sales = {'client': {
            'last_name': buyer.last_name,
            'name': buyer.name,
            'middle_name': buyer.middle_name,
            'phone_number': buyer.phone_number,
        },
            'created_at': Sale.objects.all()[number].created_at
        }
        return render(request, template_name, {'sales': sales})  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
