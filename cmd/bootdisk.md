# create a bootable disk

```bash
sudo fdisk -l
```

```
Disk /dev/sdc: 58,98 GiB, 63333990400 bytes, 123699200 sectors
Disk model: Flash Disk      
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: F...
```
```bash
df
```
```
/dev/sdc1        4914194  4914194         0 100% /media/sander/Ubuntu 22.04.3 LTS amd64
/dev/sdc4       55718056     1384  52853880   1% /media/sander/writable
```

```bash
sudo umount /dev/sdc1
sudo umount /dev/sdc4
```

```bash
sudo mkfs.vfat /dev/sdc
```

```bash
sudo dd bs=4M if=kali-linux-2023.4-installer-amd64.iso of=/dev/sdc status=progress oflag=sync
```


