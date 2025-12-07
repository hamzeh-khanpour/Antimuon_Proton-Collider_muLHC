void selection_10()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo21","canvas_plotflow_tempo21",0,0,700,500);
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
  TH1F* S11_ETA_0 = new TH1F("S11_ETA_0","S11_ETA_0",40,-10.0,10.0);
  // Content
  S11_ETA_0->SetBinContent(0,0.0); // underflow
  S11_ETA_0->SetBinContent(1,0.0);
  S11_ETA_0->SetBinContent(2,0.0);
  S11_ETA_0->SetBinContent(3,0.0);
  S11_ETA_0->SetBinContent(4,0.0);
  S11_ETA_0->SetBinContent(5,0.0);
  S11_ETA_0->SetBinContent(6,0.0);
  S11_ETA_0->SetBinContent(7,0.0);
  S11_ETA_0->SetBinContent(8,0.0);
  S11_ETA_0->SetBinContent(9,6.017219629040085e-05);
  S11_ETA_0->SetBinContent(10,0.00010530137600819408);
  S11_ETA_0->SetBinContent(11,6.017219629040085e-05);
  S11_ETA_0->SetBinContent(12,0.0004813775903232022);
  S11_ETA_0->SetBinContent(13,0.0009477120840738152);
  S11_ETA_0->SetBinContent(14,0.002196285499599555);
  S11_ETA_0->SetBinContent(15,0.00612252060504837);
  S11_ETA_0->SetBinContent(16,0.01568989642522288);
  S11_ETA_0->SetBinContent(17,0.03613340176738619);
  S11_ETA_0->SetBinContent(18,0.0651364051593583);
  S11_ETA_0->SetBinContent(19,0.10250337664568868);
  S11_ETA_0->SetBinContent(20,0.14330006735059375);
  S11_ETA_0->SetBinContent(21,0.1987337547206138);
  S11_ETA_0->SetBinContent(22,0.2462547438934585);
  S11_ETA_0->SetBinContent(23,0.2506172428995092);
  S11_ETA_0->SetBinContent(24,0.19652235522445782);
  S11_ETA_0->SetBinContent(25,0.12491747153887398);
  S11_ETA_0->SetBinContent(26,0.06552752507024577);
  S11_ETA_0->SetBinContent(27,0.02960472325487661);
  S11_ETA_0->SetBinContent(28,0.012199917220377766);
  S11_ETA_0->SetBinContent(29,0.004392569999199337);
  S11_ETA_0->SetBinContent(30,0.0016697786195585844);
  S11_ETA_0->SetBinContent(31,0.000676937245767001);
  S11_ETA_0->SetBinContent(32,0.0002406887451616125);
  S11_ETA_0->SetBinContent(33,0.00015043046572600782);
  S11_ETA_0->SetBinContent(34,3.0086103145199287e-05);
  S11_ETA_0->SetBinContent(35,3.0086103145199287e-05);
  S11_ETA_0->SetBinContent(36,0.0);
  S11_ETA_0->SetBinContent(37,0.0);
  S11_ETA_0->SetBinContent(38,0.0);
  S11_ETA_0->SetBinContent(39,0.0);
  S11_ETA_0->SetBinContent(40,0.0);
  S11_ETA_0->SetBinContent(41,0.0); // overflow
  S11_ETA_0->SetEntries(100000);
  // Style
  S11_ETA_0->SetLineColor(9);
  S11_ETA_0->SetLineStyle(1);
  S11_ETA_0->SetLineWidth(1);
  S11_ETA_0->SetFillColor(9);
  S11_ETA_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_22","mystack");
  stack->Add(S11_ETA_0);
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
  stack->GetXaxis()->SetTitle("#eta [ h_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_10.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_10.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_10.eps");

}
