# WRENCHXOO web sitesi

Adres: https://38mustafa.github.io/wrenchxoo.github.io/

## Hızlı yayınlama

1. GitHub deposu: https://github.com/38mustafa/wrenchxoo.github.io
2. Yeni tasarım için **index.html** dosyasını deponun **ana dizinindeki** `index.html` ile değiştir.
3. **Commit changes** yap ve GitHub Pages dağıtımını bekle.
4. Tarayıcıda Ctrl + Shift + R ile yenile.

Site yalnızca `index.html` yüklenerek çalışır. Kick oynatıcısı ziyaretçi "OYNATICIYI AÇ" butonuna basınca açılır. Bu, Kick'te canlı olunduğunu otomatik doğrulayan bir rozet değildir.

## İsteğe bağlı YouTube son videoları otomatik yenileme

Ek olarak şunları yükle:
- `.github/workflows/refresh-videos.yml`
- `scripts/update_videos.py`
- `data/videos.json`

GitHub deponuzda Settings > Actions > General > Workflow permissions altında **Read and write permissions** seçin. Actions > Refresh YouTube videos > Run workflow ile ilk çalıştırmayı başlatın. Başarılı olursa `data/videos.json` güncellenir ve videolar sitede listelenir. Ardından 4 saatte bir planlı çalışır (GitHub zamanlanmış işler gecikebilir). YouTube tarafındaki erişim değişiklikleri bu otomasyonu engelleyebilir; o durumda sitede YouTube kanal bağlantıları görünmeye devam eder.

**Önemli:** YouTube kanalınızın kullanıcı adını değiştirirseniz `scripts/update_videos.py` içindeki `CHANNEL` adresini güncelleyin.

## Kick canlı durum rozeti

Kick'in resmi API'si erişim belirteci gerektirir. Yalnızca statik GitHub Pages üzerinde gizli API anahtarı tutulamaz. Bu nedenle doğrulanmamış 'CANLI' rozeti veya sahte izleyici/abone sayacı kullanılmadı. İleride Kick uygulaması ve GitHub Actions Secrets ile güvenli olarak eklenebilir.

## Özellikler

- Responsive siyah-kırmızı gaming tema
- Kick resmi gömülü oynatıcı
- YouTube, Kick ve Instagram bağlantıları
- Video kartları, Shorts, animasyonlar, mobil menü, paylaş düğmesi
- Erişilebilir menü, isteğe bağlı iframe yükleme, reduced-motion tercihi
