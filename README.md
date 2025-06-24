# Bellman-Ford API (Kullanıcı Dostu Sürüm)

Bu proje, kullanıcıdan sadece düğümler ve kenar mesafeleri alarak Bellman-Ford algoritmasını çalıştırır. Kod bilgisi gerektirmez.

## Kullanım

1. Frontend kullanıcıdan:
   - Düğümleri (örn: A, B, C)
   - Kenarları (örn: A,B,4)
   - Kaynak düğümü (örn: A)
   olarak metin girişleriyle alır.

2. Backend bu bilgileri işler ve:
   - Adım adım sonuçları döner
   - Negatif döngü varsa uyarır

## Başlatmak İçin

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

## POST isteği örneği

```json
{
  "nodes": ["A", "B", "C"],
  "edges": [
    {"from_node": "A", "to_node": "B", "weight": 4},
    {"from_node": "A", "to_node": "C", "weight": 5},
    {"from_node": "B", "to_node": "C", "weight": -2}
  ],
  "source": "A"
}
```
