#cmsBatch.py 1 dimuonanalyzer_pileup_1_cfg.py -o Out/11 -r /castor/cern.ch/user/t/tjkim/ntuple/pileupstudy/RD_topref/pileup1/vallot.root -b 'bsub -q 1nh < batchScript.sh' 
#cmsBatch.py 1 dimuonanalyzer_pileup_2_cfg.py -o Out/12 -r /castor/cern.ch/user/t/tjkim/ntuple/pileupstudy/RD_topref/pileup2/vallot.root -b 'bsub -q 1nh < batchScript.sh' 
#cmsBatch.py 1 dimuonanalyzer_pileup_3_cfg.py -o Out/13 -r /castor/cern.ch/user/t/tjkim/ntuple/pileupstudy/RD_topref/pileup3/vallot.root -b 'bsub -q 1nh < batchScript.sh' 
cmsBatch.py 1 dimuonanalyzer_pileup_4_cfg.py -o Out/14 -r /castor/cern.ch/user/t/tjkim/ntuple/pileupstudy/RD_topref/pileup4/vallot.root -b 'bsub -q 1nh < batchScript.sh'

#cmsBatch.py 1 dimuonanalyzer_nopileup_1_cfg.py -o Out/21 -r /castor/cern.ch/user/t/tjkim/ntuple/pileupstudy/RD_topref/nopileup1/vallot.root -b 'bsub -q 1nh < batchScript.sh' 
#cmsBatch.py 1 dimuonanalyzer_nopileup_2_cfg.py -o Out/22 -r /castor/cern.ch/user/t/tjkim/ntuple/pileupstudy/RD_topref/nopileup2/vallot.root -b 'bsub -q 1nh < batchScript.sh' 
#cmsBatch.py 1 dimuonanalyzer_nopileup_3_cfg.py -o Out/23 -r /castor/cern.ch/user/t/tjkim/ntuple/pileupstudy/RD_topref/nopileup3/vallot.root -b 'bsub -q 1nh < batchScript.sh' 
#cmsBatch.py 1 dimuonanalyzer_nopileup_4_cfg.py -o Out/24 -r /castor/cern.ch/user/t/tjkim/ntuple/pileupstudy/RD_topref/nopileup4/vallot.root -b 'bsub -q 8nm < batchScript.sh'
