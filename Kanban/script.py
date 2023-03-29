from django.shortcuts import render
from django.contrib.auth.models import User


def check_for_user(request):
    if request.method == 'POST' and not User.objects.filter(
            username=request.POST.get('userName')).exists():
        return True
    else:
        print('user already exists')


def check_for_mail(request):
    if request.method == 'POST' and not User.objects.filter(
            email=request.POST.get('email')).exists():
        return True
    else:
        print('email already exists')


# class TaskViewset(viewsets.ModelViewSet):
#     authentication_classes = [TokenAuthentication]
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
    # def create(self, request):
    #     category_json = json.loads(request.data.get('category'))
    #     selected_category = category.objects.get(
    #         id=category_json['id'])
    #     if request.method == 'POST':
    #         # gleich löschen
    #         task = Task.objects.create(title=request.POST.get('title', ''),
    #                                    description=request.POST.get(
    #             'description', ''),
    #             due_date=datetime.strptime(request.POST.get(
    #                 'due_date', ''), '%Y-%m-%d').date(),
    #             category=selected_category,
    #             status=request.POST.get('status', ''),
    #             created_Date=request.POST.get('createdDate', ''),
    #             specificId=request.POST.get('specificId', ''),
    #             urgency=request.POST.get('prio', ''))

    #         assigned_to = request.data.get('assigned_to')[
    #             1: -1].replace(',', ' ')
    #         assigned_to_ids = [int(id) for id in assigned_to.split()]
    #     assigned_to_users = []
    #     for nr in assigned_to_ids:
    #         assigned_to_user = Contact.objects.get(id=nr)
    #         assigned_to_users.append(assigned_to_user)
    #     task.assigned_to.set(assigned_to_users)
    #     task.save()
    #     serialized_obj = serializers.serialize('json', [task, ])

    #     return HttpResponse({'test': 'test'})
