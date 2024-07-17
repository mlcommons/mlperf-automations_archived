#!/bin/bash

export CM_DOCKER_BUILD_ARGS="GID=\" $(id -g $USER) \" UID=\" $(id -u $USER) \" ${CM_DOCKER_BUILD_ARGS}"
export CM_BUILD_DOCKERFILE="no"
export CM_DOCKERFILE_WITH_PATH="/home/anandhu/CM/repos/anandhu-eng@cm4mlops/script/run-vllm-server/dockerfiles/pytorch:24.06-py3.Dockerfile"
export CM_DOCKER_ADD_ALL_GPUS="True"
export CM_DOCKER_BUILD_ARGS="--build-arg GID=\" $(id -g $USER) \" --build-arg UID=\" $(id -u $USER) \""
export CM_DOCKER_BUILD_CMD="docker build  --no-cache --build-arg GID=\" $(id -g $USER) \" --build-arg UID=\" $(id -u $USER) \" -f "/home/anandhu/CM/repos/anandhu-eng@cm4mlops/script/run-vllm-server/dockerfiles/pytorch:24.06-py3.Dockerfile" -t "cknowledge/cm-script-run-vllm-server:ubuntu-22.04-latest" ."
export CM_DOCKER_CACHE="no"
export CM_DOCKER_CACHE_ARG=" --no-cache"
export CM_DOCKER_DETACHED_MODE="no"
export CM_DOCKER_EXTRA_RUN_ARGS=" --ulimit memlock=-1"
export CM_DOCKER_IMAGE_BASE="ubuntu:22.04"
export CM_DOCKER_IMAGE_NAME="cm-script-run-vllm-server"
export CM_DOCKER_IMAGE_RECREATE="yes"
export CM_DOCKER_IMAGE_REPO="cknowledge"
export CM_DOCKER_IMAGE_TAG="ubuntu-22.04-latest"
export CM_DOCKER_IMAGE_TAG_EXTRA="-latest"
export CM_DOCKER_INTERACTIVE_MODE="True"
export CM_DOCKER_OS="ubuntu"
export CM_DOCKER_OS_VERSION="22.04"
export CM_DOCKER_PORT_MAPS="['8000:8000']"
export CM_DOCKER_PRE_RUN_COMMANDS="[]"
export CM_DOCKER_RUN_CMD="cm run script --tags=run,vllm-server --model=NousResearch/Hermes-2-Theta-Llama-3-8B --api_key= --adr.cuda.version=12.4.1 --skip_docker_model_download=True  --docker_run_deps "
export CM_DOCKER_RUN_SCRIPT_TAGS="run,server,vllm,vllm-server"
export CM_DOCKER_VOLUME_MOUNTS="[]"
export CM_MLOPS_REPO="anandhu-eng@cm4mlops"
export CM_QUIET="yes"
export CM_REAL_RUN="True"
export CM_RUN_STATE_DOCKER="True"
export CM_TMP_CURRENT_PATH="/home/anandhu/CM/repos/anandhu-eng@cm4mlops/script/run-vllm-server"
export CM_TMP_CURRENT_SCRIPT_PATH="/home/anandhu/CM/repos/anandhu-eng@cm4mlops/script/build-docker-image"
export CM_TMP_CURRENT_SCRIPT_REPO_PATH="/home/anandhu/CM/repos/anandhu-eng@cm4mlops"
export CM_TMP_CURRENT_SCRIPT_REPO_PATH_WITH_PREFIX="/home/anandhu/CM/repos/anandhu-eng@cm4mlops"
export CM_TMP_CURRENT_SCRIPT_WORK_PATH="/home/anandhu/CM/repos/anandhu-eng@cm4mlops/script/run-vllm-server/dockerfiles"
export CM_TMP_PIP_VERSION_STRING=""
export CM_VLLM_SERVER_API_KEY=""
export CM_VLLM_SERVER_MODEL_NAME="NousResearch/Hermes-2-Theta-Llama-3-8B"
export CM_VLLM_SKIP_DOCKER_MODEL_DOWNLOAD="True"


. "/home/anandhu/CM/repos/anandhu-eng@cm4mlops/script/build-docker-image/run.sh"
