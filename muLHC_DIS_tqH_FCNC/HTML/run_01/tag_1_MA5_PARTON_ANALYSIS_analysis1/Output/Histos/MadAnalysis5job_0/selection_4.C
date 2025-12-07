void selection_4()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo9","canvas_plotflow_tempo9",0,0,700,500);
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
  TH1F* S5_ETA_0 = new TH1F("S5_ETA_0","S5_ETA_0",40,-10.0,10.0);
  // Content
  S5_ETA_0->SetBinContent(0,0.0); // underflow
  S5_ETA_0->SetBinContent(1,0.0);
  S5_ETA_0->SetBinContent(2,0.0);
  S5_ETA_0->SetBinContent(3,0.0);
  S5_ETA_0->SetBinContent(4,0.0);
  S5_ETA_0->SetBinContent(5,0.0);
  S5_ETA_0->SetBinContent(6,0.0);
  S5_ETA_0->SetBinContent(7,0.0);
  S5_ETA_0->SetBinContent(8,0.0);
  S5_ETA_0->SetBinContent(9,0.0);
  S5_ETA_0->SetBinContent(10,0.0);
  S5_ETA_0->SetBinContent(11,0.04818289187687124);
  S5_ETA_0->SetBinContent(12,0.07533559729921072);
  S5_ETA_0->SetBinContent(13,0.102789182670825);
  S5_ETA_0->SetBinContent(14,0.12896407825801293);
  S5_ETA_0->SetBinContent(15,0.1743639706040686);
  S5_ETA_0->SetBinContent(16,0.22048596282838587);
  S5_ETA_0->SetBinContent(17,0.2175224633280007);
  S5_ETA_0->SetBinContent(18,0.18681966850416898);
  S5_ETA_0->SetBinContent(19,0.14503007554945477);
  S5_ETA_0->SetBinContent(20,0.10140518290415279);
  S5_ETA_0->SetBinContent(21,0.06084913974147508);
  S5_ETA_0->SetBinContent(22,0.0278145953107518);
  S5_ETA_0->SetBinContent(23,0.010093888298276605);
  S5_ETA_0->SetBinContent(24,0.0030687824826355526);
  S5_ETA_0->SetBinContent(25,0.0009627552376895937);
  S5_ETA_0->SetBinContent(26,0.00042120542898919515);
  S5_ETA_0->SetBinContent(27,0.00010530138224729455);
  S5_ETA_0->SetBinContent(28,6.0172199855600025e-05);
  S5_ETA_0->SetBinContent(29,1.5043047463900428e-05);
  S5_ETA_0->SetBinContent(30,1.5043047463900428e-05);
  S5_ETA_0->SetBinContent(31,0.0);
  S5_ETA_0->SetBinContent(32,0.0);
  S5_ETA_0->SetBinContent(33,0.0);
  S5_ETA_0->SetBinContent(34,0.0);
  S5_ETA_0->SetBinContent(35,0.0);
  S5_ETA_0->SetBinContent(36,0.0);
  S5_ETA_0->SetBinContent(37,0.0);
  S5_ETA_0->SetBinContent(38,0.0);
  S5_ETA_0->SetBinContent(39,0.0);
  S5_ETA_0->SetBinContent(40,0.0);
  S5_ETA_0->SetBinContent(41,0.0); // overflow
  S5_ETA_0->SetEntries(100000);
  // Style
  S5_ETA_0->SetLineColor(9);
  S5_ETA_0->SetLineStyle(1);
  S5_ETA_0->SetLineWidth(1);
  S5_ETA_0->SetFillColor(9);
  S5_ETA_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_10","mystack");
  stack->Add(S5_ETA_0);
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
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_4.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_4.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_4.eps");

}
