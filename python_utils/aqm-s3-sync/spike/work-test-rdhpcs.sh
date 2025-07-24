#!/bin/bash

set -xue

source ../../../gaea/env.sh

rm -rf /ncrc/home2/Benjamin.Koziol/l/scratch/tmp/aqm-use-case-download/*
git pull
${BWK_CONDA_RUN} pytest -s test_aqm_data_sync.py::test_main_gaeac6