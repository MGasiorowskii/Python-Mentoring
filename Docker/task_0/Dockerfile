# pobranie obrazu Pythona z DockerHub
FROM python:latest
# wyznaczenie ścieżki roboczej w kontenerze
WORKDIR /app
# skopiowanie zawartości pliku requirements.txt do working directory
COPY requirements.txt .
# instalacja dependencji
RUN pip install -r requirements.txt
# skopiowanie zawartości katalogu src/ do working directory
COPY src/ .
# komendy do uruchomienia aplikacji
CMD ["python", "./python_file.py"]

