Proje Kurulum ve Çalıştırma Rehberi
1. Gerekli Donanımlar ve Bağlantılar
Bu projede kullanılan donanımlar:

Raspberry Pi: Projenin merkezi kontrol birimi olarak kullanılmaktadır.
Ultrasonik ve Lidar Sensörler: Engel algılama için kullanılır.
GPS Modülü: Drone’un konumunu belirlemek için.
Kamera (Termal veya RGB): Görüntü işleme ve nesne algılama için.
Batarya ve Güneş Enerjisi Modülü: Uzun süreli kullanım için güç yönetimi sağlar.
Sinyal Bozucu (Jammer): Tehdit durumlarında sinyal bozma işlevi sunar.
Donanım bağlantıları:

Ultrasonik sensör ve lidar sensörü Raspberry Pi’nin GPIO pinlerine bağlayın (GPIO pin yapılandırmalarını config.py dosyasından kontrol edin).
Kamera modülünü Raspberry Pi’ye uygun port üzerinden bağlayın.
GPS modülünü Raspberry Pi’ye bağlayarak GPS koordinatlarını alabilirsiniz.
Jammer ve güneş enerjisi modülünü güç kaynağı ve GPIO pinlerine uygun şekilde bağlayın.
2. Gerekli Yazılımlar ve Kütüphanelerin Kurulumu
Bu projeyi çalıştırmak için Python 3.7+ sürümüne ve çeşitli Python kütüphanelerine ihtiyacınız olacak.

A) Python ve Bağımlılıkların Yüklenmesi
Python’un yüklü olduğunu doğrulayın:

bash
Kodu kopyala
python3 --version
Python kütüphanelerini yükleyin: Projede kullanılan kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın:

bash
Kodu kopyala
pip install dronekit opencv-python pycryptodome RPi.GPIO
dronekit: Drone kontrolü ve GPS navigasyonu için.
opencv-python: Görüntü işleme ve nesne tanıma için.
pycryptodome: Veri güvenliği için AES şifreleme kütüphanesi.
RPi.GPIO: Raspberry Pi GPIO pinleri ile sensör kontrolü.
B) Ek Kütüphaneler
Proje belirli donanımlarla uyumlu çalıştığından, ihtiyaç halinde sensörlerin ve donanımların sürücülerini kurabilirsiniz. Örneğin, GPS modülü veya Lidar gibi cihazların sürücüleri gerekebilir.

3. Proje Dosyalarının İndirilmesi
Projeyi GitHub’dan veya yerel dosyalarınızdan indirip çalışma dizinine geçin.

GitHub’dan İndirin:

bash
Kodu kopyala
git clone https://github.com/kullaniciadiniz/AkilliSavunmaDroneKontrolSistemi.git
cd AkilliSavunmaDroneKontrolSistemi/src
Yapılandırma Dosyasını Düzenleyin: src/config.py dosyasını açın ve kendi ayarlarınıza göre düzenleyin.

Drone bağlantı ayarları: DRONE_CONNECTION_STRING değerini kendi drone bağlantı bilgilerinize göre güncelleyin.
Sensör pin ayarları: Kullanılan sensörler için GPIO pin ayarlarını kontrol edin.
4. Projeyi Çalıştırma
Kurulum tamamlandıktan sonra projenin src dizininde aşağıdaki komutu çalıştırarak projeyi başlatabilirsiniz.

bash
Kodu kopyala
python3 main.py
5. Projenin Çalışma Süreci
Proje çalıştırıldığında aşağıdaki süreçler otonom olarak gerçekleşecektir:

Drone Bağlantısı: dronekit ile belirlenen bağlantı üzerinden drone’a bağlanır ve uçuş moduna geçilir.
Otonom Görev Başlatma: AutoPilot modülü devreye girer ve drone belirlenen GPS rotasında uçuşa başlar.
Tehdit Tespiti ve Jammer Aktivasyonu: Tehdit algılandığında sinyal bozucu otomatik olarak devreye girer.
Engel Algılama: Ultrasonik ve lidar sensörler ile engeller algılanır ve rota güncellenir.
Termal Görüntüleme ve Sinyal Analizi: Termal kamera ve sinyal analiz modülleri çevresel tehditleri analiz eder.
Veri Güvenliği ve Blockchain: AES şifreleme ile veri güvenliği sağlanır ve görev verileri blockchain tabanlı güvenlik ile kayıt altına alınır.
6. Sık Karşılaşılan Sorunlar ve Çözümleri
Bağlantı Hatası:

Drone bağlantısı sırasında bir hata alıyorsanız, DRONE_CONNECTION_STRING değerini doğru girdiğinizden emin olun. Ayrıca, drone’un kontrol modunda ve bağlı olduğundan emin olun.
Sensör Algılama Sorunları:

Sensör bağlantılarını tekrar kontrol edin ve GPIO pin ayarlarının config.py dosyasına uygun olduğundan emin olun.
Sensörlerin çalıştığından emin olmak için her bir sensörü ayrı ayrı test edin.
Python Kütüphane Hataları:

Tüm bağımlılıkların doğru şekilde yüklendiğinden emin olun. pip install komutunu kullanarak eksik kütüphaneleri yeniden yükleyebilirsiniz.
7. Proje Yapısının Genel İncelemesi
Her modül, ilgili işlevselliği sağlamak üzere tasarlanmıştır ve proje çalıştırıldığında ana dosya (main.py) sırasıyla tüm işlemleri gerçekleştirir. Sistem, gerçek zamanlı olarak drone'u otonom bir şekilde kontrol eder ve güvenliği sağlar.

