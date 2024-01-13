#!/bin/bash

CUR_DIR=$PWD
SCRIPT_DIR=${CM_TMP_CURRENT_SCRIPT_PATH}

folder=${CM_GIT_CHECKOUT_FOLDER}
if [ ! -d "${CM_TMP_GIT_PATH}" ]; then
  rm -rf ${folder}
  echo "******************************************************"
  echo "Cloning ${CM_GIT_REPO_NAME} from ${CM_GIT_URL}"
  echo "${CM_GIT_CLONE_CMD}";

  ${CM_GIT_CLONE_CMD}
  if [ "${?}" != "0" ]; then exit 1; fi

  cd ${folder}

  if [ ! -z ${CM_GIT_SHA} ]; then

    echo ""
    cmd="git checkout -b ${CM_GIT_SHA} ${CM_GIT_SHA}"
    echo "$cmd"
    eval "$cmd"
  fi
  if [ "${?}" != "0" ]; then exit 1; fi

  if [ ! -z ${CM_GIT_CHECKOUT_TAG} ]; then

    echo ""
    cmd="git fetch --all --tags"
    echo "$cmd"
    eval "$cmd"
    cmd="git checkout tags/${CM_GIT_CHECKOUT_TAG} -b ${CM_GIT_CHECKOUT_TAG}"
    echo "$cmd"
    eval "$cmd"
  fi
  if [ "${?}" != "0" ]; then exit 1; fi

else
  cd ${folder}
fi


IFS=',' read -r -a submodules <<< "${CM_GIT_SUBMODULES}"

for submodule in "${submodules[@]}"
do
    echo "Initializing submodule ${submodule}"
    git submodule update --init "${submodule}"
    if [ "${?}" != "0" ]; then exit 1; fi
done

if [ ${CM_GIT_PATCH} == "yes" ]; then
  IFS=', ' read -r -a patch_files <<< ${CM_GIT_PATCH_FILEPATHS}
  for patch_file in "${patch_files[@]}"
  do
    echo "Applying patch $patch_file"
    git apply "$patch_file"
    if [ "${?}" != "0" ]; then exit 1; fi
  done
fi
cd "$CUR_DIR"
