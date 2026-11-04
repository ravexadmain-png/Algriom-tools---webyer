# Wolfer Web Cloner & Extractor 🐺

A powerful terminal-based website cloning and asset extraction utility designed for Termux and Linux environments. It extracts core codes, stylesheets, scripts, 3D assets (`.glb`, `.gltf`, `.fbx`), configuration files, and hidden directories.

## 🛠 Features
- Extracts HTML, CSS, JS, XML, Python scripts, and PHP files.
- Extracts 3D models and media assets (`.glb`, `.gltf`, `.fbx`, `.png`, `.jpg`).
- Scans for hidden/master configuration files (`robots.txt`, `sitemap.xml`, etc.).
- Clean and colorful terminal user interface (CLI).

## 📥 Installation in Termux

Run the following commands in your Termux terminal:

```bash
pkg update && pkg upgrade
pkg install python git -y
git clone [https://github.com/YOUR_USERNAME/wolfer-web-cloner.git](https://github.com/YOUR_USERNAME/wolfer-web-cloner.git)
cd wolfer-web-cloner
pip install -r requirements.txt
python wolfer_cloner.py
