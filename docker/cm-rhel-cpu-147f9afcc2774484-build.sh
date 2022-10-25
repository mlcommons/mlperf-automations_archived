#! /bin/bash

# rhel [9]

export CM_OS_NAME="rhel"
export CM_OS_VERSION="9"

docker build -f cm-rhel-cpu-147f9afcc2774484.Dockerfile \
   -t ckrepo/cm-rhel-cpu-147f9afcc2774484:${CM_OS_NAME}-${CM_OS_VERSION} \
   --build-arg cm_os_name=${CM_OS_NAME} \
   --build-arg cm_os_version=${CM_OS_VERSION} \
   .

#    --build-arg cm_version=1.0.1 \
