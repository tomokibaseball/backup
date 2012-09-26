#!/usr/bin/perl 
#提案法の翻訳結果の句読点のを修正(手動)

my $file = "bleu1";

open(IN, $file) or die "Can't open $file: $!\n";
while(<IN>){
 
   s/\. \?/\?/g;
   s/\? \./\?/g;
   s/\. \./\./g;
   print;
  }


