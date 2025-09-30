## 🐍 Python Virtual Environment (`env`)

`env` – bu Python virtual workspace bulib, projectda ishlatiladigan barcha kutubxonalarni va configurationlarni **isolation** qilish uchun ishlatiladi. Shu bilan projectning tizim Python iga tasir qilmaydi.

### `env` ichidagi tarkib:

- **Include/** – Virtual environment yasaydigon mahsulotlar buladi
- **Lib/** – Python kutubxonalari va paketlari shu yerga urnatiladi  
- **Scripts/** – Virtual muhitni ishga tushirish va paketlarni boshqaradi
- **share/** – Bazi paketlar va Resource uchun  
- **pyvenv.cfg** – Virtual Environment configuration file  

> 🔹 Virtual environment yasash orqali command bilan ishlayotkanda version conflict larni yechish uchun ishlatidai

### Virtual Environment yasash

```bash
python -m venv env