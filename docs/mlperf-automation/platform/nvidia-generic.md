# Nvidia-based generic platforms with Ubuntu

* Ubuntu 18.04 or 20.04
* Sample platform: Lenovo T470p with Nvidia GeForce 940MX 2GB


## Notes

* [20210421] Grigori tested ck venv to prepare CK virtual environment 
  and build several python versions - it worked fine.

* [20210421] Grigori managed to build the latest loadgen 
  from [MLCommons inference](https://github.com/mlcommons/inference/tree/master/loadgen)
  (both python version and static library).


## Prerequisites

### Standard software
```
sudo apt install \
           git wget zip bzip2 libz-dev libbz2-dev cmake curl \
           openssh-client vim mc tree \
           gcc g++ autoconf autogen libtool make libc6-dev \
           libssl-dev libbz2-dev libffi-dev \
           python3 python3-pip python3-dev

pip3 install virtualenv
```

### CUDA driver

* TBD

### CUDA SDK

* TBD

### cuDNN


### TensorRT


## Test CK automation (platform detection)

```
ck pull repo:ck-ml

ck detect platform.gpgpu --cuda
```



## Misc links
