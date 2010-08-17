
import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
		     noEventSort = cms.untracked.bool(True),
		     duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
		     fileNames = readFiles
                    )
readFiles.extend([
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_100_0_xwL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_101_0_SDQ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_102_1_4F6.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_103_2_T4B.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_104_2_fyL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_105_1_h8o.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_106_2_SDr.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_107_1_qkQ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_108_1_LBC.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_109_1_ic4.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_10_0_Pja.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_110_1_cj2.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_111_2_Jkn.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_112_1_ZPj.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_113_1_mDM.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_114_1_i6M.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_115_1_0q4.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_116_1_Ccs.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_117_1_sxo.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_118_0_9Bl.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_119_1_Hrt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_11_1_tSV.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_120_1_0nP.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_121_0_nFa.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_122_0_jO5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_123_1_G53.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_124_1_JWE.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_125_1_g3F.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_126_0_ksl.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_127_0_pUC.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_128_0_q9o.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_129_2_t41.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_12_1_Ei9.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_130_0_Hoq.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_131_1_VfB.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_132_1_I2c.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_133_0_UQ1.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_134_0_NaX.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_135_0_gFU.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_136_1_Kl7.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_137_1_QJS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_138_0_ffZ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_139_1_Lu5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_13_1_7pK.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_140_1_YRR.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_141_0_d4v.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_142_0_Y6N.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_143_0_Z8s.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_144_0_huG.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_145_1_DAF.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_146_1_5p4.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_147_1_FCz.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_148_1_ZDH.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_149_1_gAt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_14_1_TRV.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_150_1_W7n.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_151_0_nYS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_152_1_zu2.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_153_1_ru8.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_154_0_KsU.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_155_1_0Ss.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_156_1_Hul.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_157_1_B6B.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_158_0_nY4.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_159_0_af3.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_15_1_aIt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_160_1_MqC.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_161_0_nsP.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_162_1_Etv.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_163_2_MLl.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_164_0_DWE.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_165_0_1EJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_166_0_b4R.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_167_1_hFh.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_168_0_gZU.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_169_1_ga4.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_16_1_To6.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_170_1_53A.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_171_1_xVF.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_172_0_X0K.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_17_1_RHW.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_18_0_J8w.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_19_1_IEl.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_1_1_T29.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_20_0_f3P.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_21_0_iLA.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_22_0_ySL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_23_0_Wru.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_24_0_ZqL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_25_0_f3n.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_26_0_6tK.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_27_0_csP.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_28_1_8up.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_29_1_EfM.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_2_0_Kvy.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_30_0_1Ah.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_31_1_7Gz.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_32_1_2Ix.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_33_1_iJZ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_34_1_iZ5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_35_1_ncG.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_36_0_UQ7.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_37_1_VCe.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_38_1_QeM.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_39_0_HXJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_3_0_xsv.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_40_1_HfQ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_41_1_BAY.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_42_0_4EG.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_43_1_5IF.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_44_1_a7G.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_45_1_W4R.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_46_0_m5g.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_47_0_3nI.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_48_1_Mx1.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_49_1_Y4w.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_4_0_lwB.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_50_1_ZlT.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_51_1_OFs.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_52_1_Cgp.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_53_0_rVM.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_54_0_API.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_55_0_EAK.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_56_1_URy.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_57_1_Njo.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_58_0_pOx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_59_0_Vxn.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_5_1_OU5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_60_1_Mz5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_61_1_Vy3.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_62_0_Bsj.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_63_0_tDM.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_64_1_5Xw.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_65_1_eCc.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_66_0_5n1.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_67_1_Nq0.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_68_1_AMc.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_69_1_L6V.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_6_1_Fk3.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_70_0_mbP.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_71_0_8h2.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_72_0_UOy.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_73_1_Rm1.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_74_1_vPX.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_75_0_9y4.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_76_0_XLH.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_77_0_b3s.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_78_1_9kJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_79_1_xwA.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_7_1_QOt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_80_0_myd.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_81_0_wLJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_82_0_4mt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_83_1_Em1.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_84_1_xoJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_85_0_MBH.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_86_1_oax.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_87_1_tJ6.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_88_1_1cu.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_89_1_8iX.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_8_0_JAA.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_90_1_Mu9.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_91_0_DHt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_92_2_p48.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_93_1_isV.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_94_0_nGr.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_95_1_v8f.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_96_2_1xQ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_97_0_GWe.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_98_1_7Do.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_99_0_o6V.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13/Run2010A-PromptReco-v4/patTuple_muon_9_0_Exk.root',
]
        )
