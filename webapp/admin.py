from django.contrib import admin
from .Entities.Users import Users
from .Entities.Children import Children
from .Entities.RewardTasks import RewardTasks
from .Entities.Transactions import Transactions
from .Entities.Schools import Schools

# Register your models here.
admin.site.register(Users)
admin.site.register(Children)
admin.site.register(RewardTasks)
admin.site.register(Transactions)
admin.site.register(Schools)