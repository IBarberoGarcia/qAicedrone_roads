# Road and Road Markings Detection: qAicedrone-Roads. A Robust Tool for Road Marking Extraction Using Aerial Photogrammetry and U-Net

Docker for the detection of roads and road marking in UAV images as presented in the paper "qAicedrone-Roads. A Robust Tool for Road Marking Extraction Using Aerial Photogrammetry and U-Net"

The model weights can be downloaded from: [Weights](https://upvedues-my.sharepoint.com/:f:/g/personal/inbargar_upv_edu_es/EtGpqhV1xN9OnFMkpg7WqI4BpnJqgUhKx5Pt-f8TekiB1g?e=qQAAYM)

Build docker:

```
docker build -f Dockerfile -t roads .
```


Detect roads:

```
docker run -it --rm --gpus all -v  D:/AICEDRONE/Roads/data_predict:/data roads /data/images/ /data/predictions/ UNet-Road.h5
```

Detect markings:

```
docker run -it --rm --gpus all -v  D:/AICEDRONE/Roads/data_predict:/data roads /data/images/ /data/predictions/ UNet-Paint.h5
```
