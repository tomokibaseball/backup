#!/usr/bin/perl 
  
my $file = "/home/is/tomoki-f/btec_ja2en/evaluation/test.txt";

open(IN, $file) or die "Can't open $file: $!\n";
while(<IN>){
  s/"/\<seg id=$.\> /g;
  s/#/\<\/seg\>/g;
   print;
  }


close(IN);

   

