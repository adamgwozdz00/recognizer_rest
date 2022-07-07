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


