# 🖱️ Mouse Interaction & Drawing Applications (HCI)

## 📌 Project Overview

This repository contains three practical examples demonstrating **Human-Computer Interaction (HCI)** using mouse and touch input in Python.

The goal is to explore how users interact with systems through:

* Clicking
* Dragging
* Drawing gestures

---

## 📂 Project Structure

```
📁 project-folder
│── circle_draw.py        # Draw circle using mouse click (OpenCV)
│── rectangle_draw.py     # Draw rectangle using drag (OpenCV)
│── kivy_paint.py         # Full drawing app (Kivy)
│── README.md
```

---

## 🎯 Objectives

* Understand mouse event handling
* Implement interactive drawing
* Explore event-driven programming
* Build a simple painting application

---

## 🛠️ Technologies Used

* Python
* OpenCV
* Kivy

---

## ⚙️ Installation

Install required libraries:

```bash
pip install opencv-python
pip install kivy
```

---

## ▶️ How to Run

### 🔵 1. Draw Circle (OpenCV)

```bash
python circle_draw.py
```

📌 Click anywhere on the image → a green circle will be drawn.

---

### 🟡 2. Draw Rectangle (OpenCV)

```bash
python rectangle_draw.py
```

📌 Click and drag → rectangle will be drawn dynamically.

---

### 🎨 3. Kivy Drawing App

```bash
python kivy_paint.py
```

📌 Draw freely using mouse or touch.
📌 Each stroke has a different color.

---

## 💡 How It Works

### 🖥️ OpenCV Examples

* Uses `cv2.setMouseCallback()`
* Detects:

  * Mouse click
  * Movement
  * Release
* Executes drawing functions based on events

---

### 📱 Kivy Application

* Uses touch event system:

  * `on_touch_down` → start drawing
  * `on_touch_move` → continue drawing
* Each touch gets a unique color
* Supports multi-touch interaction

---

## 🚀 Features

* Real-time drawing
* Interactive UI
* Mouse & touch support
* Simple and easy to use

---

## 📚 HCI Relevance

This project demonstrates key HCI concepts:

* User interaction design
* Gesture-based input
* Real-time feedback
* Usability principles

---

## 🔮 Future Improvements

* Add undo/redo
* Save drawing as image
* Add color picker
* Implement gesture recognition



