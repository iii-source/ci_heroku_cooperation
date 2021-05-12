apt update
apt install sudo
apt install -y python3.8
apt install -y curl
apt install -y vim
# pip install時に使用する
apt-get install -y python3-distutils
apt-get install  -y git

python3.8 -V

# pip install
sudo curl -kL https://bootstrap.pypa.io/get-pip.py | python3.8
pip -V

pip install --user -r requirements.txt


