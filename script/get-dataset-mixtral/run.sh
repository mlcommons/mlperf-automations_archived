#!/bin/bash

if [[ "$CM_DATASET_MIXTRAL_GENERATE_TEST_DATA" == "yes" ]]; then
  ${CM_PYTHON_BIN_WITH_PATH} ${CM_TMP_CURRENT_SCRIPT_PATH}/generate-test-dataset.py --dataset-path ${CM_DATASET_PREPROCESSED_PATH} --output-path ${CM_DATASET_MIXTRAL_TEST_DATA_GENERATED_PATH}
fi
