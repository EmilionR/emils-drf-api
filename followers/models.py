from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model
    'owner' is the User that is following another.
    'followed' is the User that 'owner' follows.
    The related_name attribute helps django to distinguish
    between 'owner' and 'followed', as both are instances of User.
    'unique_together' makes sure a user can't follow the same user twice.
    """
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'