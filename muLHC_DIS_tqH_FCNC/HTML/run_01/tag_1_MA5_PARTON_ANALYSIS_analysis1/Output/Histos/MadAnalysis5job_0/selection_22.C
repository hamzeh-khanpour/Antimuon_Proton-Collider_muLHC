void selection_22()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo45","canvas_plotflow_tempo45",0,0,700,500);
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
  TH1F* S23_DELTAR_0 = new TH1F("S23_DELTAR_0","S23_DELTAR_0",40,0.0,10.0);
  // Content
  S23_DELTAR_0->SetBinContent(0,0.0); // underflow
  S23_DELTAR_0->SetBinContent(1,0.001579520693819914);
  S23_DELTAR_0->SetBinContent(2,0.004197011186435954);
  S23_DELTAR_0->SetBinContent(3,0.007536567539084098);
  S23_DELTAR_0->SetBinContent(4,0.011522977766343714);
  S23_DELTAR_0->SetBinContent(5,0.015464257002351687);
  S23_DELTAR_0->SetBinContent(6,0.021361125859280995);
  S23_DELTAR_0->SetBinContent(7,0.028882654401280305);
  S23_DELTAR_0->SetBinContent(8,0.03879602247963666);
  S23_DELTAR_0->SetBinContent(9,0.05030396024889579);
  S23_DELTAR_0->SetBinContent(10,0.06585846723375309);
  S23_DELTAR_0->SetBinContent(11,0.09036360248358777);
  S23_DELTAR_0->SetBinContent(12,0.1239697759692438);
  S23_DELTAR_0->SetBinContent(13,0.1460379716914638);
  S23_DELTAR_0->SetBinContent(14,0.12351847605672543);
  S23_DELTAR_0->SetBinContent(15,0.10782857909811264);
  S23_DELTAR_0->SetBinContent(16,0.09811077098184821);
  S23_DELTAR_0->SetBinContent(17,0.0878514129705598);
  S23_DELTAR_0->SetBinContent(18,0.07941225460643722);
  S23_DELTAR_0->SetBinContent(19,0.06892725663888769);
  S23_DELTAR_0->SetBinContent(20,0.060909308193116234);
  S23_DELTAR_0->SetBinContent(21,0.050710120170164255);
  S23_DELTAR_0->SetBinContent(22,0.04362484154360066);
  S23_DELTAR_0->SetBinContent(23,0.03781822266917697);
  S23_DELTAR_0->SetBinContent(24,0.030808164028032457);
  S23_DELTAR_0->SetBinContent(25,0.026220034917412236);
  S23_DELTAR_0->SetBinContent(26,0.02059393600799589);
  S23_DELTAR_0->SetBinContent(27,0.016366836827392303);
  S23_DELTAR_0->SetBinContent(28,0.013704217343524233);
  S23_DELTAR_0->SetBinContent(29,0.009401906177500013);
  S23_DELTAR_0->SetBinContent(30,0.006889716664472045);
  S23_DELTAR_0->SetBinContent(31,0.0050995940114759875);
  S23_DELTAR_0->SetBinContent(32,0.0036705042884959825);
  S23_DELTAR_0->SetBinContent(33,0.0027679214634559485);
  S23_DELTAR_0->SetBinContent(34,0.001368917734643964);
  S23_DELTAR_0->SetBinContent(35,0.0012335297608880656);
  S23_DELTAR_0->SetBinContent(36,0.0006919802658640065);
  S23_DELTAR_0->SetBinContent(37,0.00028581794459600103);
  S23_DELTAR_0->SetBinContent(38,0.00022564575625999873);
  S23_DELTAR_0->SetBinContent(39,0.00015043047084000564);
  S23_DELTAR_0->SetBinContent(40,0.00010530137958799424);
  S23_DELTAR_0->SetBinContent(41,0.00013538747375599537); // overflow
  S23_DELTAR_0->SetEntries(100000);
  // Style
  S23_DELTAR_0->SetLineColor(9);
  S23_DELTAR_0->SetLineStyle(1);
  S23_DELTAR_0->SetLineWidth(1);
  S23_DELTAR_0->SetFillColor(9);
  S23_DELTAR_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_46","mystack");
  stack->Add(S23_DELTAR_0);
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
  stack->GetXaxis()->SetTitle("#DeltaR [ mu+_{1}, h_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_22.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_22.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_22.eps");

}
