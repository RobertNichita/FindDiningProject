sudo mkdir efs
sudo apt-get install --upgrade
sudo apt-get install nfs-common
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-7d0bd005.efs.us-east-2.amazonaws.com:/ efs
