# Collective Knowledge approach

Research, development and deployment of novel technologies 
is becoming increasingly [challenging, time consuming, costly and messy](https://www.mihaileric.com/posts/mlops-is-a-mess).
We often have to spend lots of time on exciting development of ad-hoc automation scripts 
to connect numerous incompatible tools to build, test, optimize and deploy complex applications and manage all related artifacts 
across rapidly evolving software and hardware from the cloud to the edge.

The Collective Knowledge approach (CK) is to automatically turn ad-hoc scripts and artifacts from the community
into an open database of [reusable, portable, customizable and deterministic components](cm/docs/tutorial-scripts.md)
with no or minimal effort from a user.

All such components have a unified API, human readable CLI and extensible JSON/YAML meta description
making it possible to reuse them in different projects and chain them together 
into powerful, efficient and portable automation workflows, applications and web services
adaptable to continuously changing software and hardware.

Originally, we have developed CK to automate [reproducibility initiatives and artifact evaluation at conferences](https://cTuning.org/ae)
and make it easier for researchers and engineers to [validate their ideas in the real world](https://learning.acm.org/techtalks/reproducibility).
However, it turned out that the CK approach also helped [multiple organizations](https://cKnowledge.org/partners.html) 
modularize complex ML and AI Systems and automate their benchmarking, optimization and deployment.

That's why we have decided to donate CK to [MLCommons](https://mlcommons.org) to continue developing 
this technology, modularize AI Systems and support reproducible research as a community effort 
within the [public workgroup](docs/mlperf-education-workgroup.md).

Everyone is welcome to join our open workgroup to develop an open-source toolkit that can help everyone
share their knowledge, experience, artifacts and automation scripts in such a way 
that they can be easily tested, reused and enhanced by the community in other projects 
with different artifacts, software and hardware.

We hope that this open-source toolkit will help researchers and engineers get rid of repetitive and unnecessary tasks,
connect incompatible tools and modularize complex software systems, support reproducible research
and make it easier to bring novel technologies to the rapidly evolving world.

## Collective Mind toolkit

CM toolkit is the next generation of the [original CK framework](#collective-knowledge-framework-ck).
It is being developed by the [open workgroup](docs/mlperf-education-workgroup.md) with a primary focus 
to connect researchers and engineers to modularize AI and ML systems, 
make it easier to plug real-world tasks, models, data sets, software 
and hardware, automate their deployment in production,
and make them adaptable to continuously changing software and hardware 
from the cloud to the edge:

* [CM development page](cm)
* [CM motivation](cm/docs/motivation.md)
* [CM tutorial](cm/docs/tutorial-scripts.md)

[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Downloads](https://pepy.tech/badge/cmind)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](https://github.com/mlcommons/ck/tree/master/cm)

[![Documentation](https://img.shields.io/badge/Documentation-available%20online-green)](https://cKnowledge.org/docs/cm)
[![CM(CK2) test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)

(C)opyright 2022 [MLCommons](https://mlcommons.org)

## Collective Knowledge framework (CK)

This legacy framework was originally developed to [make it easier to reproduce research papers and validate them in production in the real world](https://learning.acm.org/techtalks/reproducibility).
After it was successfully validated in several [academic and industrial projects including MLPerf](https://cKnowledge.org/partners.html),
we donated CK to [MLCommons](https://mlcommons.org) to continue developing it as a community effort within the [open workgroup](docs/mlperf-education-workgroup.md).
The feedback from the users has helped our workgroup to develop the next generation of the CK technology called [Collective Mind](#collective-mind-toolkit).

Go to the [CK project page](ck1) to get the legacy CK framework v2.6.1 or check the [new CM (CK2) development project](#collective-mind-toolkit).

[![PyPI version](https://badge.fury.io/py/ck.svg)](https://badge.fury.io/py/ck)
[![Downloads](https://pepy.tech/badge/ck)](https://pepy.tech/project/ck)
[![Python Version](https://img.shields.io/badge/python-2.7%20|%203.4+-blue.svg)](https://pypi.org/project/ck)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](https://github.com/mlcommons/ck/tree/master/cm)

(C)opyright 2021-2022 [MLCommons](https://mlcommons.org)<br>
(C)opyright 2014-2021 [Grigori Fursin](https://cKnowledge.io/@gfursin) and the [cTuning foundation](https://cTuning.org)

## Our community projects

* [MLPerf education workgroup to modularize AI and ML Systems](docs/mlperf-education-workgroup.md)
* [Artifact evaluation and reproducibility initiatives at ML and Systems conferences](https://cTuning.org/ae)


## Contributing

The best way to contribute to this project is to join our [open workgroup](docs/mlperf-education-workgroup.md)
to help the community modularize AI, ML and other complex systems, 
share your ML artifacts and automations as [reusable CM scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
and improve the core CM functionality.

## Maintainers

* [Grigori Fursin](https://cKnowledge.io@gfursin)
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh)

## Acknowledgments

We would like to thank all [contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md) 
and [collaborators](https://cKnowledge.org/partners.html) for their support, fruitful discussions, 
and useful feedback! See more acknowledgments in the [CK journal article](https://arxiv.org/abs/2011.01149)
and our [ACM TechTalk](https://www.youtube.com/watch?v=7zpeIVwICa4).
