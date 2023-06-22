from cmind import utils
import os

def preprocess(i):
    os_info = i['os_info']
    env = i['env']

    if env.get('CM_RUN_CMD','') == '':
        if env.get('CM_BIN_NAME','') == '':
            x = 'run.exe' if os_info['platform'] == 'windows' else 'run.out'
            env['CM_BIN_NAME'] = x

        if os_info['platform'] == 'windows':
            env['CM_RUN_CMD'] = env.get('CM_RUN_PREFIX','') + env['CM_BIN_NAME']
            if env.get('CM_RUN_SUFFIX','')!='':
                env['CM_RUN_CMD'] += ' '+env['CM_RUN_SUFFIX']

        else:
            if env['CM_ENABLE_NUMACTL'].lower() in ["on", "1", "true", "yes"]:
                env['CM_ENABLE_NUMACTL'] = "1"
                CM_RUN_PREFIX = "numactl " + env['CM_NUMACTL_MEMBIND'] + ' '
            else:
                CM_RUN_PREFIX = ''

            CM_RUN_PREFIX += env['CM_RUN_PREFIX'] if 'CM_RUN_PREFIX' in env else ''

            env['CM_RUN_PREFIX'] = CM_RUN_PREFIX

            CM_RUN_SUFFIX = (env['CM_REDIRECT_OUT'] + ' ') if 'CM_REDIRECT_OUT' in env else ''
            CM_RUN_SUFFIX += (env['CM_REDIRECT_ERR'] + ' ') if 'CM_REDIRECT_ERR' in env else ''

            env['CM_RUN_SUFFIX'] = env['CM_RUN_SUFFIX'] + CM_RUN_SUFFIX if 'CM_RUN_SUFFIX' in env else CM_RUN_SUFFIX

            if env.get('CM_RUN_DIR','') == '':
                env['CM_RUN_DIR'] = os.getcwd()

            env['CM_RUN_CMD'] = CM_RUN_PREFIX + ' ' + os.path.join(env['CM_RUN_DIR'],env['CM_BIN_NAME']) + ' ' + env['CM_RUN_SUFFIX']

    # Print info
    print ('***************************************************************************')
    print ('CM script::benchmark-program/run.sh')
    print ('')
    print ('Run Directory: {}'.format(env.get('CM_RUN_DIR','')))

    print ('')
    print ('CMD: {}'.format(env.get('CM_RUN_CMD','')))

    print ('')

    return {'return':0}

def postprocess(i):

    env = i['env']
    if env.get('CM_MLPERF_POWER', '') == "yes":
        if env.get('CM_MLPERF_SHORT_RANGING_RUN', '') == 'yes':
            os.system("echo '0' > count.txt")
            env['CM_MLPERF_RUN_CMD'] = "CM_MLPERF_RUN_COUNT=\$(cat count.txt); echo \${CM_MLPERF_RUN_COUNT};  CM_MLPERF_RUN_COUNT=\$((CM_MLPERF_RUN_COUNT+1));   echo \${CM_MLPERF_RUN_COUNT} > count.txt && if [ \${CM_MLPERF_RUN_COUNT} -eq \'1\' ]; then export CM_MLPERF_USER_CONF_PREFIX=\'ranging_\'; else export CM_MLPERF_USER_CONF_PREFIX=\'\'; fi && "+env['CM_RUN_CMD'].strip()
        else:
            env['CM_MLPERF_RUN_CMD'] = env['CM_RUN_CMD'].strip()

    return {'return':0}
