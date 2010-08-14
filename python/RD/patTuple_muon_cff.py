
import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
		     noEventSort = cms.untracked.bool(True),
		     duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
		     fileNames = readFiles
                    )
readFiles.extend([
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_10_1_xYF.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_11_1_YwG.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_12_1_s4l.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_13_1_ui7.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_14_1_KTB.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_15_1_ZZd.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_16_1_T7s.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_17_1_DYk.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_18_1_56c.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_19_1_n9z.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_1_1_yrr.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_20_0_h2g.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_21_1_NGz.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_22_1_OHD.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_23_1_bn0.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_24_1_hgs.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_25_1_p1Y.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_26_1_KrE.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_27_0_bdB.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_28_1_Dpt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_29_0_0Gg.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_2_1_CrT.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_30_1_Yvl.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_31_0_2PI.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_32_1_mx7.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_33_0_htq.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_34_1_D1f.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_35_1_peS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_36_1_S7F.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_37_0_eSS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_38_1_7fh.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_39_1_YG9.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_3_1_hlN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_40_1_6Su.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_41_1_fUq.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_42_0_Fq3.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_43_1_qu9.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_44_1_C3v.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_45_1_5ss.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_46_0_vUy.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_4_1_xmn.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_5_1_gz8.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_6_1_dLs.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_7_1_oNt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_8_1_fk0.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jul16thReReco-v1/patTuple_muon_9_1_fwz.root',
]
        )

readFiles.extend([
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_100_0_knT.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_101_1_ZA8.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_102_1_73D.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_103_0_M8V.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_104_0_hIN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_105_0_N7J.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_106_1_2YE.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_107_0_sHm.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_108_0_QCs.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_109_0_LSB.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_10_2_usC.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_110_1_dke.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_111_0_z1E.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_112_0_564.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_113_0_gH0.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_114_2_4Wa.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_115_2_oq0.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_116_0_boP.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_117_1_qb5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_118_1_EP9.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_119_2_n0p.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_11_0_ZK9.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_120_0_Dlb.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_121_0_rhU.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_122_1_GuD.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_123_1_4en.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_124_2_T9o.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_125_2_HAq.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_126_0_FRe.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_127_1_Y7y.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_128_1_w1C.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_129_0_bWE.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_12_2_RxK.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_130_0_VK9.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_13_1_dLR.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_14_1_I1T.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_15_1_n6M.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_16_0_9kz.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_17_1_1ll.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_18_0_eso.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_19_0_txj.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_1_1_vPB.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_20_0_b1I.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_21_1_g58.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_22_0_KIm.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_23_0_2K6.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_24_0_NLc.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_25_0_B9O.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_26_0_TgI.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_27_1_Pvf.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_28_3_kZu.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_29_0_hUx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_2_0_UfW.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_30_1_rww.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_31_1_Czp.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_32_2_cXD.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_33_3_MSJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_34_0_zzp.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_35_0_aF3.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_36_0_Bva.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_37_1_9na.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_38_1_rjH.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_39_0_7YP.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_3_1_Drl.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_40_1_iW0.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_41_1_0LB.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_42_0_j7u.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_43_0_tak.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_44_0_YjD.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_45_1_SnR.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_46_1_Cqt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_47_1_7vp.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_48_2_u4v.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_49_0_Zt2.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_4_0_7Gj.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_50_0_bOt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_51_0_97A.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_52_0_7T3.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_53_0_ygh.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_54_3_jn8.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_55_2_Itt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_56_0_r1s.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_57_1_Vge.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_58_1_acj.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_59_0_YnL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_5_2_lBJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_60_0_F0M.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_61_0_aPM.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_62_1_XkT.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_63_0_SBt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_64_1_RXf.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_65_1_CWZ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_66_0_IRp.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_67_0_H7Q.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_68_1_dv5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_69_0_seb.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_6_1_MoQ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_70_1_ViL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_71_0_QAe.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_72_0_jYD.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_73_0_UQD.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_74_1_cjX.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_75_2_icy.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_76_1_X5I.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_77_0_8yt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_78_1_nLG.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_79_1_10l.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_7_1_yxz.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_80_0_xqL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_81_0_sAn.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_82_0_FYT.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_83_0_KDu.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_84_3_92K.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_85_1_Z1H.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_86_1_TaA.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_87_2_0gx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_88_0_RIX.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_89_0_MIR.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_8_3_0bW.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_90_0_wOD.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_91_0_si9.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_92_2_F1j.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_93_1_OAH.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_94_1_Y8T.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_95_0_Bpb.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_96_1_C8Y.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_97_1_sgT.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_98_1_gwD.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_99_1_52K.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-PromptReco-v4/patTuple_muon_9_1_nGj.root',
]
        )

readFiles.extend([
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_10_0_wlQ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_11_1_KHO.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_12_0_2D2.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_13_0_OWK.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_14_1_0mJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_15_0_mMo.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_16_0_ML3.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_17_0_iDi.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_18_1_QNg.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_19_0_uXC.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_1_1_gg0.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_20_1_Lgv.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_21_1_7WB.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_22_1_c7t.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_23_1_ZPM.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_24_1_K0Y.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_25_0_bZy.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_26_0_VWR.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_27_1_JFG.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_28_1_5IC.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_29_0_QWw.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_2_0_Lrg.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_30_1_dmH.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_31_1_tTN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_32_1_EO5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_33_1_TXi.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_34_1_F8r.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_35_1_No3.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_36_0_DNn.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_37_1_4sR.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_38_1_b2f.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_39_0_8BM.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_3_0_XFu.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_40_1_wy3.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_41_1_ZRN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_42_1_CeC.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_43_0_GUf.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_44_0_C17.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_45_1_7bZ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_46_1_Tcg.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_47_0_EIs.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_48_0_nqz.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_49_1_Y9Y.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_4_0_KKG.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_50_1_FvQ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_51_0_hzm.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_52_0_m2a.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_53_1_811.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_54_1_RQ0.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_55_0_Ejb.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_56_1_yZ9.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_57_0_sMz.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_58_0_Anf.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_59_1_LjQ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_5_0_iZs.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_60_0_DAo.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_61_1_aLp.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_62_1_iyb.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_63_0_Yma.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_64_1_sYn.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_65_1_00X.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_6_1_yZq.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_7_1_PsW.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_8_0_iz4.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_9_1_KDa.root',
]
        )


readFiles.extend([
        'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jun14thReReco_v1/patTuple_muon_10_1_Rwu.root',
        'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jun14thReReco_v1/patTuple_muon_11_1_RnJ.root',
        'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jun14thReReco_v1/patTuple_muon_12_1_zgD.root',
        'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jun14thReReco_v1/patTuple_muon_13_1_iVi.root',
        'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jun14thReReco_v1/patTuple_muon_14_1_e4e.root',
        'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jun14thReReco_v1/patTuple_muon_15_1_okj.root',
        'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jun14thReReco_v1/patTuple_muon_16_1_ZYW.root',
        'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jun14thReReco_v1/patTuple_muon_17_1_3U4.root',
        'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jun14thReReco_v1/patTuple_muon_18_1_61Y.root',
        'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jun14thReReco_v1/patTuple_muon_19_1_g7D.root',
        'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jun14thReReco_v1/patTuple_muon_1_1_FkG.root',
        'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jun14thReReco_v1/patTuple_muon_2_1_pty.root',
        'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jun14thReReco_v1/patTuple_muon_3_1_dxp.root',
        'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jun14thReReco_v1/patTuple_muon_4_1_jhw.root',
        'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jun14thReReco_v1/patTuple_muon_5_1_JOr.root',
        'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jun14thReReco_v1/patTuple_muon_6_1_izt.root',
        'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jun14thReReco_v1/patTuple_muon_7_1_elG.root',
        'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jun14thReReco_v1/patTuple_muon_8_1_FpX.root',
        'rfio:///castor/cern.ch/user/t/tjkim/MUONSKIM/Aug9th/Run2010A-Jun14thReReco_v1/patTuple_muon_9_1_guz.root',
]
        )

