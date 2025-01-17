#!/bin/csh -f

set tool=/project/nakamura-lab01/Share/Tools
set my_dir=/home/is/tomoki-f
set xml = btec.tuned-filtered.output.sgm
set sor = btec_test_ja.sgm
set ref = btec_ref_en.sgm
set log = log

$tool/scripts/wrap-xml.perl /home/is/tomoki-f/sim/bleu_check/$xml en my-system-name < /home/is/tomoki-f/sim/mt_result > /home/is/tomoki-f/sim/bleu_check/mt_result.sgm
$tool/mteval-v11b.pl -s $my_dir/sim/bleu_check/$sor -r $my_dir/sim/bleu_check/$ref -t $my_dir/sim/bleu_check/mt_result.sgm -c > $log
