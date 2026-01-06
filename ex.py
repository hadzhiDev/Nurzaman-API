# SELECT * FROM users WHERE age > 18 AND age < 30;


from accounts.models import User

User.objects.filter(age__range=[18, 30]) # -> SELECT * FROM users WHERE age > 18 AND age < 30;