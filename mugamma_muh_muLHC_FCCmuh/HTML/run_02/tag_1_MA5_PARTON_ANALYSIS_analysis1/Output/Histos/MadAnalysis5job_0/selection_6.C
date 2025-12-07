void selection_6()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo13","canvas_plotflow_tempo13",0,0,700,500);
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
  TH1F* S7_ETA_0 = new TH1F("S7_ETA_0","S7_ETA_0",40,-10.0,10.0);
  // Content
  S7_ETA_0->SetBinContent(0,0.0); // underflow
  S7_ETA_0->SetBinContent(1,0.0);
  S7_ETA_0->SetBinContent(2,0.0);
  S7_ETA_0->SetBinContent(3,0.0);
  S7_ETA_0->SetBinContent(4,0.0);
  S7_ETA_0->SetBinContent(5,0.0);
  S7_ETA_0->SetBinContent(6,0.0);
  S7_ETA_0->SetBinContent(7,0.0);
  S7_ETA_0->SetBinContent(8,0.0);
  S7_ETA_0->SetBinContent(9,0.0);
  S7_ETA_0->SetBinContent(10,0.0);
  S7_ETA_0->SetBinContent(11,2.176755085650003e-07);
  S7_ETA_0->SetBinContent(12,2.0316380799400028e-06);
  S7_ETA_0->SetBinContent(13,9.142371359730014e-06);
  S7_ETA_0->SetBinContent(14,3.8238331504585076e-05);
  S7_ETA_0->SetBinContent(15,0.00010629820418257505);
  S7_ETA_0->SetBinContent(16,0.0002570748101152667);
  S7_ETA_0->SetBinContent(17,0.00046125441814923624);
  S7_ETA_0->SetBinContent(18,0.0006694247263402302);
  S7_ETA_0->SetBinContent(19,0.0008375427329552636);
  S7_ETA_0->SetBinContent(20,0.0009305627366153739);
  S7_ETA_0->SetBinContent(21,0.000917502236101475);
  S7_ETA_0->SetBinContent(22,0.0008162831321187502);
  S7_ETA_0->SetBinContent(23,0.0006779140266742634);
  S7_ETA_0->SetBinContent(24,0.0005346836210384962);
  S7_ETA_0->SetBinContent(25,0.00039123541539415926);
  S7_ETA_0->SetBinContent(26,0.00027115111066913485);
  S7_ETA_0->SetBinContent(27,0.00015977380628670956);
  S7_ETA_0->SetBinContent(28,9.904235389707505e-05);
  S7_ETA_0->SetBinContent(29,5.100862200706486e-05);
  S7_ETA_0->SetBinContent(30,2.54680310021049e-05);
  S7_ETA_0->SetBinContent(31,0.0);
  S7_ETA_0->SetBinContent(32,0.0);
  S7_ETA_0->SetBinContent(33,0.0);
  S7_ETA_0->SetBinContent(34,0.0);
  S7_ETA_0->SetBinContent(35,0.0);
  S7_ETA_0->SetBinContent(36,0.0);
  S7_ETA_0->SetBinContent(37,0.0);
  S7_ETA_0->SetBinContent(38,0.0);
  S7_ETA_0->SetBinContent(39,0.0);
  S7_ETA_0->SetBinContent(40,0.0);
  S7_ETA_0->SetBinContent(41,0.0); // overflow
  S7_ETA_0->SetEntries(100000);
  // Style
  S7_ETA_0->SetLineColor(9);
  S7_ETA_0->SetLineStyle(1);
  S7_ETA_0->SetLineWidth(1);
  S7_ETA_0->SetFillColor(9);
  S7_ETA_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_14","mystack");
  stack->Add(S7_ETA_0);
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
  stack->GetXaxis()->SetTitle("#eta [ mu+_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_6.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_6.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_6.eps");

}
