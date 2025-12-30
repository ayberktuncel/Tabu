# -*- coding: utf-8 -*-
"""
Created on Fri Dec 26 00:35:28 2025

@author: Ayberk Tuncel
"""
import streamlit as st
import random
import time

# Sayfa Ayarları
st.set_page_config(page_title="Yılbaşı Tabu", page_icon="🎄", layout="centered")
with st.expander("📜 OYUN KURALLARI VE BİLGİLENDİRME (Okumak için tıkla)", expanded=False):
    st.markdown("""
      **ℹ️Bilgi:**   Oyunumuzdaki kelimeler Yılbaşı temalı ayarlanmıştır.
    - **⏭️ Pas Hakkı:** Lütfen pas hakkını çok sık kullanmayın.
    - **🏁 Oyun Sonu:** Kelime havuzundaki tüm isimler bittiğinde oyun otomatik olarak sona erer.
    ---
    **💼 Emeğe Destek:** Beğendiyseniz [LinkedIn hesabımdan](https://www.linkedin.com/in/ayberk-tuncel/) **Python** yeteneğimi onaylamanızı bekliyorum. Teşekkürler! 🩵
    """)
# KELİME HAVUZU 
def get_words():
    return [
        {"word": "TOMBALA", "forbidden": ["Yılbaşı", "Numara", "Torba", "Çinko", "Kart"]},
        {"word": "MİLLİ PİYANGO", "forbidden": ["Bilet", "Para", "İkramiye", "Çeyrek", "Çıkmak"]},
        {"word": "NOEL BABA", "forbidden": ["Hediye", "Sakal", "Kırmızı", "Geyik", "Baca"]},
        {"word": "HİNDİ", "forbidden": ["Dolma", "Fırın", "Tavuk", "Yemek", "Yılbaşı"]},
        {"word": "ÇAM AĞACI", "forbidden": ["Süs", "Yeşil", "Plastik", "Kozalak", "Işık"]},
        {"word": "KESTANE", "forbidden": ["Soba", "Kebap", "Çizmek", "Ateş", "Kış"]},
        {"word": "GERİ SAYIM", "forbidden": ["10", "Süre", "Bitiş", "Yeni Yıl", "Saat"]},
        {"word": "HAVAİ FİŞEK", "forbidden": ["Patlamak", "Gökyüzü", "Renkli", "Kutlama", "Gürültü"]},
        {"word": "RUS SALATASI", "forbidden": ["Mayonez", "Garnitür", "Patates", "Soğuk", "Meze"]},
        {"word": "O SES TÜRKİYE", "forbidden": ["Yarışma", "Jüri", "Şarkı", "Yılbaşı", "TV"]},
        {"word": "KAR KÜRESİ", "forbidden": ["Sallamak", "Cam", "İçinde", "Hediyelik", "Süs"]},
        {"word": "KOKİNA", "forbidden": ["Çiçek", "Kırmızı", "Yeşil", "Diken", "Şans"]},
        {"word": "AMORTİ", "forbidden": ["Bilet", "Para", "Son Rakam", "Geri Almak", "Piyango"]},
        {"word": "PTT", "forbidden": ["Pijama", "Terlik", "Televizyon", "Ev", "Keyif"]},
        {"word": "GECE YARISI", "forbidden": ["Saat", "12", "00:00", "Geri Sayım", "Uyku"]},
        {"word": "HEDİYE", "forbidden": ["Paket", "Vermek", "Sürpriz", "Almak", "Arkadaş"]},
        {"word": "ŞÖMİNE", "forbidden": ["Ateş", "Odun", "Yakmak", "Ev", "Baca"]},
        {"word": "KARDAN ADAM", "forbidden": ["Havuç", "Kış", "Kar", "Erimek", "Atkı"]},
        {"word": "SİM", "forbidden": ["Parlak", "Dökülmek", "Süs", "Kıyafet", "Yaldız"]},
        {"word": "MAYTAP", "forbidden": ["Ateş", "Pasta", "Kıvılcım", "Yanmak", "Çubuk"]},
        {"word": "KONFETİ", "forbidden": ["Kağıt", "Renkli", "Patlatmak", "Saçılmak", "Düğün"]},
        {"word": "ZENCEFİLLİ KURABİYE", "forbidden": ["Adam", "Yılbaşı", "Fırın", "Şekil", "Tarçın"]},
        {"word": "EVDE TEK BAŞINA", "forbidden": ["Film", "Çocuk", "Hırsız", "Yılbaşı", "Kevin"]},
        {"word": "GEYİK", "forbidden": ["Boynuz", "Noel Baba", "Kızak", "Uçmak", "Hayvan"]},
        {"word": "SALEP", "forbidden": ["Tarçın", "Sıcak", "İçecek", "Süt", "Kış"]},
        {"word": "BOZA", "forbidden": ["Leblebi", "Ekşi", "İçecek", "Vefa", "Darı"]},
        {"word": "KURUYEMİŞ", "forbidden": ["Fıstık", "Leblebi", "Karışık", "Tabak", "Çerez"]},
        {"word": "MANDALİNA", "forbidden": ["Turuncu", "Meyve", "Kış", "Soymak", "Koku"]},
        {"word": "ULUDAĞ", "forbidden": ["Kayak", "Bursa", "Tatil", "Dağ", "Teleferik"]},
        {"word": "NAR KIRMAK", "forbidden": ["Bereket", "Kapı", "Atmak", "Dağılmak", "Meyve"]},
        {"word": "VICTORIA'S SECRET", "forbidden": ["Manken", "Defile", "Melek", "Kanat", "Yılbaşı"]},
        {"word": "BÜYÜK İKRAMİYE", "forbidden": ["Para", "Çıkmak", "Milyon", "Bilet", "Talih Kuşu"]},
        {"word": "TAKSİM", "forbidden": ["Meydan", "İstanbul", "Kalabalık", "Kutlama", "Yılbaşı"]},
        {"word": "AJDA PEKKAN", "forbidden": ["Süperstar", "Şarkıcı", "Estetik", "Yılbaşı", "Sahne"]},
        {"word": "KAPADOKYA", "forbidden": ["Balon", "Peri Bacaları", "Turist", "Kar", "Tatil"]},
        {"word": "KIRMIZI", "forbidden": ["Renk", "İç Çamaşırı", "Uğur", "Aşk", "Giymek"]},
        {"word": "PATLAMIŞ MISIR", "forbidden": ["Film", "Sinema", "Tuzlu", "Tencere", "Çerez"]},
        {"word": "KUTU OYUNU", "forbidden": ["Monopoly", "Tabu", "Arkadaş", "Eğlence", "Zar"]},
        {"word": "KABAK TATLISI", "forbidden": ["Tahin", "Ceviz", "Turuncu", "Yılbaşı", "Bal kabağı"]},
        {"word": "ERİK DALI", "forbidden": ["Oynamak", "Müzik", "Düğün", "Yılbaşı", "Kalkmak"]},
        {"word": "MEZE", "forbidden": ["Rakı", "Yoğurt", "Tabak", "Soğuk", "Masa"]},
        {"word": "DİLEK TUTMAK", "forbidden": ["İstemek", "Gerçekleşmek", "Yeni Yıl", "Yıldız", "Umut"]},
        {"word": "2026", "forbidden": ["Gelecek", "Sene", "Takvim", "Rakam", "Yeni"]},
        {"word": "ESKİ YIL", "forbidden": ["Geçmiş", "Bitmek", "Hatıra", "2025", "Geride"]},
        {"word": "AJANDA", "forbidden": ["Defter", "Yazmak", "Tarih", "Plan", "Yeni Yıl"]},
        {"word": "KAR", "forbidden": ["Beyaz", "Yağmak", "Soğuk", "Kış", "Lapa Lapa"]},
        {"word": "ELDİVEN", "forbidden": ["El", "Parmak", "Soğuk", "Takmak", "Kış"]},
        {"word": "ATKI", "forbidden": ["Boyun", "Sarmak", "Örgü", "Kış", "Yün"]},
        {"word": "BERE", "forbidden": ["Baş", "Kafa", "Takmak", "Yün", "Soğuk"]},
        {"word": "PİYANGO BİLETİ", "forbidden": ["Satın Almak", "Çeyrek", "Yarım", "Tam", "Nimet Abla"]},
        {"word": "VİDEO ÇEKMEK", "forbidden": ["Telefon", "Story", "Instagram", "Hatıra", "Kaydetmek"]},
        {"word": "SELFIE", "forbidden": ["Özçekim", "Telefon", "Fotoğraf", "Kendin", "Çekmek"]},
        {"word": "BALON", "forbidden": ["Şişirmek", "Patlamak", "Renkli", "Süs", "Uçmak"]},
        {"word": "KOLA", "forbidden": ["İçecek", "Siyah", "Asitli", "Soğuk", "Marka"]},
        {"word": "CİPS", "forbidden": ["Patates", "Paket", "Çıtır", "Yağlı", "Yemek"]},
        {"word": "ÇEKİRDEK", "forbidden": ["Çitlemek", "Ayçekirdeği", "Kabuk", "Tuzlu", "Dudak"]},
        {"word": "PASTA", "forbidden": ["Kesmek", "Mum", "Tatlı", "Krema", "Yılbaşı"]},
        {"word": "KAYAK MERKEZİ", "forbidden": ["Palandöken", "Erciyes", "Kartalkaya", "Kar", "Spor"]},
        {"word": "TELEFERİK", "forbidden": ["Uludağ", "Binmek", "Havada", "İp", "Taşıt"]}
    ]

# AYARLAR VE BAŞLANGIÇ 
st.sidebar.header("⚙️ Oyun Ayarları")
team_a_name = st.sidebar.text_input("1. Takım Adı", value="Kırmızı Takım")
team_b_name = st.sidebar.text_input("2. Takım Adı", value="Mavi Takım")
round_duration = st.sidebar.slider("Tur Süresi (Saniye)", 30, 180, 60)

# İMZA ALANI
st.sidebar.markdown("---")
st.sidebar.markdown("**Tasarlayan:** Ayberk Tuncel")

# Session State Tanımları
if "words" not in st.session_state:
    st.session_state.words = get_words()
    random.shuffle(st.session_state.words)

if "score_a" not in st.session_state:
    st.session_state.score_a = 0
    st.session_state.score_b = 0
    st.session_state.current_team = "A" 
    st.session_state.round_active = False
    st.session_state.round_start_time = 0  
    st.session_state.current_word = None

# Fonksiyonlar
def reset_game():
    st.session_state.score_a = 0
    st.session_state.score_b = 0
    st.session_state.words = get_words()
    random.shuffle(st.session_state.words)
    st.session_state.round_active = False
    st.session_state.current_team = "A"

def start_round():
    st.session_state.round_active = True
    st.session_state.round_start_time = time.time()
    next_card()

def next_card():
    if len(st.session_state.words) > 0:
        st.session_state.current_word = st.session_state.words.pop(0)
    else:
        st.session_state.current_word = None

def switch_team():
    st.session_state.current_team = "B" if st.session_state.current_team == "A" else "A"
    st.session_state.round_active = False
    st.session_state.current_word = None

def end_round():
    st.session_state.round_active = False

if st.sidebar.button("🆕 Oyunu Sıfırla"):
    reset_game()
    st.rerun()

# ANA EKRAN 
st.title("🎄 Yılbaşı Tabu")

# Skor Tablosu
col1, col2 = st.columns(2)
active_team_name = team_a_name if st.session_state.current_team == "A" else team_b_name

with col1:
    st.metric(label=team_a_name, value=st.session_state.score_a, delta="🔴 SIRA SENDE" if st.session_state.current_team == "A" else "")
with col2:
    st.metric(label=team_b_name, value=st.session_state.score_b, delta="🔵 SIRA SENDE" if st.session_state.current_team == "B" else "")

st.markdown("---")

#  OYUN MANTIĞI 

if not st.session_state.round_active:
    st.info(f"🎤 Sıra **{active_team_name}** grubunda.")
    st.write(f"Hazır olduğunuzda butona basın. Süre ({round_duration} sn) başlayacak!")
    
    if st.button("▶️ TURU BAŞLAT", type="primary", use_container_width=True):
        start_round()
        st.rerun()

else:
    timer_placeholder = st.empty()
    
    elapsed_time = time.time() - st.session_state.round_start_time
    remaining_time = round_duration - elapsed_time
    
    
    if remaining_time <= 0:
        timer_placeholder.error("⏰ SÜRE BİTTİ!")
        st.button("🔄 Sırayı Diğer Takıma Ver", on_click=switch_team, type="primary")
        
    else:
        progress = max(0.0, min(1.0, remaining_time / round_duration))
        timer_placeholder.progress(progress, text=f"⏳ Kalan Süre: {int(remaining_time)} saniye")

        # Kart Tasarımı
        if st.session_state.current_word:
            word_data = st.session_state.current_word
            
            st.markdown(f"""
            <div style="background-color:#FF4B4B; padding:20px; border-radius:10px; text-align:center; color:white; margin-bottom:20px;">
                <h1 style="margin:0; font-size: 40px; text-transform: uppercase;">{word_data['word']}</h1>
            </div>
            <div style="background-color:#f0f2f6; padding:15px; border-radius:10px; text-align:center; color:#333; font-weight:bold; font-size: 18px;">
                {'<br>'.join(word_data['forbidden'])}
            </div>
            <br>
            """, unsafe_allow_html=True)

            b1, b2, b3 = st.columns(3)
            
            if b1.button("✅ DOĞRU (+1)", use_container_width=True):
                if st.session_state.current_team == "A":
                    st.session_state.score_a += 1
                else:
                    st.session_state.score_b += 1
                next_card()
                st.rerun()

            if b2.button("❌ TABU (-1)", use_container_width=True):
                if st.session_state.current_team == "A":
                    st.session_state.score_a -= 1
                else:
                    st.session_state.score_b -= 1
                next_card()
                st.rerun()
                
            if b3.button("⏭️ PAS (0)", use_container_width=True):
                next_card()
                st.rerun()

            while remaining_time > 0:
                time.sleep(1) # 1 saniye bekle
                elapsed_time = time.time() - st.session_state.round_start_time
                remaining_time = round_duration - elapsed_time
                
                if remaining_time <= 0:
                    st.rerun()                 
                
                progress = max(0.0, min(1.0, remaining_time / round_duration))
                timer_placeholder.progress(progress, text=f"⏳ Kalan Süre: {int(remaining_time)} saniye")

        else:
            st.success("Tüm kelimeler bitti! Oyun sona erdi.")
            if st.button("Yeni Oyun Başlat"):
                reset_game()
                st.rerun()

# İMZA ALANI
st.markdown("---")
st.markdown("""
<div style="text-align: center; margin-top: 20px; color: #888;">
    Tasarlayan: <strong>Ayberk Tuncel</strong>
</div>
""", unsafe_allow_html=True)