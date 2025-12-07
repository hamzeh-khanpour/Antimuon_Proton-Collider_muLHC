void selection_7()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo15","canvas_plotflow_tempo15",0,0,700,500);
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
  TH1F* S8_M_0 = new TH1F("S8_M_0","S8_M_0",40,0.0,500.0);
  // Content
  S8_M_0->SetBinContent(0,0.0); // underflow
  S8_M_0->SetBinContent(1,0.0);
  S8_M_0->SetBinContent(2,0.0);
  S8_M_0->SetBinContent(3,0.0);
  S8_M_0->SetBinContent(4,0.0);
  S8_M_0->SetBinContent(5,0.0);
  S8_M_0->SetBinContent(6,0.0);
  S8_M_0->SetBinContent(7,0.0);
  S8_M_0->SetBinContent(8,0.0);
  S8_M_0->SetBinContent(9,0.0);
  S8_M_0->SetBinContent(10,0.0);
  S8_M_0->SetBinContent(11,0.0004464524030764998);
  S8_M_0->SetBinContent(12,0.0008824565060810003);
  S8_M_0->SetBinContent(13,0.0006988109048155001);
  S8_M_0->SetBinContent(14,0.0005487599037815);
  S8_M_0->SetBinContent(15,0.00045820690315749997);
  S8_M_0->SetBinContent(16,0.0003791182026125004);
  S8_M_0->SetBinContent(17,0.0003334789022980003);
  S8_M_0->SetBinContent(18,0.00029553080203650027);
  S8_M_0->SetBinContent(19,0.00026614460183400023);
  S8_M_0->SetBinContent(20,0.00023240490160150024);
  S8_M_0->SetBinContent(21,0.00021288660146699982);
  S8_M_0->SetBinContent(22,0.000193876301336);
  S8_M_0->SetBinContent(23,0.0001706576011760001);
  S8_M_0->SetBinContent(24,0.00016340170112599976);
  S8_M_0->SetBinContent(25,0.00013771600094899982);
  S8_M_0->SetBinContent(26,0.0001315486009065003);
  S8_M_0->SetBinContent(27,0.00012523600086300024);
  S8_M_0->SetBinContent(28,0.00010912800075200015);
  S8_M_0->SetBinContent(29,9.889723068149998e-05);
  S8_M_0->SetBinContent(30,8.648973059600002e-05);
  S8_M_0->SetBinContent(31,8.235390056750004e-05);
  S8_M_0->SetBinContent(32,7.567851052149998e-05);
  S8_M_0->SetBinContent(33,7.306641050350003e-05);
  S8_M_0->SetBinContent(34,7.270362050100004e-05);
  S8_M_0->SetBinContent(35,5.775656039799998e-05);
  S8_M_0->SetBinContent(36,5.630539038799997e-05);
  S8_M_0->SetBinContent(37,5.013792034549999e-05);
  S8_M_0->SetBinContent(38,4.455092030700002e-05);
  S8_M_0->SetBinContent(39,4.3462540299500003e-05);
  S8_M_0->SetBinContent(40,4.157602028650001e-05);
  S8_M_0->SetBinContent(41,0.0006870564047345); // overflow
  S8_M_0->SetEntries(100000);
  // Style
  S8_M_0->SetLineColor(9);
  S8_M_0->SetLineStyle(1);
  S8_M_0->SetLineWidth(1);
  S8_M_0->SetFillColor(9);
  S8_M_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_16","mystack");
  stack->Add(S8_M_0);
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
  stack->GetXaxis()->SetTitle("M [ h_{1} mu+_{1} ] (GeV/c^{2}) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_7.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_7.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_7.eps");

}
