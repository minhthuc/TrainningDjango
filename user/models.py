from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    PassWord = models.CharField(max_length=100)
    BirthDay = models.DateField()
    FullName = models.CharField(max_length=100, blank=True)
    Hobbies = models.CharField(max_length=100)
    Description = models.TextField()

    def save(self, *args, **kwargs):
        self.FullName = self.firstName + " " + self.lastName
        super().save(*args, **kwargs)

    def __str__(self):
        return self.FullName

class Group(models.Model):
    CHOICE = (
        (1, 'ADD'),
        (2, 'EDIT'),
        (3, 'DELETE'),
    )
    Name = models.CharField(max_length=100)
    Permission = models.IntegerField(max_length=1, choices=CHOICE)
    Description = models.TextField()
    user = models.ManyToManyField(User, through="UserGroup")

    def __str__(self):
        return self.Name

class Role(models.Model):
    Name = models.CharField(max_length=100)
    CHOICE = (
        (1, 'ADMIN'),
        (2, 'PUBLISHER'),
        (3, 'APPROVER'),
        (4, 'MODERATOR'),
        (5, 'EDITOR'),
        (6, 'CREATOR'),
    )
    Permission = models.IntegerField(max_length=1, choices=CHOICE)
    Description = models.TextField()
    user = models.ManyToManyField(User, through="UserRole")

    def __str__(self):
        return self.Name


class UserGroup(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    groupID = models.ForeignKey(Group, on_delete=models.CASCADE)

class UserRole(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    roleID = models.ForeignKey(Role, on_delete=models.CASCADE)
