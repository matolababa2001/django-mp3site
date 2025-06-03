from django.shortcuts import render
from .models import Song

def song_list(request):
    query = request.GET.get('q')
    if query:
        songs = Song.objects.filter(title__icontains=query)
    else:
        songs = Song.objects.all()

    recent_songs = songs.order_by('-id')[:5]  # last 5 added
    return render(request, 'music/song_list.html', {
        'songs': songs,
        'recent_songs': recent_songs,
        'query': query or ''
    })
