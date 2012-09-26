#!/bin/csh -f

python output.py ja_test_con | perl mt_cliant.pl > mt_result
csh bleu_check/score.sh
