# Python 3.10 tabanlı bir imaj kullan
FROM python:3.10-slim

# Ortam değişkenleri için
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Gerekli sistem bağımlılıklarını kur (Playwright için)
RUN apt-get update && apt-get install -y \
    wget \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libgbm1 \
    libpango-1.0-0 \
    libcairo2 \
    libasound2 \
    libx11-xcb1 \
    libxcb1 \
    libx11-6 \
    libxext6 \
    libxrandr2 \
    libdrm2 \
    libdbus-1-3 \
    libgtk-3-0 \
    ca-certificates \
    && apt-get clean

# Uygulama dosyalarını çalışma dizinine kopyala
WORKDIR /app
COPY . /app

# Python paketlerini kur
RUN pip install --upgrade pip
RUN pip install python-dotenv twilio playwright

# Playwright tarayıcıları indir
RUN python -m playwright install

# app.py çalıştır
CMD ["python", "app.py"]
