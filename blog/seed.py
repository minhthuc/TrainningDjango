from post.models import Post, Author
from faker import Faker

faker = Faker()
posts = Post.objects.all()
for post in posts:
    post.pub_time = faker.date_time()
    post.save()
for _ in 10:
    Author.objects.create(name = faker.name(), dob = faker.date())
    ----------
from faker import Faker
from user.models import User,Role, Group
faker = Faker()
for x in range(10):
    User.objects.create(firstName=faker.name(),
                        lastName=faker.name(),
                        PassWord=faker.text(max_nb_chars = 100),
                        BirthDay = faker.date(),
                        Hobbies = faker.text(max_nb_chars = 100),
                        Description = faker.text(max_nb_chars = 100))
