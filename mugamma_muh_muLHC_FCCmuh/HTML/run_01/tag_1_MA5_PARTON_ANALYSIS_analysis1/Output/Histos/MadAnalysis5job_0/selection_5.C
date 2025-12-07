void selection_5()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo11","canvas_plotflow_tempo11",0,0,700,500);
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
  TH1F* S6_PT_0 = new TH1F("S6_PT_0","S6_PT_0",40,0.0,500.0);
  // Content
  S6_PT_0->SetBinContent(0,0.0); // underflow
  S6_PT_0->SetBinContent(1,0.0019697290086536385);
  S6_PT_0->SetBinContent(2,0.0012516430054988611);
  S6_PT_0->SetBinContent(3,0.0005796052025463878);
  S6_PT_0->SetBinContent(4,0.00032387850142290005);
  S6_PT_0->SetBinContent(5,0.0001960877008614749);
  S6_PT_0->SetBinContent(6,0.00013282110058352483);
  S6_PT_0->SetBinContent(7,8.7160850382925e-05);
  S6_PT_0->SetBinContent(8,6.6458940291975e-05);
  S6_PT_0->SetBinContent(9,4.9481440217387516e-05);
  S6_PT_0->SetBinContent(10,3.5502810155975e-05);
  S6_PT_0->SetBinContent(11,2.9166480128137513e-05);
  S6_PT_0->SetBinContent(12,2.2733410099875012e-05);
  S6_PT_0->SetBinContent(13,1.542970006778752e-05);
  S6_PT_0->SetBinContent(14,1.19955000527e-05);
  S6_PT_0->SetBinContent(15,1.1656920051212513e-05);
  S6_PT_0->SetBinContent(16,8.0776150354875e-06);
  S6_PT_0->SetBinContent(17,7.061867031025001e-06);
  S6_PT_0->SetBinContent(18,5.562429024437499e-06);
  S6_PT_0->SetBinContent(19,4.643419020399999e-06);
  S6_PT_0->SetBinContent(20,4.208099018487501e-06);
  S6_PT_0->SetBinContent(21,3.337458014662502e-06);
  S6_PT_0->SetBinContent(22,2.5635540112624985e-06);
  S6_PT_0->SetBinContent(23,2.4668170108375025e-06);
  S6_PT_0->SetBinContent(24,1.6445440072249986e-06);
  S6_PT_0->SetBinContent(25,1.8380200080749994e-06);
  S6_PT_0->SetBinContent(26,1.0157480044625e-06);
  S6_PT_0->SetBinContent(27,1.209224005312501e-06);
  S6_PT_0->SetBinContent(28,1.741282007649999e-06);
  S6_PT_0->SetBinContent(29,1.209224005312501e-06);
  S6_PT_0->SetBinContent(30,5.8042740255e-07);
  S6_PT_0->SetBinContent(31,6.771653029749999e-07);
  S6_PT_0->SetBinContent(32,5.8042740255e-07);
  S6_PT_0->SetBinContent(33,5.320585023375002e-07);
  S6_PT_0->SetBinContent(34,6.287964027625001e-07);
  S6_PT_0->SetBinContent(35,5.320585023375002e-07);
  S6_PT_0->SetBinContent(36,4.83689502125e-07);
  S6_PT_0->SetBinContent(37,5.8042740255e-07);
  S6_PT_0->SetBinContent(38,4.353206019125002e-07);
  S6_PT_0->SetBinContent(39,1.9347580085000002e-07);
  S6_PT_0->SetBinContent(40,4.8368950212500005e-08);
  S6_PT_0->SetBinContent(41,1.6929130074374986e-06); // overflow
  S6_PT_0->SetEntries(100000);
  // Style
  S6_PT_0->SetLineColor(9);
  S6_PT_0->SetLineStyle(1);
  S6_PT_0->SetLineWidth(1);
  S6_PT_0->SetFillColor(9);
  S6_PT_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_12","mystack");
  stack->Add(S6_PT_0);
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
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_5.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_5.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_5.eps");

}
