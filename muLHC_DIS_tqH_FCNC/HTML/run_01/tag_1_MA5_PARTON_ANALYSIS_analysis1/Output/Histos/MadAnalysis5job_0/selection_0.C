void selection_0()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo1","canvas_plotflow_tempo1",0,0,700,500);
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
  TH1F* S1_THT_0 = new TH1F("S1_THT_0","S1_THT_0",40,0.0,500.0);
  // Content
  S1_THT_0->SetBinContent(0,0.0); // underflow
  S1_THT_0->SetBinContent(1,0.33020994665907705);
  S1_THT_0->SetBinContent(2,0.24911295975919165);
  S1_THT_0->SetBinContent(3,0.16350287358833596);
  S1_THT_0->SetBinContent(4,0.12004358060859328);
  S1_THT_0->SetBinContent(5,0.08672318599104956);
  S1_THT_0->SetBinContent(6,0.059811170338319425);
  S1_THT_0->SetBinContent(7,0.04463273279018944);
  S1_THT_0->SetBinContent(8,0.032297424782790574);
  S1_THT_0->SetBinContent(9,0.026430635730490502);
  S1_THT_0->SetBinContent(10,0.023331766231070694);
  S1_THT_0->SetBinContent(11,0.018397647028110503);
  S1_THT_0->SetBinContent(12,0.016667697307560337);
  S1_THT_0->SetBinContent(13,0.015990757416910764);
  S1_THT_0->SetBinContent(14,0.014095337723090021);
  S1_THT_0->SetBinContent(15,0.012771547936930245);
  S1_THT_0->SetBinContent(16,0.012064528051139684);
  S1_THT_0->SetBinContent(17,0.012079568048710177);
  S1_THT_0->SetBinContent(18,0.011267248179929397);
  S1_THT_0->SetBinContent(19,0.010394748320869875);
  S1_THT_0->SetBinContent(20,0.010635438281989687);
  S1_THT_0->SetBinContent(21,0.010169098357320557);
  S1_THT_0->SetBinContent(22,0.008935571556580021);
  S1_THT_0->SetBinContent(23,0.00923643250798003);
  S1_THT_0->SetBinContent(24,0.008409064641630049);
  S1_THT_0->SetBinContent(25,0.008394021644060041);
  S1_THT_0->SetBinContent(26,0.008544452619759965);
  S1_THT_0->SetBinContent(27,0.0075967407728499145);
  S1_THT_0->SetBinContent(28,0.008228548670789948);
  S1_THT_0->SetBinContent(29,0.00803298870238);
  S1_THT_0->SetBinContent(30,0.007882558726679914);
  S1_THT_0->SetBinContent(31,0.006844587894349976);
  S1_THT_0->SetBinContent(32,0.0072507498287400435);
  S1_THT_0->SetBinContent(33,0.006558769940519976);
  S1_THT_0->SetBinContent(34,0.006423381962390063);
  S1_THT_0->SetBinContent(35,0.006408338964820054);
  S1_THT_0->SetBinContent(36,0.00579157406445003);
  S1_THT_0->SetBinContent(37,0.00559601509603992);
  S1_THT_0->SetBinContent(38,0.00568627308145997);
  S1_THT_0->SetBinContent(39,0.005069508181089946);
  S1_THT_0->SetBinContent(40,0.0049942921932400654);
  S1_THT_0->SetBinContent(41,0.08779123581852064); // overflow
  S1_THT_0->SetEntries(100000);
  // Style
  S1_THT_0->SetLineColor(9);
  S1_THT_0->SetLineStyle(1);
  S1_THT_0->SetLineWidth(1);
  S1_THT_0->SetFillColor(9);
  S1_THT_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_2","mystack");
  stack->Add(S1_THT_0);
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
  stack->GetXaxis()->SetTitle("H_{T} (GeV) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_0.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_0.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_0.eps");

}
