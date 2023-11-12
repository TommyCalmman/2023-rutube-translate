from moviepy.editor import AudioFileClip, VideoFileClip, concatenate, CompositeAudioClip

# Загрузка видео и аудио
video = VideoFileClip("video.mp4")
audio = AudioFileClip("speech.mp3")

# Создание субклипа видео с 3-й секунды
start_time = 1.5  # начало наложения аудио на 3-й секунде
video_subclip = video.subclip(start_time)

# Приглушение оригинального звука в видео
video_subclip = video_subclip.volumex(0.7)  # уменьшает громкость до 20% от исходной

# Создание субклипа аудио с такой же длительностью, как и субклип видео
audio_subclip = audio.subclip(1.5, video_subclip.duration)

# Наложение аудио на видео
new_audio = CompositeAudioClip([video.audio, audio_subclip])
video_with_audio = video_subclip.set_audio(audio_subclip)

# Объединение видео до 3-й секунды, наложенное с аудио после 3-й секунды
final_video = concatenate([video.subclip(0, start_time), video_with_audio])

# Сохранение результата
final_video.write_videofile("output.mp4")