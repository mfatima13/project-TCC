from django.db import models, transaction
from django.db.models import F, Max


class ToDoManager(models.Manager):

    def move(self, obj, new_order):
        qs = self.get_queryset()

        with transaction.atomic():
            if obj.order > int(new_order):

                qs.filter(
                    group=obj.group,
                    order__gte=obj.order,
                    # order__lt=new_order,
                ).exclude(
                    pk=obj.pk,
                ).update(
                    order=F('order') + 1,
                )
            else:
                qs.filter(
                    group=obj.group,
                    # order__lt=new_order,
                    order__gte=obj.order,
                ).exclude(
                    pk=obj.pk,
                ).update(
                    order=F('order') - 1,
                )

            obj.order = new_order
            obj.save()

    def create(self, **kwargs):
        instance = self.model(**kwargs)

        with transaction.atomic():
            # Get our current max order number
            results = self.filter(
                group=instance.group
            ).aggregate(
                Max('order')
            )

            # Increment and use it for our new object
            current_order = results['order__max']
            if current_order is None:
                current_order = 0

            value = current_order + 1
            instance.order = value
            instance.save()
            return instance


class TaskManager(models.Manager):
    """ Magener to encapsulate bits of business logic """

    def move(self, obj, new_order, toDo):
        """ mode an objects to a new order position """
        print(obj, new_order, toDo)
        qs = self.get_queryset()
        print(qs)

        with transaction.atomic():

            if obj.toDo.pk != toDo.pk:
                # é inserido o novo item, incrementando os demais
                print("entrou")
                qs.filter(
                    toDo=obj.toDo.pk,
                    order__gt=obj.order,
                ).exclude(
                    pk=obj.pk,
                ).update(
                    order=F('order') - 1,
                )
                print(qs)

                qs.filter(
                    toDo=toDo,
                    order__gte=new_order,
                ).exclude(
                    pk=obj.pk
                ).update(
                    order=F('order') + 1,
                )  # continuar testando

                # continua aqui
                """if obj.order > int(new_order):
                    qs.filter(
                        toDo=toDo, 
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
                    print('if 02: ',qs)"""

            else:

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
            if current_order is None:
                current_order = 0

            value = current_order + 1
            instance.order = value
            instance.save()
            return instance

    """def delete(self, **kwargs):
        instance = self.model(**kwargs)

        with transaction.atomic():
            # Get our current max order number
            self.filter(
                toDo=instance.toDo,
                order__gte=instance.order,
            ).exclude(
                pk=instance.pk
            ).update(
                order=F('order') - 1,
            )

            instance.delete()
            print()
            return {"instance deleted"}"""
