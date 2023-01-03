# Label format converter

If you have ever downloaded a public dataset to play with YOLO but found that the labels come in a different format, such as CVAT, COCO or PASCAL-VOC, I have created this script to make the conversion task easier.

I have tried to make it as modular as possible so that it can be integrated in other projects.

I hope you find it useful.

## Dependencies

```bash
cd label-format-converter
python3 -m pip install -r requeriments.txt
```

## Usage

Convert labels to YOLO format.

1. Place your labels into the correct folder.
   - CVAT: ~/label-format-converter/labels/cvat/*.xml
   - COCO: ~/label-format-converter/labels/coco/*.json
   - PASCAL: ~/label-format-converter/label/Annotations/*.xml
2. (CVAT/COCO) Rename labels file.
    - CVAT:  annotations.xml
    - COCO: instances_default.xml 
3. Launch de main script with the origin format label as argument.
```bash
cd label-format-converter
python3 main.py [-f --format] [cvat, coco, pascal]
```
4. Yolo folder will be created and the new labels will be placed in the next directory: ~/label-format-converter/labels/yolo

## License

[GNU GPL](https://choosealicense.com/licenses/gpl-3.0/)

## Author

Code with :yellow_heart: by _Adrián Rodríguez Galisteo_

- Github: https://github.com/adrirg9412/ 

- LinkedIn: https://www.linkedin.com/in/adrian-rodriguez-galisteo/

- Mail: adrirg9412@gmail.com