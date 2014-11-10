# -*- coding: utf-8 -*-

import os

from get_europarl import download_europarl_cmd
from preprocess_europarl import tokenize_europarl_cmd, clean_europarl_cmd
from preprocess_europarl import train_truecase_europarl_cmd, truecase_europarl_cmd

from util import create_experiment

moses_script_path = "/home/alvas/mosesdecoder/scripts"
shutup=False

# Creates experiment
expname = "europarl_pbsmt_en_de"
script = create_experiment(expname, moses_script_path)

# Download Europarl
dl_europarl = download_europarl_cmd('en', 'de', 'corpus.org', 
                                    shutup=shutup) 

# Tokenize Europarl files
tk_europarl = tokenize_europarl_cmd('en', 'de', 'corpus.org', 'corpus.tok', 
                                    shutup=shutup)


# Train Truecaser Europarl files
trtc_europarl = train_truecase_europarl_cmd('en', 'de', 'corpus.tok',
                                          shutup=shutup)

# Truecase Europarl files
tc_europarl = truecase_europarl_cmd('en', 'de', 'corpus.tok', shutup=shutup)

# Clean Europarl files
cl_europarl = clean_europarl_cmd('en', 'de', 'corpus.tok', 1, 40,  
                                 shutup=shutup, truecase=True)


script += dl_europarl + tk_europarl + trtc_europarl + tc_europarl +  cl_europarl

for i in script:
    print i