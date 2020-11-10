from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self,username,password=None,is_active=True,is_admin=False):
        
        # if not username:
        #     raise ValueError('Users must have a valid username')
        # if not password:
        #     raise ValueError('Users must have a valid password')

        user_obj = self.model()

        user_obj.set_password(password)
        user_obj.username = username
        user_obj.isAdmin = is_admin
        user_obj.isActive = is_active
        user_obj.save(using=self._db)
        return user_obj
    
    def create_superuser(self, username, password=None):

        user = self.create_user(
            username=username,
            password=password,
            is_active=True,
            is_admin=True
        )

        return user
