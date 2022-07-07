## Wstęp
Aplikacja służąca do detekcji obiektów na obrazie wykorzystująca nauczony przez nas model sztucznej inteligencji.

## Instalacja

### Instrukcja docker
### Ważne!!!
### Docker desktop i powershell uruchamiamy jako administrator!!!!

### Instalacja i konfiguracja dockera
![Zrzut ekranu 2022-06-04 094436](https://user-images.githubusercontent.com/70854700/171991233-57163201-a008-492f-9de7-51bcc585addc.png)
![Zrzut ekranu 2022-06-04 094648](https://user-images.githubusercontent.com/70854700/171991234-da141be4-462d-4d88-bb30-bef61921f224.png)
![Zrzut ekranu 2022-06-04 095026](https://user-images.githubusercontent.com/70854700/171991235-36ddac99-f2aa-4b37-b517-bdea66707014.png)
![Zrzut ekranu 2022-06-04 100000](https://user-images.githubusercontent.com/70854700/171991236-5d93143a-020b-43c9-940b-3308986e6dff.png)
![Zrzut ekranu 2022-06-04 100957](https://user-images.githubusercontent.com/70854700/171991237-cd00b11d-155d-4d6e-a09c-a9baf16ef68a.png)
![Zrzut ekranu 2022-06-04 101025](https://user-images.githubusercontent.com/70854700/171991239-156d0bba-3f9f-4cc7-ac56-72fe84e77cf3.png)

![Zrzut ekranu 2022-06-04 101041](https://user-images.githubusercontent.com/70854700/171991240-a7623d3c-6fa5-451e-8c74-fa3f709fd6e0.png)
![obraz](https://user-images.githubusercontent.com/70854700/177262874-eec906b4-8e42-4249-933e-1a6aea3145ec.png)

### Odpalenie aplikacji

### Wklejamy do powershela:
`docker pull adamgwozdz00/recognizer_api` - zaciąga obraz dockerowy backendowej aplikacji z sieci (może potrwać bo waży 3.27 GB)
`docker run -d -p 5001:5001 adamgwozdz00/recognizer_api` - po zakończeniu powyższego, odpala backendową aplikację na porcie `5001`

![Zrzut ekranu 2022-06-04 101528](https://user-images.githubusercontent.com/70854700/171991241-6d8643fa-330f-414e-94b6-fa9dddd106e3.png)

### Test działania
![obraz](https://user-images.githubusercontent.com/70854700/177262037-ca671377-dc76-4fbf-b46e-929846e7e1ab.png)
### Strona startowa
![Zrzut ekranu 2022-06-04 101719](https://user-images.githubusercontent.com/70854700/171991246-3d10c43e-2d45-4346-bd3a-356afe7472d2.png)
### Przesłanie zdjęcia postman 
https://www.postman.com/
![Zrzut ekranu 2022-07-4 o 23 36 32](https://user-images.githubusercontent.com/70854700/177261272-f5da11ac-9c7b-4dd5-a001-41850638963d.png)
![obraz](https://user-images.githubusercontent.com/70854700/177262210-86a46d88-815c-44eb-8779-45c46bd27196.png)

### Odbieramy zdjęcie postmanem

<img width="1050" alt="obraz" src="https://user-images.githubusercontent.com/70854700/177870581-ca6ae499-1379-4267-998a-d093f30a7a5b.png">

### Kopiujemy zdekodowane zdjęcie i wklejamy na stronę https://codebeautify.org/base64-to-image-converter

<img width="975" alt="obraz" src="https://user-images.githubusercontent.com/70854700/177870997-eb4ebee7-81b0-4aa0-bd40-488d0a15462e.png">

## Lokalne budowanie obrazu docerowego
Zamiast `docker pull adamgwozdz00/recognizer_api` można zbudować obraz u siebie, w tym celu należy:
1. Pobrać plik best.py z https://drive.google.com/file/d/1rKmrWHcD3Y5qrC_3fq-XIXHIcGRX1qdg/view?usp=sharing
2. Sciągnąć to repozytorium
3. Sciągnąć oprogramowanie yolov5 `git clone https://github.com/ultralytics/yolov5.git`
4. W folderze yolov5 stworzyć foldery -> `runs/train/exp/weights` i wrzucić do weights plik best.pt
5. Przenieść folder yolov5 do folderu recognizer_api
6. W folderze recognizer_api wpisać komende `docker build -t nazwa_obrazu .`
7. Odpalić aplikację `docker run -d -p 5001:5001 nazwa_aplikacji`

Podczas 1 odpalenia aplikacji może być problem z detekcją obrazu ponieważ yolov5 nie widzi biblioteki, w takim przpadku należy poczekać do ok 15 min aż biblioteki zostaną uaktualnione i można wysłać rządanie o pobranie rozpoznanego zdjęcia.
![image](https://user-images.githubusercontent.com/70854700/177876029-3b7e1977-5f56-4365-9d0c-22a4b610ba2b.png)

```
 * Serving Flask app 'application.app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
detect: weights=['yolov5/runs/train/exp/weights/best.pt'], source=application/resources/images/image.jpg, data=yolov5/data/coco128.yaml, imgsz=[480, 480], conf_thres=0.5, iou_thres=0.45, max_det=1000, device=, view_img=False, save_txt=False, save_conf=False, save_crop=False, nosave=False, classes=None, agnostic_nms=False, augment=False, visualize=False, update=False, project=yolov5/runs/detect, name=exp, exist_ok=False, line_thickness=3, hide_labels=False, hide_conf=False, half=False, dnn=False
requirements: torch!=1.12.0,>=1.7.0 not found and is required by YOLOv5, attempting auto-update...
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
torchvision 0.13.0 requires torch==1.12.0, but you have torch 1.11.0 which is incompatible.
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
WARNING: You are using pip version 22.0.4; however, version 22.1.2 is available.
You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.
Collecting torch!=1.12.0,>=1.7.0
  Downloading torch-1.11.0-cp38-cp38-manylinux1_x86_64.whl (750.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 750.6/750.6 MB ? eta 0:00:00
Requirement already satisfied: typing-extensions in /usr/local/lib/python3.8/site-packages (from torch!=1.12.0,>=1.7.0) (4.2.0)
Installing collected packages: torch
  Attempting uninstall: torch
    Found existing installation: torch 1.12.0
    Uninstalling torch-1.12.0:
      Successfully uninstalled torch-1.12.0
Successfully installed torch-1.11.0

requirements: torchvision!=0.13.0,>=0.8.1 not found and is required by YOLOv5, attempting auto-update...
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
WARNING: You are using pip version 22.0.4; however, version 22.1.2 is available.
You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.
Collecting torchvision!=0.13.0,>=0.8.1
  Downloading torchvision-0.12.0-cp38-cp38-manylinux1_x86_64.whl (21.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 21.0/21.0 MB 5.0 MB/s eta 0:00:00
Requirement already satisfied: pillow!=8.3.*,>=5.3.0 in /usr/local/lib/python3.8/site-packages (from torchvision!=0.13.0,>=0.8.1) (9.2.0)
Requirement already satisfied: typing-extensions in /usr/local/lib/python3.8/site-packages (from torchvision!=0.13.0,>=0.8.1) (4.2.0)
Requirement already satisfied: numpy in /usr/local/lib/python3.8/site-packages (from torchvision!=0.13.0,>=0.8.1) (1.22.4)
Requirement already satisfied: torch==1.11.0 in /usr/local/lib/python3.8/site-packages (from torchvision!=0.13.0,>=0.8.1) (1.11.0)
Requirement already satisfied: requests in /usr/local/lib/python3.8/site-packages (from torchvision!=0.13.0,>=0.8.1) (2.27.1)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.8/site-packages (from requests->torchvision!=0.13.0,>=0.8.1) (1.26.9)
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.8/site-packages (from requests->torchvision!=0.13.0,>=0.8.1) (2022.5.18.1)
Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.8/site-packages (from requests->torchvision!=0.13.0,>=0.8.1) (2.0.12)
Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.8/site-packages (from requests->torchvision!=0.13.0,>=0.8.1) (3.3)
Installing collected packages: torchvision
  Attempting uninstall: torchvision
    Found existing installation: torchvision 0.13.0
    Uninstalling torchvision-0.13.0:
      Successfully uninstalled torchvision-0.13.0
Successfully installed torchvision-0.12.0

requirements: 2 packages updated per /yolov5/requirements.txt
requirements: ⚠️ Restart runtime or rerun command for updates to take effect

/bin/sh: 1: git: not found
YOLOv5 🚀 2022-7-7 Python-3.8.13 torch-1.12.0+cu102 CPU

Fusing layers... 
YOLOv5x summary: 444 layers, 86193601 parameters, 0 gradients, 203.8 GFLOPs
image 1/1 /application/resources/images/image.jpg: 320x480 3 srubas, Done. (2.433s)
Speed: 2.3ms pre-process, 2433.2ms inference, 47.7ms NMS per image at shape (1, 3, 480, 480)
Results saved to yolov5/runs/detect/exp
``` - takie logi mogą wystąpić


Pojawienie się 
```YOLOv5 🚀 2022-7-7 Python-3.8.13 torch-1.12.0+cu102 CPU

Fusing layers... 
YOLOv5x summary: 444 layers, 86193601 parameters, 0 gradients, 203.8 GFLOPs
image 1/1 /application/resources/images/image.jpg: 320x480 3 srubas, Done. (2.433s)
Speed: 2.3ms pre-process, 2433.2ms inference, 47.7ms NMS per image at shape (1, 3, 480, 480)
Results saved to yolov5/runs/detect/exp```
- zwiastuje sukcess w działaniu
