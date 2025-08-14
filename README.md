````markdown
# BPT Robotics – Ljubljana 2025

Ez a projekt a **BPT Robotics** 2025-ös ljubljanai versenyére készült robotrendszer teljes kódját és dokumentációját tartalmazza.  
A rendszer **Ubuntu 20.04.5 Server** operációs rendszeren fut, Raspberry Pi és egyéb perifériák segítségével.

---

## 📌 Áttekintés

Ez a robot önálló navigációs képességekkel, érzékelőintegrációval és versenyre optimalizált vezérlési logikával rendelkezik.  
A projekt célja, hogy gyorsan telepíthető és karbantartható legyen, valamint biztosítsa a stabil teljesítményt a versenyhelyzetekben.

**Főbb jellemzők:**
- Raspberry Pi alapú vezérlés
- Lidar-alapú térérzékelés
- Több modulból álló kódstruktúra (navigáció, érzékelők, motorvezérlés)
- Könnyen telepíthető és futtatható

---

## 🛠 Hardverkövetelmények

- Raspberry Pi (Bookworm vagy újabb támogatással)
- **YDLidar X4 Pro** érzékelő
- Motorvezérlő modul(ok)
- 3D nyomtatott alkatrészek
- Egyéb szenzorok a feladatnak megfelelően

---

## 🚀 Telepítés és futtatás

1. Klónozd a repót:
   ```bash
   git clone https://github.com/BPTRobotics/BPTrobotics-Ljubjana-2025.git
   cd BPTrobotics-Ljubjana-2025
````

2. Függőségek telepítése:

   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install python3 python3-pip
   pip3 install -r requirements.txt
   ```

3. A robot futtatása:

   ```bash
   python3 main.py
   ```

---

## 🖥 Operációs rendszer kompatibilitás

✅ Teljes mértékben kompatibilis **Ubuntu 20.04.5 Server** verzióval.

---

## 📊 Rendszerfolyamat

![flowchart.jpg](flowchart.jpg)

---

## 📄 YDLidar X4 Pro – Raspberry Pi Bookworm beállítás

A Raspberry Pi Bookworm OS-ben a `/dev/ttyUSB0` eszköz automatikusan csatlakozik a `dialout` és `plugdev` csoportokhoz.
Ezért szükséges hozzáadni a felhasználót ezekhez a csoportokhoz:

```bash
sudo usermod -aG dialout $USER
sudo usermod -aG plugdev $USER
```

Majd újraindítani a rendszert, vagy kijelentkezni és vissza.

A **YDLidar SDK** telepítéséhez:

```bash
sudo apt install cmake pkg-config
git clone https://github.com/YDLIDAR/YDLidar-SDK.git
cd YDLidar-SDK
mkdir build && cd build
cmake ..
make
sudo make install
```

Tesztelés:

```bash
ydlidar_test
```
