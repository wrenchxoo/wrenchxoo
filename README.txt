WRENCHXOO SEO + PERFORMANS GÜNCELLEMESİ

KAYNAK: Daha önce birlikte hazırladığımız çalışan YouTube abone sayacı sürümü üzerine uygulanmıştır.

GitHub deponun ANA DİZİNİNE (main / root) şu 4 dosyayı yükle:
  index.html   (mevcut dosyanın yerini alır)
  robots.txt
  sitemap.xml
  favicon.svg

DOKUNMA:
  data/ klasörü
  scripts/ klasörü
  .github/workflows/ klasörü
  GitHub Secrets

YENİLİKLER:
- Doğru canonical / Türkçe meta açıklamaları / Twitter ve Open Graph başlıkları
- WebSite yapılandırılmış verisi (schema.org)
- Sitemap, robots.txt, favicon
- Erişilebilir klavye atlama bağlantısı ve dinamik durum anonsları
- Resim boyutları, lazy loading ve async decode
- Animasyonların IntersectionObserver olmayan tarayıcılarda görünmesi

NOT: robots.txt yalnızca ana alan adının kökünde arama motorları tarafından kabul edilir. Bu dosya proje alt klasöründe olsa da sitemap.xml erişilebilir; robots.txt bu nedenle zorunlu değildir. Arama motorları indeksleme garantisi yoktur.

KONTROL:
1. GitHub Actions / Pages yayınının yeşil olmasını bekle.
2. https://wrenchxoo.github.io/wrenchxoo/?seo=1 adresini aç.
3. Video, Shorts, Kick ve abone sayacı bölümlerini test et.
4. https://wrenchxoo.github.io/wrenchxoo/sitemap.xml adresini kontrol et.
