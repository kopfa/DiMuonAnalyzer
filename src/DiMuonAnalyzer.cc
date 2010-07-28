// -*- C++ -*-
//
// Package:    DiMuonAnalyzer
// Class:      DiMuonAnalyzer
// 
/**\class DiMuonAnalyzer DiMuonAnalyzer.cc UserCode/DiMuonAnalyzer/src/DiMuonAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Tae Jeong Kim,40 R-A32,+41227678602,
//         Created:  Fri Jun  4 17:19:29 CEST 2010
// $Id: DiMuonAnalyzer.cc,v 1.8 2010/07/27 21:30:04 tjkim Exp $
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "CommonTools/Utils/interface/StringObjectFunction.h"
#include "DataFormats/PatCandidates/interface/LookupTableRecord.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "KoPFA/DataFormats/interface/ZCandidate.h"

#include "DQMServices/Core/interface/MonitorElement.h"
#include "DQMServices/Core/interface/DQMStore.h"

#include "TFile.h"
#include "TTree.h"
#include "TH1.h"

//
// class declaration
//

class DiMuonAnalyzer : public edm::EDAnalyzer {
   public:
      explicit DiMuonAnalyzer(const edm::ParameterSet&);
      ~DiMuonAnalyzer();


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      edm::InputTag muonLabel_;
      edm::InputTag metLabel_;
      std::vector<std::string> filters_;
      bool useEventCounter_;

      TTree* tree;

      TH1F * tmp;
      TH1F * h_leadingpt;
      TH1F * h_secondpt;
      TH1F * h_mass;

      std::vector<Ko::ZCandidate>* Z;
      std::vector<math::XYZTLorentzVector>* muon1;
      std::vector<math::XYZTLorentzVector>* muon2;
    
      double MET;
      // ----------member data ---------------------------

      //add run event data
      unsigned int EVENT;
      unsigned int RUN;
      unsigned int LUMI;
  
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
DiMuonAnalyzer::DiMuonAnalyzer(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed
  muonLabel_ =  iConfig.getParameter<edm::InputTag>("muonLabel");
  metLabel_ = iConfig.getParameter<edm::InputTag>("metLabel");
  useEventCounter_ = iConfig.getParameter<bool>("useEventCounter");
  filters_ = iConfig.getUntrackedParameter<std::vector<std::string> >("filters");
  edm::Service<TFileService> fs;
  tree = fs->make<TTree>("tree", "Tree for Top quark study");
  tmp = fs->make<TH1F>("EventSummary","EventSummary",filters_.size(),0,filters_.size());

  h_leadingpt   = fs->make<TH1F>( "leadingpt"  , "p_{t}", 100,  0., 100. );
  h_secondpt    = fs->make<TH1F>( "secondpt"  , "p_{t}", 100,  0., 100. );
  h_mass      = fs->make<TH1F>( "mass", "Mass", 100, 0., 200. );   

  Z = new std::vector<Ko::ZCandidate>();
  muon1 = new std::vector<math::XYZTLorentzVector>();
  muon2 = new std::vector<math::XYZTLorentzVector>();

}


DiMuonAnalyzer::~DiMuonAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to for each event  ------------
void
DiMuonAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace std;
  Z->clear();
  muon1->clear();
  muon2->clear();

  EVENT  = iEvent.id().event();
  RUN    = iEvent.id().run();
  LUMI   = iEvent.id().luminosityBlock();

  typedef pat::MuonCollection::const_iterator MI;
  edm::Handle<pat::MuonCollection> muons_;
  edm::Handle<pat::METCollection> MET_;
  iEvent.getByLabel(muonLabel_,muons_);
  iEvent.getByLabel(metLabel_,MET_);

  pat::METCollection::const_iterator mi = MET_->begin();
  MET = mi->pt(); 

  for(MI mi = muons_->begin(); mi != muons_->end()-1; mi++){
    for(MI mj = mi + 1 ; mj != muons_->end(); mj++){

      int sign = mi->charge() * mj->charge();
      Ko::ZCandidate dimuon(mi->p4(), mj->p4(), sign);

      Z->push_back(dimuon);
      muon1->push_back(mi->p4());
      muon2->push_back(mj->p4());

      h_leadingpt->Fill(mi->pt());
      h_secondpt->Fill(mj->pt());
      h_mass->Fill(dimuon.mass());

      break;
    }
  }
   
  //ESHandle<SetupData> pSetup;
  //iSetup.get<SetupRecord>().get(pSetup);
  tree->Fill();

}


// ------------ method called once each job just before starting event loop  ------------
void 
DiMuonAnalyzer::beginJob()
{
  tree->Branch("EVENT",&EVENT,"EVENT/i");
  tree->Branch("RUN",&RUN,"RUN/i");
  tree->Branch("LUMI",&LUMI,"LUMI/i");

  tree->Branch("Z","std::vector<Ko::ZCandidate>", &Z);
  tree->Branch("muon1","std::vector<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<double> > >", &muon1);
  tree->Branch("muon2","std::vector<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<double> > >", &muon2);

  tree->Branch("MET",&MET,"MET/d");
  
}

// ------------ method called once each job just after ending the event loop  ------------
void 
DiMuonAnalyzer::endJob() {
           if(useEventCounter_){
             DQMStore* store = &*edm::Service<DQMStore>();
             if(filters_.size()>0) {
               for(unsigned int i=0;i<filters_.size();++i) {
                 MonitorElement *tmpM = store->get(filters_[i]);
                 tmp->SetBinContent(i+1,tmpM->getFloatValue());
                 tmp->GetXaxis()->SetBinLabel(i+1,filters_[i].c_str());
               }
             }
           }
}

//define this as a plug-in
DEFINE_FWK_MODULE(DiMuonAnalyzer);
