void selection_24()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo49","canvas_plotflow_tempo49",0,0,700,500);
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
  TH1F* S25_DELTAR_0 = new TH1F("S25_DELTAR_0","S25_DELTAR_0",40,0.0,10.0);
  // Content
  S25_DELTAR_0->SetBinContent(0,0.0); // underflow
  S25_DELTAR_0->SetBinContent(1,0.0017600367873993072);
  S25_DELTAR_0->SetBinContent(2,0.00532524035674652);
  S25_DELTAR_0->SetBinContent(3,0.010154058773457495);
  S25_DELTAR_0->SetBinContent(4,0.014275858275571636);
  S25_DELTAR_0->SetBinContent(5,0.019270147672294822);
  S25_DELTAR_0->SetBinContent(6,0.025693526896393495);
  S25_DELTAR_0->SetBinContent(7,0.0332601859823916);
  S25_DELTAR_0->SetBinContent(8,0.04192498493574174);
  S25_DELTAR_0->SetBinContent(9,0.05417002345662284);
  S25_DELTAR_0->SetBinContent(10,0.07001036154321576);
  S25_DELTAR_0->SetBinContent(11,0.08887433926457321);
  S25_DELTAR_0->SetBinContent(12,0.116087185977443);
  S25_DELTAR_0->SetBinContent(13,0.14021628306280917);
  S25_DELTAR_0->SetBinContent(14,0.10773828698593425);
  S25_DELTAR_0->SetBinContent(15,0.09943456798896808);
  S25_DELTAR_0->SetBinContent(16,0.088648699291829);
  S25_DELTAR_0->SetBinContent(17,0.08391013986421533);
  S25_DELTAR_0->SetBinContent(18,0.07655408075277817);
  S25_DELTAR_0->SetBinContent(19,0.06841579173582915);
  S25_DELTAR_0->SetBinContent(20,0.06306047238271596);
  S25_DELTAR_0->SetBinContent(21,0.05496730336031675);
  S25_DELTAR_0->SetBinContent(22,0.047505954261597906);
  S25_DELTAR_0->SetBinContent(23,0.04079675507202437);
  S25_DELTAR_0->SetBinContent(24,0.03356104594604972);
  S25_DELTAR_0->SetBinContent(25,0.0288074465202528);
  S25_DELTAR_0->SetBinContent(26,0.022715007256178782);
  S25_DELTAR_0->SetBinContent(27,0.018352517783138386);
  S25_DELTAR_0->SetBinContent(28,0.014501498248315833);
  S25_DELTAR_0->SetBinContent(29,0.01024431876255469);
  S25_DELTAR_0->SetBinContent(30,0.007852472051473804);
  S25_DELTAR_0->SetBinContent(31,0.005641144318587431);
  S25_DELTAR_0->SetBinContent(32,0.0032342556093235162);
  S25_DELTAR_0->SetBinContent(33,0.002873222652933887);
  S25_DELTAR_0->SetBinContent(34,0.001624649803753151);
  S25_DELTAR_0->SetBinContent(35,0.0011884008564491111);
  S25_DELTAR_0->SetBinContent(36,0.0007220664127791983);
  S25_DELTAR_0->SetBinContent(37,0.0004061623509382998);
  S25_DELTAR_0->SetBinContent(38,0.0001805165781948026);
  S25_DELTAR_0->SetBinContent(39,0.00012034438546320172);
  S25_DELTAR_0->SetBinContent(40,6.0172202731599655e-05);
  S25_DELTAR_0->SetBinContent(41,0.00016547358001189633); // overflow
  S25_DELTAR_0->SetEntries(100000);
  // Style
  S25_DELTAR_0->SetLineColor(9);
  S25_DELTAR_0->SetLineStyle(1);
  S25_DELTAR_0->SetLineWidth(1);
  S25_DELTAR_0->SetFillColor(9);
  S25_DELTAR_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_50","mystack");
  stack->Add(S25_DELTAR_0);
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
  stack->GetXaxis()->SetTitle("#DeltaR [ mu+_{1}, t_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_24.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_24.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_24.eps");

}
