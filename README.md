# Лабораторийн ажил 14 — Python Image Library (Pillow)

## Суулгах

```bash
python3 -m pip install pillow numpy
```

## Өмнөх хэсэг

```bash
python3 draw_line.py
python3 draw_circle.py
```

## Нэмсэн даалгаврууд

### 1) Дүрсүүд зурах

```bash
python3 task1_draw_shapes.py
```

Гаралт:
- `task1_cross.png`
- `task1_circles.png`
- `task1_polygon.png`
- `task1_rectangles.png`
- `task1_all_shapes.png`

### 2) Thumbnails болгон нэгтгэх

1) 3 зураг `task2_input/` дотор хийнэ (`.jpg/.jpeg/.png`)
2) Дараах командыг ажиллуулна:

```bash
python3 task2_make_thumbnails.py
```

Гаралт:
- `task2_thumbnails_collage.png`

### 3) JPG -> PNG болгон хөрвүүлэх (өргөнийг өөрчлөхтэй)

`task3_input/` дотор JPG оруулаад:

```bash
python3 task3_jpg_to_png.py
```

Эсвэл:

```bash
python3 task3_jpg_to_png.py --input /path/to/file.jpg --output output.png --width 700
```

Гаралт (default):
- `task3_converted.png`

### 4) Монгол улсын төрийн далбаа (NumPy)

```bash
python3 task4_mongolia_flag_numpy.py
```

Гаралт:
- `task4_mongolia_flag.png`
