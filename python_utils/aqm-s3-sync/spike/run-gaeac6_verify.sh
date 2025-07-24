#!/bin/bash

root=/gpfs/f6/bil-fire8/scratch/Benjamin.Koziol/sandbox/AQM-utils/python_utils/aqm-s3-sync
conda_bin=/gpfs/f6/bil-fire8/scratch/Benjamin.Koziol/sandbox/miniconda3/condabin/conda
test_path=/gpfs/f6/bil-fire8/scratch/Benjamin.Koziol/sandbox/AQM-utils/python_utils/aqm-s3-sync/spike/gaeac6_verify.py

export PYTHONPATH=${root}/src:${PYTHONPATH}

${conda_bin} run -n benkozi-work --no-capture-output pytest -s ${test_path}
