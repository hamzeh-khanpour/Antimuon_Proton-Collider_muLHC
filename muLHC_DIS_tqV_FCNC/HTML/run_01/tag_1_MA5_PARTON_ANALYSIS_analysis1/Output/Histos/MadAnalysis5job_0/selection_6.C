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
  S7_ETA_0->SetBinContent(11,30.96085033249299);
  S7_ETA_0->SetBinContent(12,35.213920378167316);
  S7_ETA_0->SetBinContent(13,38.80057041668486);
  S7_ETA_0->SetBinContent(14,44.73820048044992);
  S7_ETA_0->SetBinContent(15,53.6099405757248);
  S7_ETA_0->SetBinContent(16,62.12533066717279);
  S7_ETA_0->SetBinContent(17,65.7721407063364);
  S7_ETA_0->SetBinContent(18,55.53516059640001);
  S7_ETA_0->SetBinContent(19,38.920890417977);
  S7_ETA_0->SetBinContent(20,22.3112502396037);
  S7_ETA_0->SetBinContent(21,10.366560111327969);
  S7_ETA_0->SetBinContent(22,3.3135980355852026);
  S7_ETA_0->SetBinContent(23,0.8793067094430003);
  S7_ETA_0->SetBinContent(24,0.1943731020874005);
  S7_ETA_0->SetBinContent(25,0.04627930049700001);
  S7_ETA_0->SetBinContent(26,0.004627930049700002);
  S7_ETA_0->SetBinContent(27,0.0);
  S7_ETA_0->SetBinContent(28,0.0);
  S7_ETA_0->SetBinContent(29,0.0);
  S7_ETA_0->SetBinContent(30,0.0);
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
