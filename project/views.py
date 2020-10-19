from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import ToDo, Task
from .serializers import TaskSerializer, ToDoSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('order')
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('toDo', )
    # permission_classes = []

    # @action(methods=['delete'], detail=True)#url_path='change-password', url_name='change_password'
    """def destroy(self, request, pk):
		task = Task.objects.delete(pk)
		
    	return Response({"ok":""}, status=status.HTTP_202_ACCEPTED)	"""

    @action(methods=['post'], detail=True)
    def move(self, request, pk):
        """ Move a single Step to a new position """
        obj = self.get_object()
        # params = request.data
        new_order = request.data.get('order', None)
        toDo_target = request.data.get('toDo', None)

        toDo = ToDo.objects.filter(pk=toDo_target).get()
        # Make sure we received an order
        if new_order is None and toDo is None:
            return Response(
                data={'error': 'No order or toDo given'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Make sure our new order is not below one
        if int(new_order) < 1:
            return Response(
                data={'error': 'Order nd toDo cannot be zero or below'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        Task.objects.move(obj, new_order, toDo)
        return Response({'success': True, 'order': new_order})


# Create order in toDo
class TodoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    filter_backends = (DjangoFilterBackend, )

    filter_fields = ('group', )
