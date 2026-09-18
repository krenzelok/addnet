### This is a python script that adds your wifi automaticly into the wpa_supplicant.conf config file
## Compiling and installing
Get the repo
```bash
git clone https://github.com/krenzelok/addnet.git
```
Change directory
```bash
cd addnet
```
Get the requrd dependencies

For chimera/alpine run
```bash
doas apk add uv
```
For void run
```bash
sudo xbps-install -S uv
```
For any other distos
install thru your package manager uv

Make an new enviroment
```bash
uv venv compile
```
Activate it
```bash
source ./compile/bin/activate
```
Install pyinstaller (dont worry it just installs into the new enviroment)
```bash
uv pip install pyinstaller
```
To compile it run
```bash
pyinstaller --onefile ./addnet.py
```
install
```bash
install -Dm755 ./dist/addnet "${PREFIX:-/usr/local}/bin/addnet"
```
