#models.py for Likes&Dislikes

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.article.title}'

    class Meta:
        verbose_name = 'Лайки'
        verbose_name_plural = 'Лайки'


class Dislike(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.article.title}'

    class Meta:
        verbose_name = 'Дизлайк'
        verbose_name_plural = 'Дизлайки'

#views.py for Likes& Dislikes

def add_delete_like(request,pk,action):
    user = request.user
    article = Article.objects.get(pk=pk)

    if action == 'add':
        like = Like.objects.create(user=user,article=article)
        like.save()
    else: #delete
        like = Like.objects.get(user=user, article=article)
        like.delete()
    return redirect('index')

def add_delete_dislike(request,pk,action):
    user = request.user
    article = Article.objects.get(pk=pk)

    if action == 'add':
        dislike = Dislike.objects.create(user=user,article=article)
        dislike.save()
    else: #delete
        dislike = Dislike.objects.get(user=user, article=article)
        dislike.delete()
    return redirect('index')

#templatetages/blog_tags.py for Likes&Dislikes

@register.simple_tag()
def get_like(article,user):
    return Like.objects.filter(article=article,user=user).exists()

@register.simple_tag()
def get_dislike(article,user):
    return Dislike.objects.filter(article=article,user=user).exists()

#article_card.html for Likes& Dislikes

{% get_like article request.user as like %}
          {% if like %}
          <a class="text-danger" href="{% url 'like' article.pk 'delete' %}"><i class="bi bi-hand-thumbs-up-fill"></i></a>
          {% else %}
          <a class="text-danger" href="{% url 'like' article.pk 'add' %}"><i class="bi bi-hand-thumbs-up"></i></a>
          {% endif %}
          <p>{{ likes_count }}</p>
        {% endif %}

        {% get_dislike article request.user as dislike %}
          {% if dislike %}
          <a class="text-danger" href="{% url 'dislike' article.pk 'delete' %}"><i class="bi bi-hand-thumbs-down-fill"></i></a>
          {% else %}
          <a class="text-danger" href="{% url 'dislike' article.pk 'add' %}"><i class="bi bi-hand-thumbs-down"></i></a>
        {% endif %}

#urls.py 

    path('like/<int:pk>/<str:action>/',add_delete_like,name='like'),
    path('dislike/<int:pk>/<str:action>/',add_delete_dislike,name='dislike'),
