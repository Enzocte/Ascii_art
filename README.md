# 📄 README.md

```markdown
# 🎨 ASCII Art Generator

A simple Python project that converts images into ASCII art using grayscale mapping.

## 📌 Features

- Convert any image into ASCII art
- Customizable output width
- Brightness-based character mapping
- Save result as a `.txt` file
- Optional cleaning of ANSI escape sequences

---

## 🧠 How it works

The program:
1. Loads an image
2. Resizes it while keeping aspect ratio
3. Converts it to grayscale
4. Maps pixel brightness to ASCII characters
5. Writes the result into a text file

Example of charset used:

```

$@B%8&WM#*oahkbdpqwmZO0QLCJU Xzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,"^'.

```

---

## 📂 Project Structure

```

Ascii_art/
│── image.py              # Main script: image → ASCII
│── clean_ascii.py        # Remove ANSI escape sequences
│
├── examples/
│   ├── images/
│   │   └── skull.png
│   └── result/
│       ├── Skull_ascii.txt
│       └── Skull_ascii_clean.txt

````

---

## ⚙️ Installation

```bash
pip install pillow numpy
````

---

## 🚀 Usage

### 1. Generate ASCII art

```bash
python image.py
```

This will:

* Read the image
* Generate ASCII output
* Save it in:

```
examples/result/Skull_ascii.txt
```

---

### 2. Clean ANSI characters (optional)

```bash
python clean_ascii.py
```

Output:

```
Skull_ascii_clean.txt
```

---

## 📊 Output Info

The script also prints:

* Image dimensions
* Max brightness
* Min brightness
* Mean brightness

---

## 🛠️ Customization

You can modify:

* `ascii_width` → resolution of ASCII output
* `charset` → style of rendering
* `myimgPath` → input image

---

## 📸 Example

```
@@@@@@@%%%%%%%#########***********
@@@@@@%%%%%%%########************
@@@%%%%%%%######********oooooooo
...
```

---

## 🧩 Dependencies

* Python 3
* Pillow
* NumPy

---

## 📄 License

MIT License

```