# 🌍 Pressure-to-Depth Converter  
**One-click CLI tool for CTD / SBE 37 users**  
Convert **pressure (dbar) → depth (m)** using the *Sea-Bird SBE 37 simplified formula*.

> Works **offline**, supports **English & Chinese**, ships as a single executable.

---

## 📌 What it does
1. Reads any CSV with **pressure + latitude** columns  
2. Computes depth with *SBE 37 simplified UNESCO 1983* formula  
3. Creates `*_depth.csv` next to your file  
4. Auto-detects **Windows / macOS / Linux** language

---

## 🚀 30-second start

### 1. Grab the latest release  
Download `pressure2depth.exe` (Windows) or `pressure2depth` (macOS/Linux) from  
[Releases ➜](https://github.com/iyuxiaoyan/pressure_to_depth/releases)

### 2. Prepare your CSV  
Use the provided template [`input.csv`](input.csv):

| Pressure_dbar | Latitude_deg |
| ------------- | ------------ |
| 249.805       | 0            |
| 249.805       | 45           |

> Column order does **not** matter; names are auto-detected.

### 3. Run  
```bash
# Double-click the EXE or
./pressure2depth
Drag or paste the CSV file path and press Enter:
> /path/to/your.csv
✅ Processing complete! Result saved to: your_depth.csv
```

---

## 📐 Formula (Sea-Bird SBE 37)

Sea-Bird simplifies **UNESCO 1983 / Fofonoff & Millard** for typical CTD work  
by fixing **salinity = 35 PSU, temperature = 0 °C, latitude = 0 °**  
and approximating gravity as

```
g(p,φ=0) = 9.780318 + 1.092×10⁻⁶ p
```

Depth is then

```
z = [ ((-1.82×10⁻¹⁵ p + 2.279×10⁻¹⁰) p - 2.2512×10⁻⁵) p + 9.72659 ] · p / g
```

Accuracy: < 0.2 m for 0–10 000 dbar.

---

## 🌐 Languages

| Language | File                                   |
| -------- | -------------------------------------- |
| English  | `locale/en_US/LC_MESSAGES/messages.mo` |
| 中文     | `locale/zh_CN/LC_MESSAGES/messages.mo` |

Add more: `pybabel init -l <lang>` → translate → compile.

---

## 🛠️ Build from source

```bash
git clone https://github.com/iyuxiaoyan/pressure_to_depth.git
cd pressure_to_depth
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pybabel compile -d locale
pyinstaller pressure2depth.spec
```

---

## 📄 License

MIT © 2025 — feel free to fork, embed, or redistribute.
