FROM tensorflow/tensorflow:2.10.0-gpu
WORKDIR ./

RUN apt-get update \
&& apt-get install --no-install-recommends -y \
libgl1-mesa-glx libglib2.0-0 python3 python3-pip \
&& pip install numpy \
&& pip install segmentation-models \
&& pip install opencv-python \
&& pip install Pillow \

&& rm -rf /var/lib/apt/lists/*

COPY . .

ENTRYPOINT [ "python3", "predict_roads_paint.py"]