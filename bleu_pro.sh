#!/bin/csh -f

set phrase = mon_0.5000_ja
set test_set = ja_test_con

python dict_ja.py $phrase $test_set | perl mt_cliant.pl > result
python bleu.py result > mt_result
csh bleu_check/score.sh
