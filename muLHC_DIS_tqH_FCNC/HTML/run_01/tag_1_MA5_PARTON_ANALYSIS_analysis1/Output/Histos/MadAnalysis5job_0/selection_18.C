void selection_18()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo37","canvas_plotflow_tempo37",0,0,700,500);
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
  TH1F* S19_M_0 = new TH1F("S19_M_0","S19_M_0",40,0.0,500.0);
  // Content
  S19_M_0->SetBinContent(0,0.0); // underflow
  S19_M_0->SetBinContent(1,0.0);
  S19_M_0->SetBinContent(2,0.0);
  S19_M_0->SetBinContent(3,0.0);
  S19_M_0->SetBinContent(4,0.0);
  S19_M_0->SetBinContent(5,0.0);
  S19_M_0->SetBinContent(6,0.0);
  S19_M_0->SetBinContent(7,0.0);
  S19_M_0->SetBinContent(8,0.0);
  S19_M_0->SetBinContent(9,0.0);
  S19_M_0->SetBinContent(10,0.0);
  S19_M_0->SetBinContent(11,0.04655824195299962);
  S19_M_0->SetBinContent(12,0.07993876618360025);
  S19_M_0->SetBinContent(13,0.07404188720280085);
  S19_M_0->SetBinContent(14,0.3327974424801918);
  S19_M_0->SetBinContent(15,0.08548965522419963);
  S19_M_0->SetBinContent(16,0.05558407039299988);
  S19_M_0->SetBinContent(17,0.04904034152400025);
  S19_M_0->SetBinContent(18,0.0432788525198004);
  S19_M_0->SetBinContent(19,0.04005964307619984);
  S19_M_0->SetBinContent(20,0.03509543393420029);
  S19_M_0->SetBinContent(21,0.03291419431119984);
  S19_M_0->SetBinContent(22,0.030025924810400513);
  S19_M_0->SetBinContent(23,0.027934945171799765);
  S19_M_0->SetBinContent(24,0.025317455624199573);
  S19_M_0->SetBinContent(25,0.025497965593000712);
  S19_M_0->SetBinContent(26,0.022730046071400424);
  S19_M_0->SetBinContent(27,0.021120446349599278);
  S19_M_0->SetBinContent(28,0.020729326417199392);
  S19_M_0->SetBinContent(29,0.018638336778600374);
  S19_M_0->SetBinContent(30,0.01826226684359928);
  S19_M_0->SetBinContent(31,0.01755523696580041);
  S19_M_0->SetBinContent(32,0.01612614721280041);
  S19_M_0->SetBinContent(33,0.015238607366200392);
  S19_M_0->SetBinContent(34,0.014351067519600373);
  S19_M_0->SetBinContent(35,0.013974997584599285);
  S19_M_0->SetBinContent(36,0.013057367743199938);
  S19_M_0->SetBinContent(37,0.012365387862799867);
  S19_M_0->SetBinContent(38,0.011643317987600467);
  S19_M_0->SetBinContent(39,0.011583147998000086);
  S19_M_0->SetBinContent(40,0.010876128120199486);
  S19_M_0->SetBinContent(41,0.2824783511772072); // overflow
  S19_M_0->SetEntries(100000);
  // Style
  S19_M_0->SetLineColor(9);
  S19_M_0->SetLineStyle(1);
  S19_M_0->SetLineWidth(1);
  S19_M_0->SetFillColor(9);
  S19_M_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_38","mystack");
  stack->Add(S19_M_0);
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
  stack->GetXaxis()->SetTitle("M [ h_{1} p_{1} ] (GeV/c^{2}) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_18.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_18.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_18.eps");

}
