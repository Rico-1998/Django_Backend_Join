from multiprocessing import managers
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Contact, Task, category, subtask

# in dem serializer wird festgelegt welche felder man aus dem entsprechenden model in seiner api haben möchte.
# mit der zeile model = User wird das entsprechende Model was man serialisieren möchte festgelegt. zum bsp könnte man auch schreiben model = todo


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'username', 'password']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = category
        fields = ['id', 'name', 'color']


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'phone', 'initial', 'color']


class SubtaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = subtask
        fields = ['id', 'description', 'checked']


class TaskSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=Contact.objects.all(), many=True)
    subtasks = serializers.PrimaryKeyRelatedField(
        queryset=subtask.objects.all(), many=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'category', 'urgency', 'status', 'created_Date', 'specificId', 'subtasks',
                  'assigned_to', 'due_date']
