# 🤗 HugBot – Psikolojik Destek Chatbot'u

HugBot, duygusal destek sağlamak amacıyla geliştirilmiş bir yapay zeka destekli psikolojik danışma chatbotudur. Kullanıcıya empatik, nazik ve cesaret verici yanıtlar sunmayı hedefler. Flask + Vue.js mimarisi ile geliştirilmiş olup, arka planda Google Gemini API ve metin benzerliği için FAISS kullanır.

---

## 🎯 Projenin Amacı

Bu projenin amacı, özellikle duygusal olarak zor zamanlar geçiren kullanıcıların ihtiyaç duyduğu psikolojik destek cümlelerini anlamlı ve empatik bir şekilde sunmaktır. HugBot, kullanıcıdan gelen mesajları anlayarak, ona moral verici, sakinleştirici ve destekleyici yanıtlar üretir.

---

## 📁 Veri Seti Hakkında

`data.txt` dosyasında, psikolojik destek niteliğinde kısa ve anlamlı cümleler yer alır. Bu veri seti:
- Duygusal destek
- Moral ve motivasyon
- Anlayış ve empati  
odaklı cümlelerden oluşur.

**Örnek veriler:**
Kendine karşı nazik ol. Başkalarına gösterdiğin anlayışı kendine de göster.
Kendini kötü hissettiğinde, geçmişte başardıklarını hatırla.
Her yeni gün, iyileşmek için bir fırsattır.

---

## 🧠 Kullanılan Yöntemler

### Backend (Flask)
- **Sentence-Transformers (all-MiniLM-L6-v2):** Kullanıcıdan gelen mesaj embedding'e çevrilerek, veri setindeki cümlelerle benzerliği ölçülür.
- **FAISS:** En alakalı 3 cümle seçilir ve Gemini API'ye context olarak gönderilir.
- **Gemini 1.5 Flash (Google Generative AI):** Anlamlı, empatik ve kullanıcı odaklı cevap üretimi yapılır.

### Frontend (Vue 3 + Vite + TailwindCSS)
- Kullanıcı mesajı gönderir.
- Flask API'den gelen cevaplar şık bir arayüzde gösterilir.
- `ChatBox.vue` ve `MessageInput.vue` bileşenleriyle minimal ve kullanıcı dostu bir tasarım sunar.

---

## ⚙️ Kurulum ve Çalıştırma

1. Gerekli ortamı oluştur 
```bash
#isteğe bağlı
- python -m venv venv
- venv\Scripts\activate  # Windows
```
2. Gerekli kütüphaneleri yükle
```bash
- pip install -r requirements.txt
```

3. .env Dosyası
- Proje dizinine .env adında bir dosya oluştur ve aşağıdaki satırı ekle:
```
GOOGLE_API_KEY=senin_gemini_api_anahtarin

```

4. Backend’i Çalıştır
```bash
- python app.py
```
- Sunucu şu adreste çalışacaktır:
👉 http://localhost:5000

# Frontend Kurulumu (Vue)
5. Paketleri yükle
```bash
- npm install
```
6. Uygulamayı başlat
```bash
- npm run dev
```
<img src= "./images/ss1.png" alt="Screenshot" width="600"

## 🚀 Nasıl Çalışır?

- Kullanıcı mesaj yazar.

- Flask sunucusu, gelen mesajla en benzer 3 cümleyi data.txt içinden bulur.

- Bu cümleler ve kullanıcı mesajı, bir sistem prompt'u ile birlikte Gemini API’ye gönderilir.

- API'den gelen cevap Vue arayüzünde kullanıcıya gösterilir.

## 🧪 Örnek Kullanım

- Kullanıcı mesajı:

- Kendimi çok yalnız hissediyorum.

- HugBot cevabı:

- Yalnızlık zor bir duygu olabilir ama bil ki bu duyguyu yaşayan tek kişi değilsin. Kendine nazik ol ve bir nefes al. Yardım istemek güçlü bir adımdır.

## 💡 Elde Edilen Sonuçlar

- Kullanıcılardan gelen mesajlara anlamlı, nazik ve empatik yanıtlar başarıyla üretilmiştir.

- FAISS ile yapılan benzerlik eşleşmesi, daha isabetli ve konuyla ilgili yanıtlar üretmeyi sağlamıştır.

- Arayüz, kullanıcıyı yormadan destekleyici iletişim kurmaya elverişli olacak şekilde tasarlanmıştır.

## 📌 Notlar

- Bu proje profesyonel psikolojik danışmanlık yerine geçmez.

- Amaç, moral ve destek niteliğinde basit cevaplar sunmaktır.

- Uzun vadeli sıkıntılarda profesyonel yardım önerilir.

## 👨‍💻 Geliştirici

- Bu proje bireysel bir öğrenme, geliştirme ve sosyal fayda amacıyla oluşturulmuştur.

## 📞 İletişim
- **E-mail:** [sevincmehtap614@gmail.com](mailto:sevincmehtap614@gmail.com)
- **GitHub:** [github.com/MehtapSevincc](https://github.com/MehtapSevincc)