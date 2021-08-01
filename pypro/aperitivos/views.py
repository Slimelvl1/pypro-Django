from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, titulo):
        self.titulo = titulo
        self.slug = slug

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))


videos = [
    Video('motivacao', 'Video Aperitivo: Motivação'),
    Video('instalacao-windows', 'Video Aperitivo: Motivação'),

]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
