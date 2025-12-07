void selection_16()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo33","canvas_plotflow_tempo33",0,0,700,500);
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
  TH1F* S17_M_0 = new TH1F("S17_M_0","S17_M_0",40,0.0,500.0);
  // Content
  S17_M_0->SetBinContent(0,0.0); // underflow
  S17_M_0->SetBinContent(1,0.0);
  S17_M_0->SetBinContent(2,0.0);
  S17_M_0->SetBinContent(3,0.0);
  S17_M_0->SetBinContent(4,0.0);
  S17_M_0->SetBinContent(5,0.0);
  S17_M_0->SetBinContent(6,0.0);
  S17_M_0->SetBinContent(7,0.0);
  S17_M_0->SetBinContent(8,0.0);
  S17_M_0->SetBinContent(9,0.0);
  S17_M_0->SetBinContent(10,0.0);
  S17_M_0->SetBinContent(11,0.0);
  S17_M_0->SetBinContent(12,0.0);
  S17_M_0->SetBinContent(13,0.0);
  S17_M_0->SetBinContent(14,6.0172197431600534e-05);
  S17_M_0->SetBinContent(15,0.006318080680318066);
  S17_M_0->SetBinContent(16,0.012666247354351956);
  S17_M_0->SetBinContent(17,0.014561666958448334);
  S17_M_0->SetBinContent(18,0.017735756295464027);
  S17_M_0->SetBinContent(19,0.020217855777018314);
  S17_M_0->SetBinContent(20,0.020684195679612095);
  S17_M_0->SetBinContent(21,0.021812425443954384);
  S17_M_0->SetBinContent(22,0.022233625355976727);
  S17_M_0->SetBinContent(23,0.022760135246002573);
  S17_M_0->SetBinContent(24,0.023602545070045177);
  S17_M_0->SetBinContent(25,0.024098964966356034);
  S17_M_0->SetBinContent(26,0.023557415079471653);
  S17_M_0->SetBinContent(27,0.024174184950644547);
  S17_M_0->SetBinContent(28,0.024490084884661305);
  S17_M_0->SetBinContent(29,0.025543094664715084);
  S17_M_0->SetBinContent(30,0.024098964966356034);
  S17_M_0->SetBinContent(31,0.024189224947503085);
  S17_M_0->SetBinContent(32,0.024098964966356034);
  S17_M_0->SetBinContent(33,0.02373793504176575);
  S17_M_0->SetBinContent(34,0.02358750507318664);
  S17_M_0->SetBinContent(35,0.02349724509203959);
  S17_M_0->SetBinContent(36,0.02312116517059286);
  S17_M_0->SetBinContent(37,0.023151255164307844);
  S17_M_0->SetBinContent(38,0.02301586519258727);
  S17_M_0->SetBinContent(39,0.022007985403107017);
  S17_M_0->SetBinContent(40,0.021782335450239398);
  S17_M_0->SetBinContent(41,0.9435001029274864); // overflow
  S17_M_0->SetEntries(100000);
  // Style
  S17_M_0->SetLineColor(9);
  S17_M_0->SetLineStyle(1);
  S17_M_0->SetLineWidth(1);
  S17_M_0->SetFillColor(9);
  S17_M_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_34","mystack");
  stack->Add(S17_M_0);
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
  stack->GetXaxis()->SetTitle("M [ mu+_{1} t_{1} ] (GeV/c^{2}) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_16.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_16.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_16.eps");

}
