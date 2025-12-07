void selection_13()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo27","canvas_plotflow_tempo27",0,0,700,500);
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
  TH1F* S14_M_0 = new TH1F("S14_M_0","S14_M_0",40,0.0,500.0);
  // Content
  S14_M_0->SetBinContent(0,0.0); // underflow
  S14_M_0->SetBinContent(1,0.0);
  S14_M_0->SetBinContent(2,0.0);
  S14_M_0->SetBinContent(3,0.0);
  S14_M_0->SetBinContent(4,0.0);
  S14_M_0->SetBinContent(5,0.0);
  S14_M_0->SetBinContent(6,0.0);
  S14_M_0->SetBinContent(7,0.0);
  S14_M_0->SetBinContent(8,0.0);
  S14_M_0->SetBinContent(9,0.0);
  S14_M_0->SetBinContent(10,0.0);
  S14_M_0->SetBinContent(11,0.0);
  S14_M_0->SetBinContent(12,0.0002256457145000134);
  S14_M_0->SetBinContent(13,0.0006167649663000316);
  S14_M_0->SetBinContent(14,0.001098142583900025);
  S14_M_0->SetBinContent(15,0.0038359765465004556);
  S14_M_0->SetBinContent(16,0.00753656614430072);
  S14_M_0->SetBinContent(17,0.00985319526650094);
  S14_M_0->SetBinContent(18,0.010755775924501826);
  S14_M_0->SetBinContent(19,0.01200435545139941);
  S14_M_0->SetBinContent(20,0.012275125348801305);
  S14_M_0->SetBinContent(21,0.013839604756000469);
  S14_M_0->SetBinContent(22,0.01382456476169931);
  S14_M_0->SetBinContent(23,0.014486454510900998);
  S14_M_0->SetBinContent(24,0.015313824197400265);
  S14_M_0->SetBinContent(25,0.015088174282901842);
  S14_M_0->SetBinContent(26,0.015960673952300792);
  S14_M_0->SetBinContent(27,0.015674854060601526);
  S14_M_0->SetBinContent(28,0.015028004305700999);
  S14_M_0->SetBinContent(29,0.015614684083400686);
  S14_M_0->SetBinContent(30,0.016171273872501845);
  S14_M_0->SetBinContent(31,0.01550938412330016);
  S14_M_0->SetBinContent(32,0.017043773541900797);
  S14_M_0->SetBinContent(33,0.016081013906702475);
  S14_M_0->SetBinContent(34,0.015449204146103105);
  S14_M_0->SetBinContent(35,0.01623144384970269);
  S14_M_0->SetBinContent(36,0.01653230373570311);
  S14_M_0->SetBinContent(37,0.01620136386110037);
  S14_M_0->SetBinContent(38,0.015644764072003);
  S14_M_0->SetBinContent(39,0.016547353730000477);
  S14_M_0->SetBinContent(40,0.015434164151801948);
  S14_M_0->SetBinContent(41,1.1344265701515681); // overflow
  S14_M_0->SetEntries(100000);
  // Style
  S14_M_0->SetLineColor(9);
  S14_M_0->SetLineStyle(1);
  S14_M_0->SetLineWidth(1);
  S14_M_0->SetFillColor(9);
  S14_M_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_28","mystack");
  stack->Add(S14_M_0);
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
  stack->GetXaxis()->SetTitle("M [ h_{1} mu+_{1} p_{1} ] (GeV/c^{2}) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_13.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_13.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_13.eps");

}
