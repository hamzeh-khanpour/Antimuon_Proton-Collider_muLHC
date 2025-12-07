void selection_14()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo29","canvas_plotflow_tempo29",0,0,700,500);
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
  TH1F* S15_M_0 = new TH1F("S15_M_0","S15_M_0",40,0.0,500.0);
  // Content
  S15_M_0->SetBinContent(0,0.0); // underflow
  S15_M_0->SetBinContent(1,0.0);
  S15_M_0->SetBinContent(2,0.0);
  S15_M_0->SetBinContent(3,0.0);
  S15_M_0->SetBinContent(4,0.0);
  S15_M_0->SetBinContent(5,0.0);
  S15_M_0->SetBinContent(6,0.0);
  S15_M_0->SetBinContent(7,0.0);
  S15_M_0->SetBinContent(8,0.0);
  S15_M_0->SetBinContent(9,0.0);
  S15_M_0->SetBinContent(10,0.0);
  S15_M_0->SetBinContent(11,0.0);
  S15_M_0->SetBinContent(12,0.0);
  S15_M_0->SetBinContent(13,0.0);
  S15_M_0->SetBinContent(14,0.0);
  S15_M_0->SetBinContent(15,3.008610158779955e-05);
  S15_M_0->SetBinContent(16,0.0004212053822292049);
  S15_M_0->SetBinContent(17,0.0016096065499472437);
  S15_M_0->SetBinContent(18,0.0026776622513143807);
  S15_M_0->SetBinContent(19,0.003805890935856899);
  S15_M_0->SetBinContent(20,0.0053703684984223975);
  S15_M_0->SetBinContent(21,0.007040147031545301);
  S15_M_0->SetBinContent(22,0.0087249675604624);
  S15_M_0->SetBinContent(23,0.009747895274447513);
  S15_M_0->SetBinContent(24,0.010184147152469654);
  S15_M_0->SetBinContent(25,0.011673406736066415);
  S15_M_0->SetBinContent(26,0.013267966290220864);
  S15_M_0->SetBinContent(27,0.01402011607991662);
  S15_M_0->SetBinContent(28,0.013944906100945646);
  S15_M_0->SetBinContent(29,0.014561665928497005);
  S15_M_0->SetBinContent(30,0.015012965802311665);
  S15_M_0->SetBinContent(31,0.01558459564248156);
  S15_M_0->SetBinContent(32,0.016291625444793054);
  S15_M_0->SetBinContent(33,0.017149075205046497);
  S15_M_0->SetBinContent(34,0.016291625444793054);
  S15_M_0->SetBinContent(35,0.017434895125130048);
  S15_M_0->SetBinContent(36,0.01720924518822272);
  S15_M_0->SetBinContent(37,0.016201365470030125);
  S15_M_0->SetBinContent(38,0.01689334527654966);
  S15_M_0->SetBinContent(39,0.017284465167190895);
  S15_M_0->SetBinContent(40,0.01645709539852696);
  S15_M_0->SetBinContent(41,1.205414662960994); // overflow
  S15_M_0->SetEntries(100000);
  // Style
  S15_M_0->SetLineColor(9);
  S15_M_0->SetLineStyle(1);
  S15_M_0->SetLineWidth(1);
  S15_M_0->SetFillColor(9);
  S15_M_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_30","mystack");
  stack->Add(S15_M_0);
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
  stack->GetXaxis()->SetTitle("M [ mu+_{1} p_{1} t_{1} ] (GeV/c^{2}) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_14.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_14.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_14.eps");

}
