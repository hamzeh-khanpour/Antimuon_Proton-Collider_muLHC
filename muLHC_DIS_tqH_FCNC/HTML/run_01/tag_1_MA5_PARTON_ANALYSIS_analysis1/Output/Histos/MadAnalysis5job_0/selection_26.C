void selection_26()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo53","canvas_plotflow_tempo53",0,0,700,500);
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
  TH1F* S27_DELTAR_0 = new TH1F("S27_DELTAR_0","S27_DELTAR_0",40,0.0,10.0);
  // Content
  S27_DELTAR_0->SetBinContent(0,0.0); // underflow
  S27_DELTAR_0->SetBinContent(1,0.00902582979272005);
  S27_DELTAR_0->SetBinContent(2,0.029890542690223825);
  S27_DELTAR_0->SetBinContent(3,0.04452742911075173);
  S27_DELTAR_0->SetBinContent(4,0.054591226649635234);
  S27_DELTAR_0->SetBinContent(5,0.0642187742952043);
  S27_DELTAR_0->SetBinContent(6,0.07187569242269372);
  S27_DELTAR_0->SetBinContent(7,0.07861497077459327);
  S27_DELTAR_0->SetBinContent(8,0.08955126810010568);
  S27_DELTAR_0->SetBinContent(9,0.1000663755286207);
  S27_DELTAR_0->SetBinContent(10,0.12102137040404587);
  S27_DELTAR_0->SetBinContent(11,0.14409736476077753);
  S27_DELTAR_0->SetBinContent(12,0.17603375695068585);
  S27_DELTAR_0->SetBinContent(13,0.19343855269431745);
  S27_DELTAR_0->SetBinContent(14,0.10305997479653159);
  S27_DELTAR_0->SetBinContent(15,0.06695661362566166);
  S27_DELTAR_0->SetBinContent(16,0.04705465849271406);
  S27_DELTAR_0->SetBinContent(17,0.033636261774202716);
  S27_DELTAR_0->SetBinContent(18,0.02415913409184823);
  S27_DELTAR_0->SetBinContent(19,0.01699864584295616);
  S27_DELTAR_0->SetBinContent(20,0.011116817281365984);
  S27_DELTAR_0->SetBinContent(21,0.007747170105418156);
  S27_DELTAR_0->SetBinContent(22,0.005926961550552836);
  S27_DELTAR_0->SetBinContent(23,0.003911193043511989);
  S27_DELTAR_0->SetBinContent(24,0.0025874043672464565);
  S27_DELTAR_0->SetBinContent(25,0.0013990036578715981);
  S27_DELTAR_0->SetBinContent(26,0.0008875398829508163);
  S27_DELTAR_0->SetBinContent(27,0.0007972816050236109);
  S27_DELTAR_0->SetBinContent(28,0.0004813775822784043);
  S27_DELTAR_0->SetBinContent(29,0.0003008610264239935);
  S27_DELTAR_0->SetBinContent(30,0.00016547355953319765);
  S27_DELTAR_0->SetBinContent(31,6.0172195284801147e-05);
  S27_DELTAR_0->SetBinContent(32,3.0086102642399354e-05);
  S27_DELTAR_0->SetBinContent(33,4.5129148963600245e-05);
  S27_DELTAR_0->SetBinContent(34,0.0);
  S27_DELTAR_0->SetBinContent(35,0.0);
  S27_DELTAR_0->SetBinContent(36,1.5043046321200898e-05);
  S27_DELTAR_0->SetBinContent(37,0.0);
  S27_DELTAR_0->SetBinContent(38,1.5043046321200898e-05);
  S27_DELTAR_0->SetBinContent(39,0.0);
  S27_DELTAR_0->SetBinContent(40,0.0);
  S27_DELTAR_0->SetBinContent(41,0.0); // overflow
  S27_DELTAR_0->SetEntries(100000);
  // Style
  S27_DELTAR_0->SetLineColor(9);
  S27_DELTAR_0->SetLineStyle(1);
  S27_DELTAR_0->SetLineWidth(1);
  S27_DELTAR_0->SetFillColor(9);
  S27_DELTAR_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_54","mystack");
  stack->Add(S27_DELTAR_0);
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
  stack->GetXaxis()->SetTitle("#DeltaR [ p_{1}, t_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_26.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_26.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_26.eps");

}
