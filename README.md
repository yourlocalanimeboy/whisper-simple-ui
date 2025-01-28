# Whiisper Basit UI

## Gereksinimler Kurulum Rehberi

Bu projeyi çalıştırabilmek için bazı gereksinimleri bilgisayarınıza kurmanız gerekmektedir. Aşağıdaki adımları takip ederek kurulumları gerçekleştirebilirsiniz.

### 1. Python, Pip ve Tkinter Kurulumu

**Python**, bu projeyi çalıştırmak için gerekli programlama dilidir. **Pip** ise ek kütüphaneleri yüklemek için kullanılan paket yöneticisidir. **Tkinter** ise Python ile GUI (grafiksel kullanıcı arayüzü) uygulamaları geliştirmek için kullanılan bir kütüphanedir.

#### Adım Adım Kurulum:

1. **Python İndirin ve Kurun**:
   - [Python'un resmi web sitesine](https://www.python.org/downloads/) gidin.
   - İşletim sisteminize uygun en son Python sürümünü indirin.
   - Kurulum sırasında **"Add Python to PATH"** seçeneğinin işaretli olduğundan emin olun.

2. **Python ve Pip Kurulumu Kontrol Edin**:
   - Komut istemcisini (cmd) açın ve aşağıdaki komutları çalıştırarak Python ve Pip'in doğru kurulduğunu kontrol edin:
     ```bash
     python --version
     pip --version
     ```
   - Eğer her iki komut da sürüm numarası gösteriyorsa, kurulum başarılı olmuştur.

3. **Tkinter Kurulumu**:
   - Tkinter, Python ile birlikte genellikle yüklü gelir. Eğer yüklenmemişse, manuel olarak yükleyebilirsiniz:
     - Windows üzerinde genellikle Tkinter önceden yüklüdür.
     - Eğer yüklenmemişse, Python'u tekrar yüklerken **"Tcl/Tk and IDLE"** seçeneğini işaretlediğinizden emin olun.

### 2. FFMPEG Kurulumu

**FFMPEG**, ses ve video işlemleri için kullanılan güçlü bir multimedya aracıdır.

#### Adım Adım Kurulum:

1. **FFMPEG İndirin**:
   - [FFMPEG'in resmi web sitesine](https://ffmpeg.org/download.html) gidin.
   - İşletim sisteminize uygun FFMPEG sürümünü indirin ve çıkarın.

2. **FFMPEG'i PATH'e Ekleyin**:
   - FFMPEG'i çıkardıktan sonra, bu klasörü sisteminizin PATH değişkenine eklemeniz gerekecek.
   
   - **Windows**:
     1. **Bu PC** ya da **Bilgisayar**'a sağ tıklayın ve **Özellikler**'i seçin.
     2. **Gelişmiş sistem ayarları**'na tıklayın, ardından **Ortam Değişkenleri**'ni seçin.
     3. **Sistem Değişkenleri** altında **Path** adlı değişkeni bulun ve **Düzenle**'ye tıklayın.
     4. FFMPEG'in bulunduğu klasör yolunu (örneğin `C:\ffmpeg\bin`) listeye ekleyin.

3. **FFMPEG Kurulumunu Doğrulayın**:
   - Komut istemcisini açın ve aşağıdaki komutu çalıştırın:
     ```bash
     ffmpeg -version
     ```

### 3. Whisper AI Kurulumu

**Whisper AI**, sesli metin çözümlemesi için kullanılan bir araçtır.

#### Adım Adım Kurulum:

1. **Whisper AI'yi Kurun**:
   - Komut istemcisini açın ve aşağıdaki komutu çalıştırarak Whisper AI'yi yükleyin:
     ```bash
     pip install openai-whisper
     ```

2. **Whisper AI Kurulumunu Doğrulayın**:
   - Kurulumdan sonra, aşağıdaki komutla Whisper'in doğru şekilde yüklendiğini kontrol edebilirsiniz:
     ```bash
     whisper --help
     ```

---

### Projeyi Çalıştırmak İçin Ek Adımlar

Gereksinimler kurulduktan sonra, projeyi çalıştırmaya hazırsınız.

1. Bu depo dosyasını bilgisayarınıza indirin veya klonlayın.
2. Proje dizinine gidin.
3. Python bağımlılıklarını yüklemek için aşağıdaki komutu çalıştırın:
   ```bash
   pip install -r requirements.txt

