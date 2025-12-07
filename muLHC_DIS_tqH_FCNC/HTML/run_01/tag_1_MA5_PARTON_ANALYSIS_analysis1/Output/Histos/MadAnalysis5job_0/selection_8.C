void selection_8()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo17","canvas_plotflow_tempo17",0,0,700,500);
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
  TH1F* S9_ETA_0 = new TH1F("S9_ETA_0","S9_ETA_0",40,-10.0,10.0);
  // Content
  S9_ETA_0->SetBinContent(0,0.0); // underflow
  S9_ETA_0->SetBinContent(1,0.0);
  S9_ETA_0->SetBinContent(2,0.0);
  S9_ETA_0->SetBinContent(3,0.0);
  S9_ETA_0->SetBinContent(4,0.0);
  S9_ETA_0->SetBinContent(5,0.0);
  S9_ETA_0->SetBinContent(6,0.0);
  S9_ETA_0->SetBinContent(7,0.0);
  S9_ETA_0->SetBinContent(8,0.0);
  S9_ETA_0->SetBinContent(9,0.0);
  S9_ETA_0->SetBinContent(10,3.008610500659917e-05);
  S9_ETA_0->SetBinContent(11,0.0001203443800264033);
  S9_ETA_0->SetBinContent(12,0.00036103324007919337);
  S9_ETA_0->SetBinContent(13,0.0007521524751650041);
  S9_ETA_0->SetBinContent(14,0.0027227925480972173);
  S9_ETA_0->SetBinContent(15,0.0062579089613727735);
  S9_ETA_0->SetBinContent(16,0.015930587355995132);
  S9_ETA_0->SetBinContent(17,0.034839704217642736);
  S9_ETA_0->SetBinContent(18,0.06626463900203589);
  S9_ETA_0->SetBinContent(19,0.10617388237828551);
  S9_ETA_0->SetBinContent(20,0.1477377754799124);
  S9_ETA_0->SetBinContent(21,0.19771076718587838);
  S9_ETA_0->SetBinContent(22,0.23886856035490578);
  S9_ETA_0->SetBinContent(23,0.23766516055463444);
  S9_ETA_0->SetBinContent(24,0.18671436901095423);
  S9_ETA_0->SetBinContent(25,0.12872337863573813);
  S9_ETA_0->SetBinContent(26,0.07119875818311848);
  S9_ETA_0->SetBinContent(27,0.0357573340653434);
  S9_ETA_0->SetBinContent(28,0.015238607470843261);
  S9_ETA_0->SetBinContent(29,0.00714544881406749);
  S9_ETA_0->SetBinContent(30,0.002587404570567605);
  S9_ETA_0->SetBinContent(31,0.0009025830501979916);
  S9_ETA_0->SetBinContent(32,0.00034599014257590124);
  S9_ETA_0->SetBinContent(33,0.00015043047503300415);
  S9_ETA_0->SetBinContent(34,7.521524751650041e-05);
  S9_ETA_0->SetBinContent(35,1.5043047503300413e-05);
  S9_ETA_0->SetBinContent(36,1.5043047503300413e-05);
  S9_ETA_0->SetBinContent(37,0.0);
  S9_ETA_0->SetBinContent(38,0.0);
  S9_ETA_0->SetBinContent(39,0.0);
  S9_ETA_0->SetBinContent(40,0.0);
  S9_ETA_0->SetBinContent(41,0.0); // overflow
  S9_ETA_0->SetEntries(100000);
  // Style
  S9_ETA_0->SetLineColor(9);
  S9_ETA_0->SetLineStyle(1);
  S9_ETA_0->SetLineWidth(1);
  S9_ETA_0->SetFillColor(9);
  S9_ETA_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_18","mystack");
  stack->Add(S9_ETA_0);
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
  stack->GetXaxis()->SetTitle("#eta [ t_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_8.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_8.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_8.eps");

}
