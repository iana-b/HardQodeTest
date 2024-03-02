from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Purchase, Group, GroupMembership, Product


@receiver(post_save, sender=Purchase)
def distribute_user_to_group(sender, instance, created, **kwargs):
    # if created:
    print(f"created {instance.product.name}, customer {instance.customer.username}")
    groups = Group.objects.filter(product=instance.product)

    group = None
    if groups.count() == 0:
        group = Group(product=instance.product, name=f'{instance.product.name} Group 1')
        group.save()
    else:
        for each in groups:
            users_in_group = GroupMembership.objects.filter(group=each)
            print(f'Users in group: {users_in_group.count()}')
            if users_in_group.count() < instance.product.max_users:
                group = each
                break
        if group is None:
            group = Group(product=instance.product, name=f'{instance.product.name} Group {groups.count() + 1}')
            group.save()
    print(f'count of groups {group.name}')
    print(f'Minimum {instance.product.min_users}, Maximum {instance.product.max_users}')
    group_membership = GroupMembership(group=group, user=instance.customer)
    group_membership.save()



