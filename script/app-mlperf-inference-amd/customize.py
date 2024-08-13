from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}
    env = i['env']

    if env.get('CM_MLPERF_SKIP_RUN', '') == "yes":
        return {'return':0}

    if 'CM_MODEL' not in env:
        return {'return': 1, 'error': 'Please select a variation specifying the model to run'}
    if 'CM_MLPERF_BACKEND' not in env:
        return {'return': 1, 'error': 'Please select a variation specifying the backend'}
    if 'CM_MLPERF_DEVICE' not in env:
        return {'return': 1, 'error': 'Please select a variation specifying the device to run on'}

    if llama2 in env['CM_MODEL']:
        env['CM_RUN_DIR'] = i['run_script_input']['path']
        env['CM_RUN_CMD'] = "bash run-llama2.sh "
    else:
        return {'return':1, 'error':'Model {} not supported'.format(env['CM_MODEL'])}
    

    return {'return':0}
    #return {'return':1, 'error': 'Run command needs to be tested'}


def postprocess(i):

    env = i['env']

    return {'return':0}
