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
  S9_DELTAR_0->SetBinContent(13,85.95453832843012);
  S9_DELTAR_0->SetBinContent(14,64.13847875269008);
  S9_DELTAR_0->SetBinContent(15,38.749659246429985);
  S9_DELTAR_0->SetBinContent(16,28.401609447669948);
  S9_DELTAR_0->SetBinContent(17,22.62594955999001);
  S9_DELTAR_0->SetBinContent(18,19.73811961615004);
  S9_DELTAR_0->SetBinContent(19,17.192759665650012);
  S9_DELTAR_0->SetBinContent(20,15.892309690940042);
  S9_DELTAR_0->SetBinContent(21,14.226259723339945);
  S9_DELTAR_0->SetBinContent(22,13.027619746650064);
  S9_DELTAR_0->SetBinContent(23,12.162199763480007);
  S9_DELTAR_0->SetBinContent(24,11.546689775449916);
  S9_DELTAR_0->SetBinContent(25,10.398959797769981);
  S9_DELTAR_0->SetBinContent(26,9.764931810100013);
  S9_DELTAR_0->SetBinContent(27,8.857857827740006);
  S9_DELTAR_0->SetBinContent(28,8.2839948389);
  S9_DELTAR_0->SetBinContent(29,8.020202844029997);
  S9_DELTAR_0->SetBinContent(30,7.298245858069997);
  S9_DELTAR_0->SetBinContent(31,6.988173864100009);
  S9_DELTAR_0->SetBinContent(32,6.409682875350004);
  S9_DELTAR_0->SetBinContent(33,5.983912883630013);
  S9_DELTAR_0->SetBinContent(34,5.997796883360009);
  S9_DELTAR_0->SetBinContent(35,5.771028887769998);
  S9_DELTAR_0->SetBinContent(36,5.622934890650002);
  S9_DELTAR_0->SetBinContent(37,4.780651907029997);
  S9_DELTAR_0->SetBinContent(38,4.461324913239993);
  S9_DELTAR_0->SetBinContent(39,4.054066921159996);
  S9_DELTAR_0->SetBinContent(40,3.5542499308800064);
  S9_DELTAR_0->SetBinContent(41,12.888789749349911); // overflow
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
  stack->GetXaxis()->SetTitle("#DeltaR [ t_{1}, mu+_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_8.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_8.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_8.eps");

}
