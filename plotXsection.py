#!/bin/env python

# Author: Rafael Lopes de Sa
# Date: A moment of boredom

# This is to read XML output (LHE files)
import xml.etree.ElementTree as ET

# ROOT interface
import ROOT

# LHAPDF interface
import lhapdf

def readFiles(eventFiles):

    ''' This is just to concatenate many MadGraph runs '''

    retval = []
    for LHEFile in eventFiles:
        retval = retval + getEvents(LHEFile, float(len(eventFiles)))
    return retval
    

def getEvents(LHEFile, numberOfRuns):

    ''' Reads LHE file and returns the weights and dependent variables '''
    
    tree = ET.parse(LHEFile)
    root = tree.getroot()

    retval = []

    for child in root:

        # All the info I may ever want
        
        alphaSOrder = 0
        renormalizationScale = 0.
        factorizationScale = 0.

        eventWeight = 0.
        passSelection = 1.
        
        x1 = 0.
        id1 = 0    
        x2 = 0.
        id2 = 0

        lep = []
        nu = []
        jet = []

        renormalizationUp = 0.
        renormalizationDown = 0.

        factorizationUp = 0.
        factorizationDown = 0.
        
        if 'event' in child.tag:

            # This below is a mess
            # I wish the LHE people would provide a python parser

            renormalizationInfo = child[0][0].text.split()
            alphaSOrder = int(renormalizationInfo[0])
            renormalizationScale = float(renormalizationInfo[1])

            renormalizationUp = recalculateRenormalization(alphaSOrder, renormalizationScale, 2.)
            renormalizationDown = recalculateRenormalization(alphaSOrder, renormalizationScale, 0.5)

            factorizationInfo = child[0][2].text.split()
            id1 = int(factorizationInfo[1])
            x1 = float(factorizationInfo[2])
            factorizationScale1 = float(factorizationInfo[3])

            factorizationInfo = child[0][3].text.split()
            id2 = int(factorizationInfo[1])
            x2 = float(factorizationInfo[2])
            factorizationScale2 = float(factorizationInfo[3])

            factorizationUp = recalculateFactorization(x1, id1, factorizationScale1, x2, id2, factorizationScale2, 2.)
            factorizationDown = recalculateFactorization(x1, id1, factorizationScale1, x2, id2, factorizationScale2, 0.5)

            eventInfo = child.text.splitlines()
            eventWeight = float(eventInfo[1].split()[2])

            for line in eventInfo[4:]:
                particleInfo = line.split()
                pdgID = int(particleInfo[0])
                isStable = bool(particleInfo[1])
                px = float(particleInfo[6])
                py = float(particleInfo[7])
                pz = float(particleInfo[8])
                E = float(particleInfo[9])

                if not isStable:
                    continue
                if ROOT.TMath.Abs(pdgID) == 11 or ROOT.TMath.Abs(pdgID) == 13 or ROOT.TMath.Abs(pdgID) == 15:
                    lep.append(ROOT.TLorentzVector(px,py,pz,E))
                elif ROOT.TMath.Abs(pdgID) == 12 or ROOT.TMath.Abs(pdgID) == 14 or ROOT.TMath.Abs(pdgID) == 16:
                    nu.append(ROOT.TLorentzVector(px,py,pz,E))
                else:
                    jet.append(ROOT.TLorentzVector(px,py,pz,E))

            # Sort in pT. I won't use this, but it is nice if I want in the future
            
            lep.sort(key=lambda particle: particle.Pt(), reverse=True)
            jet.sort(key=lambda particle: particle.Pt(), reverse=True)
            MET = reduce(lambda x,y:x+y, nu)

            passSelection = eventSelector(lep, jet, MET)
            
            # Now, prepare the output
            mjj = (jet[0] + jet[1]).M()
            detajj = ROOT.TMath.Abs(jet[0].Eta() - jet[1].Eta())
            
            retval.append([passSelection*eventWeight/numberOfRuns,
                           passSelection*eventWeight*renormalizationDown*factorizationDown/numberOfRuns, 
                           passSelection*eventWeight*renormalizationUp*factorizationUp/numberOfRuns,
                           mjj,
                           detajj])

    return retval

def recalculateRenormalization(alphaSOrder, renormalizationScale, multiplier):

    ''' Recalculate the invariant amplitude using the new renormalization scale '''

    retval = ROOT.TMath.Power(lhapdf.alphasPDF(renormalizationScale*multiplier)/lhapdf.alphasPDF(renormalizationScale), alphaSOrder)
    return retval

def recalculateFactorization(x1, id1, factorizationScale1, x2, id2, factorizationScale2, multiplier):

    ''' Recalculate the PDF using the new factorization scale '''

    lhapdfID1 = id1
    if lhapdfID1 == 21:
        lhapdfID1 = 0
        
    lhapdfID2 = id1
    if lhapdfID2 == 21:
        lhapdfID2 = 0

    # LHAPDF only returns x * f(x, Q) ... that's why I divide by x.
    # Not strictly necessary, since we are interest in ratios, but anyway...

    oldWeight1 = lhapdf.xfx(x1, factorizationScale1, lhapdfID1)/x1
    newWeight1 = lhapdf.xfx(x1, factorizationScale1*multiplier, lhapdfID1)/x1

    oldWeight2 = lhapdf.xfx(x2, factorizationScale2, lhapdfID2)/x2
    newWeight2 = lhapdf.xfx(x2, factorizationScale2*multiplier, lhapdfID2)/x2

    return (newWeight1*newWeight2)/(oldWeight1*oldWeight2)

def eventSelector(lep, jet, MET):

    '''Event selection but mjj and detajj, that will be used as dependent variables for the cross section'''

    retval = 1.

    # I know that I could write this in less lines, but I think it is more readable this way
    if lep[0].Pt() < 20. or lep[1].Pt() < 20.:
        retval = 0.
    if ROOT.TMath.Abs(lep[0].Eta()) > 2.5 or ROOT.TMath.Abs(lep[1].Eta()) > 2.5:
        retval = 0.
    if (lep[0] + lep[1]).M() < 50.:
        retval = 0.
    if MET.Pt() < 30.:
        retval = 0.
    if jet[0].Pt() < 30. or jet[1].Pt() < 30.:
        retval = 0.
    if ROOT.TMath.Abs(jet[0].Eta()) > 4.7 or ROOT.TMath.Abs(jet[1].Eta()) > 4.7:
        retval = 0.

    return retval
    

        
if __name__ == "__main__":

    # This here has to match the generation info in run_card.dat
    
    lhapdf.initPDFSetByName("cteq6ll.LHpdf")
    lhapdf.initPDF(0)
    mjj_min = 150.
    detajj_min = 1.5

    # Be careful, this thing will stash all the weights in memory.
    # It shouldn't be much, but don't go crazy with extremely large LHE files

    print 'Reading WmWm EWK + QCD'
    WmWmEWKQCD = readFiles(['../WmWm_VBS_QED4_QCD99_SM/Events/run_01/unweighted_events.lhe',
                            '../WmWm_VBS_QED4_QCD99_SM/Events/run_02/unweighted_events.lhe',
                            '../WmWm_VBS_QED4_QCD99_SM/Events/run_03/unweighted_events.lhe',
                            '../WmWm_VBS_QED4_QCD99_SM/Events/run_04/unweighted_events.lhe',
                            '../WmWm_VBS_QED4_QCD99_SM/Events/run_05/unweighted_events.lhe',
                            '../WmWm_VBS_QED4_QCD99_SM/Events/run_06/unweighted_events.lhe'])
    print 'Reading WmWm EWK'
    WmWmEWK = readFiles(['../WmWm_VBS_QED4_QCD0_SM/Events/run_01/unweighted_events.lhe',
                         '../WmWm_VBS_QED4_QCD0_SM/Events/run_02/unweighted_events.lhe',
                         '../WmWm_VBS_QED4_QCD0_SM/Events/run_03/unweighted_events.lhe',
                         '../WmWm_VBS_QED4_QCD0_SM/Events/run_04/unweighted_events.lhe',
                         '../WmWm_VBS_QED4_QCD0_SM/Events/run_05/unweighted_events.lhe',
                         '../WmWm_VBS_QED4_QCD0_SM/Events/run_06/unweighted_events.lhe'])
    print 'Reading WmWm QCD'
    WmWmQCD = readFiles(['../WmWm_VBS_QED2_QCD99_SM/Events/run_01/unweighted_events.lhe',
                         '../WmWm_VBS_QED2_QCD99_SM/Events/run_02/unweighted_events.lhe',
                         '../WmWm_VBS_QED2_QCD99_SM/Events/run_03/unweighted_events.lhe',
                         '../WmWm_VBS_QED2_QCD99_SM/Events/run_04/unweighted_events.lhe',
                         '../WmWm_VBS_QED2_QCD99_SM/Events/run_05/unweighted_events.lhe',
                         '../WmWm_VBS_QED2_QCD99_SM/Events/run_06/unweighted_events.lhe',
                         '../WmWm_VBS_QED2_QCD99_SM/Events/run_07/unweighted_events.lhe',
                         '../WmWm_VBS_QED2_QCD99_SM/Events/run_08/unweighted_events.lhe'])

    print 'Reading WpWp EWK + QCD'
    WpWpEWKQCD = readFiles(['../WpWp_VBS_QED4_QCD99_SM/Events/run_01/unweighted_events.lhe',
                            '../WpWp_VBS_QED4_QCD99_SM/Events/run_02/unweighted_events.lhe',
                            '../WpWp_VBS_QED4_QCD99_SM/Events/run_03/unweighted_events.lhe',
                            '../WpWp_VBS_QED4_QCD99_SM/Events/run_04/unweighted_events.lhe',
                            '../WpWp_VBS_QED4_QCD99_SM/Events/run_05/unweighted_events.lhe',
                            '../WpWp_VBS_QED4_QCD99_SM/Events/run_06/unweighted_events.lhe'])
    print 'Reading WpWp EWK'
    WpWpEWK = readFiles(['../WpWp_VBS_QED4_QCD0_SM/Events/run_01/unweighted_events.lhe',
                         '../WpWp_VBS_QED4_QCD0_SM/Events/run_02/unweighted_events.lhe',
                         '../WpWp_VBS_QED4_QCD0_SM/Events/run_03/unweighted_events.lhe',
                         '../WpWp_VBS_QED4_QCD0_SM/Events/run_04/unweighted_events.lhe',
                         '../WpWp_VBS_QED4_QCD0_SM/Events/run_05/unweighted_events.lhe',
                         '../WpWp_VBS_QED4_QCD0_SM/Events/run_06/unweighted_events.lhe'])
    print 'Reading WpWp QCD'
    WpWpQCD = readFiles(['../WpWp_VBS_QED2_QCD99_SM/Events/run_01/unweighted_events.lhe',
                         '../WpWp_VBS_QED2_QCD99_SM/Events/run_02/unweighted_events.lhe',
                         '../WpWp_VBS_QED2_QCD99_SM/Events/run_03/unweighted_events.lhe',
                         '../WpWp_VBS_QED2_QCD99_SM/Events/run_04/unweighted_events.lhe',
                         '../WpWp_VBS_QED2_QCD99_SM/Events/run_05/unweighted_events.lhe',
                         '../WpWp_VBS_QED2_QCD99_SM/Events/run_06/unweighted_events.lhe',
                         '../WpWp_VBS_QED2_QCD99_SM/Events/run_07/unweighted_events.lhe',
                         '../WpWp_VBS_QED2_QCD99_SM/Events/run_08/unweighted_events.lhe'])

    # Now let's fill histograms
    # I don't know if this is the best way to save the data, but there are
    # two uncertainties: the statistical, from MC integration, and the scale variation, from factorization and renormalization.
    # So I will put in diferent profiles.

    print 'Doing analysis'
    ROOT.TH1.SetDefaultSumw2()
    
    WmWmEWKQCD_mjj = [ROOT.TH1D('WmWmEWKQCD_mjj', '', 100, mjj_min, 550.),
                      ROOT.TH1D('WmWmEWKQCD_mjj_down', '', 100, mjj_min, 550.),
                      ROOT.TH1D('WmWmEWKQCD_mjj_up', '', 100, mjj_min, 550.)]
    WmWmEWKQCD_detajj = [ROOT.TH1D('WmWmEWKQCD_detajj', '', 100, detajj_min, 3.5),
                         ROOT.TH1D('WmWmEWKQCD_detajj_down', '', 100, detajj_min, 3.5),
                         ROOT.TH1D('WmWmEWKQCD_detajj_up', '', 100, detajj_min, 3.5)]
    WmWmEWK_mjj = [ROOT.TH1D('WmWmEWK_mjj', '', 100, mjj_min, 550.),
                      ROOT.TH1D('WmWmEWK_mjj_down', '', 100, mjj_min, 550.),
                      ROOT.TH1D('WmWmEWK_mjj_up', '', 100, mjj_min, 550.)]
    WmWmEWK_detajj = [ROOT.TH1D('WmWmEWK_detajj', '', 100, detajj_min, 3.5),
                         ROOT.TH1D('WmWmEWK_detajj_down', '', 100, detajj_min, 3.5),
                         ROOT.TH1D('WmWmEWK_detajj_up', '', 100, detajj_min, 3.5)]
    WmWmQCD_mjj = [ROOT.TH1D('WmWmQCD_mjj', '', 100, mjj_min, 550.),
                      ROOT.TH1D('WmWmQCD_mjj_down', '', 100, mjj_min, 550.),
                      ROOT.TH1D('WmWmQCD_mjj_up', '', 100, mjj_min, 550.)]
    WmWmQCD_detajj = [ROOT.TH1D('WmWmQCD_detajj', '', 100, detajj_min, 3.5),
                         ROOT.TH1D('WmWmQCD_detajj_down', '', 100, detajj_min, 3.5),
                         ROOT.TH1D('WmWmQCD_detajj_up', '', 100, detajj_min, 3.5)]

    WpWpEWKQCD_mjj = [ROOT.TH1D('WpWpEWKQCD_mjj', '', 100, mjj_min, 550.),
                      ROOT.TH1D('WpWpEWKQCD_mjj_down', '', 100, mjj_min, 550.),
                      ROOT.TH1D('WpWpEWKQCD_mjj_up', '', 100, mjj_min, 550.)]
    WpWpEWKQCD_detajj = [ROOT.TH1D('WpWpEWKQCD_detajj', '', 100, detajj_min, 3.5),
                         ROOT.TH1D('WpWpEWKQCD_detajj_down', '', 100, detajj_min, 3.5),
                         ROOT.TH1D('WpWpEWKQCD_detajj_up', '', 100, detajj_min, 3.5)]
    WpWpEWK_mjj = [ROOT.TH1D('WpWpEWK_mjj', '', 100, mjj_min, 550.),
                      ROOT.TH1D('WpWpEWK_mjj_down', '', 100, mjj_min, 550.),
                      ROOT.TH1D('WpWpEWK_mjj_up', '', 100, mjj_min, 550.)]
    WpWpEWK_detajj = [ROOT.TH1D('WpWpEWK_detajj', '', 100, detajj_min, 3.5),
                         ROOT.TH1D('WpWpEWK_detajj_down', '', 100, detajj_min, 3.5),
                         ROOT.TH1D('WpWpEWK_detajj_up', '', 100, detajj_min, 3.5)]
    WpWpQCD_mjj = [ROOT.TH1D('WpWpQCD_mjj', '', 100, mjj_min, 550.),
                      ROOT.TH1D('WpWpQCD_mjj_down', '', 100, mjj_min, 550.),
                      ROOT.TH1D('WpWpQCD_mjj_up', '', 100, mjj_min, 550.)]
    WpWpQCD_detajj = [ROOT.TH1D('WpWpQCD_detajj', '', 100, detajj_min, 3.5),
                         ROOT.TH1D('WpWpQCD_detajj_down', '', 100, detajj_min, 3.5),
                         ROOT.TH1D('WpWpQCD_detajj_up', '', 100, detajj_min, 3.5)]

    for event in WmWmEWKQCD:
        for ibin in xrange(1,WmWmEWKQCD_mjj[0].GetNbinsX()+1):
            if event[3] > WmWmEWKQCD_mjj[0].GetXaxis().GetBinLowEdge(ibin) and event[4] > 2.5:
                WmWmEWKQCD_mjj[0].Fill(WmWmEWKQCD_mjj[0].GetXaxis().GetBinCenter(ibin), event[0])
                WmWmEWKQCD_mjj[1].Fill(WmWmEWKQCD_mjj[1].GetXaxis().GetBinCenter(ibin), event[1])
                WmWmEWKQCD_mjj[2].Fill(WmWmEWKQCD_mjj[2].GetXaxis().GetBinCenter(ibin), event[2])
            if event[4] > WmWmEWKQCD_detajj[0].GetXaxis().GetBinLowEdge(ibin) and event[3] > 500:
                WmWmEWKQCD_detajj[0].Fill(WmWmEWKQCD_detajj[0].GetXaxis().GetBinCenter(ibin), event[0])
                WmWmEWKQCD_detajj[1].Fill(WmWmEWKQCD_detajj[1].GetXaxis().GetBinCenter(ibin), event[1])
                WmWmEWKQCD_detajj[2].Fill(WmWmEWKQCD_detajj[2].GetXaxis().GetBinCenter(ibin), event[2])
        

    for event in WmWmEWK:
        for ibin in xrange(1,WmWmEWK_mjj[0].GetNbinsX()+1):
            if event[3] > WmWmEWK_mjj[0].GetXaxis().GetBinLowEdge(ibin) and event[4] > 2.5:
                WmWmEWK_mjj[0].Fill(WmWmEWK_mjj[0].GetXaxis().GetBinCenter(ibin), event[0])
                WmWmEWK_mjj[1].Fill(WmWmEWK_mjj[1].GetXaxis().GetBinCenter(ibin), event[1])
                WmWmEWK_mjj[2].Fill(WmWmEWK_mjj[2].GetXaxis().GetBinCenter(ibin), event[2])
            if event[4] > WmWmEWK_detajj[0].GetXaxis().GetBinLowEdge(ibin) and event[3] > 500:
                WmWmEWK_detajj[0].Fill(WmWmEWK_detajj[0].GetXaxis().GetBinCenter(ibin), event[0])
                WmWmEWK_detajj[1].Fill(WmWmEWK_detajj[1].GetXaxis().GetBinCenter(ibin), event[1])
                WmWmEWK_detajj[2].Fill(WmWmEWK_detajj[2].GetXaxis().GetBinCenter(ibin), event[2])
        

    for event in WmWmQCD:
        for ibin in xrange(1,WmWmQCD_mjj[0].GetNbinsX()+1):
            if event[3] > WmWmQCD_mjj[0].GetXaxis().GetBinLowEdge(ibin) and event[4] > 2.5:
                WmWmQCD_mjj[0].Fill(WmWmQCD_mjj[0].GetXaxis().GetBinCenter(ibin), event[0])
                WmWmQCD_mjj[1].Fill(WmWmQCD_mjj[1].GetXaxis().GetBinCenter(ibin), event[1])
                WmWmQCD_mjj[2].Fill(WmWmQCD_mjj[2].GetXaxis().GetBinCenter(ibin), event[2])
            if event[4] > WmWmQCD_detajj[0].GetXaxis().GetBinLowEdge(ibin) and event[3] > 500:
                WmWmQCD_detajj[0].Fill(WmWmQCD_detajj[0].GetXaxis().GetBinCenter(ibin), event[0])
                WmWmQCD_detajj[1].Fill(WmWmQCD_detajj[1].GetXaxis().GetBinCenter(ibin), event[1])
                WmWmQCD_detajj[2].Fill(WmWmQCD_detajj[2].GetXaxis().GetBinCenter(ibin), event[2])
        

    for event in WpWpEWKQCD:
        for ibin in xrange(1,WpWpEWKQCD_mjj[0].GetNbinsX()+1):
            if event[3] > WpWpEWKQCD_mjj[0].GetXaxis().GetBinLowEdge(ibin) and event[4] > 2.5:
                WpWpEWKQCD_mjj[0].Fill(WpWpEWKQCD_mjj[0].GetXaxis().GetBinCenter(ibin), event[0])
                WpWpEWKQCD_mjj[1].Fill(WpWpEWKQCD_mjj[1].GetXaxis().GetBinCenter(ibin), event[1])
                WpWpEWKQCD_mjj[2].Fill(WpWpEWKQCD_mjj[2].GetXaxis().GetBinCenter(ibin), event[2])
            if event[4] > WpWpEWKQCD_detajj[0].GetXaxis().GetBinLowEdge(ibin) and event[3] > 500:
                WpWpEWKQCD_detajj[0].Fill(WpWpEWKQCD_detajj[0].GetXaxis().GetBinCenter(ibin), event[0])
                WpWpEWKQCD_detajj[1].Fill(WpWpEWKQCD_detajj[1].GetXaxis().GetBinCenter(ibin), event[1])
                WpWpEWKQCD_detajj[2].Fill(WpWpEWKQCD_detajj[2].GetXaxis().GetBinCenter(ibin), event[2])
        

    for event in WpWpEWK:
        for ibin in xrange(1,WpWpEWK_mjj[0].GetNbinsX()+1):
            if event[3] > WpWpEWK_mjj[0].GetXaxis().GetBinLowEdge(ibin) and event[4] > 2.5:
                WpWpEWK_mjj[0].Fill(WpWpEWK_mjj[0].GetXaxis().GetBinCenter(ibin), event[0])
                WpWpEWK_mjj[1].Fill(WpWpEWK_mjj[1].GetXaxis().GetBinCenter(ibin), event[1])
                WpWpEWK_mjj[2].Fill(WpWpEWK_mjj[2].GetXaxis().GetBinCenter(ibin), event[2])
            if event[4] > WpWpEWK_detajj[0].GetXaxis().GetBinLowEdge(ibin) and event[3] > 500:
                WpWpEWK_detajj[0].Fill(WpWpEWK_detajj[0].GetXaxis().GetBinCenter(ibin), event[0])
                WpWpEWK_detajj[1].Fill(WpWpEWK_detajj[1].GetXaxis().GetBinCenter(ibin), event[1])
                WpWpEWK_detajj[2].Fill(WpWpEWK_detajj[2].GetXaxis().GetBinCenter(ibin), event[2])
        

    for event in WpWpQCD:
        for ibin in xrange(1,WpWpQCD_mjj[0].GetNbinsX()+1):
            if event[3] > WpWpQCD_mjj[0].GetXaxis().GetBinLowEdge(ibin) and event[4] > 2.5:
                WpWpQCD_mjj[0].Fill(WpWpQCD_mjj[0].GetXaxis().GetBinCenter(ibin), event[0])
                WpWpQCD_mjj[1].Fill(WpWpQCD_mjj[1].GetXaxis().GetBinCenter(ibin), event[1])
                WpWpQCD_mjj[2].Fill(WpWpQCD_mjj[2].GetXaxis().GetBinCenter(ibin), event[2])
            if event[4] > WpWpQCD_detajj[0].GetXaxis().GetBinLowEdge(ibin) and event[3] > 500:
                WpWpQCD_detajj[0].Fill(WpWpQCD_detajj[0].GetXaxis().GetBinCenter(ibin), event[0])
                WpWpQCD_detajj[1].Fill(WpWpQCD_detajj[1].GetXaxis().GetBinCenter(ibin), event[1])
                WpWpQCD_detajj[2].Fill(WpWpQCD_detajj[2].GetXaxis().GetBinCenter(ibin), event[2])
        

    # Finally, the interference analysis
    print 'Doing interference calculation'

    WmWmInterference_mjj = [ROOT.TH1D('WmWmInterference_mjj', '', 100, mjj_min, 550.),
                            ROOT.TH1D('WmWmInterference_mjj_down', '', 100, mjj_min, 550.),
                            ROOT.TH1D('WmWmInterference_mjj_up', '', 100, mjj_min, 550.)]
    

    WpWpInterference_mjj = [ROOT.TH1D('WpWpInterference_mjj', '', 100, mjj_min, 550.),
                            ROOT.TH1D('WpWpInterference_mjj_down', '', 100, mjj_min, 550.),
                            ROOT.TH1D('WpWpInterference_mjj_up', '', 100, mjj_min, 550.)]
    

    WmWmInterference_detajj = [ROOT.TH1D('WmWmInterference_detajj', '', 100, detajj_min, 3.5),
                            ROOT.TH1D('WmWmInterference_detajj_down', '', 100, detajj_min, 3.5),
                            ROOT.TH1D('WmWmInterference_detajj_up', '', 100, detajj_min, 3.5)]
    

    WpWpInterference_detajj = [ROOT.TH1D('WpWpInterference_detajj', '', 100, detajj_min, 3.5),
                            ROOT.TH1D('WpWpInterference_detajj_down', '', 100, detajj_min, 3.5),
                            ROOT.TH1D('WpWpInterference_detajj_up', '', 100, detajj_min, 3.5)]
    

    WmWmInterference_mjj[0].Add(WmWmEWKQCD_mjj[0], WmWmEWK_mjj[0], 1., -1.)
    WmWmInterference_mjj[0].Add(WmWmQCD_mjj[0], -1.)
    WmWmInterference_mjj[1].Add(WmWmEWKQCD_mjj[1], WmWmEWK_mjj[1], 1., -1.)
    WmWmInterference_mjj[1].Add(WmWmQCD_mjj[1], -1.)
    WmWmInterference_mjj[2].Add(WmWmEWKQCD_mjj[2], WmWmEWK_mjj[2], 1., -1.)
    WmWmInterference_mjj[2].Add(WmWmQCD_mjj[2], -1.)

    WpWpInterference_mjj[0].Add(WpWpEWKQCD_mjj[0], WpWpEWK_mjj[0], 1., -1.)
    WpWpInterference_mjj[0].Add(WpWpQCD_mjj[0], -1.)
    WpWpInterference_mjj[1].Add(WpWpEWKQCD_mjj[1], WpWpEWK_mjj[1], 1., -1.)
    WpWpInterference_mjj[1].Add(WpWpQCD_mjj[1], -1.)
    WpWpInterference_mjj[2].Add(WpWpEWKQCD_mjj[2], WpWpEWK_mjj[2], 1., -1.)
    WpWpInterference_mjj[2].Add(WpWpQCD_mjj[2], -1.)

    WmWmInterference_detajj[0].Add(WmWmEWKQCD_detajj[0], WmWmEWK_detajj[0], 1., -1.)
    WmWmInterference_detajj[0].Add(WmWmQCD_detajj[0], -1.)
    WmWmInterference_detajj[1].Add(WmWmEWKQCD_detajj[1], WmWmEWK_detajj[1], 1., -1.)
    WmWmInterference_detajj[1].Add(WmWmQCD_detajj[1], -1.)
    WmWmInterference_detajj[2].Add(WmWmEWKQCD_detajj[2], WmWmEWK_detajj[2], 1., -1.)
    WmWmInterference_detajj[2].Add(WmWmQCD_detajj[2], -1.)

    WpWpInterference_detajj[0].Add(WpWpEWKQCD_detajj[0], WpWpEWK_detajj[0], 1., -1.)
    WpWpInterference_detajj[0].Add(WpWpQCD_detajj[0], -1.)
    WpWpInterference_detajj[1].Add(WpWpEWKQCD_detajj[1], WpWpEWK_detajj[1], 1., -1.)
    WpWpInterference_detajj[1].Add(WpWpQCD_detajj[1], -1.)
    WpWpInterference_detajj[2].Add(WpWpEWKQCD_detajj[2], WpWpEWK_detajj[2], 1., -1.)
    WpWpInterference_detajj[2].Add(WpWpQCD_detajj[2], -1.)


    # Now saves this bunch of stuff
    print 'Writing output'
    outputFile = ROOT.TFile.Open('output.root', 'recreate')

    WmWmEWKQCD_mjj[0].Write()
    WmWmEWKQCD_mjj[1].Write()
    WmWmEWKQCD_mjj[2].Write()
    WmWmEWKQCD_detajj[0].Write()
    WmWmEWKQCD_detajj[1].Write()
    WmWmEWKQCD_detajj[2].Write()

    WpWpEWKQCD_mjj[0].Write()
    WpWpEWKQCD_mjj[1].Write()
    WpWpEWKQCD_mjj[2].Write()
    WpWpEWKQCD_detajj[0].Write()
    WpWpEWKQCD_detajj[1].Write()
    WpWpEWKQCD_detajj[2].Write()

    WmWmEWK_mjj[0].Write()
    WmWmEWK_mjj[1].Write()
    WmWmEWK_mjj[2].Write()
    WmWmEWK_detajj[0].Write()
    WmWmEWK_detajj[1].Write()
    WmWmEWK_detajj[2].Write()

    WpWpEWK_mjj[0].Write()
    WpWpEWK_mjj[1].Write()
    WpWpEWK_mjj[2].Write()
    WpWpEWK_detajj[0].Write()
    WpWpEWK_detajj[1].Write()
    WpWpEWK_detajj[2].Write()

    WmWmQCD_mjj[0].Write()
    WmWmQCD_mjj[1].Write()
    WmWmQCD_mjj[2].Write()
    WmWmQCD_detajj[0].Write()
    WmWmQCD_detajj[1].Write()
    WmWmQCD_detajj[2].Write()

    WpWpQCD_mjj[0].Write()
    WpWpQCD_mjj[1].Write()
    WpWpQCD_mjj[2].Write()
    WpWpQCD_detajj[0].Write()
    WpWpQCD_detajj[1].Write()
    WpWpQCD_detajj[2].Write()

    WmWmInterference_mjj[0].Write()
    WmWmInterference_mjj[1].Write()
    WmWmInterference_mjj[2].Write()
    WmWmInterference_detajj[0].Write()
    WmWmInterference_detajj[1].Write()
    WmWmInterference_detajj[2].Write()

    WpWpInterference_mjj[0].Write()
    WpWpInterference_mjj[1].Write()
    WpWpInterference_mjj[2].Write()
    WpWpInterference_detajj[0].Write()
    WpWpInterference_detajj[1].Write()
    WpWpInterference_detajj[2].Write()

    outputFile.Close()
    
