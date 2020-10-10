from django.db import models, transaction
from django.db.models import F, Max

class TaskManager(models.Manager):
    """ Magener to encapsulate bits of business logic """

    def move(self, obj, new_order, toDo):
        """ mode an objects to a new order position """
        print(obj, new_order, toDo)
        qs = self.get_queryset()
        print(qs)

        with transaction.atomic():

            if obj.toDo.pk != toDo.pk: # nesso caso não precisa alterar a ordem com base no ordem anterior, so colocar o novo valor e alterar o elementos seguintes
                print("entrou")
                qs.filter(
                        toDo=obj.toDo.pk, #Alterar essa logica, pq tenho que alterar o ToDo anterior para o novo
                        order__gt=obj.order,
                    ).exclude(
                        pk=obj.pk,
                        toDo=obj.toDo.pk
                    ).update(
                        order=F('order') - 1,
                    )
                print(qs)
                 
                qs.filter(
                        toDo=toDo, 
                        order__lt=new_order, 
                    ).exclude(
                        pk=obj.pk
                    ).update(
                        order=F('order') + 1,
                        toDo=toDo.pk,
                    )
                #continua aqui
                if obj.order > int(new_order):
                    qs.filter(
                        toDo=toDo.pk, 
                        order__gte=new_order, 
                    ).exclude(
                        pk=obj.pk
                    ).update(
                        order=F('order') + 1,
                    )
                    print('if 01: ',qs)
                else:
                    qs.filter(
                        toDo=toDo,
                        order__lte=new_order,
                        order__gt=obj.order,
                    ).exclude(
                        pk=obj.pk,
                    ).update(
                        toDo=toDo,
                        order=F('order') - 1,
                    )
                    print('if 02: ',qs)

            else:#ok aqui

                if obj.order > int(new_order):
                    qs.filter(
                        toDo=obj.toDo.pk,
                        order__lte=obj.order, 
                        order__gte=new_order, 
                    ).exclude(
                        pk=obj.pk
                    ).update(
                        order=F('order') + 1,
                    )
                else:
                    qs.filter(
                        toDo=obj.toDo.pk,
                        order__lte=new_order,
                        order__gt=obj.order,
                    ).exclude(
                        pk=obj.pk,
                    ).update(
                        order=F('order') - 1,
                    )
                    
            obj.order = new_order
            obj.toDo = toDo
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