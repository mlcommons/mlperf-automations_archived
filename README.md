[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)

[![CM test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)
[![CM script automation features test](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml)

### About

The [Collective Knowledge project](https://arxiv.org/abs/2011.01149)
is motivated by our tedious experience reproducing experiments 
from [150 research papers](https://learning.acm.org/techtalks/reproducibility)
and validating them in the real world. 
We decided to collaborate with the community and [MLCommons](https://mlcommons.org)
to develop a [free, open-source and technology-agnostic platform](platform)
that can help everyone reproduce any novel technology including new ML models 
and end-to-end AI applications and optimize them in a fully automated way
in terms of costs, accuracy, performance, power consumption and other metrics
across any rapidly evolving software, hardware and data via 
public or private challenges.

This platform is powered by the [Collective Mind workflow automation framework (CM aka CK2)](https://github.com/mlcommons/ck/tree/master/cm/cmind) -
the 2nd version of the [CK framework](https://arxiv.org/abs/2011.01149) 
originally designed by the [cTuning foundation](https://cTuning.org) and donated to MLCommons in 2022.
It is being developed by the [open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)
to help users of the [CK platform](https://x.cKnowledge.org) solve the "dependency hell" and interconnect diverse and rapidly evolving software and hardware
from any company including Nvidia, Intel, Qualcomm, AMD, Microsoft, Amazon, Google, 
Neural Magic, Meta, OctoML, Krai, cKnowledge and Hugging Face in a transparent and non-intrusive way
using  [portable CM scripts  developed by the community](https://github.com/mlcommons/ck/blob/master/docs/list_of_scripts.md).

For example, [CK has already helped](https://access.cknowledge.org/playground/?action=challenges&name=optimize-mlperf-inference-v3.0-2023) 
the community, cTuning foundation, Qualcomm, Neural Magic, Krai, DELL, HPE and Lenovo
automate 98% of all recent MLPerf inference benchmark submissions, make them more reproducible and reusable,
and obtain record inference performance on the latest Qualcomm and Nvidia devices.

We continue improving the MLCommons CK/CM technology to help AI, ML and systems developers focus on innovation 
by automating all their tedious and repetitive tasks
and slashing their research, development, benchmarking, optimization, reproducibility and deployment time and costs
by 10..100 times across continuously changing software, hardware and data.

The ultimate goal for our Collective Knowledge platform is to help everyone automatically generate the most efficient, reproducible and deployable 
solutions for their applications using the most suitable software and hardware stack at any given time (model, framework, inference engine and any other related dependency) 
based on their requirements and constraints including costs, throughput, latency, power consumption, accuracy, target devices (cloud/edge/mobile/tiny), 
environment and data. 


### Discussions

Join our [Discord server](https://discord.gg/JjWNWXKxwT) 
to learn more about our technology, participate in public developments and discussions,
and request platform features and support for your technology.

### Documentation and the Getting Started Guide

* [Table of contents](https://github.com/mlcommons/ck/tree/master/docs/README.md)

### Copyright

2021-2023 [MLCommons](https://mlcommons.org)

### License

Apache 2.0

### Authors and maintainers

* [Grigori Fursin](https://cKnowledge.org/gfursin)
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh)

### Acknowledgments

This project is supported by [MLCommons](https://mlcommons.org), [cTuning foundation](https://cTuning.org),
[cKnowledge](https://cKnowledge.org) and [individual contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md).
