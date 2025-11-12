# 🗳️ Proyek Akhir: Aplikasi Polling "Pilih Mana?"

Proyek ini mengimplementasikan sebuah sistem terdistribusi menggunakan arsitektur **Microservices** untuk memfasilitasi pengambilan keputusan (polling) secara real-time.

Status Progres: **Perencanaan Arsitektur & Proof-of-Concept Skeleton (MVP)**

## 1. STRUKTUR ARSITEKTUR & PEMBAGIAN TUGAS

Kami membagi sistem menjadi **lima layanan (API)** independen yang merepresentasikan **Application Logic (Tier 2)**.

| Layanan (API) | Tujuan Utama | Penanggung Jawab |
| :--- | :--- | :--- |
| **API User** | Otentikasi, Registrasi, dan Profil Pengguna. | (Nama Anggota 1) |
| **API Poll** | Mengelola data pertanyaan dan pilihan polling. | (Nama Anggota 2) |
| **API Vote** | Merekam suara/data voting yang masuk. | (Nama Anggota 3) |
| **API Result** | Menghitung agregasi dan menyajikan hasil akhir polling. | (Nama Anggota 4) |
| **API Sharing** | Layanan utilitas untuk men-generate link sharing dan notifikasi. | (Nama Anggota 5) |

## 2. KONTRAK API (The Blueprint)

Ini adalah format Request dan Response yang wajib ditaati oleh semua layanan agar komunikasi antar *microservice* terjamin.

### Layanan: API User (Port: 5001)

| Endpoint | Method | Deskripsi | JSON Request | JSON Response (Success) |
| :--- | :--- | :--- | :--- | :--- |
| `/login` | `POST` | Autentikasi pengguna | `{ "email": "...", "password": "..." }` | `{ "status": "ok", "user_id": 123, "token": "..." }` |
| `/register` | `POST` | Registrasi pengguna baru | `{ "name": "...", "email": "...", "password": "..." }` | `{ "status": "created", "user_id": 123 }` |

### Layanan: API Poll (Port: 5002)

| Endpoint | Method | Deskripsi | JSON Request | JSON Response (Success) |
| :--- | :--- | :--- | :--- | :--- |
| `/polls` | `POST` | Membuat polling baru | `{ "token": "...", "question": "...", "options": [...] }` | `{ "status": "sukses", "poll_id": 456 }` |
| `/polls` | `GET` | Mendapatkan daftar semua polling aktif | (Tidak ada) | `[ { "id": 456, "question": "..." }, ... ]` |

### Layanan: API Vote (Port: 5003)

| Endpoint | Method | Deskripsi | JSON Request | JSON Response (Success) |
| :--- | :--- | :--- | :--- | :--- |
| `/vote` | `POST` | Mengirimkan suara | `{ "user_id": 123, "poll_id": 456, "option": "A" }` | `{ "status": "vote_recorded" }` |

## 3. Bukti Konsep (PoC)

* File kerangka (`app_*.py`) sudah dibuat di setiap folder API.
* Layanan dapat dijalankan secara independen: **`API User` di Port 5001** dan **`API Poll` di Port 5002** dapat berjalan bersamaan dan siap merespons.
