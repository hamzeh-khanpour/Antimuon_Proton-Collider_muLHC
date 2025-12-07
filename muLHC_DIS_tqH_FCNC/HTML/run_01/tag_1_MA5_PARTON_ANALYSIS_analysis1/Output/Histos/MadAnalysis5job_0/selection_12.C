void selection_12()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo25","canvas_plotflow_tempo25",0,0,700,500);
  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(0);
  canvas->SetHighLightColor(2);
  canvas->SetFillColor(0);
  canvas->SetBorderMode(0);
  canvas->SetBorderSize(3);
  canvas->SetFrameBorderMode(0);
  canvas->SetFrameBorderSize(0);
  canvas->SetTickx(1);
  canvas->SetTicky(1);
  canvas->SetLeftMargin(0.14);
  canvas->SetRightMargin(0.05);
  canvas->SetBottomMargin(0.15);
  canvas->SetTopMargin(0.05);

  // Creating a new TH1F
  TH1F* S13_M_0 = new TH1F("S13_M_0","S13_M_0",40,0.0,500.0);
  // Content
  S13_M_0->SetBinContent(0,0.0); // underflow
  S13_M_0->SetBinContent(1,0.0030086105379999173);
  S13_M_0->SetBinContent(2,0.012320258108109976);
  S13_M_0->SetBinContent(3,0.018924157094019973);
  S13_M_0->SetBinContent(4,0.025076766149229723);
  S13_M_0->SetBinContent(5,0.030010885391549905);
  S13_M_0->SetBinContent(6,0.03226734504504957);
  S13_M_0->SetBinContent(7,0.03508039461307969);
  S13_M_0->SetBinContent(8,0.036735124358980575);
  S13_M_0->SetBinContent(9,0.03873585405174996);
  S13_M_0->SetBinContent(10,0.03870576405637055);
  S13_M_0->SetBinContent(11,0.03718642428967928);
  S13_M_0->SetBinContent(12,0.037532414236549315);
  S13_M_0->SetBinContent(13,0.035937844481410304);
  S13_M_0->SetBinContent(14,0.03581750449988963);
  S13_M_0->SetBinContent(15,0.03479457465697);
  S13_M_0->SetBinContent(16,0.03465918467776039);
  S13_M_0->SetBinContent(17,0.03363626483483923);
  S13_M_0->SetBinContent(18,0.03232751503580991);
  S13_M_0->SetBinContent(19,0.030206445361519854);
  S13_M_0->SetBinContent(20,0.03156031515362057);
  S13_M_0->SetBinContent(21,0.02967993544237034);
  S13_M_0->SetBinContent(22,0.028852565569420667);
  S13_M_0->SetBinContent(23,0.02751373577501041);
  S13_M_0->SetBinContent(24,0.026475765934400316);
  S13_M_0->SetBinContent(25,0.02649081593208925);
  S13_M_0->SetBinContent(26,0.025618316066069707);
  S13_M_0->SetBinContent(27,0.025407716098409288);
  S13_M_0->SetBinContent(28,0.022715006511899845);
  S13_M_0->SetBinContent(29,0.022985776470320605);
  S13_M_0->SetBinContent(30,0.022970736472630135);
  S13_M_0->SetBinContent(31,0.022549536537309296);
  S13_M_0->SetBinContent(32,0.019856826950799857);
  S13_M_0->SetBinContent(33,0.019841786953109387);
  S13_M_0->SetBinContent(34,0.01844277716794033);
  S13_M_0->SetBinContent(35,0.01920997705012966);
  S13_M_0->SetBinContent(36,0.017795927267270136);
  S13_M_0->SetBinContent(37,0.0166676974405203);
  S13_M_0->SetBinContent(38,0.017209247357360284);
  S13_M_0->SetBinContent(39,0.016201367512129593);
  S13_M_0->SetBinContent(40,0.01579520757449922);
  S13_M_0->SetBinContent(41,0.4475006312821231); // overflow
  S13_M_0->SetEntries(100000);
  // Style
  S13_M_0->SetLineColor(9);
  S13_M_0->SetLineStyle(1);
  S13_M_0->SetLineWidth(1);
  S13_M_0->SetFillColor(9);
  S13_M_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_26","mystack");
  stack->Add(S13_M_0);
  stack->Draw("");

  // Y axis
  stack->GetYaxis()->SetLabelSize(0.04);
  stack->GetYaxis()->SetLabelOffset(0.005);
  stack->GetYaxis()->SetTitleSize(0.06);
  stack->GetYaxis()->SetTitleFont(22);
  stack->GetYaxis()->SetTitleOffset(1);
  stack->GetYaxis()->SetTitle("Events  ( L_{int} = 10 fb^{-1} )");

  // X axis
  stack->GetXaxis()->SetLabelSize(0.04);
  stack->GetXaxis()->SetLabelOffset(0.005);
  stack->GetXaxis()->SetTitleSize(0.06);
  stack->GetXaxis()->SetTitleFont(22);
  stack->GetXaxis()->SetTitleOffset(1);
  stack->GetXaxis()->SetTitle("M [ mu+_{1} p_{1} ] (GeV/c^{2}) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_12.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_12.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_12.eps");

}
