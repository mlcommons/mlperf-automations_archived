﻿# Developer(s): Grigori Fursin

import cmind
import os
import misc

import streamlit.components.v1 as components

import streamlit as st

announcement = 'Under development - please get in touch via [Discord](https://discord.gg/JjWNWXKxwT) for more details ...'

initialized = False
external_module_path = ''
external_module_meta = {}

def main():
    params = misc.get_params(st)

    # Set title
    st.title('How to run benchmarks')

    st.markdown(announcement)

    return page(st, params)




def make_selection(st, selection, param_key, text, x_uid):

    x_meta = {}
    
    if len(selection)>0:
         selection = sorted(selection, key = lambda v: v['name'])

         if x_uid != '':
             x_meta = selection[0]
             st.markdown('Selected {}: {}'.format(text, x_meta['name']))
         else:
             x_selection = [{'name':''}]
             x_selection += selection
             
             x_id = st.selectbox('Select {}:'.format(text),
                                 range(len(x_selection)), 
                                 format_func=lambda x: x_selection[x]['name'],
                                 index = 0,
                                 key = param_key)

             if x_id>0:
                 x_meta = x_selection[x_id]

    return {'return':0, 'meta':x_meta}


def page(st, params, action = ''):

    global initialized, external_module_path, external_module_meta

    end_html = ''
    
    # Announcement
    st.markdown('----')
    st.markdown(announcement)
    

    ############################################################################################
    # Select target hardware
    compute_uid = ''
    x = params.get('compute_uid',[''])
    if len(x)>0 and x[0]!='': compute_uid = x[0].strip()
    
    ii = {'action':'load_cfg',
          'automation':'utils',
          'tags':'benchmark,compute',
          'skip_files':False}

    if compute_uid!='':
        ii['prune']={'uid':compute_uid}

    r = cmind.access(ii)
    if r['return']>0: return r

    r = make_selection(st, r['selection'], 'compute', 'target hardware', compute_uid)
    if r['return']>0: return r

    compute_meta = r['meta']
#    st.markdown(compute_meta)
        

    ############################################################################################
    # Select benchmark
    bench_uid = ''
    x = params.get('bench_uid',[''])
    if len(x)>0 and x[0]!='': bench_uid = x[0].strip()
    
    ii = {'action':'load_cfg',
          'automation':'utils',
          'tags':'benchmark,list',
          'skip_files':False}

    if bench_uid!='':
        ii['prune']={'uid':bench_uid}

    r = cmind.access(ii)
    if r['return']>0: return r

    r = make_selection(st, r['selection'], 'benchmark', 'benchmark', bench_uid)
    if r['return']>0: return r

    bench_meta = r['meta']
#    st.markdown(bench_meta)

    if len(bench_meta)>0:
        urls = bench_meta.get('urls',[])
        if len(urls)>0:
            x = '\n'
            for u in urls:
                name = u['name']
                url = u['url']

                x+=' [ [{}]({}) ] '.format(name, url)
            x+='\n'

            st.markdown(x)




    return {'return':0, 'end_html':end_html}
