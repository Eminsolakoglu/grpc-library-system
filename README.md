# 📚 gRPC University Library System

Bu proje, bir üniversiteye ait çevrim içi kütüphane sisteminin `gRPC` teknolojisi ile Python dili kullanılarak geliştirilmesini kapsamaktadır. Projede `Protocol Buffers (.proto)` tanımı ile kitap, öğrenci ve ödünç alma işlemleri servis olarak sunulmaktadır.

---

## 🗂️ Proje Yapısı

grpc_university_library/
├── protos/ # .proto dosyası
│ └── university.proto
├── server/ # gRPC sunucu uygulaması
│ └── server.py
├── client/ # gRPC istemci uygulaması
│ └── client.py
├── grpcurl-tests.md # Test çıktıları
├── DELIVERY.md # Teslim belgesi
└── README.md # Bu dosya


---

## 🔧 Gereksinimler

- Python 3.10+  
- grpcio  
- grpcio-tools  
- grpcio-reflection

Kurulum:

```bash
pip install grpcio grpcio-tools grpcio-reflection
```
⚙️ .proto Derleme

```bash
python -m grpc_tools.protoc \
  -I./protos \
  -I$(python -c 'import grpc_tools; import os; print(os.path.dirname(grpc_tools.__file__) + "/_proto")') \
  --python_out=./server \
  --grpc_python_out=./server \
  ./protos/university.proto
```

Ardından university_pb2.py ve university_pb2_grpc.py dosyaları oluşacaktır.

▶️ Uygulama Çalıştırma

Sunucu:
```bash
python server/server.py
```
İstemci:
```bash
python client/client.py
```

🧪 grpcurl Testi
Sunucu çalışıyorken başka bir terminalde şu komutla test yapılabilir:
```bash
grpcurl -plaintext -d '{}' localhost:50051 university.BookService/ListBooks
```
Tüm testler için grpcurl-tests.md dosyasına bakınız.

