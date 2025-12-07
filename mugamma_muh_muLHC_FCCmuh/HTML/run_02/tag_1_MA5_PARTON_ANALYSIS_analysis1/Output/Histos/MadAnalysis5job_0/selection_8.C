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
  TH1F* S9_DELTAR_0 = new TH1F("S9_DELTAR_0","S9_DELTAR_0",40,0.0,10.0);
  // Content
  S9_DELTAR_0->SetBinContent(0,0.0); // underflow
  S9_DELTAR_0->SetBinContent(1,0.0);
  S9_DELTAR_0->SetBinContent(2,0.0);
  S9_DELTAR_0->SetBinContent(3,0.0);
  S9_DELTAR_0->SetBinContent(4,0.0);
  S9_DELTAR_0->SetBinContent(5,0.0);
  S9_DELTAR_0->SetBinContent(6,0.0);
  S9_DELTAR_0->SetBinContent(7,0.0);
  S9_DELTAR_0->SetBinContent(8,0.0);
  S9_DELTAR_0->SetBinContent(9,0.0);
  S9_DELTAR_0->SetBinContent(10,0.0);
  S9_DELTAR_0->SetBinContent(11,0.0);
  S9_DELTAR_0->SetBinContent(12,0.0);
  S9_DELTAR_0->SetBinContent(13,0.0002156439056468012);
  S9_DELTAR_0->SetBinContent(14,0.0004116244107787011);
  S9_DELTAR_0->SetBinContent(15,0.0004505883117990007);
  S9_DELTAR_0->SetBinContent(16,0.00047293631238420035);
  S9_DELTAR_0->SetBinContent(17,0.00047801541251720045);
  S9_DELTAR_0->SetBinContent(18,0.00046792981225310127);
  S9_DELTAR_0->SetBinContent(19,0.00046256041211249944);
  S9_DELTAR_0->SetBinContent(20,0.00045102361181039943);
  S9_DELTAR_0->SetBinContent(21,0.00044108311155009977);
  S9_DELTAR_0->SetBinContent(22,0.0004032801105601992);
  S9_DELTAR_0->SetBinContent(23,0.00038789771015739925);
  S9_DELTAR_0->SetBinContent(24,0.00036337300951520113);
  S9_DELTAR_0->SetBinContent(25,0.00032201460843219967);
  S9_DELTAR_0->SetBinContent(26,0.0003008275078773992);
  S9_DELTAR_0->SetBinContent(27,0.00026338730689699877);
  S9_DELTAR_0->SetBinContent(28,0.00023958820627380104);
  S9_DELTAR_0->SetBinContent(29,0.00020316380532000019);
  S9_DELTAR_0->SetBinContent(30,0.00018110600474239972);
  S9_DELTAR_0->SetBinContent(31,0.00015607330408689925);
  S9_DELTAR_0->SetBinContent(32,0.0001340881035111999);
  S9_DELTAR_0->SetBinContent(33,0.00011028890288799957);
  S9_DELTAR_0->SetBinContent(34,8.90292823313001e-05);
  S9_DELTAR_0->SetBinContent(35,7.132500186769992e-05);
  S9_DELTAR_0->SetBinContent(36,5.333050139650011e-05);
  S9_DELTAR_0->SetBinContent(37,4.46234811685001e-05);
  S9_DELTAR_0->SetBinContent(38,3.1345270820799975e-05);
  S9_DELTAR_0->SetBinContent(39,1.8937770495900055e-05);
  S9_DELTAR_0->SetBinContent(40,1.6180550423700133e-05);
  S9_DELTAR_0->SetBinContent(41,1.458426038190005e-05); // overflow
  S9_DELTAR_0->SetEntries(100000);
  // Style
  S9_DELTAR_0->SetLineColor(9);
  S9_DELTAR_0->SetLineStyle(1);
  S9_DELTAR_0->SetLineWidth(1);
  S9_DELTAR_0->SetFillColor(9);
  S9_DELTAR_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_18","mystack");
  stack->Add(S9_DELTAR_0);
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
  stack->GetXaxis()->SetTitle("#DeltaR [ h_{1}, mu+_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_8.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_8.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_8.eps");

}
