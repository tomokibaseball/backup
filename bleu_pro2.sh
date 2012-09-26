#!/bin/csh -f

set phrase = ja_dict_pro
set test_set = ja_test_con

python dict_ja_3.py $phrase $test_set | perl mt_cliant.pl > result
python bleu.py result > mt_result
csh bleu_check/score.sh
