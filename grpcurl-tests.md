# 🧪 grpcurl Test Dokümantasyonu

---

## 1. Kitap Listeleme – `ListBooks`

**Komut:**

```bash
grpcurl -plaintext -d '{}' localhost:50051 university.BookService/ListBooks

Çıktı:
{
  "books": [
    {
      "id": "047de5bf-c208-4dc6-8cc6-43f2103e746a",
      "title": "1984",
      "author": "George Orwell",
      "isbn": "9780451524935",
      "publisher": "Penguin",
      "pageCount": 328,
      "stock": 3
    },
    {
      "id": "70eea4ad-d0a4-4892-a5c6-551bb0c61281",
      "title": "Sapiens",
      "author": "Yuval Noah Harari",
      "isbn": "9780062316097",
      "publisher": "Harper",
      "pageCount": 498,
      "stock": 5
    }
  ]
}


## 2. Kitap Ekleme – `CreateBook`

**Komut:**

```bash
grpcurl -plaintext -d '{
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "isbn": "9780132350884",
  "publisher": "Prentice Hall",
  "pageCount": 464,
  "stock": 4
}' localhost:50051 university.BookService/CreateBook


Çıktı:
{
  "id": "48dfabf1-82b9-48de-92aa-89e9238a6829",
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "isbn": "9780132350884",
  "publisher": "Prentice Hall",
  "pageCount": 464,
  "stock": 4
}


## 3. Kitap Getirme – `GetBook`

**Komut:**

```bash

grpcurl -plaintext -d '{"id":"48dfabf1-82b9-48de-92aa-89e9238a6829"}' localhost:50051 university.BookService/GetBook

Çıktı:

{
  "id": "48dfabf1-82b9-48de-92aa-89e9238a6829",
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "isbn": "9780132350884",
  "publisher": "Prentice Hall",
  "pageCount": 464,
  "stock": 4
}

## 4. Kitap Getirme – `GetBook` HATALI ID

**Komut:**

```bash

grpcurl -plaintext -d '{"id":"gecersiz_id"}' localhost:50051 university.BookService/GetBook

Çıktı:
ERROR:
  Code: NotFound
  Message: Book not found


## 5. Kitap Silme – `DeleteBook`

**Komut:**

```bash

grpcurl -plaintext -d '{"id":"48dfabf1-82b9-48de-92aa-89e9238a6829"}' localhost:50051 university.BookService/DeleteBook

Çıktı:
{}


## 6. Kitap Güncelleme – `UpdateBook` 

**Komut:**

```bash

grpcurl -plaintext -d '{
  "id": "047de5bf-c208-4dc6-8cc6-43f2103e746a",
  "title": "1984 (Updated)",
  "author": "George Orwell",
  "isbn": "9780451524935",
  "publisher": "Penguin",
  "pageCount": 350,
  "stock": 10
}' localhost:50051 university.BookService/UpdateBook


Çıktı:

{
  "id": "047de5bf-c208-4dc6-8cc6-43f2103e746a",
  "title": "1984 (Updated)",
  "author": "George Orwell",
  "isbn": "9780451524935",
  "publisher": "Penguin",
  "pageCount": 350,
  "stock": 10
}