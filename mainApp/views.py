from django.shortcuts import redirect, render
from . import models
# Create your views here.




def indexPage(request):

    return render(request,'index.html',{
        "testimonials":models.Testimonial.objects.all()
    })


def AllServices(request):

    all_services = models.Service.objects.all()
    return render( request,'AllServices.html',{
        'all_services':all_services
        
    })


def serviesCategory(request,serviceID=None):
    if not  models.ServiceCategory.objects.filter(id=serviceID):
        return redirect('our-services') 

    all_services_under_selected_category= models.ServiceCategory.objects.all()
    return render(request,'AllServicesUnderACategory.html',{
        'categories':all_services_under_selected_category
    })

def SeriviceDetail(request,serviceID=None):
    "this is will show the detail page  of the servie u want to Request for"
    if not  models.ServiceCategory.objects.filter(id=serviceID):
        return redirect('our-services') 
    if request.method =='POST':
        "THEN collect all the data for the user and create a bookinh"
        serviceCategoryDetail = models.ServiceCategory.objects.get(id=serviceID)
        addOnList = request.POST.getlist('addOn')
        date = request.POST['date']
        time = request.POST['time']
        name = request.POST['name']
        phone = request.POST['phone']

        addOnNames =""
        total_amount =0
  
        # print(type(addOnList))
        # print(list(addOnList))
        for DataBaseAddOns in models.ServiceCategoryAddOns.objects.all():
        
            if str(DataBaseAddOns.id )in addOnList:
                total_amount+= DataBaseAddOns.amount
                addOnNames += f'\n\n {DataBaseAddOns.name},' 


        total_amount+=serviceCategoryDetail.amount

        booking = models.Bookings.objects.create(
            name=name,
            phone_number=phone,
            Total_amount_of_order=total_amount,
            service_category=serviceCategoryDetail,
            selected_addOns=addOnNames,)
        booking.save()
        print(addOnNames)
    else:
        "this means is just a get request so we just render a template"
        serviceCategoryDetail = models.ServiceCategory.objects.get(id=serviceID)
        serviceAddOns = models.ServiceCategoryAddOns.objects.filter(service_category=serviceCategoryDetail)
        return render(request,'SeriviceDetail.html',{
            'serviceDetail':serviceCategoryDetail,
            # this is a list of all addons Associated to One Service Category
            "addOnsList":serviceAddOns
        })