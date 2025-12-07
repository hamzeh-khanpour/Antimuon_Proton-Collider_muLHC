void selection_3()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo7","canvas_plotflow_tempo7",0,0,700,500);
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
  TH1F* S4_PT_0 = new TH1F("S4_PT_0","S4_PT_0",40,0.0,500.0);
  // Content
  S4_PT_0->SetBinContent(0,0.0); // underflow
  S4_PT_0->SetBinContent(1,0.1902043639645925);
  S4_PT_0->SetBinContent(2,0.19819216245125407);
  S4_PT_0->SetBinContent(3,0.14632377227804533);
  S4_PT_0->SetBinContent(4,0.12105137706605881);
  S4_PT_0->SetBinContent(5,0.10038228098194843);
  S4_PT_0->SetBinContent(6,0.08202975445894949);
  S4_PT_0->SetBinContent(7,0.07059703662494944);
  S4_PT_0->SetBinContent(8,0.05740427912439995);
  S4_PT_0->SetBinContent(9,0.04840853082870078);
  S4_PT_0->SetBinContent(10,0.041819682076999425);
  S4_PT_0->SetBinContent(11,0.03455388345355046);
  S4_PT_0->SetBinContent(12,0.031093984109050052);
  S4_PT_0->SetBinContent(13,0.027032364878549243);
  S4_PT_0->SetBinContent(14,0.02361758552550057);
  S4_PT_0->SetBinContent(15,0.02121069598150086);
  S4_PT_0->SetBinContent(16,0.0193002363434494);
  S4_PT_0->SetBinContent(17,0.017886186611349972);
  S4_PT_0->SetBinContent(18,0.015674857030300204);
  S4_PT_0->SetBinContent(19,0.015012967155699388);
  S4_PT_0->SetBinContent(20,0.013358227469200179);
  S4_PT_0->SetBinContent(21,0.012651207603149518);
  S4_PT_0->SetBinContent(22,0.011718537779849656);
  S4_PT_0->SetBinContent(23,0.01045491801925033);
  S4_PT_0->SetBinContent(24,0.010169098073400709);
  S4_PT_0->SetBinContent(25,0.009296604238700127);
  S4_PT_0->SetBinContent(26,0.009477121204500057);
  S4_PT_0->SetBinContent(27,0.008243591438199995);
  S4_PT_0->SetBinContent(28,0.008318806423950045);
  S4_PT_0->SetBinContent(29,0.007431266592100022);
  S4_PT_0->SetBinContent(30,0.0072808356206001115);
  S4_PT_0->SetBinContent(31,0.007070233660499971);
  S4_PT_0->SetBinContent(32,0.006618941746000049);
  S4_PT_0->SetBinContent(33,0.006318080803000039);
  S4_PT_0->SetBinContent(34,0.005791573902750067);
  S4_PT_0->SetBinContent(35,0.005325239991099946);
  S4_PT_0->SetBinContent(36,0.005310196993949936);
  S4_PT_0->SetBinContent(37,0.005686272922699997);
  S4_PT_0->SetBinContent(38,0.0048438620823000045);
  S4_PT_0->SetBinContent(39,0.0041368382162501015);
  S4_PT_0->SetBinContent(40,0.004287269187750012);
  S4_PT_0->SetBinContent(41,0.07872027508595107); // overflow
  S4_PT_0->SetEntries(100000);
  // Style
  S4_PT_0->SetLineColor(9);
  S4_PT_0->SetLineStyle(1);
  S4_PT_0->SetLineWidth(1);
  S4_PT_0->SetFillColor(9);
  S4_PT_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_8","mystack");
  stack->Add(S4_PT_0);
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
  stack->GetXaxis()->SetTitle("p_{T} [ mu+_{1} ] (GeV/c) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_3.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_3.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_3.eps");

}
