#!/bin/csh -f

python dict_ja.py ja_phrase ja_test_con | perl mt_cliant.pl > mt_result
python bleu.py result > mt_result
csh bleu_check/score.sh