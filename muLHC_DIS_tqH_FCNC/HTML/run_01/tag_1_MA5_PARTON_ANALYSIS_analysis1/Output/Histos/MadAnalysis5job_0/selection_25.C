void selection_25()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo51","canvas_plotflow_tempo51",0,0,700,500);
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
  TH1F* S26_DELTAR_0 = new TH1F("S26_DELTAR_0","S26_DELTAR_0",40,0.0,10.0);
  // Content
  S26_DELTAR_0->SetBinContent(0,0.0); // underflow
  S26_DELTAR_0->SetBinContent(1,0.009116088720188539);
  S26_DELTAR_0->SetBinContent(2,0.03071790568750053);
  S26_DELTAR_0->SetBinContent(3,0.049401373064520825);
  S26_DELTAR_0->SetBinContent(4,0.06665576064217023);
  S26_DELTAR_0->SetBinContent(5,0.07753187911526746);
  S26_DELTAR_0->SetBinContent(6,0.08727977774675595);
  S26_DELTAR_0->SetBinContent(7,0.0988328461248159);
  S26_DELTAR_0->SetBinContent(8,0.10700118497805944);
  S26_DELTAR_0->SetBinContent(9,0.12007358314282006);
  S26_DELTAR_0->SetBinContent(10,0.13313098130968654);
  S26_DELTAR_0->SetBinContent(11,0.145240679609601);
  S26_DELTAR_0->SetBinContent(12,0.15935107762863637);
  S26_DELTAR_0->SetBinContent(13,0.14697057936673963);
  S26_DELTAR_0->SetBinContent(14,0.08425612817124736);
  S26_DELTAR_0->SetBinContent(15,0.05239494264425235);
  S26_DELTAR_0->SetBinContent(16,0.03893141453440263);
  S26_DELTAR_0->SetBinContent(17,0.028025206065529742);
  S26_DELTAR_0->SetBinContent(18,0.020112557176389788);
  S26_DELTAR_0->SetBinContent(19,0.014140468014813853);
  S26_DELTAR_0->SetBinContent(20,0.011282288416074869);
  S26_DELTAR_0->SetBinContent(21,0.007220663986288);
  S26_DELTAR_0->SetBinContent(22,0.0052048952692826025);
  S26_DELTAR_0->SetBinContent(23,0.003971365442458364);
  S26_DELTAR_0->SetBinContent(24,0.0026927056219699453);
  S26_DELTAR_0->SetBinContent(25,0.0018653387381243238);
  S26_DELTAR_0->SetBinContent(26,0.0009777982627264979);
  S26_DELTAR_0->SetBinContent(27,0.0007972816880692944);
  S26_DELTAR_0->SetBinContent(28,0.0004512915366429947);
  S26_DELTAR_0->SetBinContent(29,0.0002858179598738985);
  S26_DELTAR_0->SetBinContent(30,0.0001353874809928956);
  S26_DELTAR_0->SetBinContent(31,6.017220155239976e-05);
  S26_DELTAR_0->SetBinContent(32,6.017220155239976e-05);
  S26_DELTAR_0->SetBinContent(33,6.017220155239976e-05);
  S26_DELTAR_0->SetBinContent(34,1.5043047888100291e-05);
  S26_DELTAR_0->SetBinContent(35,3.008610577619918e-05);
  S26_DELTAR_0->SetBinContent(36,0.0);
  S26_DELTAR_0->SetBinContent(37,1.5043047888100291e-05);
  S26_DELTAR_0->SetBinContent(38,1.5043047888100291e-05);
  S26_DELTAR_0->SetBinContent(39,0.0);
  S26_DELTAR_0->SetBinContent(40,0.0);
  S26_DELTAR_0->SetBinContent(41,0.0); // overflow
  S26_DELTAR_0->SetEntries(100000);
  // Style
  S26_DELTAR_0->SetLineColor(9);
  S26_DELTAR_0->SetLineStyle(1);
  S26_DELTAR_0->SetLineWidth(1);
  S26_DELTAR_0->SetFillColor(9);
  S26_DELTAR_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_52","mystack");
  stack->Add(S26_DELTAR_0);
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
  stack->GetXaxis()->SetTitle("#DeltaR [ p_{1}, h_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_25.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_25.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_25.eps");

}
