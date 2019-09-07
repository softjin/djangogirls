from django.db import models
from django.utils import timezone

# 클래스 이름은 대문자로 시작하는 것이 좋다!
# 장고모델에서 파생되는 객체이다!
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

# 메서드는 공백없이 __와 소문자로만 작성
    def publish(self):
        self.published_date = timezone.now()
        self.save()

# 객체 안에 정의되어 있는 함수 = 메서드 / 란 것을 알려주기 위한 표시
    def __str__(self):
        return self.title


