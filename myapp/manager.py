from django.contrib.auth.models import BaseUserManager


class CustomManager(BaseUserManager):
          def create_user(self,phone,email,password, **extra_field):
                if not email:
                        raise ValueError("Give the proper email")
                
                if len(phone) != 11:
                        raise ValueError("Phone number must be 11 digits")
                
               
                email = self.normalize_email(email)
                user = self.model(email=email, phone=phone, **extra_field)
                user.set_password(password)
                user.save(using=self._db)
                return user

          def create_superuser(self,phone,email,password, **extra_field):
                extra_field.setdefault("is_staff",True)
                extra_field.setdefault("is_superuser",True)
                extra_field.setdefault("is_member",True)

                return self.create_user(phone,email,password, **extra_field)
                
               
                  



               
                  
