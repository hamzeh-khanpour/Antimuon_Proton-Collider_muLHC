void selection_23()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo47","canvas_plotflow_tempo47",0,0,700,500);
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
  TH1F* S24_DELTAR_0 = new TH1F("S24_DELTAR_0","S24_DELTAR_0",40,0.0,10.0);
  // Content
  S24_DELTAR_0->SetBinContent(0,0.0); // underflow
  S24_DELTAR_0->SetBinContent(1,0.0017600367237630202);
  S24_DELTAR_0->SetBinContent(2,0.005189852185455011);
  S24_DELTAR_0->SetBinContent(3,0.00947712151257);
  S24_DELTAR_0->SetBinContent(4,0.01313257793884774);
  S24_DELTAR_0->SetBinContent(5,0.01934536696375327);
  S24_DELTAR_0->SetBinContent(6,0.026641245818668335);
  S24_DELTAR_0->SetBinContent(7,0.03347078474677524);
  S24_DELTAR_0->SetBinContent(8,0.04544505286741919);
  S24_DELTAR_0->SetBinContent(9,0.05582476123832859);
  S24_DELTAR_0->SetBinContent(10,0.0686113492314793);
  S24_DELTAR_0->SetBinContent(11,0.08246599705699849);
  S24_DELTAR_0->SetBinContent(12,0.09431992519652975);
  S24_DELTAR_0->SetBinContent(13,0.102969683838954);
  S24_DELTAR_0->SetBinContent(14,0.09740375471252408);
  S24_DELTAR_0->SetBinContent(15,0.09404914523902855);
  S24_DELTAR_0->SetBinContent(16,0.08795671619523257);
  S24_DELTAR_0->SetBinContent(17,0.08293233698380664);
  S24_DELTAR_0->SetBinContent(18,0.07620808803917452);
  S24_DELTAR_0->SetBinContent(19,0.06931837912051127);
  S24_DELTAR_0->SetBinContent(20,0.06214284024670891);
  S24_DELTAR_0->SetBinContent(21,0.05605040120291449);
  S24_DELTAR_0->SetBinContent(22,0.05110124197968283);
  S24_DELTAR_0->SetBinContent(23,0.04445221302324496);
  S24_DELTAR_0->SetBinContent(24,0.03814917401250413);
  S24_DELTAR_0->SetBinContent(25,0.034418494598032603);
  S24_DELTAR_0->SetBinContent(26,0.029484375372440415);
  S24_DELTAR_0->SetBinContent(27,0.02588908593671949);
  S24_DELTAR_0->SetBinContent(28,0.021225746668628514);
  S24_DELTAR_0->SetBinContent(29,0.017464977258879598);
  S24_DELTAR_0->SetBinContent(30,0.014260807761772572);
  S24_DELTAR_0->SetBinContent(31,0.011583148182030052);
  S24_DELTAR_0->SetBinContent(32,0.008649753642425019);
  S24_DELTAR_0->SetBinContent(33,0.006664070954077032);
  S24_DELTAR_0->SetBinContent(34,0.00528011017128906);
  S24_DELTAR_0->SetBinContent(35,0.0034899874522480237);
  S24_DELTAR_0->SetBinContent(36,0.002632533586825026);
  S24_DELTAR_0->SetBinContent(37,0.002030811681265011);
  S24_DELTAR_0->SetBinContent(38,0.0013689177851489633);
  S24_DELTAR_0->SetBinContent(39,0.0008574538654229978);
  S24_DELTAR_0->SetBinContent(40,0.00045129152916999546);
  S24_DELTAR_0->SetBinContent(41,0.00013538747875099552); // overflow
  S24_DELTAR_0->SetEntries(100000);
  // Style
  S24_DELTAR_0->SetLineColor(9);
  S24_DELTAR_0->SetLineStyle(1);
  S24_DELTAR_0->SetLineWidth(1);
  S24_DELTAR_0->SetFillColor(9);
  S24_DELTAR_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_48","mystack");
  stack->Add(S24_DELTAR_0);
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
  stack->GetXaxis()->SetTitle("#DeltaR [ mu+_{1}, p_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_23.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_23.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_23.eps");

}
