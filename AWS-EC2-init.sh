#create mount point for EFS
sudo mkdir efs

#upgrade apt/apt-get, add deadsnakes for python install
sudo apt install
sudo apt install software-properties-common
sudo add-apt-repository --yes ppa:deadsnakes/ppa
sudo apt-get install --upgrade

#for mounting EFS
sudo apt-get install nfs-common

#install python and set correct python version
sudo apt install python3.8
sudo update-alternatives  --set python /usr/bin/python3.8

#install nvm and node.js 12.16.2
sudo apt install curl
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" 
nvm install 12.16.2

#install docker-compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

#mount external fs
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-7d0bd005.efs.us-east-2.amazonaws.com:/ efs

#cd into git repo
cd efs/scarb-dine-repo/team_08-project