# 🚗 Jant Doğruluk Tespiti – YOLOv8 + Raspberry Pi Projesi

Bu proje, bir oyuncak araç üzerindeki jantın **doğru mu yoksa yanlış mı takıldığını** gerçek zamanlı olarak tespit etmek için geliştirilmiş bir bilgisayarlı görü uygulamasıdır.  
Model, YOLOv8 ile Macbook Pro (M1 Pro) üzerinde eğitilmiş ve Raspberry Pi 5 üzerinde canlı kamera akışıyla çalışacak şekilde optimize edilmiştir.

---

## 📌 Özellikler

- 🔍 **Doğru / Yanlış jant** için iki sınıflı demo YOLO modeli  
- 📸 iPad ile çekilen veri → Pi Camera üzerinde sorunsuz çalışacak şekilde optimize  
- 💻 **Macbook Pro + M1 Pro** üzerinde eğitim  
- 🥧 **Raspberry Pi** üzerinde gerçek zamanlı inference  
- 🎥 Canlı görüntüde kutucuk çizimi ve etiket gösterimi  
- ⚡ Düşük gecikmeli, hafif model (YOLOv8s)

---

## 🗂️ Proje Yapısı

```bash
project/
│
├── data/               # Roboflow’dan indirilen dataset
├── models/             # Eğitilmiş YOLO ağırlıkları (best.pt)
├── src/
│    ├── train.py       # Eğitim scripti
│    ├── detect.py      # Raspberry Pi üzerinde canlı tespit
│    └── utils.py       # Yardımcı fonksiyonlar
│
├── requirements.txt    # Gerekli Python paketleri
└── README.md
