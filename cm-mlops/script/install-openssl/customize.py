from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']

    automation = i['automation']

    recursion_spaces = i['recursion_spaces']

    need_version = env.get('CM_VERSION','')
    if need_version == '':
        return {'return':1, 'error':'internal problem - CM_VERSION is not defined in env'}

    print (recursion_spaces + '    # Requested version: {}'.format(need_version))

    path_bin = os.path.join(os.getcwd(), 'install', 'bin')

    env['CM_TMP_PATH'] = path_bin
    env['CM_TMP_FAIL_IF_NOT_FOUND'] = 'yes'

    return {'return':0}

def postprocess(i):
    inp = i['input']
    env = i['env']
    tags = inp['tags']
    tag_list = tags.split(",")
    if "_shared" in tag_list:
        path_lib = os.path.join(os.getcwd(), 'install', 'lib')
        if '+LD_LIBRARY_PATH' not in env:
            env['+LD_LIBRARY_PATH'] = []
        env['+LD_LIBRARY_PATH'].append(path_lib)
    return {'return':0}
