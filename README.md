# 🎄 Yılbaşı Temalı Dijital Tabu Oyunu
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ayberk-yilbasi-tabu.streamlit.app)
👉 **[CANLI OYNA: Oyunu denemek için buraya tıkla!](https://ayberk-yilbasi-tabu.streamlit.app)**

Bu proje, yılbaşı gecelerinde arkadaşlarınız ve ailenizle keyifli vakit geçirmeniz için **Python** ve **Streamlit** kullanılarak geliştirilmiş modern bir Tabu oyunudur.

## ✨ Özellikler

* **⚡ İnteraktif Web Arayüzü:** Streamlit sayesinde kullanıcı dostu, renkli ve hızlı bir deneyim.
* **⚙️ Özelleştirilebilir Ayarlar:**
    * Takım isimlerini değiştirebilme.
    * Tur süresini ayarlayabilme (30 - 180 saniye arası).
* **🎲 Zengin Kelime Havuzu:** "Tombala", "O Ses Türkiye", "Milli Piyango", "Kestane" gibi yılbaşı ruhunu yansıtan özel kelimeler.
* **📊 Otomatik Skor Takibi:** Doğru, Tabu ve Pas durumlarına göre puanlar anlık olarak hesaplanır.
* **⏱️ Görsel Sayaç:** Süre ilerledikçe azalan dinamik ilerleme çubuğu.

## 🛠️ Kullanılan Teknolojiler

* **Dil:** Python 3.x
* **Framework:** [Streamlit](https://streamlit.io/)
* **Kütüphaneler:** `random`, `time`

## 🚀 Kurulum ve Çalıştırma

Bu projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

1.  **Projeyi indirin:**
    ```bash
    git clone [https://github.com/ayberktuncel/Tabu.git](https://github.com/ayberktuncel/Tabu.git)
    cd Tabu
    ```

2.  **Gerekli kütüphaneyi yükleyin:**
    ```bash
    pip install streamlit
    ```

3.  **Uygulamayı başlatın:**
    Terminal veya komut satırına şu kodu yazın:
    ```bash
    streamlit run tabu.py
    ```
    *(Tarayıcınız otomatik olarak açılacak ve oyun başlayacaktır.)*

## 🎮 Nasıl Oynanır?

1.  Yan menüden **Takım İsimlerini** belirleyin ve **Süreyi** ayarlayın.
2.  "Turu Başlat" butonuna basın.
3.  Ekrana gelen kelimeyi, altındaki **Yasaklı Kelimeleri** kullanmadan takım arkadaşınıza anlatın.
4.  Duruma göre butonları kullanın:
    * ✅ **Doğru:** Kelime bilindiğinde (+1 Puan).
    * ❌ **Tabu:** Yasaklı kelime kullanıldığında (-1 Puan).
    * ⏭️ **Pas:** Kelimeyi geçmek için (Puan değişmez).
5.  Süre bittiğinde sıra diğer takıma geçer!

---

## 👨‍💻 Geliştirici

Bu proje **Ayberk Tuncel** tarafından geliştirilmiştir.

* 🐍 Python projelerime destek olmak için: **[LinkedIn Profilim](https://www.linkedin.com/in/ayberk-tuncel/)**

**İyi Eğlenceler ve Mutlu Yıllar! 🎅**
