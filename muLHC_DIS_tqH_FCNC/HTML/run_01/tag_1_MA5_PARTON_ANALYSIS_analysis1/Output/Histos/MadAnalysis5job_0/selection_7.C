void selection_7()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo15","canvas_plotflow_tempo15",0,0,700,500);
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
  TH1F* S8_PT_0 = new TH1F("S8_PT_0","S8_PT_0",40,0.0,500.0);
  // Content
  S8_PT_0->SetBinContent(0,0.0); // underflow
  S8_PT_0->SetBinContent(1,0.007626826894739919);
  S8_PT_0->SetBinContent(2,0.021331046908759702);
  S8_PT_0->SetBinContent(3,0.03497509493149946);
  S8_PT_0->SetBinContent(4,0.04600164333356051);
  S8_PT_0->SetBinContent(5,0.054892092045179613);
  S8_PT_0->SetBinContent(6,0.059209441419520475);
  S8_PT_0->SetBinContent(7,0.06471520062164006);
  S8_PT_0->SetBinContent(8,0.06516649055624028);
  S8_PT_0->SetBinContent(9,0.06423382069140039);
  S8_PT_0->SetBinContent(10,0.06286491088977927);
  S8_PT_0->SetBinContent(11,0.061706591057639995);
  S8_PT_0->SetBinContent(12,0.05856259151326029);
  S8_PT_0->SetBinContent(13,0.05465140208005978);
  S8_PT_0->SetBinContent(14,0.05180826249208024);
  S8_PT_0->SetBinContent(15,0.0503641327013598);
  S8_PT_0->SetBinContent(16,0.04463273353193938);
  S8_PT_0->SetBinContent(17,0.04219575388510019);
  S8_PT_0->SetBinContent(18,0.0405560641227198);
  S8_PT_0->SetBinContent(19,0.03753241456089929);
  S8_PT_0->SetBinContent(20,0.0349901349293199);
  S8_PT_0->SetBinContent(21,0.032312475317359424);
  S8_PT_0->SetBinContent(22,0.030552435572419843);
  S8_PT_0->SetBinContent(23,0.029093255783880414);
  S8_PT_0->SetBinContent(24,0.02692705609780049);
  S8_PT_0->SetBinContent(25,0.025257286339779212);
  S8_PT_0->SetBinContent(26,0.023858276542520106);
  S8_PT_0->SetBinContent(27,0.022218586780139715);
  S8_PT_0->SetBinContent(28,0.02160181686952042);
  S8_PT_0->SetBinContent(29,0.018848937268460632);
  S8_PT_0->SetBinContent(30,0.017991487392720055);
  S8_PT_0->SetBinContent(31,0.01823217735783989);
  S8_PT_0->SetBinContent(32,0.017118987519160488);
  S8_PT_0->SetBinContent(33,0.015629727734980173);
  S8_PT_0->SetBinContent(34,0.01585537770227956);
  S8_PT_0->SetBinContent(35,0.014351067920280253);
  S8_PT_0->SetBinContent(36,0.01367412801838064);
  S8_PT_0->SetBinContent(37,0.012801638144819622);
  S8_PT_0->SetBinContent(38,0.011432718343199947);
  S8_PT_0->SetBinContent(39,0.010921258417319401);
  S8_PT_0->SetBinContent(40,0.010439878487079739);
  S8_PT_0->SetBinContent(41,0.1571697772233613); // overflow
  S8_PT_0->SetEntries(100000);
  // Style
  S8_PT_0->SetLineColor(9);
  S8_PT_0->SetLineStyle(1);
  S8_PT_0->SetLineWidth(1);
  S8_PT_0->SetFillColor(9);
  S8_PT_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_16","mystack");
  stack->Add(S8_PT_0);
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
  stack->GetXaxis()->SetTitle("p_{T} [ t_{1} ] (GeV/c) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_7.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_7.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_7.eps");

}
