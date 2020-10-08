from django.db import models, transaction
from django.db.models import F, Max

class TaskManager(models.Manager):
    """ Magener to encapsulate bits of business logic """

    def move(self, obj, new_order, toDo):
        """ mode an objects to a new order position """
        print(obj, new_order, toDo)
        qs = self.get_queryset()

        with transaction.atomic():

            if obj.toDo.pk != toDo:
                qs.filter(
                        toDo=obj.toDo.pk,
                        order__lt=obj.order, 
                        order__gte=new_order, 
                    ).exclude(
                        pk=obj.pk
                    ).update(
                        order=F('order') - 1,
                    )
                
                if obj.order > int(new_order):
                    qs.filter(
                        toDo=toDo,
                        order__lt=obj.order, 
                        order__gte=new_order, 
                    ).exclude(
                        pk=obj.pk
                    ).update(
                        order=F('order') + 1,
                    )
                else:
                    qs.filter(
                        toDo=toDo,
                        order__lte=new_order,
                        order__gt=obj.order,
                    ).exclude(
                        pk=obj.pk,
                    ).update(
                        order=F('order') - 1,
                    )

            else:

                if obj.order > int(new_order):
                    qs.filter(
                        toDo=toDo,
                        order__lte=obj.order, 
                        order__gt=new_order, 
                    ).exclude(
                        pk=obj.pk
                    ).update(
                        order=F('order') + 1,
                    )
                else:
                    qs.filter(
                        toDo=toDo,
                        order__lte=new_order,
                        order__gt=obj.order,
                    ).exclude(
                        pk=obj.pk,
                    ).update(
                        order=F('order') - 1,
                    )

            obj.order = new_order
            obj.toDo.pk = toDo
            obj.save()

    def create(self, **kwargs):
        instance = self.model(**kwargs)

        with transaction.atomic():
            # Get our current max order number 
            results = self.filter( 
                toDo=instance.toDo 
            ).aggregate( 
                Max('order') 
            ) 

            # Increment and use it for our new object 
            current_order = results['order__max']
            print('\nhere \n', current_order)
            if current_order is None: 
                current_order = 0

            value = current_order + 1 
            instance.order = value 
            instance.save() 
            return instance